# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(i,end=" ")
#         j=j+1
#     i=i+1
#     print()
    
  
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=5:
#         print(j,end=" ")
#         j=j+1
#     i=i+1
#     print()




# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     k=1
#     while k<=i:

#         print("*",end=" ")
#         k=k+1
#     i=i+1
#     print()


n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print(i,end=" ")
        else:
            print("*",end=" ")
        j=j+1
    i=i+1
    print()



# n=int(input("enter the number"))
# i=1
# v=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(v,end=" ")
#         j=j+1
#         v=v+1
#     i=i+1
#     v=v-1
#     print()