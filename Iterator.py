class iterator:
    def __init__(self,data):
        self.data = data

    def get_len(self):
        return len(self.data)

    def get_items(self):
        return list(self.data.items())