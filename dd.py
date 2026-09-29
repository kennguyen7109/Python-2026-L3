import socket
import threading
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '170.20.10.3'
PORT = 8080
client_socket.connect((HOST, PORT))
def receive_messages(sock):
    print("Luồng tin nhắn nhận được từ server\n")
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print('\n[Hệ thống] Mất kết nối tới Server.')
                break
            print(f'\n[Server]: {data.decode("utf-8")}')
            print('[Client]: ', end='', flush=True)
        except Exception:
            break
    sock.close()
    
thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
thread.start()
try:
  while True:
    msg = input('[Client]: ')
    if msg.strip():
      client_socket.sendall(msg.encode('utf-8'))
except KeyboardInterrupt:
  print('\nĐang ngắt kết nối...')
finally:
  client_socket.close()
