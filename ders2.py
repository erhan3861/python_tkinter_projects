from tkinter import *
# tkinter kütüphanesinden hepsini (all) içeri aktar

pencere = Tk()
pencere.title("İkinci Tkinter Projesi")
pencere.config(background="cyan")
pencere.geometry("500x600+500+200") # widthxheight+x+y

# yeniden boyutlandırma
pencere.resizable(width=True, height=True)

# tam ekran kodu
pencere.attributes("-fullscreen", True)

pencere.mainloop() # ana döngü

# basketbol oynamak
# yüzmek
# tenis oynamak
# doğa yürüyüşü
# futbol oynamak
# voleybol oynamak
# kodlamak
# kitap okumak
# sohbet etmek
# arkadaşlar ile vakit geçirmek