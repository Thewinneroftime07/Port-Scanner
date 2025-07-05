import socket
import threading
from queue import Queue

target = input("Enter target IP or hostname: ").strip()  # Clean whitespace

if not target:
    print("No target specified. Exiting.")
    exit()

port_range = range(1, 65535)
queue = Queue()
print_lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        with print_lock:
            print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass

def threader():
    while True:
        port = queue.get()
        scan_port(port)
        queue.task_done()

for _ in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for port in port_range:
    queue.put(port)

queue.join()
print("Scan complete.")
