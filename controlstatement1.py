# control statement activity 1
x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
if x != y and y != z and z!= x :
    print("All numbers are different")
elif x == y and y == z and z == x :
    print("All numbers are equal")
else:
    print("Neither all are equal or different")