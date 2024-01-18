# control statement activity 1
x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
if x > y and y > z and z < x :
    print("Decreasing order")
elif z > y and y > x and x < z :
    print("Increasing order")
else:
    print("Neither increasing or decreasing order")