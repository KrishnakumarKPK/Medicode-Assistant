from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load ICD codes from Excel file
def load_icd_codes():
    """Load ICD-10 codes from Excel file"""
    try:
        df = pd.read_excel('icd_codes_2026.xlsx')
        # Create a dictionary with description as key and code as value
        icd_dict = {}
        for idx, row in df.iterrows():
            code = str(row['Code']).strip()
            description = str(row['Description']).strip().lower()
            icd_dict[description] = {"ICD": code}
        return icd_dict
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return {}

# Fallback rule-based coding dictionary with default CPT codes
default_cpt_mapping = {
    "diabetes": "83036",
    "hypertension": "99213",
    "fever": "99214",
    "asthma": "94010",
    "covid": "87635",
    "anemia": "85027",
    "chest pain": "93000",
    "migraine": "99213"
}

# Load ICD codes from Excel
icd_codes = load_icd_codes()

# Create combined coding rules
coding_rules = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        # Get the diagnosis from the request
        data = request.get_json()
        diagnosis = data.get("diagnosis", "").lower().strip()
        
        if not diagnosis:
            return jsonify({"results": [], "message": "Please enter a diagnosis"})
        
        # Search for matches in ICD codes
        matches = []
        for description, codes in icd_codes.items():
            # Check if any part of diagnosis matches any word in the description
            diagnosis_words = diagnosis.split()
            description_words = description.split()
            
            # Match if any diagnosis word is found in description
            for word in diagnosis_words:
                if word in description_words or description.find(word) != -1:
                    # Extract the primary condition name from description
                    condition_name = description.split(',')[0].title()  # Get first part before comma
                    
                    # Get CPT code if available, otherwise use generic code
                    cpt_code = default_cpt_mapping.get(word, "99999")
                    
                    matches.append({
                        "condition": condition_name,
                        "icd": codes["ICD"],
                        "cpt": cpt_code
                    })
                    break  # Move to next description after first match
        
        # Remove duplicates while preserving order
        seen = set()
        unique_matches = []
        for match in matches:
            key = (match['icd'], match['cpt'])
            if key not in seen:
                seen.add(key)
                unique_matches.append(match)
        
        if not unique_matches:
            return jsonify({"results": [], "message": "No codes found"})
        
        return jsonify({"results": unique_matches, "message": ""})


if __name__ == "__main__":
    app.run(debug=True)
