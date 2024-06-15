class iconfactory:
    def __init__(self,icon):
        self.icon = icon

    def get_root(self):
        if self.icon == "star":
            return "★"
        else:
            return "❤"

    def get_leaf(self):
        if self.icon == "star":
            return "☆"
        else:
            return "♡"