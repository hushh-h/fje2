import StyleFactory
import IconFactory

class strategy:
    def __init__(self,data,icon,style):
        self.data = data
        self.icon = icon
        self.style = style

    def display(self):
        icons = IconFactory.iconfactory(self.icon)
        styles = StyleFactory.stylefactory(self.style)
        displayer = styles.get_display()
        displayer.show(self.data,icons)