# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# if a<b<c:
#     print(c)
# elif a<b>c:
#     print(b)
# else:
    # print(a)


# b=12
# c=pooja
# d=str(c)
# print(d+c)

# a="18"
# b=45
# c=int(a)
# print(c+b)


# n=int(input("enter a number "))
# i=0
# m=1
# while i<=n:
#     a=n%10+n%10+n%10
#     m=m*a
#     s=m%10+m%10+m%10
#     d=s*n
#     i=i+1
# print(d)




# user=int(input("enter a number: "))
# i=1
# a={}
# while i<=user:
#     name=str(input("enter a name:"))
#     age=int(input("enter a age:"))
#     while i<=len(name):
#         a.update({name:age})
#         i=i+1
#         break
# print(a)


name=input("entrr a name :")
i=0
while i<len(name):
    print(name.upper()[i],end=" ")
    if i!=len(name):
        print("_",end=" ")
    print(name.lower()[i],end=" ")
    print()
    i=i+1
    