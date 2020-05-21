x,n=map(int,input().split())
if(n>9):
    print(1)
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    fact=fact%10
    print(pow(x,fact)%10)