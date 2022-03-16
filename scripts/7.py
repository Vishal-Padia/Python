#Use of AND & OR operators
mcq_marks = float(input("Enter you MCQ marks "))
theory_marks = float(input("Enter your theory marks "))
if (mcq_marks >= 40 and theory_marks >=30) or (mcq_marks + theory_marks) >= 70:
	print("\n You have passed moron")
else:
	print("\n You failed moron")
