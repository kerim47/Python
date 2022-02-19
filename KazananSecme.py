import random
liste = ["haluk","kerim","arda","yusuf","hacı","deliyürek","Musk","muhammed","ali","ömer"]
boş_liste = []
for i in range(0,3):
    boş_liste.append(random.choice(liste))
for i in range(0,3):
    print(boş_liste[i])