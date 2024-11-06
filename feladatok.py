def negativ_szam(lista):
    print(lista)
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            db+=1
        i+=1
    return db   

def legnagyobb_szam(lista):
    max_index:int=0
    for i in range (0, len(lista), 1):
        if (lista[i]>lista[max_index]):
            max_index=i
    return lista[max_index]


def paros_szamok(lista):
    print(lista)
    i:int=0
    db:int=0
    while(i>len(lista)):
        if(lista[i]==0):
            db+=1
        i+=1
    return db 