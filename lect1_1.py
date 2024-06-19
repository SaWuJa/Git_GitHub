# -*- coding: utf-8 -*-
"""
Write a program that reads the name, age, weight, and height of an 
individual and prints out the details in the form:
Name: <name value>
Age: <age value> years old
Weight: <weight value> kgs
Height: <height value> cm

@author: George
"""
name=input("Enter your name:")

age=int(input("Next enter your age:"))

weight=float(input("Now enter your weight in kgs:"))

height=float(input("Finally, enter your height in cm:"))

#Now print out the values,
print("Name:", name)
print("Age:", age," years old")
print("Weight:", weight," kgs")
print("Height:", height," cm")
