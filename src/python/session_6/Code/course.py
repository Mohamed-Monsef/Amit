class course:
    _id_counter = 1
    
    def __init__(self, name):
        self.course_id = course._id_counter
        course._id_counter += 1
        self.name = name
       
        self.enrolled_student = [] 

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Enrolled Students: {len(self.enrolled_student)}"
    
    def __repr__(self):
        return f"course ID: {self.course_id}, Name: {self.name}, Enrolled Students:  {len(self.enrolled_student)}"

    def enroll_student(self, student):
        if student not in self.enrolled_student:
            self.enrolled_student.append(student)
            print(f"Student enrolled successfully in {self.name}")
        else:
            print(f"Student is already enrolled in {self.name}")

    def remove_student(self,student):
        if student in self.enrolled_student:
            print(f"Student removed from {self.name}")
        else:
            print(f"Student is not enrolled in {self.name}")

    