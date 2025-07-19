import csv
def recep_pw_check(s_id, s_pw):
    #Reading the Receptionist_details.csv file and writing it into a list
    rec_details = []
    with open('Receptionist_details.csv') as file:
        r_data = csv.reader(file)
        for row in r_data:
            rec_details.append(row)
    #Checking ID and Password
    for row in rec_details[1:]:
        if row[0] == s_id and row[2] == s_pw:
            print(f"Welcome Receptionist {row[1]}")
            return
    print("Invalid Receptionist credentials.")

def doc_pw_check(s_id, s_pw, d_details):
    #Verifying the credentials
    for row in d_details[1:]:
        if row[0] == s_id and row[2] == s_pw:
            print(f"Welcome Doctor {row[1]} ({row[3]})")
            return
    print("Invalid Doctor credentials.")

def nurse_pw_check(s_id, s_pw):
    #Reading the Receptionist_details.csv file and writing it into a list
    nurse_details = []
    with open('Nurse_details.csv') as file:
        n_data = csv.reader(file)
        for row in n_data:
            nurse_details.append(row)
    #
    for row in nurse_details[1:]:
        if row[0] == s_id and row[2] == s_pw:
            print(f"Welcome Nurse {row[1]}")
            return
    print("Invalid Nurse credentials.")
    

print('--------LOGIN PAGE--------')
staff_type = int(input('''1 - Receptioinist
2 - Doctor
3 - Nurse\n'''))
staff_ID_inp = input('Enter your ID: ')
staff_password_inp = input('Enter Password: ')

#Below code reads the doctor's details in the csv file and stores in doc_details for future use
doc_details = []
with open('Doctor_details.csv') as file:
    d_data = csv.reader(file)
    for row in d_data:
        doc_details.append(row)

if staff_type == 1:
    recep_pw_check(staff_ID_inp,staff_password_inp)
if staff_type == 2:
    doc_pw_check(staff_ID_inp,staff_password_inp,doc_details)
if staff_type == 3:
    nurse_pw_check(staff_ID_inp,staff_password_inp)
