from colors import *

class Tile():
    def __init__(self):
        self.symbol = ""
        self.name = ""
        self.Id = ""
        self.color = ""
        self.resource = ""
    def showSymbol(self):
        return self.color.addColor(self.symbol)
    def showName(self):
        return self.name
    def showId(self):
        return self.Id
    def showResource(self):
        return self.resource

class Water(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "≈"
        self.name = "Water"
        self.Id = "0"
        self.color = Blue()
        

class Ground(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "▒"
        self.name = "Ground"
        self.Id = "1"
        self.color = LightBrown()

class IronMountain(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "Â"
        self.name = "IronMountain"
        self.Id = "2"
        self.color = White()
        self.resource = "Iron"

class Forest(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "░"
        self.name = "Forest"
        self.Id = "3"
        self.color = Green()
        self.resource = "Wood"

class HorizontalBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "═"
        self.Id = "4"
        self.color = White()

class VerticalBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "║"
        self.Id = "5"
        self.color = White()

class LeftUpperCornerBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "╔"
        self.Id = "6"
        self.color = White()

class LeftBottomCornerBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "╚"
        self.Id = "7"
        self.color = White()

class RightUpperCornerBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "╗"
        self.Id = "8"
        self.color = White()

class RightBottomCornerBorder(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "╝"
        self.Id = "9"
        self.color = White()

class PlayerTile(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "¥"
        self.Id = "10"
        self.color = Yellow()

class ShallowWater(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "~"
        self.Id = "11"
        self.color = Cyan()
        self.resource = "Water"
    
class CopperMountain(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "Å"
        self.name = "copperMountain"
        self.Id = "12"
        self.color = White()
        self.resource = "Copper"

class QuartzMountain(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "Ã"
        self.name = "quartzMountain"
        self.Id = "13"
        self.color = White()
        self.resource = "Quartz"

class Lava(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "≈"
        self.name = "Lava"
        self.Id = "14"
        self.color = Red()

class deadPlayer(Tile):
    def __init__(self):
        super().__init__()
        self.symbol = "X"
        self.name = "deadPlayer"
        self.Id = "15"
        self.color = Red()
        








