import tkinter as tk
from PIL import Image, ImageTk
import os # işletim sistemi

FONT = ("Arial", 12, "bold")

# Basit bir hesap bilgisi sözlüğü
hesap_bilgisi = {"hesap_no" : '123456', 'bakiye' : 1000}

def para_cek(miktar):
    if miktar <= hesap_bilgisi["bakiye"]:
        hesap_bilgisi["bakiye"] -= miktar
        bakiye_label.config(text = f"Yeni bakiye={hesap_bilgisi['bakiye']}")
        hata_label.config(text="")
    else:
        hata_label.config(text = "Yetersiz Bakiye !")

def para_ekle(miktar):
    hesap_bilgisi["bakiye"] += miktar
    # config = ayarlamak
    bakiye_label.config(text = f"Yeni bakiye={hesap_bilgisi['bakiye']}")
    hata_label.config(text = "")

def bakiye_goster():
    bakiye_label.config(text = f"Yeni bakiye={hesap_bilgisi['bakiye']}")
    hata_label.config(text = "")

# Resimleri yeniden boyutlandırma işlemi
def resize_image(image, width, height):
    img = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

# Ana pencere oluşturma
root = tk.Tk()
root.title("Bankamatik Uygulaması")
root.config(bg="#AED2FF")

# Bakiye bilgisini görüntüleme
bakiye_label = tk.Label(root, text=f"Bakiye: {hesap_bilgisi['bakiye']}",font=FONT)
bakiye_label.pack(pady=10)


# Para çekme işlemi
cekme_miktari_label = tk.Label(root, text="Çekmek İstediğiniz Miktar:", font=FONT)
cekme_miktari_label.pack()

cekme_miktari = tk.Entry(root)
cekme_miktari.pack(pady=10)

cekme_buton = tk.Button(root, text="Para Çek", bg="lime", font=FONT, command = lambda: para_cek(float(cekme_miktari.get())))
cekme_buton.pack(pady=10)


# Bakiyeyi görüntüleme işlemi
bakiye_goster_buton = tk.Button(root, text="Bakiyeyi Göster", font=FONT, bg="tomato", command = bakiye_goster)
bakiye_goster_buton.pack(pady=10)

# Hata mesajları
hata_label = tk.Label(root, text="", fg="red", font=FONT)
hata_label.pack()

# Eklemek için label
ekleme_label = tk.Label(root, text="Eklemek İçin Tıklayınız", fg="green", font=FONT)
ekleme_label.pack()

# Para resimlerini yükleme ve yeniden boyutlandırma
para_resmi_5 = Image.open(os.path.join("images", "money5.png"))
para_resmi_5 = resize_image(para_resmi_5, 300, 80)

para_resmi_20 = Image.open(os.path.join("images", "money20.png"))
para_resmi_20 = resize_image(para_resmi_20, 300, 80)

para_resmi_100 = Image.open(os.path.join("images", "money100.png"))
para_resmi_100 = resize_image(para_resmi_100, 300, 80)

# Para yatırma işlemi
para_ekle_buton_5 = tk.Button(root, image=para_resmi_5, command = lambda: para_ekle(5))
para_ekle_buton_5.pack()

para_ekle_buton_20 = tk.Button(root, image=para_resmi_5, command = lambda: para_ekle(20))
para_ekle_buton_20.pack()

para_ekle_buton_100 = tk.Button(root, image=para_resmi_5, command = lambda: para_ekle(100))
para_ekle_buton_100.pack()


root.mainloop()
