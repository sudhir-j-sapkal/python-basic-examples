class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
       # setAge(age)

    def setAge(self,age):
        self.age = age

person_dagdu = Person("Dagdu", 40)
print(person_dagdu)
print("Person Name:" + person_dagdu.name)
print("Person Age:" + str(person_dagdu.age))
