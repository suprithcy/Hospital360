import csv

def doctor_assignment(p_id):
    # Load patient details
    with open('Patient_Details.csv') as file:
        patient_details = list(csv.reader(file))

    # Find patient index
    header = patient_details[0]
    for patient_index, row in enumerate(patient_details[1:], start=1):
        if row[0] == p_id:
            break
    else:
        print("Patient ID not found.")
        return
    
    flag = input("Do you want to see any specific Doctor (yes or no) : ").lower()
    if flag == "no":
        d_name = "nope"
    else:
        d_name = input("Provide the Doctor Name to visit : ")

    # Get and clean symptoms
    symptoms = [s.strip().lower() for s in patient_details[patient_index][4].split(',')]

    # Load doctor details
    with open('Doctor_details.csv') as file:
        doctors_details = list(csv.reader(file))

    # Doctor assignment configuration
    #This id a Dictionary of dictionary of list and list of tuples
    doctor_config = {
        "General Physician": {
            "symptoms": ["fever", "headache", "fatigue"],
            "doctors": [(1, "Dr. Ayesha Mehta"), (2, "Dr. Rohan Kapoor")]
        },
        "Cardiologist": {
            "symptoms": ["chest pain", "shortness of breath", "palpitations"],
            "doctors": [(3, "Dr. Sneha Reddy"), (4, "Dr. Vikram Desai")]
        },
        "Orthopedist": {
            "symptoms": ["joint pain", "back pain", "swelling in limbs"],
            "doctors": [(5, "Dr. Anjali Verma"), (6, "Dr. Arjun Sharma")]
        },
        "Dermatologist": {
            "symptoms": ["skin rash", "acne", "itching"],
            "doctors": [(7, "Dr. Neha Joshi"), (8, "Dr. Karan Malhotra")]
        },
        "Pediatrician": {
            "symptoms": ["cough", "vomiting"],
            "doctors": [(9, "Dr. Priya Nair"), (10, "Dr. Rajeev Menon")]
        }
    }
    if d_name == "nope":
        assigned = False

        for specialization, data in doctor_config.items():
            if any(symptom in symptoms for symptom in data["symptoms"]):
                patient_details[patient_index][5] = specialization

                if patient_details[patient_index][6].lower() == "none":
                    # Get load of each doctor
                    doc1_idx, doc1_name = data["doctors"][0]
                    doc2_idx, doc2_name = data["doctors"][1]

                    load1 = int(doctors_details[doc1_idx][4])
                    load2 = int(doctors_details[doc2_idx][4])

                    if load1 <= load2:
                        selected_doc = doc1_name
                        doctors_details[doc1_idx][4] = str(load1 + 1)
                    else:
                        selected_doc = doc2_name
                        doctors_details[doc2_idx][4] = str(load2 + 1)

                    patient_details[patient_index][6] = selected_doc
                    assigned = True
                else:
                    print("Doctor already assigned.")
                break

        if not assigned:
            print("No matching symptoms found or doctor already assigned.")

    else:
        for specialization, data in doctor_config.items():
            if d_name in data["doctors"][0]:
                doc_idx, doc_name = data["doctors"][0]
                patient_details[patient_index][5] = specialization
                patient_details[patient_index][6] = doc_name
                break
            elif d_name in data["doctors"][1]:
                doc_idx, doc_name = data["doctors"][1]
                patient_details[patient_index][5] = specialization
                patient_details[patient_index][6] = doc_name
                break

        load = int(doctors_details[doc_idx][4])
        doctors_details[doc_idx][4] = str(load + 1)

    # Write updated patient details
    with open('Patient_Details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(patient_details)

    # Write updated doctor details
    with open('Doctor_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(doctors_details)

    print("Doctor assignment updated successfully.")
    # for row in doctors_details:
    #     print(row)
    # for row in patient_details:  
    #     print(row)

# Test the function
patient_id = input("Enter the Patient ID : ")



doctor_assignment(patient_id)
