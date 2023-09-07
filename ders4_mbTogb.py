import tkinter as tk

pencere = tk.Tk()
pencere.title("💻 MB --> GB 💻")
pencere.geometry("350x250") # pencere 350 genişlik 250 yükseklik
pencere.resizable(False, False) # pencereyi büyüt / küçült özelliği olmasın

def hesapla():
    mb = float(mb_entry.get()) # get() bilgiyi alır
    gb = mb / 1024
    gb_entry.insert(tk.END, round(gb, 3)) # gb_entry sonuna yerleştirmek

def temizle():
    mb_entry.delete(0, "end") # silmek
    gb_entry.delete(0, tk.END)

resim = tk.PhotoImage(file="images/mb.png")
resim_label = tk.Label(pencere, image = resim) # etiket demek
resim_label.place(x=-45, y=-150) # yerleştirmek

mb_label = tk.Label(pencere, text="Magabytes (MB)")
mb_label.place(x=10, y=150)

gb_label = tk.Label(pencere, text="Gigabytes (GB)")
gb_label.place(x=10, y=175)

mb_entry = tk.Entry(pencere)
mb_entry.place(x=120, y=150)
mb_entry.focus()

gb_entry = tk.Entry(pencere)
gb_entry.place(x=120, y=175)

hesapla_buton = tk.Button(pencere,
                          text = "HESAPLA",
                          command = hesapla) # command -> komut
hesapla_buton.place(x=100, y=200)

temizle_buton = tk.Button(pencere,
                          text = "TEMİZLE",
                          command = temizle
                          )
temizle_buton.place(x=170, y=200)

pencere.mainloop() # ana döngü