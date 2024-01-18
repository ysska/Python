# Activity 2 Python Functions to calculate the factorial of a number
def function(x):
    if x <= 1:
        return 1

    return x * function(x - 1)
print("The factorial of a number 6 is: ", function(6))
