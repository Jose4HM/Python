import random
c1=0
c2=0
c3=0
ctg=0
cga=0
win=0
i=0
partida=0
prom=[]
j=0
while j<1000:
    while i<1000:
        while ctg<1000:
            ctg=ctg+1
            r1=random.randint(1, 6)
            r2=random.randint(1, 6)
            if r1+r2==7:
                c1=c1+1               
                win=win+1
                break        
            else:
                ctg=ctg+1
                r1=random.randint(1, 6)
                r2=random.randint(1, 6)
                if r1+r2==7:
                    c2=c2+1
                    break
                else:
                    ctg=ctg+1
                    r1=random.randint(1, 6)
                    r2=random.randint(1, 6)
                    if r1+r2==7:
                        c3=c3+1
                    break
                    break          
                break      
        break
        partida=partida+1
        i=i+1
    break
    p=win/partida
    prom.append(p)
    j=j+1

