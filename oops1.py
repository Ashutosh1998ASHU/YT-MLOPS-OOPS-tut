# initialize a class 
class employee:
    # special method/magic method/dunder method - constructor 
    def __init__(self):
        # print(f"self id from init: {id(self)}")
        # print("Started executing attributes/data")
        self.id = 123 
        self.salary = 50000
        self.designation = "SDE"
        # print("attributes/data have been initiated")


    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# create an object/instance of the class 
sam = employee()
print(f"sam id : {id(sam)}")

# sam.name = "Sam Kumar"
# print(sam.name)

# shaktiman = employee()
# print(f"shaktiman id: {id(shaktiman)}")

# printing the attributes of the object
# print(sam.id,sam.salary,sam.designation)

# calling a method
# sam.travel("North Carolina")
# sam.travel()

# print(type(sam))

