import display

class stylefactory:
    def __init__(self,style):
        self.style = style

    def get_display(self):
        if self.style == "tree":
            return display.TreeDisplay()
        else:
            return display.RecDisplay()