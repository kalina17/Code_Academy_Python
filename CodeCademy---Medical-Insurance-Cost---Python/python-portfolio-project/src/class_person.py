### CREATING A CLASS PERSON
class Person:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges
    def __str__(self):
        return f"Age: {self.age} Sex: {self.sex}, BMI: {self.bmi}, Children: {self.children}, Smoker: {self.smoker}, Region: {self.region}, Insurance Cost: {self.charges}."
    def who_are_you(self):
        return f"Age: {self.age}, Sex: {self.sex}, BMI: {self.bmi}, Children: {self.children}, Smoker: {self.smoker}, Region: {self.region}, Insurance Cost: {self.charges}."


        