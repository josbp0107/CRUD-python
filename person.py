

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print (f"Hello {self.name}, You have {self.age} years old")


if __name__ == "__main__":
    person = Person("Jose", 22)
    person.say_hello()