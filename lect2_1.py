"""
Created on Wed Jun 14 10:12:05 2023

@author: George
"""

import math

def compute_area (radius):
    """
    Computes and returns the area given the radius
    Parameters: radius : float.
    Returns: float.
    """
    return math.pi*math.pow (radius,2)


def compute_circumference (radius):
    """
    Computes and returns the circumference given the radius
    Parameters: radius : float.
    Returns: float.
    """
    return 2* math.pi*radius


def main():
    """
    Requests for the radius and calls functions to compute area
    and perimeter.
    """
    radius=float(input('Enter radius of circle: '))
    #compute and print area and circumference
    print("Radius:", radius,", Area:",\
    compute_area (radius),\
    ", Circumference:",\
    round(compute_circumference (radius),2))