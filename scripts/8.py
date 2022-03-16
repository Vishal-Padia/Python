#Using Switch case
def employee_details(ID):
	swithcer = {
	    "1004" : "Employee Name : Johnny Deep",
	    "1009" : "Employee Name : Ryan Reynolds",
	    "1010" : "Employee Name : Steve Carell" }
	return swithcer.get(ID, "nothing")
ID = input("Enter your Employee ID ")
print(employee_details(ID))
