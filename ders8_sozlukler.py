# sozluk -> dictionary

sozluk = {"number" : "numara"} 

# sözlüğe eleman ekleme
sozluk["notebook"] = "defter"
print(sozluk)

sozluk["ball"] = "top"
print(sozluk) 

# eleman sayısını bulma
# {'number': 'numara', 'notebook': 'defter', 'ball': 'top'}
print(len(sozluk)) # 3 

# sözlüğün anahtarlarını bulmak
keys = sozluk.keys()
print(list(keys)) # ['number', 'notebook', 'ball']

# sözlüğün değerlerini (values) bulmak
values = sozluk.values() 
print(list(values)) # ['numara', 'defter', 'top']

# hem keys hem de values elde etmek
items = sozluk.items()
print(list(items)) # [('number', 'numara'), ('notebook', 'defter'), ('ball', 'top')]

# sözlüğü bastırmak istiyoruz
print("Sözlüğümde ne var?")
print("*" * 20)

for key,value in sozluk.items():
    print(key, " = ", value)

print("*" * 20)

print("""Kelime Kutusuna Hoşgeldiniz 
      Eklemek(e) Çıkarmak(ç) 
      Göster(g) Çıkmak(q)""")

while True:
    secenek = input("Seçeneği giriniz : ")

    if secenek == "q":
        print("çıkılıyor")
        break
    elif secenek.lower() == "e":
        kelime = input("kelimenizi giriniz = ")
        anlam = input("anlamını giriniz = ")
        sozluk[kelime] = anlam
        print("kelimeniz eklenmiştir")

    elif secenek.lower() == "g": # büyük harfi küşük harfe çevirir
        print("*" * 20)
        for kelime, anlam in sozluk.items():
            print(kelime," : ", anlam)
        print("*" * 20)

    elif secenek.lower() == "ç":
        key = input("çıkarmak istediğini kelimenizi giriniz = ")
        if key in sozluk: # eğer key sözlüğün bir anahtarıysa
            sozluk.pop(key)
        else:
            print("Girmiş olduğunuz kelime bulunamadı...")





    