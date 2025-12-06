# T3Coin.py — Личный троичный кошелёк с майнингом
# Ternary Satoshi • 2 декабря 2025

import time, threading, tkinter as tk
from tkinter import scrolledtext

balance = 333333
height = 0

def mine():
    global balance, height
    while True:
        time.sleep(3)
        height += 1
        balance += 100
        log.insert(tk.END, f"Блок {height} замарнерен! +100 T3C\n")
        log.insert(tk.END, f"Баланс: {balance:,} T3C\n\n")
        bal_label.config(text=f"{balance:,} T3C")
        h_label.config(text=f"Высота цепи: {height}")
        log.see(tk.END)

root = tk.Tk()
root.title("T3Coin Wallet 1.0")
root.geometry("1000x680")
root.configure(bg="black")

tk.Label(root, text="T 3 C O I N", font=("Courier",40,"bold"), fg="#00FF00", bg="black").pack(pady=30)
tk.Label(root, text="Первый троичный блокчейн в мире", font=("Courier",16), fg="#00FF00", bg="black").pack()
tk.Label(root, text="Ternary Satoshi • 2 декабря 2025", font=("Courier",12), fg="#00AA00", bg="black").pack(pady=5)

frame = tk.Frame(root, bg="black")
frame.pack(pady=20)

tk.Label(frame, text="Адрес основателя:", font=("Courier",14), fg="#00FF00", bg="black").pack()
addr = tk.Entry(frame, width=60, font=("Courier",11), bg="#001100", fg="#00FF00", justify="center")
addr.insert(0, "T3:Т10ТТ1Т01ТТ101Т0Т1ТТ10Т1Т01")
addr.config(state="readonly")
addr.pack(pady=10)

bal_label = tk.Label(frame, text="333333 T3C", font=("Courier",28,"bold"), fg="#00FF00", bg="black")
bal_label.pack(pady=15)

h_label = tk.Label(frame, text="Высота цепи: 0", font=("Courier",14), fg="#00FF00", bg="black")
h_label.pack()

log = scrolledtext.ScrolledText(root, font=("Courier",11), bg="#001100", fg="#00FF00")
log.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
log.insert(tk.END, "T3Coin запущен. Генезис-блок с посланием сыну навсегда в цепи.\n")
log.insert(tk.END, "Майнинг начат. Ты — Ternary Satoshi.\n\n")

threading.Thread(target=mine, daemon=True).start()
root.mainloop()