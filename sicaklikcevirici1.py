# f = c * 1.8 + 32

import tkinter as tk

pencere = tk.Tk()
pencere.title("🌡️Sıcaklık Dönüşümü(C/F)♨️☀️")
pencere.geometry("330x250+650+250")
pencere.config(bg="#666666")
pencere.resizable(False,False)

pencere_icon = tk.PhotoImage(file="images/sicaklikTermometre.png")
pencere.iconphoto(False,pencere_icon)

def pencereyi_kapat():
    pencere.destroy()

def cevir():
    
    c = int(e1.get())
    f = c * 1.8 + 32
    label4.config(text=f)
    e1.delete(0,"end")

label1 = tk.Label(pencere,
              text="Sıcaklık Dönüşümü",
              fg="white",
              bg="black",
              font=("Arial 15 bold")
              )
label1.pack()

label2 = tk.Label(pencere,
              text="Sıcaklık Değerini Giriniz(C): ",
              fg="white",
              bg="#666666",
              font=("Arial 15 bold")
              )
label2.pack()

e1 = tk.Entry(pencere,
              font=("arial 15"),
              fg="red",
              bg="cyan")
e1.pack()
e1.focus()

cevir_buton = tk.Button(pencere,
                        text="Çevir(C/F)",
                        font=("arial 10"),
                        fg="white",
                        bg="#666666",
                        width=10,
                        command=cevir)
cevir_buton.pack(pady=5)

label3 = tk.Label(pencere,
                  text="Sıcaklık Değeri(F)",
                  font=("arial 10 bold"),
                  fg="white",
                  bg="#666666")
label3.pack()

label4 = tk.Label(pencere,
                  text="...........",
                  font=("arial 10 bold"),
                  fg="lime",
                  bg="#666666")
label4.pack()

kapat_buton = tk.Button(pencere,
                        text="Kapat",
                        font=("arial 10"),
                        fg="white",
                        bg="#666666",
                        width=10,
                        command=pencereyi_kapat)
kapat_buton.pack(pady=5)
pencere.mainloop()