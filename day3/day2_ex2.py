# 多态
class Dog(object):
    def print_self(self):
        print("大家好，我是XXXX")

class Xiaotq(Dog):
    def print_self(self):
        print("Hello,erverybody,我是你们的老大，我是XXXXX")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)