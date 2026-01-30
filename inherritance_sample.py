from models.person import Person
from models.staff import Staff
from models.student import Student


person = Person(2222222222222,"Jecob",30)
studen = Student(1234567890123,"Alice",20,"S123")
staff = Staff(2342342234234,"Bob",35,"ST456")
print(person)
print(studen)
print(staff)


def get_person_info(person):
    if not isinstance(person, Person):
        return f"Name: {person.name}, Age:{person.age}"

get_person_info(studen)
get_person_info(staff)

class Employee:
    pass

