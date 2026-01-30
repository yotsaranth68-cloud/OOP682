from models.person import Person

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

    def __str__(self):
        return f"Staff[{self.pid}, {self.name}, {self.age}]"