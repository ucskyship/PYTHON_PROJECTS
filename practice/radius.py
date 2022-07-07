""" Calculate the area and circumference of a circle from its radius
Step1. Prompt for a radius
Step2. Apply the area formula
Step3. Print out the results
"""

import math

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print("\n""The circumference is:", round(circumference, 2), "\n""\n""And the area is: ", round(area, 2), "\n")
