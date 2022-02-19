
class fatura:
    def __init__(self, hitap_sekli, abone_numarası, tüketim_dönemi, tüketim_tutarı):
        self.hitap_sekli = hitap_sekli
        self.abone_numarası = abone_numarası
        self.tüketim_dönemi = tüketim_dönemi
        self.tüketim_tutarı = tüketim_tutarı

hitap_sekli = "Sayın"
abone_numarası = 1
tüketim_dönemi = "Ocak"
tüketim_tutarı = 1000

print("{} {} nolu abonemiz {} dönemi faturaniz {} TL'dir. Python Belediyesi.".format(hitap_sekli, abone_numarası, tüketim_dönemi, tüketim_tutarı))
