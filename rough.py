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

from oops_proj import chatbook

user1 = chatbook()    # creating an object of class chatbook

# This is modularity in OOPS, we can create multiple objects of the same class and they will have their own attributes and methods.