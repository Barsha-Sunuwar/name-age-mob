#Write a program to print the multiplication table of the number entered by the user#
number=int(input("Enter number to be mutiplied"))
for multiplication in range(1,11):
    print("multiplication is")
    print("%d * %d =%d" %(number,multiplication,number*multiplication))