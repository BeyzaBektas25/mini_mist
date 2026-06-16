#in this programme will be calculated some geometric perimeter for us.
import math
print(f"Welcome to the geometric perimeter calculation program. \nPlease make your selection using the numbers.")

geometric= int(input("1-square\n 2-triangle\n 3-rectangle\n 4-circle \n 5-trapezoid\n"))

match geometric:
    case 1:
        a=float(input("enter edge value... "))
        square=4*a
        print("result->",square)
     
    case 2:
        sideA = float(input("Enter the side A: "))
        sideB = float(input("Enter the side B: "))
        sideC = float(input("Enter the side C: "))
        triangle=sideA+sideB+sideC
        print("result->",triangle)
    case 3:
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        rectangle=2*(width+height)
        print("result->",rectangle)
    case 4: 
        radius=float(input("enter radius value"))
        circle=2*math.pi*radius
        print("result->",circle)
    case 5:
        top_base = float(input("Enter the top base value: "))
        bottom_base = float(input("Enter the bottom base value: "))
        left_leg= float(input("Enter the left leg value: "))
        right_leg= float(input("Enter the right leg value: "))
        trapezoid=(top_base+bottom_base+left_leg+right_leg)
        print("result->",trapezoid)
    
