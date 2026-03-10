# Exercise 3: Simple Class and Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student("Ola", 21, "S12345")
student.greet()
print("Student ID:", student.student_id)