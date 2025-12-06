# t3node.py — Нода T3Coin (P2P сеть)
# Запускай на любом компьютере — все увидят твои блоки

import socket, threading, time, json, random

PORT = 3939
address = "T3:" + "".join(random.choice("Т10") for _ in range(27))

def broadcast(block):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(json.dumps(block).encode(), ("255.255.255.255", PORT))

def mine():
    h = 0
    while True:
        time.sleep(5)
        h += 1
        block = {"type":"block", "height":h, "miner":address, "reward":100}
        broadcast(block)
        print(f"Блок {h} замарнерен → {address[:15]}...")

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", PORT))
    print(f"Нода запущена • Адрес: {address}")
    while True:
        data, _ = s.recvfrom(4096)
        msg = json.loads(data)
        if msg["type"] == "block":
            print(f"Принят блок {msg['height']} от {msg['miner'][:15]}...")

print("T3Coin нода запущена")
threading.Thread(target=mine, daemon=True).start()
threading.Thread(target=listen, daemon=True).start()
input("\nНажми Enter для выхода...\n")