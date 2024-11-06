import fajlkezeles, feladatok

"""lista=fajlkezeles.lista_letrehozasa()
print(lista)

sz:str=fajlkezeles.szovegge_alakít(lista)
print(sz)
fajlkezeles.fajlba_mentes(sz)"""
lista=fajlkezeles.fajlbol_olvas()
print(lista)


db:int=feladatok.negativ_szam(lista)
print(f"Ennyi negatív szám van: {db}")

legnagyobb:int=feladatok.legnagyobb_szam(lista)
print(f"Legnagyobb szám: {legnagyobb}")

paros:int=feladatok.paros_szamok(lista)
print(f"Paros szamk összege: {paros}")
