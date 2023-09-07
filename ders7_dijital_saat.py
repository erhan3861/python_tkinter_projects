import tkinter as tk
import time
from datetime import datetime, timedelta

def update(): # güncelle
    for city, offset, label in clock_labels:
        simdiki_zaman = get_time(offset)
        label.config(text = f"{city} : {simdiki_zaman}", bg="#B9DD9B")
    # zamanı tekrarlamak
    pencere.after(1000, update) # 1 saniye sonra zamanı güncelledik

def get_time(offset):
    yerel_zaman = datetime.now()
    hedef_zaman = yerel_zaman + timedelta(hours = offset)
    formatlanmis_zaman = hedef_zaman.strftime("%H:%M:%S")
    return formatlanmis_zaman

def show():
    city_frame.pack()

def add_city():
    city_name = city_entry.get() # şehir bilgisini alıyor
    try:
        offset = int(offset_entry.get())
        label = tk.Label(pencere, text=city_name, font=("arial 20"), bg = "#B9DD9B", fg="black")
        label.pack()
        clock_labels.append((city_name, offset, label))
        city_entry.delete(0, tk.END)
        offset_entry.delete(0, tk.END)
        # city_frame ekrandan temizlemek
        city_frame.pack_forget() # frame'i unut -> ekrandan sil
    except:
        # burası hata aldığımızda çalışır
        print("Lütfen saat farkını sayı giriniz")



pencere = tk.Tk()
pencere.title("🌍 Dünya Saatleri 🕰️")
pencere.geometry("600x400+700+350")
pencere.config(bg="#B9DD9B")

saat_label = tk.Label(pencere,
                      text = "⏲️Dijital Saat⏲️",
                      font=("arial 20"),
                      bg = "#B9DD9B", # background
                      fg = "blue") # foreground
saat_label.pack(pady = 20)


clock_labels = [
    ("İstanbul", 0), # tuple  tipi -> demet
    ("Berlin", -1),
    ("New york", -7)
]

sira = 0 # index
for city, offset in clock_labels:
    label = tk.Label(pencere, text=city, font=("arial 20"), bg = "#B9DD9B", fg="black")
    label.pack()

    clock_labels[sira] = (city, offset, label)
    sira += 1

# şehir ekle butonu
add_button = tk.Button(pencere, text="Şehir Ekle", font=("arial 12 bold"), command=show)
add_button.pack(pady=10) # padding yukarıdan 10 px boşluk bırak

# şehir frame -> çerçeve kodları
city_frame = tk.Frame(pencere, bg = "#B9DD9B")
# dikkat -> pack yapmıyoruz

city_label = tk.Label(city_frame, text="Şehir Adı:", font=("arial 12 bold"), bg="#B9DD9B")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(city_frame, font=("arial 12"))
city_entry.grid(row=0, column=1, padx=10, pady=10)

# saat farkı kodları
offset_label = tk.Label(city_frame, text="Saat Farkı:", font=("arial 12 bold"), bg="#B9DD9B")
offset_label.grid(row=1, column=0, padx=10, pady=10)

offset_entry = tk.Entry(city_frame, font=("arial 12"))
offset_entry.grid(row=1, column=1, padx=10, pady=10)


add_button_in_frame = tk.Button(city_frame, text="Kaydet", font=("arial 12 bold"), command=add_city)
add_button_in_frame.grid(row=2, columnspan=2, padx=10, pady=10)

update()

pencere.mainloop()