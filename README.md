# Medical Coding Assistant (Rule-Based)

A simple full-stack web application that uses rule-based keyword matching to return relevant ICD-10 and CPT codes for medical diagnoses.

## Project Structure

```
MedProject/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # HTML template
└── static/
    ├── style.css         # CSS styling
    └── script.js         # JavaScript for frontend interactivity
```

## Features

- **Rule-Based Matching**: Uses keyword matching to identify relevant medical codes
- **Real Medical Codes**: Contains actual ICD-10 and CPT codes
- **AJAX Integration**: Submits forms without page reload
- **Responsive Design**: Works on desktop and mobile devices
- **Clean UI**: Modern gradient design with card-based results display

## Supported Diagnoses

The system currently recognizes these keywords:
- Diabetes → ICD-10: E11.9, CPT: 83036
- Hypertension → ICD-10: I10, CPT: 99213
- Fever → ICD-10: R50.9, CPT: 99214
- Asthma → ICD-10: J45.909, CPT: 94010
- COVID → ICD-10: U07.1, CPT: 87635
- Anemia → ICD-10: D64.9, CPT: 85027
- Chest Pain → ICD-10: R07.9, CPT: 93000
- Migraine → ICD-10: G43.909, CPT: 99213

## Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Navigate to project directory**:
   ```bash
   cd C:\Users\kondo\MedProject
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Enter a diagnosis** in the input field, such as:
   - "patient has diabetes"
   - "diabetes and hypertension"
   - "fever and chest pain"

4. **Click "Get Codes"** to retrieve matching ICD-10 and CPT codes

## How It Works

### Backend (Flask)

- **Route**: `GET /` serves the HTML page
- **Route**: `POST /` processes diagnosis input and returns matching codes
- **Logic**: Converts input to lowercase, searches for keyword matches in the coding_rules dictionary
- **Response**: Returns JSON with matching conditions, ICD codes, and CPT codes

### Frontend (HTML/CSS/JavaScript)

- **Form Submission**: Uses fetch API to send diagnosis to backend
- **Display Results**: Shows results in card format with ICD and CPT codes
- **Error Handling**: Displays appropriate messages for no matches or errors
- **Responsive Design**: Adapts to different screen sizes

## Example Usage

**Input**: "patient has diabetes and hypertension"

**Output**:
```
Diabetes
ICD-10 Code: E11.9
CPT Code: 83036

Hypertension
ICD-10 Code: I10
CPT Code: 99213
```

## Extending the Application

To add more diagnosis mappings, edit the `coding_rules` dictionary in `app.py`:

```python
coding_rules = {
    "your_condition": {"ICD": "CODE", "CPT": "CODE"},
    ...
}
```

## Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python 3 with Flask 2.3.3
- **Communication**: RESTful API with JSON

## Edge Cases Handled

✅ Empty input: Shows error message
✅ No matches found: Displays "No codes found"
✅ Multiple matches: Shows all matching conditions
✅ Case-insensitive: Handles uppercase, lowercase, mixed case
✅ Partial matches: Finds keywords within the input text

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Notes

- This is a demonstration application for educational purposes
- For production use, integrate with a proper medical coding database
- Always validate medical codes with official healthcare standards (CDC, CMS)

## License

This project is provided as-is for educational purposes.
