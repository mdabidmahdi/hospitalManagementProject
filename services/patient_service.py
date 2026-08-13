import random
import json
from models.patient import Patient
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PATIENT_DATA_FILE = BASE_DIR/ "data"/"patients.json"

def patient_id_gen():
        num_gen = random.randint(1,10000)
        patient_id = ("P" + str(num_gen))
        return patient_id  


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

    patient_id = patient_id_gen()
    new_patient = Patient(patient_id, first_name, last_name, dob, gender, phone, address)
    with open(PATIENT_DATA_FILE, "a") as file:
        json.dump(new_patient.to_dict(), file, indent=4)
    print("New patient has been registered!")
    

    



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
                patient_reg()
                continue
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