import threading
from networking import PeerNetworking
from peer_discovery import PeerDiscovery
from file_handling import split_file, write_file, calculate_checksum
from search_index import FileIndex
from cli import menu_display, get_input

HOST = '127.0.0.1'
PORT = 5000

def main():
    networking = PeerNetworking(HOST, PORT)
    discovery = PeerDiscovery()
    file_index = FileIndex()

    threading.Thread(target=networking.listen).start()

    while True:
        menu_display()
        choice = get_input("Enter your choice: ")

        if choice == '1':
            file_path = get_user_input("Enter file path to share: ")
            if os.path.exists(file_path):
                file_name = os.path.basename(file_path)
                file_hash = calculate_checksum(file_path)
                file_index.add_file(file_name, file_hash, (HOST, PORT))
                print(f"[Shared] {file_name} with hash {file_hash}")
            else:
                print("[Error] File not found.")

        elif choice == '2':
            keyword = get_input("Enter file name or keyword to search: ")
            results = file_index.search_file(keyword)
            if results:
                print("[Search Results]")
                for file_name, file_hash, peers in results:
                    print(f"File: {file_name}, Hash: {file_hash}, Peers: {peers}")
            else:
                print("[No Results]")

        elif choice == '3':
            file_hash = get_input("Enter file hash to download: ")
            # Logic to download file chunks and reassemble
            print("[Download] Not yet implemented.")

        elif choice == '4':
            peers = discovery.get_peers()
            print("[Known Peers]")
            for peer in peers:
                print(peer)

        elif choice == '5':
            print("[Exiting]")
            break

        else:
            print("[Invalid Choice]")

if __name__ == "__main__":
    main()
