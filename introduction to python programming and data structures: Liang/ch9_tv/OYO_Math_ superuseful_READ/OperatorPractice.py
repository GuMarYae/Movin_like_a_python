# This one is to get a better understanding of how to use math operators.
# This was ignored by me for the most part when learning C++.
# Now is the time to make this make more sense.

# How to use operators with objects is called OPERATOR OVERLOADING.
# Operator overloading simply means telling a class what an operator like +, -, *, or / should do with its objects.

# So earlier I didn't know that in C++, once you make/overload an operator like add or subtract in a class,
# you can simply use the symbol in int main and it will automatically know which operator to use in the class.
# Example in int main:
# mathNum1 + mathNum2 --> uses the overloaded + operator in the class,
# with the objects being used in the parameters.

# Python is the same idea:
# num1 + num2 --> num1.__add__(num2)

# In Python, you don't have to import the whole module.
# This is good when a module has multiple classes in it.

# We have the OperatorPractice module, and inside it we will have:
# Add class
# Subtract class
# Divide class
# Multiply class

# So for one main.py file I'll use:
# import OperatorPractice

# Then I'll have a separate main2.py file and use:
# from OperatorPractice import Add

# This is so I can see the difference between importing the entire module
# and importing one specific class from the module. 
# LETS GET IT




class OperatorPractice:
    # Each object only needs ONE value (a).
    # We do not need "b" because when we create main(), the second value
    # will come from a SECOND object.
    def __init__(currentObject, a):
        currentObject.__a = a


class Add:
    # Example later in main:
    # num1 = Add(10)
    # num2 = Add(5)
    # num1 stores 10 and num2 stores 5.
    def __init__(currentObject, a = 0): # this just means that when making an object you can only store one value in it ex a1 = Add(3)
        currentObject.__a = a

    # When main uses: num1 + num2
    # Python automatically calls: num1.__add__(num2)
    # currentObject = num1 (left object)
    # otherObject = num2 (right object)
    # So we add the value stored in num1 to the value stored in num2.
    def __add__(currentObject, otherObject):
        return currentObject.__a + otherObject.__a


class Subtract:
    # Each Subtract object stores ONE number.
    def __init__(currentObject, a = 0): # this just means that when making an object you can only store one value in it ex s1 = Subtract(3)
        currentObject.__a = a

    # num1 - num2 automatically calls num1.__sub__(num2)
    # currentObject holds the first number.
    # otherObject holds the second number.
    def __sub__(currentObject, otherObject):
        return currentObject.__a - otherObject.__a


class Multiply:
    # Each Multiply object stores ONE number.
    def __init__(currentObject, a = 0): # this just means that when making an object you can only store one value in it ex m1 = Multiply(3)
        currentObject.__a = a

    # num1 * num2 automatically calls num1.__mul__(num2)
    # The two numbers come from the two different objects.
    def __mul__(currentObject, otherObject): # you can call an object __a for the sane class, different object and use them both in the same param
        return currentObject.__a * otherObject.__a


class Divide:
    # Each Divide object stores ONE number.
    def __init__(currentObject, a = 0): # this just means that when making an object you can only store one value in it ex d1 = Divide(3)
        currentObject.__a = a

    # num1 / num2 automatically calls num1.__truediv__(num2)
    # currentObject.__a = value from num1
    # otherObject.__a = value from num2
    def __truediv__(currentObject, otherObject):
        return currentObject.__a / otherObject.__a