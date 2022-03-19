#Use of getpass

import getpass

passwd = getpass.getpass('Password: ')

if passwd == "root123":
    print("You are authenticated")
else:
    print("You are not authenticated")
