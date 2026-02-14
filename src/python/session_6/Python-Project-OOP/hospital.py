class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name}.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name}.")

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")