a=int(input())
b=int(input())
if(a>b):
    temp=a
    a=b
    b=temp
lst=[]
for k in range(a,b+1):
    lst.append(k)
for i in range(a,b):
    for j in range(i+1,b+1):
        lst.append(i|j)
st=set(lst)
print(len(st))