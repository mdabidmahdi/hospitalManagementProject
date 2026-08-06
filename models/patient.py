from datetime import date
class Patient:
    def __init__(self, patient_id, first_name, last_name, dob, gender, phone, address):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.phone = phone
        self.address = address
        self.age = self.calcAge()

    def calcAge(self):
        current_date = date.today()
        dob = self.dob.split("/")
        birth_year = dob[2]
        birth_month = dob[0]
        birth_day = dob[1]
        has_had_birthday = (current_date.month, current_date.day) >= (int(birth_month), int(birth_day))
        age = (current_date.year - int(birth_year) - 1) + has_had_birthday
        return age



Abid = Patient("P1001", "Mohammad", "Mahdi", "10/14/2002", "M", "929-494-4056", "88-22 186th street, Hollis, NY-11423")
print(Abid.age)