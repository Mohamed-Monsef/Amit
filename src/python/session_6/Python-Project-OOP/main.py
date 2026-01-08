from hospital import Hospital, Department
from patient import Patient
from staff import Staff

def main():
    # 1. Setup the Hospital
    my_hospital = Hospital("CHG Hospitals", "Almaza, Cairo")
    
    # 2. Create Departments
    Orthopedics = Department("Orthopedics")
    my_hospital.add_department(Orthopedics)

  
    new_patient = Patient("Ali", 25, "Broken bones")
    new_doctor = Staff("Dr. Smith", 32, "Diagnostician")

    # 4. Assign them
    Orthopedics.add_patient(new_patient)
    Orthopedics.add_staff(new_doctor)

    print("\n--- System Check ---")
    print(new_patient.view_record())
    print(new_doctor.view_info())

if __name__ == "__main__":
    main()