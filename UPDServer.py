import socket

host = 'localhost'
port = 50001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"Сервер запущен на {host}:{port}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Получены данные от {client_address[0]}:{client_address[1]}: {data.decode('utf-8')}")
    response = "Привет, клиент!"
    server_socket.sendto(response.encode('utf-8'), client_address)
