from tkinter import *
# tkinter kütüphanesinden hepsini (all) içeri aktar
import random

pencere = Tk()
pencere.title("Hobi Asistanı Projesi")
pencere.config(background="cyan")
pencere.geometry("500x600+300+100") # widthxheight+x+y

hobi_listesi = [
    "Oyun Geliştirmek",
    "Aile ile zaman geçirmek",
    "Kitap okumak",
    "basketbol oynamak",
    "yüzmek",
    "tenis oynamak",
    "doğa yürüyüşü",
    "futbol oynamak",
    "voleybol oynamak",
    "kodlamak",
    "kitap okumak",
    "sohbet etmek",
    "arkadaşlar ile vakit geçirmek",
    "Yürüyüş yapmak",
    "Kitap okumak",
    "Müzik dinlemek",
    "Yoga yapmak",
    "Resim çizmek",
    "Film izlemek",
    "Bisiklete binmek",
    "Bahçe işleri yapmak",
    "Yemek yapmak",
    "Dans etmek"
]

def hobi_getir():
    # hobi listesinden bir tane hobi seçer
    hobi = random.choice(hobi_listesi)
    # label değişkenine yazı yazıyoruz
    label.config(text = hobi)
    button.config(bg="green")
    pencere.attributes("-fullscreen", True)

label = Label(pencere, text="Henüz hobi seçilmedi.", font=("Helvetica", 16))
label.pack(pady=50) # ekrana çiz

button = Button(pencere, text="HOBİ GETİR", command=hobi_getir, bg="red")
button.place()

def tamEkran():
    pencere.attributes("-fullscreen", True)

# tam ekran modu
button_fs = Button(pencere, text="O", command=tamEkran, bg="red")
button_fs.pack()

def kucukEkran():
    pencere.attributes("-fullscreen", False)

# küçük ekran modu
button_ke = Button(pencere, text="_", command=kucukEkran, bg="red")
button_ke.pack()

# en sona yazılır ana döngü anlamına gelir
pencere.mainloop()