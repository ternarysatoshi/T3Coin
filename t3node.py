# t3node.py — Нода T3Coin (ФИНАЛЬНАЯ ЧИСТАЯ ВЕРСИЯ)

import socket, threading, time, json, random

PORT = 3939
my_address = "T3:" + "".join(random.choice("Т10") for _ in range(27))
height = 0

def broadcast(block):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(json.dumps(block).encode(), ("<broadcast>", PORT))

def mine():
    global height
    while True:
        time.sleep(5)
        height += 1
        block = {
            "type": "block",
            "height": height,
            "miner": my_address,
            "reward": 100
        }
        broadcast(block)
        print(f"Блок {height} замарнерен -> {my_address[:15]}... (+100 T3C)")

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", PORT))
    print(f"Нода запущена • Адрес: {my_address}")
    while True:
        data, _ = s.recvfrom(4096)
        msg = json.loads(data)
        if msg["type"] == "block" and msg["miner"] != my_address:
            print(f"Принят блок {msg['height']} от {msg['miner'][:15]}...")

print("T3Coin нода запущена")
threading.Thread(target=mine, daemon=True).start()
threading.Thread(target=listen, daemon=True).start()
input("\nНажми Enter для выхода...\n")