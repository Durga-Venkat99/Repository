class hospitalmanagement:
    def __init__(self):
        self.patients = []
    def details(self,name,patient_id,age,gender,address):
        patient = {
            "ID" : patient_id,
            "Name": name,
            "Age" : age,
            "Gender": gender,
            "Adress": address
        }
        self.patients.append(patient)
        print("details added successfully")

    def display_patient(self):
        if not self.patients:
            print("No patient record available")
        else:
            print("Patient Details")
            for patient in self.patients:
                for key,value in patient.items():
                    print(f"{key} : {value}")
                print("-"*20)
    
    def search_patient_by_id(self,patient_id):
        for patient in self.patients:
            for key,value in patient.items():
                print(f"{key}:{value}")
            print("-"*20)

    def delete_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient["ID"] == patient_id:
                self.patients.remove(patient)
                print("patient deleted successfully!")
                return

    def update_patient_by_id(self,patient_id,name,age,gender,address):
        for patient in self.patients:
            if patient["ID"] == patient_id:
                patient["Name"] = name
                patient["Age"] = age
                patient["Gender"] = gender
                patient["Address"] = address
                print("patient details updated successfully")
                return
hospital = hospitalmanagement()

hospital.details(1,"sindu",23,"female","876 prakasam")
hospital.details(2,"jane smith",34,"male","23-us")

hospital.display_patient()
patient = hospital.search_patient_by_id(1)
if patient:
    print("Patient found:")
    for key, value in patient.items():
        print(f"{key}:{value}")
else:
    print("patient not found")

hospital.update_patient_by_id(2,"jane smith",34,"male","23-us")
hospital.display_patient()

hospital.delete_patient_by_id(1)
hospital.display_patient()