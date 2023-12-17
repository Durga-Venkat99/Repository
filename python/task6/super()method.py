class Patient:
    def __init__(self, patient_id, name, age, gender, address):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def display_info(self):
        print("Patient Details:")
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")
        
class Management(Patient):
    def __init__(self):
        super().__init__(self,Patient)
        self.patients = []
    def add_patient(self, patient):
        self.patients.append(patient)
    def display_patients(self):
        if not self.patients:
            print("No patient records available")
        else:
            print("patient details: ") 
            for patient in self.patients:
                patient.display_info()
                print("-"*20)
        
    def delete_patient(self,patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patient.remove(patient)
                print(f"patient with ID{patient_id}has ben deleted")
                return
            
hospital = Management()

patient0 = Patient(1,"john abraham",35,"Male","32423 jfg ys")
patient1 = Patient(2,"dory shash",28,"Female","tourno")

hospital.add_patient(patient0)
hospital.add_patient(patient1)

hospital.display_info()

hospital.delete_patient(1)

hospital.display_patients()