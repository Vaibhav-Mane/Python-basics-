class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print("hi i am ", self.name , "i am ", self.age , "years old")

    def Add_weight(self,weight):
        self.weight = weight
        print("my weight is  ", self.weight )

tim = Dog ('tim', 24)
tim.speak()
tim.Add_weight(75)
