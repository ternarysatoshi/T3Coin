# t3wallet.py — Сетевой кошелёк T3Coin
import socket, threading, json, tkinter as tk
from tkinter import scrolledtext

PORT = 3939
my_addr = "T3:" + "".join(__import__("random").choice("Т10") for _ in range(27))
balance = 0
net_height = 0

def listen():
    global balance, net_height
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", PORT))
    while True:
        data, _ = s.recvfrom(4096)
        b = json.loads(data)
        if b["type"] == "block":
            net_height = max(net_height, b["height"])
            if b["miner"] == my_addr:
                balance += 100
            log.insert(tk.END, f"Блок {b['height']:>4} → {b['miner'][:15]}...\n")
            bal_label.config(text=f"{balance:,} T3C")
            height_label.config(text=f"Сеть: {net_height} блоков")
            log.see(tk.END)

root = tk.Tk()
root.title("T3Coin Network Wallet")
root.geometry("900x600")
root.configure(bg="black")

tk.Label(root, text="T 3 C O I N • Сеть", font=("Courier",36,"bold"), fg="#00FF00", bg="black").pack(pady=30)
tk.Label(root, text=my_addr, font=("Courier",11), fg="#00FF00", bg="black").pack(pady=5)

bal_label = tk.Label(root, text="0 T3C", font=("Courier",32,"bold"), fg="#00FF00", bg="black")
bal_label.pack(pady=20)
height_label = tk.Label(root, text="Сеть: 0 блоков", font=("Courier",14), fg="#00AA00", bg="black")
height_label.pack()

log = scrolledtext.ScrolledText(root, font=("Courier",11), bg="#001100", fg="#00FF00")
log.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
log.insert(tk.END, "Кошелёк подключён к сети T3Coin\nОжидание блоков...\n\n")

threading.Thread(target=listen, daemon=True).start()
root.mainloop()