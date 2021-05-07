a=[]
for i in range(1,5):
    a.append("#")
    print(*a)
for i in range(1,4):
    del a[0]
    print(*a)