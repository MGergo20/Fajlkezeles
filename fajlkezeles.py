import random

def lista_letrehozasa():
    #generálj 100 véletlen egész számot [-50, 150] között
    #A függvény térjen vissza a listával
    lista=[]
    for i in range(0, 100, 1):
        szam:int=int(random.random()*(151+50)-50)
        lista.append(szam)
    return lista




#a listában lévő számokat fűzd össze stringgé, az elválasztó jel ;
#legyen az utolsó után ne legyen ;

def szovegge_alakít(lista):
    szoveg:str=""
    for i in range(0,len(lista),1):
        if (i<len(lista)-1):
            szoveg+=f"{lista[i]};"
        else:
            szoveg+=f"{lista[i]}"

    return szoveg



def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()



def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str=fajlom.read()
    szoveges_lista=szoveg_fajlbol.split(";")
    """"Végigmegy a szöveglistán, és minden elemét számmá alakítom
    és eltávolítom belőle a felesleges szóközöket"""
    lista=[]
    for i in range (0, len(szoveges_lista),1):
            szam:int=int(szoveges_lista[i].strip())
            lista.append(szam)
    '''print(szoveg_fajlbol)
    print(lista)'''
    fajlom.close()
    return lista
