# f = c * 1.8 + 32

from tkinter import *

pencere = Tk()
pencere.title("🌡️Sıcaklık Dönüşümü(C/F)♨️☀️")
pencere.geometry("330x250+650+250")
pencere.config(bg="#666666") # config -> ayar
pencere.resizable(False,False) # pencereyi ayarlamayı iptal et

pencere_icon = PhotoImage(file="images\sicaklikTermometre.png")
pencere.iconphoto(False,pencere_icon)

def cevir():
    "Bu fonksiyonun görevi C->F çevirmek"
    c = int(entry1.get()) # entry1 girdisini almak
    f = c * 1.8 + 32
    label4.config(text = f)
    entry1.delete(0,"end") # ekranı temizleri

label1 = Label(pencere,
               text = "Sıcaklık Dönüşümü",
               fg="white", # frontground
               bg="black", # background
               font=("Arial 15 bold") 
               )
label1.pack() # ekranda göster

label2 = Label(pencere,
               text = "Sıcaklık Değerini Giriniz (C)",
               fg="white", # frontground
               bg="#666666", # background
               font=("Arial 15 bold") 
               )
label2.pack(pady = 5) # ekranda göster 5 pixel y konumundan boşluk ver

entry1 = Entry(pencere,
               fg="red", # frontground
               bg="cyan", # background
               font=("Arial 15 bold") 
               )
entry1.pack()
entry1.focus() # imlec bu entrye gidecek

cevir_buton = Button(pencere,
                    text = "ÇEVİR (C/F)",
                    fg="white", # frontground
                    bg="#666666", # background
                    font=("Arial 10 bold"),
                    command = cevir # cevir isimli fonksiyon çalışacak
                    )
cevir_buton.pack(pady=5)

label3 = Label(pencere,
               text = "Sıcaklık Değeri (F)",
               fg="white", # frontground
               bg="#666666", # background
               font=("Arial 10 bold") 
               )
label3.pack(pady = 5) 


label4 = Label(pencere,
               text = "",
               fg="lime", # frontground
               bg="#666666", # background
               font=("Arial 15 bold") 
               )
label4.pack(pady = 5) 

mod = True
def mod_degistir():
    global mod
    if mod:
        mod_buton.config(text="LIGHT")
        pencere.config(bg="#999999")
    else:
        mod_buton.config(text="DARK")
        pencere.config(bg="#666666")
    mod = not mod # True ise FAlse, FAlse ise True yap


mod_buton = Button(pencere,
                    text = "DARK",
                    fg="white", # frontground
                    bg="#666666", # background
                    font=("Arial 10 bold"),
                    command = mod_degistir # cevir isimli fonksiyon çalışacak
                    )
mod_buton.pack(pady=5)

# en alt kısım
pencere.mainloop() # ana döngü