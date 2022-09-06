from ast import Num


num=int(input("enter the number"))
b=num
c=str(num)
n=len(c)
sum=0
for i in c:
    sum=sum+int(i)**n
if sum==b:
    print("armstrong number")
else:
    print("not a armstrong number")