from tkinter import * 
import random
# * all -> hepsi
# import -> içeri aktar
pencere = Tk()
pencere.title("İlk Tkinter Projem") # string
pencere.geometry("600x600")
pencere.config(background="red")

etiket = Label(pencere, text="Bu buton renk değiştirir")
etiket.pack()

renk_listesi = ["red", "green", "blue", "yellow"]

def change_color():
    print("renk değişti")
    renk = random.choice(renk_listesi)
    pencere.config(background=renk)

button = Button(pencere, text="TIKLA", command=change_color)
button.pack()

pencere.mainloop() # ana döngü