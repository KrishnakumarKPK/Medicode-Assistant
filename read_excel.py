from app import icd_codes, default_cpt_mapping

print(f"Total ICD codes loaded: {len(icd_codes)}")
print(f"\nSample ICD codes:")
for i, (description, code_dict) in enumerate(list(icd_codes.items())[:10]):
    print(f"  {description}: {code_dict['ICD']}")

print(f"\nDefault CPT codes:")
for condition, cpt in default_cpt_mapping.items():
    print(f"  {condition}: {cpt}")

