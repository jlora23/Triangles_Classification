"""   
The primary goal of this file is to be able to classify a triangle based on the given inputs for the side lengths

@author: Julio Lora
"""

import unittest     # this makes Python unittest module available

def classify_triangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    
    #first, I will ensure the input given is valid
    if not(isinstance(a,int)):
           return "Invalid Input"
        
    if not(isinstance(b,int)):
           return "Invalid Input" 
        
    if not(isinstance(c,int)):
           return "Invalid Input"

    if (a<=0 or b<=0 or c<=0):
        return "Invalid Input"
    
    #then, I will test whether the 3 sides given can form a triangle using the Triangle Inequality Theorem
    if ((a+b<=c) or (a+c<=b) or (b+c<=a)):
        return "NotATriangle"
    
    #now I will classify the type of triangle based on the given inputs
    if (a == b == c):
        return "Equilateral"
    elif ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2)):
        return "Right"
    elif((a!=b) and (b!=c) and (a!=c)):
        return "Scalene"
    else:
        return "Isoceles"

