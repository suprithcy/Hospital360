import pandas as pd
import os

# Paths
NURSE_CSV_PATH = r"C:\Users\Sharath A L\Desktop\Hospital360\Nurse_details.csv"
PATIENT_CSV_PATH = r"C:\Users\Sharath A L\Desktop\Hospital360\Patient_Details.csv"
RECORDS_FOLDER = r"C:\Users\Sharath A L\Desktop\Hospital360"  # Where patient text files are stored

def authenticate_nurse():
    try:
        nurse_df = pd.read_csv(NURSE_CSV_PATH)
        nurse_df.columns = nurse_df.columns.str.strip()
    except Exception as e:
        print(" Failed to read nurse CSV:", e)
        return None

    name = input("Enter Nurse Name: ").strip().lower()
    password = input(" Enter Password: ").strip()

    matched = nurse_df[
        (nurse_df['Name'].str.lower().str.strip() == name) &
        (nurse_df['Password'].str.strip() == password)
    ]

    if matched.empty:
        print(" Invalid credentials.")
        return None
    else:
        print(f"\n Access granted. Welcome Nurse {name.title()}!")
        return matched.iloc[0]  # return nurse row (optional)

def nurse_view_patient_record():
    if not os.path.exists(PATIENT_CSV_PATH):
        print(" Patient details CSV file not found:", PATIENT_CSV_PATH)
        return

    try:
        df = pd.read_csv(PATIENT_CSV_PATH)
        df.columns = df.columns.str.strip()
    except Exception as e:
        print("⚠ Failed to read Patient CSV file:", e)
        return

    # Ask for Patient ID
    patient_id = input("\n Enter Patient ID to view (e.g., P001): ").strip().upper()

    # Get patient details from CSV
    patient_row = df[df['Patient_ID'].astype(str).str.upper() == patient_id]

    if patient_row.empty:
        print(" No patient found with ID:", patient_id)
        return

    print("\n Patient Details:\n" + "-" * 40)
    for col in df.columns:
        print(f"{col}: {patient_row.iloc[0][col]}")
    print("-" * 40)

    # Check for Doctor's record file
    txt_filename = f"patient_{patient_id}.txt"
    txt_path = os.path.join(RECORDS_FOLDER, txt_filename)

    if os.path.exists(txt_path):
        print(f"\n Doctor's Notes from: {txt_filename}\n" + "-" * 40)
        with open(txt_path, 'r') as file:
            print(file.read())
        print("-" * 40)
    else:
        print(f"No doctor notes found for Patient ID: {patient_id} ({txt_filename} not found)")

# Main
if __name__ == "__main__":
    nurse = authenticate_nurse()
    if nurse is not None:
        nurse_view_patient_record()