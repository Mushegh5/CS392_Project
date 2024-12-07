import socket
import threading

class PeerNetworking:
    def __init__(self, ip_address, port_number):
        self.ip_address = ip_address
        self.port_number = port_number
        self.clients = []

    def start_server(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.bind((self.ip_address, self.port_number))
                server.listen(5)
                print(f"[SERVER] Running at {self.ip_address} at the port:{self.port_number}")

                while True:
                    client_conn, client_addr = server.accept()
                    print(f"[NEW CONNECTION] Client connected from {client_addr}")
                    thread = threading.Thread(target=self.handle_client, args=(client_conn, client_addr))
                    thread.start()
        except Exception as error:
            print(f"[ERROR] Unable to start server: {error}")

    def handle_client(self, conn, addr):
        try:
            while True:
                message = conn.recv(1024)
                if not message:
                    print(f"[DISCONNECT] Client {addr} left.")
                    break

                decoded_msg = message.decode('utf-8')
                print(f"[RECEIVED] {decoded_msg} from {addr}")

                reply = self.generate_response(decoded_msg)
                conn.send(reply.encode('utf-8'))
        except Exception as error:
            print(f"[ERROR] Issue with {addr}: {error}")
        finally:
            conn.close()

    def generate_response(self, msg):
        return f"Server received: {msg}"

    def connect_to_server(self, server_ip, server_port):
        try:
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_socket.connect((server_ip, server_port))
            self.clients.append((server_ip, server_port))
            print(f"[CONNECTED] Linked to {server_ip}:{server_port}")
            return remote_socket
        except socket.error as error:
            print(f"[ERROR] Can't connect to {server_ip}:{server_port}: {error}")
            return None


if __name__ == "__main__":
    manager = PeerNetworking("127.0.0.1", 8080)
    threading.Thread(target=manager.start_server).start()





