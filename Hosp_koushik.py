import csv
def recep_pw_check(s_type,s_pw):
    with open('Receptionist_details') as file:
        r_data = csv.reader(file)
        for row in r_data:
            doc_details.append(row)
        pass

  
def doc_pw_check(s_type,s_pw,d_details):
    if doc_details[s_type[1:]][0] == 
    pass

def nurse_pw_check(s_type,s_pw):
    pass
# def login():
#     '''This method gets the Staff type and verifies the ID and Password to proceed'''
    
#     doc_details = []
#     with open('Doctor_details.csv') as file:
#         data = csv.reader(file)
#         for row in data:
#             doc_details.append(row)
#         if doc_details[1][0]
# login()

print('--------LOGIN PAGE--------')
staff_type = int(input('''1 - Receptioinist
2 - Doctor
3 - Nurse\n'''))
staff_ID_inp = input('Enter your ID: ')
staff_password_inp = input('Enter Password: ')
doc_details = []
with open('Doctor_details.csv') as file:
    d_data = csv.reader(file)
    for row in d_data:
        doc_details.append(row)
if staff_type == 1:
    recep_pw_check(staff_ID_inp,staff_password_inp)
if staff_type == 2:
    doc_pw_check(staff_type,staff_password_inp,doc_details)
if staff_type == 3:
    nurse_pw_check(staff_type,staff_password_inp)