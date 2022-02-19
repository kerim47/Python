anahtar1 = input("İsminizi girin : ")
anahtar2 = input("Soy isminizi girin : ")
anahtar3 = int(input("Telefon no girin : "))
anahtar4 = input("Ev adresi girin : ")


sozluk = {
    "isim":anahtar1,
    "soyisim":anahtar2,
    "telefon_no":anahtar3,
    "ev_adresi":anahtar4
}

print("{} {} {} {}".format(sozluk["isim"], sozluk["soyisim"], sozluk["telefon_no"], sozluk["ev_adresi"]))