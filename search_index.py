class FileIndex:
    def __init__(self):
        self.file_index = {}

    def addFile(self, file_name, file_hash, peer_address):
        if file_hash not in self.file_index:
            self.file_index[file_hash] = {"file_name": file_name, "peers": []}
        self.file_index[file_hash]["peers"].append(peer_address)

    def searchFile(self, keyword):
        results = []
        for file_hash, data in self.file_index.items():
            if keyword.lower() in data["file_name"].lower():
                results.append((data["file_name"], file_hash, data["peers"]))
        return results
