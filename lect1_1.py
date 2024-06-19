"""
Write a program that reads the name, age, weight, and height of an 
individual and prints out the details in the form:
Name: <name value>
Age: <age value> years old
Weight: <weight value> kgs
Height: <height value> cm

@author: Dr. George
"""
name = input("Enter your name: ")

age = int(input("Please enter your age: "))

weight = float(input("Please enter your weight in kgs: "))

height=float(input("Finally, please enter your height in cm: "))

# Now print out the values
print(f'Your name is {name}, aged {age}, and you weigh {weight}kg with a height of {height}cm.')
print("Name:", name)
print("Age:", age," years old")
print("Weight:", weight," kgs")
print("Height:", height," cm")
