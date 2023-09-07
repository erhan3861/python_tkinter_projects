"""
    Ben --------- AI
1 - Tas           Makas
2 - Kagit         Tas
3 - Makas         Kagit
"""

import tkinter as tk # modül
import random as r
import os # işletim sistemi

# pencere
pencere = tk.Tk()
pencere.title("🪨📜✂️ Oyunu")
pencere.geometry("400x250+700+350") # yatay -> 400 dikey -> 250
pencere.config(bg="#5A67BD") # arkaplan rengini ayarla

# tüm işletim sistemlerinde çalışacak kod
icon = tk.PhotoImage(file = os.path.join("images", "logotkm.png")) # G
pencere.iconphoto(False, icon)

ai_tercih_list = ["taş", "kağıt", "makas"]

def kim_kazandi(insanTercihi):
    insan_label.config(text  = f"İnsan \n\n {insanTercihi}")
    ai_tercih = r.choice(ai_tercih_list) # rastgele seçenek
    ai_label.config(text  = f"AI \n\n {ai_tercih}")

    # algoritma
    if insanTercihi == ai_tercih:
        sonuc_label.config(text="BERABERE")
    elif insanTercihi == "taş" and ai_tercih == "makas":
        sonuc_label.config(text="KAZANDINIZ")
    elif insanTercihi == "kağıt" and ai_tercih == "taş":
        sonuc_label.config(text="KAZANDINIZ")
    elif insanTercihi == "makas" and ai_tercih == "kağıt":
        sonuc_label.config(text="KAZANDINIZ")
    else:
        sonuc_label.config(text="KAYBETTİNİZ")

tas_btn = tk.Button(pencere,
                    text = "TAŞ",
                    width = 10,
                    command = lambda : kim_kazandi("taş") # Günlük
                    )
tas_btn.pack(pady=10)


kagit_btn = tk.Button(pencere,
                    text = "KAĞIT",
                    width = 10,
                    command = lambda : kim_kazandi("kağıt") # Günlük
                    )
kagit_btn.pack(pady=10)

makas_btn = tk.Button(pencere,
                    text = "MAKAS",
                    width = 10,
                    command = lambda : kim_kazandi("makas") # Günlük
                    )
makas_btn.pack(pady=10)



sonuc_label = tk.Label(pencere,
                       text = "?",
                       bg = "#5A67BD",
                       font = ("Arial 18 bold") # yazı tipi
)
sonuc_label.pack()


insan_label = tk.Label(pencere,
                       text = "İnsan \n\n ?",
                       bg = "light blue",
                       width = 6,
                       font = ("Arial 18 bold") # yazı tipi
)
insan_label.place(x=15, y=5)


ai_label = tk.Label(pencere,
                       text = "AI \n\n ?",
                       bg = "light blue",
                       width = 6,
                       font = ("Arial 18 bold") # yazı tipi
)
ai_label.place(x=295, y=5)


pencere.mainloop()
