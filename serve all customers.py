m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
lst=[]
for i in range(n):
    lst.append(a[i]+b[i])
    print(a[i],end=" ")
lst=sorted(lst)
for j in range(i+1,m):
    if(a[j]>=lst[0]):
        print(a[j], end=" ")
        lst[0]=lst[0]+b[j]
    else:
        print(lst[0],end=" ")
        lst[0]=lst[0]+b[j]
    sorted(lst)

