import csv
'''This code specifies Different tests for different categories of doctors and 
Stores it in the file'''
# Dictionary mapping Doctor_type to required test names
test_map = {
    "General Physician": ["Blood Pressure", "WBC Count", "Hemoglobin"],
    "Cardiologist": ["ECG Result", "Ejection Fraction", "Lipid Profile"],
    "Orthopedist": ["X-ray Result", "Mobility Test", "MRI Result"],
    "Dermatologist": ["Skin Biopsy", "Dermoscopy", "Allergy Patch Test"],
    "Pediatrician": ["Growth Check", "Vaccination Status", "Throat Exam"]
}

# Load existing patient data into a list patients[], each record as a dictionary
patients = []
with open('Patient_details.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        patients.append(row)
# print(patients)       

# Ask for Patient ID
p_id = input("Enter Patient ID: ")

# Search for patient
for p in patients:
    if p["Patient_ID"] == p_id:
        doc_type = p["Doctor_type"]
        doc_name = p["Doctor_name"]
        print(f"Doctor Type: {doc_type}, Doctor Name: {doc_name}")
        
        if doc_type in test_map:
            test_results = {}
            for test in test_map[doc_type]:
                result = input(f"Enter result for {test}: ")
                test_results[test] = result
            
            # Store Test results as a key:value string
            test_results_str = ", ".join([f"{k}:{v}" for k, v in test_results.items()])
            p["Test_results"] = test_results_str
            # Store Doctor's observations as a string
            observation = input("Enter Doctor's Summary/Observation: ")
            p["Doctor_Observation"] = observation
            # Store the admission status as Boolean
            admission_input = input("Enter 'Yes' if Admission required, otherwise press Enter: ").lower()
            p["Admission_Status"] = True if admission_input == "yes" else False
        else:
            print("Unknown Doctor Type")
        break
else:
    print("Patient not found")

# Write back updated data
with open('Patient_details.csv', 'w', newline='') as file:
    fieldnames = patients[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for p in patients:
        writer.writerow(p)

print("Test results updated successfully.")
