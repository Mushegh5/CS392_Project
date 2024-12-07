This project implements a peer-to-peer (P2P) file-sharing network where peers can share files directly without relying on a central server. Decentralized file sharing is made possible by each peer serving as both a client and a server. To ensure scalability and efficiency, the network has features for file indexing, searching, and downloading via a chunk-based transfer system.


1. Search and File Indexing Features

Peers keep track of the files they exchange.

Peers can use file hashes or keywords to look for files on the network.



2. Management of Connections and Peer Discovery

Using dynamic peer discovery, you may locate and get in touch with other engaged peers.

A method for bringing in new peers through bootstrapping.



3. Reassembly and Chunked File Transfer

To facilitate effective transfer, files are divided into chunks.

Multiple peers download chunks at the same time, which are then put back together to form the original file.



4. Decentralized Architecture

Lack of a central server guarantees scalability and fault tolerance.

Every peer serves as a client as well as a server.



5. Improved Connectivity and Security

Peers behind firewalls can be connected via NAT traversal.

Secure communication with SSL/TLS encryption.

Firewall setups for smooth functioning.



Configuring NAT traversal
I used the tool STUN in order to allow all the peers behind NAT to connect.
Configuring the STUN server with the following: (In Linux)

# /etc/turnserver.conf
listening-port=3478
relay-ip=192.168.27.16
fingerprint
use-auth-secret
static-auth-secret=#Aa123456


Then, using OpenSSL to generate SSL certificates: (command below)

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ssl_key.pem -out ssl_cert.pem



Firewall Rule configuration: Allow ports for communication (for instance ports 8000-8080)

sudo ufw allow 5000:5005/tcp
sudo ufw allow 3478/udp  (STUN port)

sudo ufw enable
sudo ufw status




Future Improvements


Use encryption to share files securely.

Compression: Use file compression to minimize the size of transfers.

When transferring larger files, optimize chunk transfer.

Rate Limiting: To defend against denial-of-service (DoS) attacks, implement rate limitation.

Graphical User Interface (GUI): Include a GUI to facilitate management and interaction.

Search Filters: Provide the option to filter by peer location, file type, or size.
