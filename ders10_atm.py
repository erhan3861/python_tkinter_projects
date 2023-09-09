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











