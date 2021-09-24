import math 

def validate_input_to_float(userInput): 
     while userInput!=float:
         try:
             value = float(input(userInput)) 
         except ValueError:
            print("Enter a valid floating point number ")
            continue
         if value<0 :
            print("Sorry, your input must not be negative:  "  )
         else:
            break
     return value


def main():

    radius= validate_input_to_float(("Enter the Radius of the Cone:  "))
    height= validate_input_to_float(("Enter the Height of the Cone: "))
    length= math.sqrt(radius*radius+height*height)
    surfaceArea= math.pi*radius*(radius+length)
    volume= (1.0/3)*math.pi*radius*radius*height
    lateralSurfaceArea= math.pi * radius * length
    print("The Length of a side of the Cone is = %.2f " %length)
    print("The Surface Area of a Cone is= %.2f" %surfaceArea)
    print("The Volume of the Cone is = %.2f "%volume)
    print("The Lateral Surface Area is= %.2f" %lateralSurfaceArea)

if __name__ == "__main__":
    main()