#Ask the user to enter 10 number using only one input statement#
x=1
list=[]
for x in range(1,11,1):
    num1=input("Enter the number")
    list.append(int(num1))
    list.sort()
    print(list)
    print("List is obtained")