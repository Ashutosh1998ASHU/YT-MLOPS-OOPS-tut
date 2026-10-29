# #  Single or basic inheritance 

# # Base Class
# class Parent:
#     def __init__(self,name):
#         self.name = name 

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived Class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child 

# child = Child("Alice")
# child.greet()    # Output: Hello, my name is Alice.
# child.play()     # Output: Alice is playing.

# ------------------

# # Multi-Level Inheritance

# # Base Class
# class Grandparent:
#     def __init__(self,name):
#         self.name = name 

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediate Class
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.")

# # Derived Class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child 

# child = Child("Charlie")
# child.tell_story()    # Output: Charlie tells a story.
# child.work()    # Output: Charlie is working.
# child.play()     # Output: Charlie is playing.

# ------------------

# Hierarchical Inheritance

# # Base Class
# class Parent:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived Class 1
# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Derived Class 2
# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# # Create an instance of Child1 and Child2
# child1 = Child1("Dave") 
# child2 = Child2("Eve") 

# child1.greet()   # Output: Charlie tells a story.
# child1.play()    # Output: Charlie tells a story.

# child2.greet()   # Output: Charlie is working.
# # child2.play()  # Output: AttributeError: 'Child2' object has no attribute 'play'
# child2.study()   # Output: Charlie is playing.

# Dono child ke paas individual methods hai 


# ------------------

# Multiple Inheritance (Diamond Problem)

# # Common Base Class
# class A:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # Intermediate Class 1
# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # Intermediate Class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# # Derived Class
# class D(B,C):
#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # Create an instance of D
# d = D("Frank Castle")
# d.greet()

# # Output:
# # Hello from D, Frank Castle.
# # Hello from B, Frank Castle.
# # Hello from C, Frank Castle.
# # Hello from A, Frank Castle.

# ------------------

# Hybrid Inheritance

# Base Class
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate Class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate Class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived Class (Multiple Inheritance)
class Bat(Mammal,Bird):
    def __init__(self,name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor
 
    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()

# Output
# Bruce makes a sound.
# Bruce is feeding milk.
# Bruce is flying.
# Bruce is nocturnal.