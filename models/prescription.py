class Prescription:
    def __init__(self, prescription_id, patient, doctor, rx_name, dosage, directions, date):
        self.prescription_id = prescription_id
        self.patient_id = patient
        self.doctor = doctor
        self.rx_name = rx_name
        self.dosage = dosage
        self.directions = directions
        self.date = date