#!/usr/bin/env python3

class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        if isinstance(self.name, str):
            return self.name

    def get_age(self):
        if isinstance(self.age, int):
            return self.age

    def get_score(self):
        if isinstance(max(self.score), int):
            return max(self.score)


s1 = Student('Lic', 20, [88,95,99])
print(s1.get_name())
print(s1.get_age())
print(s1.get_score())



