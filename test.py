import time
lista = [1, 3, 3, 5, 6, 5, 6 ,7 ,1, 3 ,0]
length=len(lista)
porcent=round(100/length)
jump=round(20/length)

for i in range(len(lista)):
    # print(lista[i])
    time.sleep(1)
    if i==length-1:
        print("["+"*"*jump*(i+1)+"]"+"100%")
    else:
        print("["+"*"*jump*(i+1)+"]"+str(porcent*(i+1))+"%")
