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































# import socket
# import threading
#
#
# class PeerNetworking:
#     def __init__(self, host1, port1):
#         self.host = host1
#         self.port = port1
#         self.peers = []
#
#     def serverStart(self):
#         try:
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#                 server_socket.bind((self.host, self.port))
#                 server_socket.listen(8)
#                 print(f"[THE SERVER STARTED] and Listens to {self.host}:{self.port}")
#
#                 while True:
#                     con, address = server_socket.accept()
#                     print(f"[NEW CONNECTION] Connected by {address}")
#                     threading.Thread(target=self.handleClient, args=(con, address)).start()
#         except Exception as e:
#             print(f"[ERROR] The server startup failed: {e}")
#
#     def handleClient(self, con, address):
#         try:
#             while True:
#                 data = con.recv(1024)
#                 if not data:
#                     print(f"[DISCONNECTED] {address} disconnected")
#                     break
#
#                 message = data.decode('utf-8')
#                 print(f"[MESSAGE RECEIVED] {message} from {address}")
#
#                 response = self.messageProcess(message)
#                 con.sendall(response.encode('utf-8'))
#         except Exception as e:
#             print(f"[ERROR] Handling client {address}: {e}")
#         finally:
#             con.close()
#
#     def messageProcess(self, message):
#         # Custom logic for processing incoming messages
#         return f"Received: {message}"
#
#     def connectToPeer(self, peer_host, peer_port):
#         try:
#             peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             peer_socket.connect((peer_host, peer_port))
#             self.peers.append((peer_host, peer_port))
#             print(f"[PEER CONNECTED] Connected to {peer_host}:{peer_port}")
#             return peer_socket
#         except socket.error as e:
#             print(f"[ERROR] Unable to connect to {peer_host}:{peer_port}: {e}")
#             return None
#
#
# if name == "__main__":
#     peer = PeerNetworking("127.0.0.1", 8080)
#     threading.Thread(target=peer.serverStart()).start()
