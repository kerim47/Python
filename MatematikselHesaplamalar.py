import math
def logaritma(sayi):
    sayi = math.log10(sayi)
    return float(sayi)
def karekok(sayi):
    sayi = math.sqrt(sayi)
    return float(sayi)
def mutlak_deger(sayi):
    sayi = math.fabs(sayi)
    return float(sayi)
while True:
    try:
        sayi = int(input("Lutfen bir sayi giriniz : "))
        islem = int(input("Logaritma[1] Karekok[2] Mutlak değer[3] çıkış[4]"))

        if islem == 1:
            dosya = open("deneme.txt", "w+")
            dosya.write(str(logaritma(sayi)))
            dosya.close()
        elif islem == 2:
            dosya = open("deneme.txt", "w+")
            dosya.write(str(karekok(sayi)))
            dosya.close()
        elif islem == 3:
            dosya = open("deneme.txt", "w+")
            dosya.write(str(mutlak_deger(sayi)))
            dosya.close()
        elif islem == 4:
            break
        else:
            print("Belirtilen aralıklarda değer girin :")
    except:
        print("Geçerli bir değer girin:")