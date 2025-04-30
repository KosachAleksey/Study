import threading
import socket

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received from {addr}: {message}")
            conn.sendall(f"Server received: {message}".encode('utf-8'))
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed from {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listennig on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()