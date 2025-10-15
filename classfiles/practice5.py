username =input("Enter username")
password =input("Enter password")

if username == "admin":
    if password =="1234":
        print("access granted")
    else:
        print("wrong password")
else:
    print("invalid user name")

   