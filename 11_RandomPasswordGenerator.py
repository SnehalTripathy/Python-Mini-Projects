import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$&_"
password_length = int(input("Enter the length of the password: "))
a = "".join(random.sample(password, password_length))
print(f"Your random password is: {a}")
