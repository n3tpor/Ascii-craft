class Color():
    def __init__(self):
        self.name = ""
        self.ANSICode = ""
    def showName(self):
        return self.name
    def addColor(self,text):
        return self.ANSICode.format(text)

class Red(Color):
    def __init__(self):
        self.name = "red"
        self.ANSICode = "\033[91m{}\033[00m"


class Green(Color):
    def __init__(self):
        self.name = "green"
        self.ANSICode = "\033[92m{}\033[00m"


class Blue(Color):
    def __init__(self):
        self.name = "blue"
        self.ANSICode = "\u001b[34m{}\033[00m"


class Black(Color):
    def __init__(self):
        self.name = "black"
        self.ANSICode = "\u001b[30m{}\033[00m"


class Grey(Color):
    def __init__(self):
        self.name = "grey"
        self.ANSICode = "\u001b[30;1m{}\033[00m"

class Yellow(Color):
    def __init__(self):
        self.name = "yellow"
        self.ANSICode = "\u001b[33;1m{}\033[00m"

class White(Color):
    def __init__(self):
        self.name = "white"
        self.ANSICode = "\u001b[37m{}\033[00m"

class Cyan(Color):
    def __init__(self):
        self.name = "cyan"
        self.ANSICode = "\u001b[36m{}\033[00m"

class Brown(Color):
    def __init__(self):
        self.name = "brown"
        self.ANSICode = "\u001b[38;5;130m{}\033[00m"

class LightBrown(Color):
    def __init__(self):
        self.name = "light_brown"
        self.ANSICode = "\u001b[38;5;172m{}\033[00m"




