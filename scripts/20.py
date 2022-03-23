#Add or search data in set:

numbers = {23, 90, 56, 78, 90, 12, 67}
numbers.add(50)

print(numbers)

message = "Number not found"

search_number = int(input("Enter a number: "))
for val in numbers:
    if val == search_number:
        message = "Number Found"
        break

print(message)