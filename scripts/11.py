#Run python script from another
import vacation as vac

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

flag = 0
for month in months :
    if month == "June" or month == "July":
        if flag == 0:
            print("Now",vac.vacation1)
    elif month == "December":
        print("Now",vac.vacation2)
    else:
        print("The Current month is :" , month)