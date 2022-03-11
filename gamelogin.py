import time
import random


mail = input("Enter a valid email :")
mail_pw = input("Enter the password of your email :")
print(" ")
print("Please wait until we verify your account... ")

delay = rand_num = random.randint(1, 10)
time.sleep(delay)
print(f"Time taken to verify {delay} seconds ")

print("Your account has been verified")
print(" ")

x = True
while x:
    user_name = input("Enter your name for this virtual world : ")
    if 3 < len(user_name) < 15:
        break
    else:
        print("Character should be between 3-15")

age_limit = 18

y = True
while y:
    user_age = int(input(f"{user_name} Enter your age :"))
    if user_age >= age_limit:
        break
    else:
        print("According to policies you should be above 18 years to play this game ")
        exit()

delay_1 = rand_num_1 = random.randint(4, 10)
time.sleep(delay_1)

intro = """
This Game Is based in virtual world
Please don't imitate it at home or with friends 
"""
print(f"        {intro}        ")

delay_2 = rand_num_2 = random.randint(5, 10)
time.sleep(delay_2)

print("        *        " * 20)
print("                                      WELCOME TO THE GAME                                        ")
print("        *        " * 20)
tri = rand_num_3 = random.randint(5, 7)

import random

tri = rand_num_3 = random.randint(5, 7)

trian = 1
while trian < tri:
    print(" * " * trian)
    trian = trian + 1

print(" ")
print("*" * 40)

