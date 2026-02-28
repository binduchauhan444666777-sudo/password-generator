
#password generator
import random 
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+'

length = int(input("enter length of the password :"))
password = ""
for i in range(length):
    password += random.choice(characters)
    
print("your generated password : " , password)



