not1 = int(input("Lutfen birinci notu girin : "))
not2 = int(input("Lutfen birinci notu girin : "))
ortalama = (not1+not2)/2
if ortalama>=50 and ortalama<60:
  print("Geçtin")
elif ortalama>60 and ortalama<80:
  print("İyi bir ortalama ile geçtin")
elif ortalama>80:
  print("Çok iyi bir ortalama ile geçtin")
elif ortalama<50:
  print("Kaldınız")       