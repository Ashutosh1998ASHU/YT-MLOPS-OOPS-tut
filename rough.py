# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 155

# print(f"Type of list is {type(lst)}")
# print(f"Type of my_str is {type(my_str)}")
# print(f"Type of my_int is {type(my_int)}")

# lst.clear()
# print(lst)

# AttributeError: 'list' object has no attribute 'capitalize'
# lst = lst.capitalize()
# print(lst)


# my_str = my_str.capitalize()
# print(my_str)

# a = "x"
# b = "y"

# print(a + b) # according to algebra , we should have got x + y , but we got xy instead 


# creating an object of class chatbook
# user1 = chatbook()

# This is modularity in OOPS, we can create multiple objects of the same class and they will have their own attributes and methods.

# function vs method below 
# lst = [1,2,3]
# this is how  we call len function to get the length of a list
# a1 = len(lst)
# print(f"Length of List is {a1}")

# from oops_proj import chatbook
# user1 = chatbook()
# print(user1._chatbook__name)
# print(user1.__name)

#  this is how we call a method sendmsg() of class chatbook using the object user1
# user1.sendmsg()

#  Checking getter and setter methods 

# print(user1.get_name())
# user1.set_name("Agent X")
# getting the name after setting it using setter method
# print(user1.get_name())


# Static method implementation

from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

# Using static method directly from class rather than object 
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)