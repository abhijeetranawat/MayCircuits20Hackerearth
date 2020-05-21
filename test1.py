for i in range(2):
    lst=[]
    for i in range(35,21,-1):
        for j in range(35,21,-1):
            lst.append(i|j)
    print(len(lst))
    print(set(lst),len(set(lst)))
#done