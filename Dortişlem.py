try:
    while True:
        işlem = int(input("Yapmak istediğiniz işlemi seçin(1-toplama | 2-çıkarma | 3-bölme | 4-çarpma | 5-çıkış): )"))
        if işlem > 0 and işlem < 6:
            if işlem == 5:
                break;
            sayi1 = int(input("Birinci sayiyi girin : "))
            sayi2 = int(input("İkinci sayiyi girin : "))
        if işlem == 1:
            sonuç = sayi1 + sayi2
            print("Sonuç : {}".format(sonuç))
        elif işlem == 2:
            sonuç = sayi1 - sayi2
            print("Sonuç : {}".format(sonuç))
        elif işlem == 3:
            sonuç = sayi1 / sayi2
            print("Sonuç : {}".format(sonuç))
        elif işlem == 4:
            sonuç = sayi1 * sayi2
            print("Sonuç : {}".format(sonuç))
        else:
            print("Lutfen belirtilen aralıklar arasında işlem değerlerini giriniz : ")

except ValueError as err:
    print("Lutfen deger giriniz.")
except ZeroDivisionError:
    print("Sıfıra bölemezsiniz.")