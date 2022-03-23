#Add and Seach data in the dictionary

customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali', '02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}
customers['05634'] = 'Mehboba Ferdous'

print("The customer names are : ")
for customer in customers:
    print(customers[customer])

name = input("Enter the custormer ID: ")

for customer in customers:
    if customer == name:
        print(customers[customer])
        break