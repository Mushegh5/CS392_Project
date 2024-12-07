class PeerDiscovery:
    def __init__(self):
        self.member_list = []

    def add_member(self, host, port):
        """Add a peer if it's not registered."""
        member = (host, port)
        if member not in self.member_list:
            self.member_list.append(member)
            print(f"Peer added successfully: {host}:{port}")
        else:
            print(f"Peer already exists: {host}:{port}. Nothing needs to be done.")

    def get_member(self):
        if self.member_list:
            print("Current list of peers:")
            for host, port in self.member_list:
                print(f" - {host}:{port}")
        else:
            print("There are no peers found.")
        return self.member_list

    def remove_member(self, host, port):
        """Remove a peer if it already exists in our list."""
        member = (host, port)
        if member in self.member_list:
            self.member_list.remove(member)
            print(f"Peer removed: {host}:{port}")
        else:
            print(f"Peer not found: {host}:{port}. Nothing needs to remove.")
