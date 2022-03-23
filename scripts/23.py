#Use throw and catch exception

try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

except (ValueError):
    print("Enter a numeric value")