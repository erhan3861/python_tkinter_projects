from tkinter import * # * anlamı all
import datetime # tarih, zaman, modül
from tkinter import messagebox # mesaj kutusu dw
from tkinter.colorchooser import askcolor

pencere = Tk()
pencere.title("Age Calculator")
pencere.geometry("350x200+600+350") # 350 yatay 150 dikey genişlik 600 sağdan, 350 yukarıdan boşluk bırak
pencere.resizable(False, False) # yatayda ve dikeyde yeniden boyutlandırma

icon = PhotoImage(file = "images/yashesaplama0.png")
pencere.iconphoto(False, icon)

def hesapla():  # Function definition
    isim = isim_entry.get() # get-> almak, getir
    bugun = datetime.date.today() # bugün bilgisi
    yil = bugun.year # bugün hangi yıl onu bulduk

    dogum_yili = int(yil_entry.get()) # sayıya çevirdik
    yas = yil - dogum_yili
    mesaj = f"Sevgili {isim}, {yas} yaşındasın."
    messagebox.showinfo("Age Calculator", mesaj)

def temizle():
    isim_entry.delete(0, "end")
    yil_entry.delete(0, "end")
    ay_entry.delete(0, "end")
    gun_entry.delete(0, "end")

def renk_degistir():
    color = askcolor()[1]
    pencere.config(bg = color)

isim_label = Label(pencere,
                   text = "Adınız : ",
                   font = ("Helvatica 12 bold")
                   )
isim_label.grid(row=0, column=0)

yil_label = Label(pencere,
                   text = "Yıl : ",
                   font = ("Helvatica 12 bold")
                   )
yil_label.grid(row=1, column=0)


ay_label = Label(pencere,
                   text = "Ay : ",
                   font = ("Helvatica 12 bold")
                   )
ay_label.grid(row=2, column=0)


gun_label = Label(pencere,
                   text = "Gün: ",
                   font = ("Helvatica 12 bold")
                   )
gun_label.grid(row=3, column=0)

isim_entry = Entry(pencere,
                   font = ("Helvatica 12 bold")
)
isim_entry.grid(row=0, column=1)
isim_entry.focus()

yil_entry = Entry(pencere,
                   font = ("Helvatica 12 bold")
)
yil_entry.grid(row=1, column=1)

ay_entry = Entry(pencere,
                   font = ("Helvatica 12 bold")
)
ay_entry.grid(row=2, column=1)

gun_entry = Entry(pencere,
                   font = ("Helvatica 12 bold")
)
gun_entry.grid(row=3, column=1)

resim = PhotoImage(file="images/yashesaplama1.png")
resim_label = Label(pencere,
                    image = resim
                    )
resim_label.grid(row = 0, column=2, rowspan=4)

hesapla_buton = Button(pencere,
                        text = "Hesapla",
                        width = 10,
                        command = hesapla # Function call
)
hesapla_buton.grid(row=4, column=1, sticky = W) # West -> batı sol kenar

temizle_buton = Button(pencere,
                        text = "Temizle",
                        width = 10,
                        command =  temizle # Function call
)
temizle_buton.grid(row=4, column=1, sticky = E)  # East -> sağ  kenar

renk_buton = Button(pencere,
              text = "Renk Seç",
              width = 10,
              command =  renk_degistir
 ) # Function call)
renk_buton.grid(row=5, column=1)


pencere.mainloop() # ana döngü
