class Patient:
    def __init__(self,patient_id,name,age,gender,address):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    def display(self):
        print("Patient Details")
        print(f"ID = {self.patient_id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Address = {self.address}")
class Outpatient(Patient):
    def __init__(self,patient_id,name,age,gender,address,appointment_date):
        super().__init__(patient_id,name,age,gender,address)
        self.appointment_date = appointment_date
    def display(self):
        super().display()
        print(f"Appointment_date : {self.appointment_date}")
class inpatient(Patient):
    def __init__(self, patient_id, name, age, gender, address,room_number):
        super().__init__(patient_id, name, age, gender, address)
        self.room_number = room_number
    def display(self):
        super().display()
        print(f"Room_number : {self.room_number}")

class hospital(Patient):
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display(self):
        if not self.patients:
            print("No patient records available.")
        else:
            for patient in self.patients:
                patient.display()
                print("-" * 20)

    def delete_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} has been deleted.")
                return
        print(f"Patient with ID {patient_id} not found.")

# Example usage
hospital = hospital()

patient1 = Outpatient(1, "John Doe", 35, "Male", "123 Main St", "2023-10-26")
patient2 = inpatient(2, "Jane Smith", 28, "Female", "456 Elm St", 101)

hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.display()

hospital.delete_patient(1)  # Delete patient with ID 1

hospital.display()
