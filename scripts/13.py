#use of regex
import re

string = input("Enter a String value: ")
pattern = '^[A-Z]'

found = re.match(pattern, string)

if found:
    print("The input value is started with the capital letter")
else:
    print("You have to type string start with the capital letter")