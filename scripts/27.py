#Define class and methods

class Employee:
    name = "Elon Musk"
    def details(self):
        print("Post: Marketing Staff")
        print("Department: Sales")
        print("Salary : $100000")

emp = Employee()
print("Name: ",emp.name)
emp.details()