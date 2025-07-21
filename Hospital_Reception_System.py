import csv
import os

RECEPTIONIST_FILE = "Receptionist_details.csv"
PATIENTS_FILE = "Patient_details.csv"

# ------------------ LOGIN FUNCTION ------------------
def login():
    receptionist_id = input("Enter Receptionist ID: ").strip()
    password = input("Enter Password: ").strip()
    try:
        with open(RECEPTIONIST_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Receptionist_ID'] == receptionist_id and row['Password'] == password:
                    print(f"\nWelcome {receptionist_id}!\n")
                    return True
    except FileNotFoundError:
        print(" Receptionist file not found.")
    print("\n Invalid ID or Password.\n")
    return False

# ------------------ MENU FUNCTION ------------------
def display_menu():
    print("----- Reception Menu -----")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Delete Patient")
    print("4. Assign Doctor to Patient")
    print("5. Billing the Expendature and Discharge")
    print("6. Exit")

# ------------------ ADD PATIENT ------------------
def add_new_patient():
    def get_input(prompt, validate_func, error_msg):
        while True:
            value = input(prompt).strip()
            if validate_func(value):
                return value
            print(error_msg)

    name = get_input("Enter Patient Name: ", lambda x: all(c.isalpha() or c.isspace() for c in x) and x.strip() != "", " Enter a valid name (alphabets and spaces only).")
    gender = get_input("Enter Gender (Male/Female/Other): ", lambda x: x.lower() in ['male', 'female', 'other'], " Enter 'Male', 'Female', or 'Other'.")
    address = input("Enter Address: ").strip() or "None"
    symptoms = input("Enter Symptoms (comma separated): ").strip() or "None"

    Doctor_type = "None"
    Doctor_name = "None"
    Test_results = "None"

    def get_next_patient_id():
        if not os.path.isfile(PATIENTS_FILE):
            return "P001"
        with open(PATIENTS_FILE, newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]
            if len(rows) <= 1:
                return "P001"
            last_row = rows[-1]
            last_id = last_row[0] if last_row else "P000"
            if last_id.startswith("P") and last_id[1:].isdigit():
                next_id_num = int(last_id[1:]) + 1
                return f"P{next_id_num:03d}"
            else:
                return "P001"

    patient_id = get_next_patient_id()
    patient_data = [
        patient_id, name, gender, address, symptoms, Doctor_type, Doctor_name, Test_results
    ]

    file_exists = os.path.isfile(PATIENTS_FILE)
    header = [
        "Patient_ID", "Name", "Gender", "Address", "Symptoms",
        "Doctor_type", "Doctor_name", "Test_results"
    ]
    if not file_exists:
        with open(PATIENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
    with open(PATIENTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(patient_data)
    print(f"\nPatient '{name}' added successfully with ID {patient_id}.\n")

# ------------------ DELETE PATIENT FUNCTION ------------------
def delete_patient_by_id():
    patient_id = input("Enter Patient ID to delete: ").strip()
    try:
        with open(PATIENTS_FILE, newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            header = reader.fieldnames
        found = False
        new_rows = []
        for row in rows:
            if row['Patient_ID'] == patient_id:
                found = True
            else:
                new_rows.append(row)
        if found:
            with open(PATIENTS_FILE, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                writer.writerows(new_rows)
            print(f"\nPatient with ID '{patient_id}' deleted successfully.\n")
        else:
            print(" No matching patient found.\n")
    except FileNotFoundError:
        print(" Patient file not found.\n")

# ------------------ MAIN FUNCTION ------------------
def main():
    if not login():
        return
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_new_patient()
        elif choice == '2':
            print("\n--- Search Patient Menu ---")
            print("1. All patient details")
            print("2. Specific patient by ID")
            sub_choice = input("Enter your choice (1-2): ").strip()
            if sub_choice == '1':
                try:
                    with open(PATIENTS_FILE, newline='') as file:
                        reader = csv.DictReader(file)
                        rows = list(reader)
                        if not rows:
                            print(" No patient records found.\n")
                        else:
                            print("\n--- All Patient Details ---")
                            headers = reader.fieldnames
                            print("-" * 80)
                            print("{:<12} {:<15} {:<10} {:<20} {:<15} {:<12} {:<15} {:<15}".format(
                                "Patient_ID", "Name", "Gender", "Address", "Symptoms", "Doctor_type", "Doctor_name", "Test_results"
                            ))
                            print("-" * 80)
                            for row in rows:
                                print("{:<12} {:<15} {:<10} {:<20} {:<15} {:<12} {:<15} {:<15}".format(
                                    row["Patient_ID"], row["Name"], row["Gender"], row["Address"],
                                    row["Symptoms"], row["Doctor_type"], row["Doctor_name"], row["Test_results"]
                                ))
                            print("-" * 80 + "\n")
                except FileNotFoundError:
                    print(" Patient file not found.\n")
            elif sub_choice == '2':
                search_id = input("Enter Patient ID to search: ").strip()
                try:
                    with open(PATIENTS_FILE, newline='') as file:
                        reader = csv.DictReader(file)
                        found = False
                        print("\n--- Search Results ---")
                        for row in reader:
                            if row['Patient_ID'] == search_id:
                                for key, value in row.items():
                                    print(f"{key}: {value}")
                                found = True
                                break
                        if not found:
                            print(" No matching patient found.")
                        print()
                except FileNotFoundError:
                    print(" Patient file not found.\n")
            else:
                print(" Invalid choice. Please try again.\n")
                
        elif choice == '3':
            delete_patient_by_id()

        elif choice == '4':
            # Run Doctor_Assignment.py
            try:
                os.system('python Doctor_Assignment.py')
            except Exception as e:
                print(f" Failed to run Doctor_Assignment.py: {e}")

        elif choice=='5':
            try:
                os.system('python Billing_System.py')
            except Exception as e:
                print(f" Failed to run Billing_System.py: {e}")

        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
