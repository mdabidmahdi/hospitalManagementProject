class Appointment:
    def __init__(self, appointment_id, DOS, patient, doctor, reason, time):
        self.patient_id = appointment_id
        self.DOS = DOS
        self.patient = patient
        self.doctor = doctor
        self.reason = reason
        self.time = time