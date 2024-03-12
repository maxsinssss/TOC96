import re 
email_cond = "^[a-z]+[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email: ")
if re.search(email_cond,user_email):
    print("Valid Email!")
else:
    print("Invalid Email!")