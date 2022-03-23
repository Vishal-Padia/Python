#Define and call function

def addition(number1, number2):
    result = number1 + number2
    print("Addition result: ", result)

def area(radius):
    result = 3.14 * radius * radius
    return result

addition(300, 200)
print("Area of the circle is", area(4))
