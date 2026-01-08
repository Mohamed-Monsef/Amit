from person import Person

class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        # Overriding the parent method
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"