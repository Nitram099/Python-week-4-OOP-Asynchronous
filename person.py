class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is", self.name, ". I am", self.age, "years old and I am", self.gender, ".")

# Create an instance of the Person class
person1 = Person("Nora 3.0", 30, "Female")

# Call the introduce method
person1.introduce()