import tkinter as tk
from tkinter import messagebox

products = {
    "Kalem": {"fiyat": 2.5, "stok": 100},
    "Defter": {"fiyat": 5.0, "stok": 50},
    "Silgi": {"fiyat": 1.0, "stok": 200}
    # Diğer ürünleri ekleyin
}

def show_product():
    selected_product = product_listbox.get(tk.ACTIVE)
    product_info = products.get(selected_product) # products isimli sözlüğün anahtarını kullandk
    if product_info:
        messagebox.showinfo(
            "Ürün Bilgileri",
            f"{selected_product}\nFiyat: {product_info['fiyat']} TL\nStok: {product_info['stok']} adet",
        )
    else:
        messagebox.showerror("Hata", "Ürün bulunamadı.")


pencere = tk.Tk()
pencere.title("Kırtasiye Ürünleri")
pencere.geometry("300x400")

product_listbox = tk.Listbox(pencere)

for product in products:
    product_listbox.insert(tk.END, product) # listbox sonuna ürün ismi yerleştir
product_listbox.insert(tk.END, "etiket")
product_listbox.pack()

show_button = tk.Button(pencere, text="Ürün Bilgisi Göster", command=show_product)
show_button.pack()

pencere.mainloop()


