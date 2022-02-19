def vucutKitleEndeksi(boy, kilo):
    endeks = kilo/(boy/100*boy/100)
    if endeks < 18.5:
      print("Zayıfsınız")
    elif endeks>18.5 and endeks<25:
      print("Normalsiniz")
    elif endeks > 25 and endeks < 30:
      print("Kilolusunuz")
    elif endeks > 30:
      print("Obezsiniz")
boy = int(input("Boy  girin :"))
kilo = int(input("Kilo girin :"))
vucutKitleEndeksi(boy,kilo)