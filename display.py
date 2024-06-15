import Iterator
class Display:
    def show(self,data,icons):
        pass
class TreeDisplay(Display):
    def show(self,data,icons):
        self.icons = icons
        ite = Iterator.iterator(data)
        length = ite.get_len()
        items = ite.get_items()
        for key, value in items:
            length-=1
            str = ""
            if length == 0:
                str=str+"└─"+icons.get_root()+" "+key
                print(str)
                self.show2(value,1,0)
            else:
                str = str + "├─" + icons.get_root()+" " + key
                print(str)
                self.show2(value, 1,1)

    def show2(self,data,space,flag):
        ite = Iterator.iterator(data)
        length = ite.get_len()
        flags=""
        spaces = " " * (space * 4-1)
        if flag ==1:
            flags="│"
        else:
            spaces+=" "
        items = ite.get_items()
        for key, value in items:
            length-=1
            str = ""
            if isinstance(value, dict):
                if length == 0:
                    str = str + flags + spaces + "└─" + self.icons.get_root()+" " + key
                    print(str)
                    self.show2(value, space+1,flag)
                else:
                    str = str + flags + spaces + "├─" + self.icons.get_root()+" " + key
                    print(str)
                    self.show2(value, space+1,flag)
            else:
                if length == 0:
                    str = str + flags + spaces + "└─" + self.icons.get_leaf()+" " + key
                    if value != None:
                        str = str + ": " + value
                    print(str)
                else:
                    str = str + flags + spaces + "├─" + self.icons.get_leaf()+" " + key
                    if value != None:
                        str = str + ": " + value
                    print(str)

class RecDisplay(Display):
    def show(self, data, icons):
        self.icons = icons
        ite = Iterator.iterator(data)
        length = ite.get_len()
        items = ite.get_items()
        for key, value in items:
            length -= 1
            str = ""
            if length==ite.get_len()-1:
                line = "─"*(60-2-2-len(key)-2)
                line +="┐"
                str = str + "┌─" + self.icons.get_root()+ " " + key + " " + line
                print(str)
                self.show2(value, 1, 1)
            else:
                line = "─" * (60 - 2 - 2 - len(key) - 2)
                line += "┤"
                str = str + "├─" + self.icons.get_root()+ " " + key + " " + line
                print(str)
                flag = 1
                if length==0:
                    flag=0
                self.show2(value, 1, flag)

    def show2(self, data, space, flag):
        ite = Iterator.iterator(data)
        length = ite.get_len()
        spaces = "  │" * (space-1)
        spaces += "  "
        items = ite.get_items()
        if flag==1:
            for key, value in items:
                str=""
                if isinstance(value, dict):
                    line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 2)
                    line += "┤"
                    str = str +"│" + spaces +"├─" +self.icons.get_root()+ " "+ key + " " + line
                    print(str)
                    self.show2(value,space+1,flag)
                else:
                    if value!=None:
                        line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 3 - len(value)-1)
                        line += "┤"
                        str = str + "│" + spaces + "├─" +self.icons.get_leaf()+ " " + key + ": " + value + " " + line
                    else:
                        line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 2)
                        line += "┤"
                        str = str + "│" + spaces + "├─" + self.icons.get_leaf()+" " + key + " " + line
                    print(str)
        else:
            for key, value in items:
                str=""
                length -= 1
                if isinstance(value, dict):
                    line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 2)
                    line += "┤"
                    str = str +"│" + spaces +"├─" +self.icons.get_root()+ " "+ key + " " + line
                    print(str)
                    self.show2(value,space+1,flag)
                else:
                    if length!=0:
                        if value != None:
                            line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 3 - len(value)-1)
                            line += "┤"
                            str = str + "│" + spaces + "├─" + self.icons.get_leaf()+" " + key + ": " + value + " " + line
                        else:
                            line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 2)
                            line += "┤"
                            str = str + "│" + spaces + "├─" + self.icons.get_leaf()+" " + key + " " + line
                    else:
                        spaces=""
                        spaces = "──┘" * (space - 1)
                        spaces += "──"
                        if value != None:
                            line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 3 - len(value)-1)
                            line += "┘"
                            str = str + "└" + spaces + "└─" + self.icons.get_leaf()+" " + key + ": " + value + " " + line
                        else:
                            line = "─" * (60 - 2 - 2 - len(key) - 1 - len(spaces) - 2)
                            line += "┘"
                            str = str + "└" + spaces + "└─" + self.icons.get_leaf()+" " + key + " " + line
                    print(str)
