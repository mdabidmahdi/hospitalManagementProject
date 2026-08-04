from models.patient import Patient
def patient_reg():
    first_name = input("Please enter the patient's first name: ")
    last_name = input("Please enter the patient's first name: ")
    dob = input("Please enter the patient's date of birth(MM/DD/YYYY): ")
    while True:
        gender = input("Please enter the patient's gender(M/F): ")
        if gender.lower() == 'm':
            break
        elif gender.lower() == 'f':
            break
        else:
            print('Please selecta correct gender. ')
            continue
    phone = input("Please enter the patient's phone number: ")     
    address = input("Please enter the patient's address: ")
    



def patient_menu():
    print("===================================")
    print("PATIENT MENU")
    print("===================================")

    options = ["Register Patient", "Search patient", "Update Patient", "Delete patient", "View all patients", "Back"]
    y = 1

    for x in options:
        print(str(y) +". " + x)
        y +=1

    while True:
        user_input = int(input("Please select a number between 1-6: "))

        match user_input:
            case 1:
                print("Loading....")
            case 2:
                print("Loading....")
            case 3:
                print("Loading....")
            case 4:
                print("Loading....")
            case 5:
                print("Loading....")
            case 6:
                print("Loading....")
            case _:
                print("Please select a correct option")
                continue