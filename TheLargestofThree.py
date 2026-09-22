x = int(input("Please Type First Number: "))
y = int(input("Please Type Secong Number: "))
z = int(input("Please Type Third Number: "))

if x > y and x > z:
    largest = x
    print("The largest is: ", x)
elif y > x and y > z:
    largest = y
    print("The largest is: ", y)
elif z > x and z > y:
    largest = z
    print("The largest is: ", z)
else:
    print("There no Largest Number")
