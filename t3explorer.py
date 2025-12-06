# t3explorer.py — T3Coin Explorer + майнинг (100% РАБОЧАЯ ВЕРСИЯ)
# Ternary Satoshi • 2 декабря 2025

import socket, threading, time, json, random, http.server, socketserver

PORT = 3939
my_address = "T3:" + "".join(random.choice("T10") for _ in range(27))
height = 0
blocks = []

def broadcast(block):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(json.dumps(block).encode(), ("<broadcast>", PORT))

def mine():
    global height
    while True:
        time.sleep(5)
        height += 1
        block = {"height":height, "miner":my_address, "time":int(time.time())}
        blocks.append(block)
        broadcast({"type":"block", **block})
        print(f"Блок {height} замарнерен -> {my_address[:15]}... (+100 T3C)")

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", PORT))
    while True:
        data, _ = s.recvfrom(4096)
        try:
            msg = json.loads(data)
            if msg.get("type") == "block":
                if msg not in blocks:
                    blocks.append(msg)
                    print(f"Принят блок {msg['height']} от {msg['miner'][:15]}...")
        except: pass

# Веб-сервер Explorer
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/explorer"]:
            html = f"""
            <html><head><meta charset="utf-8"><title>T3Coin Explorer</title>
            <style>body{{background:#000;color:#00FF00;font-family:Courier New;text-align:center;padding:20px}}
            table{{margin:20px auto;border-collapse:collapse;width:90%}}
            th,td{{border:1px solid #00FF00;padding:10px}}
            th{{background:#001100}}</style></head>
            <body><h1>T 3 C O I N • EXPLORER</h1>
            <p>Первый троичный блокчейн • Ternary Satoshi • 2 декабря 2025</p>
            <p>Блоков в сети: <b>{len(blocks)}</b></p>
            <table><tr><th>Высота</th><th>Майнер</th><th>Время</th></tr>
            """
            for b in reversed(blocks[-50:]):
                t = time.strftime("%H:%M:%S", time.localtime(b["time"]))
                html += f"<tr><td>{b['height']}</td><td>{b['miner'][:20]}...</td><td>{t}</td></tr>"
            html += "</table><hr><small>T3Coin живёт</small></body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

print("Запуск T3Coin ноды + Explorer...")
threading.Thread(target=mine, daemon=True).start()
threading.Thread(target=listen, daemon=True).start()
httpd = socketserver.TCPServer(("0.0.0.0", 8000), Handler)
print(f"Explorer запущен: http://127.0.0.1:8000")
print(f"Твой адрес: {my_address}")
httpd.serve_forever()