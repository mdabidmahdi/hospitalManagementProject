from services.patient_service import patient_menu


print("===================================")
print("HOSPITAL MANAGEMENT SYSTEM")
print("===================================")

options = ["Patients", "Doctors", "Appointments", "Medical Records", "Billing", "Prescriptions", "Reports", "Save", "Exit"]
y = 1
for x in options:  
    print(str(y)+". "+x)
    y +=1


while True:
    user_input = int(input("Please select a number between 1-9: "))

    match user_input:
        case 1:
            patient_menu()
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
        case 7:
            print("Loading....")
        case 8:
            print("Loading....")
        case 9:    
            print("Loading....")
        case _:
            print("Please select a correct option")
            continue    