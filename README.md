Python Port Scanner:

A simple multithreaded port scanner written in Python that scans for open TCP ports on a specified target IP address or hostname.

Features:

1. Scans ports from 1 to 65534 (the number of ports available on a device)
2. Uses multithreading for fast scanning (100 threads)
3. Clean, user-friendly terminal output
4. Graceful handling of closed ports
5. Customizable and beginner-friendly

How It Works:

1. You enter the IP address or hostname to scan.
2. The program starts 100 threads using Python’s "threading" module.
3. Each thread pulls a port number from a queue and attempts to connect using a TCP socket.
4. If a connection is successful, the port is reported as open.

Requirements

- Python 3.x  
- No external libraries required ("socket", "threading", and "queue" are built-in)

Installation

```bash
git clone https://github.com/Thewinneroftime07/Port-Scanner.git
cd port-scanner
python port_scanner.py
