import pandas as pd
from datetime import datetime
import os
from tabulate import tabulate

def update_patient_checkup():
    csv_path = r"C:\\Users\Sharath A L\Desktop\\Hospital360\\Patient_Details.csv"
    records_folder = r"C:\\Users\Sharath A L\\Desktop\\Hospital360\\Patient_Dailylogs"

    # Create the folder if it doesn't exist
    os.makedirs(records_folder, exist_ok=True)

    if not os.path.exists(csv_path):
        print("Patient details CSV file not found:", csv_path)
        return

    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
        df.columns = df.columns.str.strip()
    except Exception as e:
        print(" Failed to read CSV file:", e)
        return

    print("\n Patient List:")
    print(tabulate(df[['Patient_ID', 'Name', 'Symptoms']], headers='keys', tablefmt='grid'))

    patient_id = input("\n Enter Patient ID to update (e.g., P001): ").strip().upper()

    if 'Patient_ID' not in df.columns:
        print("Column 'Patient_ID' not found in the CSV!")
        print("Available columns:", df.columns.tolist())
        return

    patient_row = df[df['Patient_ID'].astype(str).str.upper() == patient_id]

    if patient_row.empty:
        print(f"Patient with ID '{patient_id}' not found.")
        return

    patient_info = patient_row.iloc[0]

    print("\n Patient Details:")
    for col in df.columns:
        print(f"{col}: {patient_info[col]}")

    update_notes = input("\n Enter daily checkup notes / observations: ").strip()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the notes in Patient_Dailylogs folder
    txt_filename = f"patient_{patient_id}.txt"
    txt_path = os.path.join(records_folder, txt_filename)

    with open(txt_path, 'a', encoding='utf-8') as file:
        file.write(f"\n--- Daily Update on {timestamp} ---\n")
        for col in df.columns:
            file.write(f"{col}: {patient_info[col]}\n")
        file.write(f"Checkup Notes: {update_notes}\n")
        file.write("-" * 40 + "\n")

    print(f"\nPatient record updated and saved to: {txt_path}")

if __name__ == "__main__":
    update_patient_checkup()
