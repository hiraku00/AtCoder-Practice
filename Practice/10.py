class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

# Personの使用例
p = Person("Alice", 20)
print(p.name, p.age)  # Alice 20
p.birthday()
print(p.age)  # 21

# Studentの使用例
s = Student("Bob", 18, "S12345")
print(s.name, s.age, s.student_id)  # Bob 18 S12345
s.birthday()
print(s.age)  # 19
print(s.get_student_id())  # S12345
