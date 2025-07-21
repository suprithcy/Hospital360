import csv  #for Handling the csv files
import os  # For running external Python files

# Load doctor credentials and names from Doctor_Details.csv
def load_doctor_credentials():
    credentials = {}
    names = {}
    with open('Doctor_Details.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            credentials[row['Doctor_ID']] = row['Password']
            names[row['Doctor_ID']] = row['Name']
    return credentials, names

# Load all patient records from Patient_details.csv
def load_patients():
    patients = []
    with open('Patient_details.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(row)
    return patients

# Save updated patient data to file
def save_patients(patients):
    with open('Patient_details.csv', 'w', newline='') as file:
        fieldnames = patients[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in patients:
            writer.writerow(p)

# ------------------ Doctor Functionalities ------------------

# View Assigned Patients
def view_assigned_patients(doctor_name, patients):
    print(f"\nAssigned Patients for {doctor_name}:")
    found = False
    print("-" * 100)
    print(f"{'Patient_ID':<12} {'Name':<15} {'Gender':<8} {'Address':<15} {'Symptoms':<20} {'Test_results'}")
    print("-" * 100)
    for row in patients:
        if row['Doctor_name'].strip().lower() == doctor_name.strip().lower():
            print(f"{row['Patient_ID']:<12} {row['Name']:<15} {row['Gender']:<8} {row['Address']:<15} {row['Symptoms']:<20} {row['Test_results']}")
            found = True
    if not found:
        print(" No patients assigned.")

# View Patient Details
def view_patient_details(patients):
    patient_id = input("Enter Patient ID: ")
    for p in patients:
        if p["Patient_ID"] == patient_id:
            print("\n🧾 Patient Details:")
            for key, value in p.items():
                print(f"{key}: {value}")
            return
    print("Patient not found.")

# Update Test Results
def update_test_results(patients):
    test_map = {
        "General Physician": ["Blood Pressure", "WBC Count", "Hemoglobin"],
        "Cardiologist": ["ECG Result", "Ejection Fraction", "Lipid Profile"],
        "Orthopedist": ["X-ray Result", "Mobility Test", "MRI Result"],
        "Dermatologist": ["Skin Biopsy", "Dermoscopy", "Allergy Patch Test"],
        "Pediatrician": ["Growth Check", "Vaccination Status", "Throat Exam"]
    }

    p_id = input("Enter Patient ID to update test results: ")
    for p in patients:
        if p["Patient_ID"] == p_id:
            doc_type = p["Doctor_type"]
            doc_name = p["Doctor_name"]
            print(f"\nDoctor Type: {doc_type}, Doctor Name: {doc_name}")
            
            if doc_type in test_map:
                print("Enter the following test results:")
                test_results = {}
                for test in test_map[doc_type]:
                    result = input(f"{test}: ")
                    test_results[test] = result

                test_results_str = ", ".join([f"{k}:{v}" for k, v in test_results.items()])
                p["Test_results"] = test_results_str
                print(" Test results updated.")
            else:
                print(" Unknown Doctor Type.")
            return
    print(" Patient not found.")

# Run Daily Checkup Script
def run_daily_checkup():
    print("\n🩺 Opening Daily Checkup Module...")
    try:
        os.system("python Doctor_checkup.py")  # Ensure this file exists in the same directory
    except Exception as e:
        print(f" Failed to run Doctor_checkup.py: {e}")

# ------------------ Main Program ------------------

def doctor_main():
    print("===== Doctor Login Portal =====")
    credentials, doctor_names = load_doctor_credentials()

    doctor_id = input("Enter Doctor ID: ")
    password = input("Enter Password: ")

    if doctor_id in credentials and credentials[doctor_id] == password:
        print(" Login successful!")
        doctor_name = doctor_names[doctor_id]

        patients = load_patients()

        while True:
            print("\n---- Doctor Menu ----")
            print("1. View Assigned Patients")
            print("2. View Patient Details")
            print("3. Update Patient Test Results")
            print("4. Daily Doctor Visit")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                view_assigned_patients(doctor_name, patients)
            elif choice == '2':
                view_patient_details(patients)
            elif choice == '3':
                update_test_results(patients)
                save_patients(patients)
            elif choice == '4':
                run_daily_checkup()
            elif choice == '5':
                print("Logging out. Goodbye")
                break
            else:
                print(" Invalid choice. Please try again.")
    else:
        print(" Invalid Doctor ID or Password.")

if __name__ == "__main__":
    doctor_main()
