# TreatmentStatusUpdater.py
import csv

def update_treatment_status(patient_id, status):
    updated = False
    try:
        with open('Patient_details.csv', newline='') as file:
            reader = csv.DictReader(file)
            patients = list(reader)
            fieldnames = reader.fieldnames

        # Add 'Treatment_status' field if not present
        if 'Treatment_status' not in fieldnames:
            fieldnames.append('Treatment_status')
            for p in patients:
                p['Treatment_status'] = 'False'

        # Update the treatment status for the given patient
        for patient in patients:
            if patient['Patient_ID'] == patient_id:
                patient['Treatment_status'] = 'True' if status else 'False'
                updated = True
                break

        with open('Patient_details.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(patients)

        if updated:
            print(f"✅ Treatment status updated for patient {patient_id}.")
        else:
            print(f"❌ Patient ID {patient_id} not found.")
    except FileNotFoundError:
        print("❌ Patient_details.csv not found.")
