# question1

from typing import List


def maximum_number(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

print(maximum_number([2,4,5,8,6,1]))



# Question2

def square(x):
    new_list=[]
    for i in x:
        squares=i*i
        new_list.append(squares)
    return new_list
print(square([4,5,6]))

# Question3
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return a + b

    def subtraction(self):
        return a - b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
calculator=Calculator(a,b)

print(f"The sum of the two numbers is {calculator.sum()}")
print(f"The difference of the two numbers is {calculator.subtraction()}")




