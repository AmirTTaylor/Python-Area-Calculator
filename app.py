import math
# Title

print("========================")
print(" AmirT's Area Calulator")
print("========================")

# Menu
print("Enter a Number to Select an Option:")
choice = int(input( "1) Triangle\n"+
                    "2) Rectangle\n"+
                    "3) Square\n"+
                    "4) Circle\n"+
                    "5) Quit\n" ))

# Make sure the number entered is valid

while choice not in [1,2,3,4,5]:
    choice = int(input("Invalid Choice. Please Enter a Number 1-5: "))

# 1: Triangle

if choice == 1:

    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (base*height)/2

    print("The area of your triangle is " + str(area))

# 2: Rectangle

if choice == 2:

    length = float(input("Length: "))
    width = float(input("Width: "))
    area = (width*length)

    print("The area of your Rectangle is " + str(area))

# 3: Square

if choice == 3:

    side = float(input("Side: "))
    area = (side**2)

    print("The area of your Square is " + str(area))

# 4: Circle

if choice == 4:

    radius = float(input("Radius: "))
    area = math.pi*(radius**2)

    print("The area of your Circle is " + str(area))

# 5: Quit

