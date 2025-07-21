import pandas as pd
import os

def generate_patient_bill_interactive(patient_id, csv_path):
    try:
        # Load CSV and clean column names
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Ensure necessary columns
        required_columns = {'patient_id', 'name', 'doctor_name'}
        if not required_columns.issubset(df.columns):
            print(f" Missing columns: {required_columns - set(df.columns)}")
            return

        # Normalize patient ID
        patient_id = patient_id.strip().upper()
        df['patient_id'] = df['patient_id'].str.strip().str.upper()

        patient = df[df['patient_id'] == patient_id]

        if patient.empty:
            print(f" No record found for Patient ID: {patient_id}")
            return

        name = patient.iloc[0]['name']
        doctor_name = patient.iloc[0]['doctor_name']

        # Input from receptionist
        try:
            days_stayed = int(input("Enter number of days patient stayed: "))
            room_charge_per_day = float(input("Enter room charge per day (₹): "))
            doctor_fee = float(input(f"Enter consultation fee for {doctor_name} (₹): "))
        except ValueError:
            print(" Invalid input. Please enter numeric values only.")
            return

        total_room_charges = days_stayed * room_charge_per_day
        total_bill = doctor_fee + total_room_charges

        # Print bill
        print("\n--- Patient Hospital Bill ---")
        print(f"Patient ID         : {patient_id}")
        print(f"Patient Name       : {name}")
        print(f"Consulting Doctor  : {doctor_name}")
        print(f"Doctor Fee         : ₹{doctor_fee}")
        print(f"Days Stayed        : {days_stayed}")
        print(f"Room Charge/Day    : ₹{room_charge_per_day}")
        print(f"Total Room Charges : ₹{total_room_charges}")
        print(f"------------------------------")
        print(f"Total Bill Amount  : ₹{total_bill}")

        # Create a folder to store bills
        bill_folder = os.path.join(os.getcwd(), "Bills")
        os.makedirs(bill_folder, exist_ok=True)

        # File path
        bill_filename = f"{patient_id}.txt"
        bill_path = os.path.join(bill_folder, bill_filename)

        # Save bill to file
        bill_text = f"""--- Patient Hospital Bill ---
Patient ID         : {patient_id}
Patient Name       : {name}
Consulting Doctor  : {doctor_name}
Doctor Fee         : ₹{doctor_fee}
Days Stayed        : {days_stayed}
Room Charge/Day    : ₹{room_charge_per_day}
Total Room Charges : ₹{total_room_charges}
------------------------------
Total Bill Amount  : ₹{total_bill}
"""

        with open(bill_path, "w", encoding="utf-8") as file:
            file.write(bill_text)

        print(f"\n Bill saved at: {bill_path}")

    except FileNotFoundError:
        print(" CSV file not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

# Main
if __name__ == "__main__":
    print("----------- Welcome to Billing System ----------")
    csv_file_path = r"C:\\Users\Sharath A L\Desktop\\Hospital360\\Patient_Details.csv"
    patient_id_input = input("Enter Patient ID: ")
    generate_patient_bill_interactive(patient_id_input, csv_file_path)
