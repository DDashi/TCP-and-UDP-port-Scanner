import socket

host = 'localhost'
port = 50000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Сервер запущен на {host}:{port}")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Получено подключение от {client_address[0]}:{client_address[1]}")
    response = "Привет, клиент!"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
