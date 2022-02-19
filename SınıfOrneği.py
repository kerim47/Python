class user:
   def __init__(self, name, surname, phone_no):
     self.name = name
     self.surname = surname
     self.phone_no = phone_no
adı = input("Adinizi giriniz :")
soyadı = input("Soyadinizi giriniz :")
telefon_no = int(input("Telefon no giriniz :"))
adi = user(adı, soyadı, telefon_no)
print("Adı : {}\nSoyadı : {}\n  Telefon no: {}".format(adı, soyadı, telefon_no))