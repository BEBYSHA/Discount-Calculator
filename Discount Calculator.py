import tkinter as tk
from tkinter import messagebox

def hitung_diskon():
    try:
        harga = float(entry_harga.get())
        jumlah = int(entry_jumlah.get())
        diskon = float(entry_diskon.get())

        if harga < 0 or jumlah <= 0 or diskon < 0:
            raise ValueError

        total_awal = harga * jumlah
        nilai_diskon = total_awal * (diskon / 100)
        total_akhir = total_awal - nilai_diskon

        label_total_awal.config(text=f"Rp {total_awal:,.2f}")
        label_diskon.config(text=f"Rp {nilai_diskon:,.2f}")
        label_total_akhir.config(text=f"Rp {total_akhir:,.2f}")

    except ValueError:
        messagebox.showerror("Input Salah", "Masukkan angka yang valid!")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Diskon")
root.geometry("350x350")
root.resizable(False, False)

# Judul
judul = tk.Label(root, text="KALKULATOR DISKON", font=("Arial", 14, "bold"))
judul.pack(pady=10)

# Untuk Input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Harga Barang (Rp)").grid(row=0, column=0, sticky="w")
entry_harga = tk.Entry(frame_input)
entry_harga.grid(row=0, column=1)

tk.Label(frame_input, text="Jumlah Barang").grid(row=1, column=0, sticky="w")
entry_jumlah = tk.Entry(frame_input)
entry_jumlah.grid(row=1, column=1)

tk.Label(frame_input, text="Diskon (%)").grid(row=2, column=0, sticky="w")
entry_diskon = tk.Entry(frame_input)
entry_diskon.grid(row=2, column=1)

# Tombol Hitung
btn_hitung = tk.Button(root, text="Hitung", width=20, command=hitung_diskon)
btn_hitung.pack(pady=10)

# Untuk Output
frame_output = tk.Frame(root)
frame_output.pack(pady=10)

tk.Label(frame_output, text="Total Harga Awal").grid(row=0, column=0, sticky="w")
label_total_awal = tk.Label(frame_output, text="Rp 0.00")
label_total_awal.grid(row=0, column=1)

tk.Label(frame_output, text="Total Diskon").grid(row=1, column=0, sticky="w")
label_diskon = tk.Label(frame_output, text="Rp 0.00")
label_diskon.grid(row=1, column=1)

tk.Label(frame_output, text="Total Bayar").grid(row=2, column=0, sticky="w")
label_total_akhir = tk.Label(frame_output, text="Rp 0.00")
label_total_akhir.grid(row=2, column=1)

# Menjalankan aplikasi
root.mainloop()