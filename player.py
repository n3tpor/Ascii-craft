from tiles import *
class Player():
    def __init__(self,worldName):
        self.state = True
        self.worldName = worldName
        self.xposition = 1
        self.yposition = 1
        self.inventory = Inventory()
        self.tileUnderPlayer = self.worldName.getGround()
    def spawn(self,gameType="new"):
        if gameType == "loaded":
            f = open("saveFile.txt","r")
            saveArray = f.readlines()
            self.xposition = int(str(saveArray[2]).strip())
            self.yposition = int(str(saveArray[3]).strip())
            
        elif gameType == "new":
            self.worldName.playerSpawn(self.xposition,self.yposition)

    def checkState(self):
            return self.state
    def command(self,playerCommand):
        lastxPosition = self.xposition
        lastyPosition = self.yposition
        lastTileUnderPlayer = self.tileUnderPlayer
        def positonUpdate():
            self.worldName.updatePosition(self.xposition,self.yposition,lastxPosition,lastyPosition,lastTileUnderPlayer)
        def checkTile():
            if self.worldName.checkTile(self.tileUnderPlayer) == True:
                self.state = False
        def collect():
            self.inventory.addItem(self.tileUnderPlayer.showResource())
            print(f"Collected {self.tileUnderPlayer.showResource()}")
            self.tileUnderPlayer = self.worldName.getGround()
            
        if playerCommand in("l","r","u","d"):
            if playerCommand == "l" and self.worldName.validateMove(self.xposition,self.yposition,-1,0) == True:
                self.tileUnderPlayer = self.worldName.getTile(self.xposition,self.yposition,-1,0)
                self.xposition -= 1
                checkTile()
                positonUpdate()
            if playerCommand == "r" and self.worldName.validateMove(self.xposition,self.yposition,1,0) == True:
                self.tileUnderPlayer = self.worldName.getTile(self.xposition,self.yposition,+1,0)
                self.xposition += 1
                checkTile()
                positonUpdate()
            if playerCommand == "u" and self.worldName.validateMove(self.xposition,self.yposition,0,-1) == True:
                self.tileUnderPlayer = self.worldName.getTile(self.xposition,self.yposition,0,-1)
                self.yposition -= 1
                checkTile()
                positonUpdate()
            if playerCommand == "d" and self.worldName.validateMove(self.xposition,self.yposition,0,1) == True:
                self.tileUnderPlayer = self.worldName.getTile(self.xposition,self.yposition,0,+1)
                self.yposition += 1
                checkTile()
                positonUpdate()
        if playerCommand == "c" and self.tileUnderPlayer != self.worldName.getGround():
            collect()
        if playerCommand == "e":
            self.inventory.showInventory()
        if playerCommand == "s":
            self.worldName.saveState(self.xposition,self.yposition)
        

class Inventory(Player):
    def __init__(self):
        self.inventoryArray = []
    def addItem(self,item):
        self.inventoryArray.append(item)
    def showInventory(self):
        print("Inventory:")
        for i in range(0,len(self.inventoryArray)):
            print(self.inventoryArray[i])



        

            

        