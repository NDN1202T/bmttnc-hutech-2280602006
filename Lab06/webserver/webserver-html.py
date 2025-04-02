import socket
import os

def hand_request(client_socket, request_data):
    base_dir = os.path.dirname(__file__)  # Lấy thư mục chứa script

    print("Request received:", request_data)  # Kiểm tra request

    if request_data.startswith("GET /admin "):  # Kiểm tra chính xác request
        file_path = os.path.join(base_dir, "admin.html")
    else:
        file_path = os.path.join(base_dir, "index.html")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + file.read()
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)

    print("Listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        request_data = client_socket.recv(1024).decode('utf-8')
        hand_request(client_socket, request_data)

if __name__ == '__main__':
    main()
