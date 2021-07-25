# char_list=["pooja","priyanka","pooja","gayu","priyanka"]
# k=[]
# i=0
# while i<len(char_list):
#     j=0
#     count=0
#     a=[]
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count=count+1
#         j=j+1
#     a.append(char_list[i])
#     a.append(count)
#     if a not in k:
#         k.append(a)
#     i=i+1
# print(k)

l=["pooja","priyanka","pooja","gayu","priyanka"]
i=0
a=[]
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)

