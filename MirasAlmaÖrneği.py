import datetime as dt
class kullanicilar:
    def __init__(self, isim, soy_isim, kullanici_id):
        self.isim = isim
        self.soy_isim = soy_isim
        self.kullanici_id = kullanici_id
        self.yas_hesapla()
    def yas_hesapla(self,dogum):
        dogum = dt.datetime.strptime(dogum, "%d.%m.%Y")
        simdi = dt.datetime.now()
        fark = simdi - dogum
        Yıl = fark.days // 365
        return Yıl


class ogrenci(kullanicilar):
    def __init__(self, ogrenci_no):
        self.ogrenci_no = ogrenci_no
        super().__init__(isim = "zeynep", soy_isim = "Kaya", kullanici_id = 2)
class ogretmen(kullanicilar):
    def __init__(self, email):
        self.email = email
        super().__init__(isim="Mustafa", soy_isim="Topal", kullanici_id=1)


ogretmenn  = ogrenci.yas_hesapla(kullanicilar,"04.04.1980")
ogrencii = ogretmen.yas_hesapla(kullanicilar,"14.07.2000")

print("{} adli öğrencinin yaşi : {}".format("Zeynep",ogrencii))
print("{} adli öğretmenin yaşi : {}".format("Mustafa",ogretmenn))
