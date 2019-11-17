#From a list of numbers make a new list containing only the even number#
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
evenlist=[]
for num in list:
 if num%2==0:
     evenlist.append(num)
print("The list of even number is: \n")
print(evenlist)



