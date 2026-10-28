# # Simple Inheritance 

# # Base Class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived Class -> by passing classname as an argument in Dog class
# # no constructor in Dog class just a simple method called speak
# # in Dog class the speak method is overriden 
# class Dog(Animal):
#     # constructor overloading :- when we initiate an attribute inside the child class , the parent attribute goes null and void
#     # def __init__(self):
#     #     self.behaviour = "friendly"
#     # def speak(self):
#     #     print(f"{self.name} barks. He is very {self.behaviour}")

#     # method overloading :- 
#     def speak(self):
#         print(f"{self.name} makes a barking sound.")
    
#     # def speak1(self):
#     #     print(f"{self.name} makes a barking sound.")

# # Creates an instance of Animal 
# # animal = Animal("Generic Animal")
# # animal.speak()    
# # output :- Generic Animal makes a sound 

# # Create an instance of Dog
# dog = Dog()
# dog.speak()
# # dog.speak1()
# # output :- Generic Animal makes a sound 


#  Super Keyword

# Base Class 

class Animal:
    def __init__(self):
        self.name = "Buddy"
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        # call the base class method
        super().speak()    
        print(f"{self.name} barks. It is a {self.breed}.")
    
    # def speak1(self):
    #     # call the base class method
    #     # super().speak()    
    #     print(f"{self.name} barks. It is a {self.breed}.")

# Create an instance of Dog

dog = Dog("Golden Retriever")
dog.speak()
# dog.super().speak()   -> AttributeError: 'Dog' object has no attribute 'super'
# dog.speak1()

# Output
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.