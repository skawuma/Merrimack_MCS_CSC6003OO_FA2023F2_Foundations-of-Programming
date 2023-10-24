import math

# Function to find Area of Circle using radius
def area_of_circle(r):
   
    area=  math.pi*r*r
     #use round function to retun to 5 decimal places
    return  round(area,5)

# Function to find circumference of Circle using radius
def circumference_of_circle(r):
   
    circumference= 2 * math.pi*r
     #use round function to retun to 5 decimal places
    return  round(circumference,5)

# Function to find  volume of Circle using radius
def volume_of_circle(r):
   
    volume= (4/3)*math.pi*r*r*r
    #use round function to retun to 5 decimal places
    return round(volume,5)


# Taking radius from user
r = float(input("Enter the radius of circle : "))

# Taking radius measure unit from user
unit = input("Enter the measure unit of radius (e.g. in, cm) : ")


area =area_of_circle(r)
circumference =circumference_of_circle(r)
volume= volume_of_circle(r)

# Print the area
print("The area of a circle with a radius of", r ,"is",area,unit+"2")
# Print the Circumference
print("The circumference of a circle with a radius of" , r ,"is",circumference ,unit)
# Print the Volume
print("The volume of a sphere with a radius of" , r ,"is",volume,unit+"3")
