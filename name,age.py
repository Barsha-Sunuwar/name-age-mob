name=input("Enter your name")
if name.isalpha()==False or len(name) <3:
    print("your name should be character and must be more than 2 digit")
else:
    age=int(input("Enter your age"))
    if age<19:
        print("your age must be more than 18")
    else:
        mobile=input("Enter your mobile number")
        if len(mobile)!=10 or mobile.isalpha()==True:
            print("your number should be 10digit and should not be character ")
        else:
            print("Your name is ",name)
            print("Your age is ",age)
            print("your mobile number is ",mobile)
