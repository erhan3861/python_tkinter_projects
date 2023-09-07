import tkinter as tk
from tkinter import messagebox

dictionary = {
    "hello": "merhaba",
    "world": "dünya",
    "apple": "elma",
    # Diğer kelimeleri ekleyin
}

def translate_word():
    word = entry.get().lower()  # Kullanıcının girdiği kelimeyi alın
    translation = dictionary.get(word, "Kelime bulunamadı.")
    label_result.config(text=translation)
    # messagebox.showinfo("Çeviri", f"{word}: {translation}")

root = tk.Tk()
root.title("İngilizce-Türkçe Sözlük")
root.geometry("300x400")

label = tk.Label(root, text="Bir kelime girin:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Çevir", command=translate_word)
button.pack(pady=20)

label_result = tk.Label(root, text="")
label_result.pack(pady=20)

root.mainloop()