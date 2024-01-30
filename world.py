import random
import os
import time
from tiles import *

class World():
    def __init__(self,length=0,height=0):
        
        self.worldArray = []
        self.length = length
        self.height = height
        self.water = Water()
        self.shallowWater = ShallowWater()
        self.lava = Lava()
        self.ground = Ground()
        self.ironMountain = IronMountain()
        self.copperMountain = CopperMountain()
        self.quartzMountain = QuartzMountain()
        self.forest = Forest()
        self.horizontalBorder = HorizontalBorder()
        self.verticalBorder = VerticalBorder()
        self.LeftUpperCorner = LeftUpperCornerBorder()
        self.LeftBottomCorner = LeftBottomCornerBorder()
        self.RightUpperCorner = RightUpperCornerBorder()
        self.RightBottomCorner = RightBottomCornerBorder()
        self.PlayerTile = PlayerTile()
        self.mountainTiles = [self.ironMountain,self.copperMountain,self.quartzMountain]
        self.landTiles = [self.ground,self.forest,self.ironMountain,self.copperMountain,self.quartzMountain,self.lava]
        self.borderTiles = [self.horizontalBorder,self.verticalBorder,self.LeftUpperCorner,self.LeftBottomCorner,self.RightUpperCorner,self.RightBottomCorner]
        self.allTiles = [self.water,self.ground,self.ironMountain,self.PlayerTile,self.forest,self.LeftUpperCorner,self.RightUpperCorner,self.LeftBottomCorner,self.RightBottomCorner,self.verticalBorder,self.horizontalBorder,self.shallowWater,self.copperMountain,self.quartzMountain,self.lava]

    def generateWorld(self):
        for y in range(0,self.height):
            self.worldArray.append([])
        for y in range(0,self.height):
            for x in range(0,self.length):
                self.worldArray[y].append(self.water)
        for y in range(0,self.height):
            for x in range(0,self.length):
                if y == 0 or y == self.height - 1:
                    self.worldArray[y][x] = self.horizontalBorder
                elif x == 0 or x == self.length -1:
                    self.worldArray[y][x] = self.verticalBorder
        self.worldArray[1][1] = self.ground
        for y in range(1,self.height-1):
            for x in range(1,self.length-1):
                if self.worldArray[y][x-1] == self.water:
                    if random.randint(1,10) in range(0,10):   
                        self.worldArray[y][x] = self.water
                    else:
                        self.worldArray[y][x] = self.ground
                elif self.worldArray[y][x-1] == self.ground:
                    if random.randint(1,10) in range(0,10):
                        self.worldArray[y][x] = self.ground
                    elif random.randint(1,10) in range(0,4):
                        self.worldArray[y][x] = random.choice(self.mountainTiles)
                    else:
                        self.worldArray[y][x] = self.forest

                elif self.worldArray[y][x-1] in self.mountainTiles:
                    self.worldArray[y][x] = self.ground

                elif self.worldArray[y][x-1] == self.forest:
                    if random.randint(1,10) in range(0,9):
                        self.worldArray[y][x] = self.forest
                    elif random.randint(1,10) in range(0,5):
                        self.worldArray[y][x] = self.ground
                    else:
                        self.worldArray[y][x] = self.water

            for y in range(1,self.height-1):
                for x in range(1,self.length-1):
                    if self.worldArray[y][x] == self.water:
                        if self.worldArray[y][x-1] in self.landTiles or self.worldArray[y][x+1] in self.landTiles or self.worldArray[y+1][x]in self.landTiles or self.worldArray[y-1][x] in self.landTiles:
                            self.worldArray[y][x] = self.shallowWater
                    elif self.worldArray[y][x] in self.mountainTiles:
                        if (self.worldArray[y][x-1] not in self.borderTiles) and (self.worldArray[y][x+1] not in self.borderTiles) and (self.worldArray[y+1][x] not in self.borderTiles) and (self.worldArray[y-1][x] not in self.borderTiles):
                            if random.randint(1,10) in range(0,6):
                                self.worldArray[y][x-1] = self.lava
                            elif random.randint(1,10) in range(0,2):
                                self.worldArray[y][x+1] = self.lava
                            elif random.randint(1,10) in range(0,2):
                                self.worldArray[y+1][x] = self.lava
                            elif random.randint(1,10) in range(0,2):
                                self.worldArray[y-1][x] = self.lava
                        
                
        self.worldArray[0][0] = self.LeftUpperCorner
        self.worldArray[0][self.length-1] = self.RightUpperCorner
        self.worldArray[self.height-1][self.length-1] = self.RightBottomCorner
        self.worldArray[self.height-1][0] = self.LeftBottomCorner
    def displayWorld(self):
        os.system("clear")
        for x in range(0,len(self.worldArray)):
            for y in range(0,len(self.worldArray[x])):
                print(self.worldArray[x][y].showSymbol(),end="")
            print()
    def playerSpawn(self,playerX,playerY):
        self.worldArray[int(playerY)][int(playerX)] = self.PlayerTile
        self.displayWorld()
    def checkTile(self,tileUnderPlayer):
        if tileUnderPlayer == self.lava or tileUnderPlayer == self.water:
            self.PlayerTile = deadPlayer()
            return True

    def updatePosition(self,playerX,playerY,playerLastX, playerLastY,tileUnderPlayer):
        self.worldArray[int(playerY)][int(playerX)] = self.PlayerTile
        self.worldArray[int(playerLastY)][int(playerLastX)] = tileUnderPlayer
        self.displayWorld()
    def getWorldArray(self):
        return self.worldArray
    def validateMove(self,playerX,playerY,directionX,directionY):
        if playerX+directionX != 0 and directionX == -1:
            return True
        elif playerX+directionX != self.length-1 and directionX == 1:
            return True
        elif playerY+directionY != 0 and directionY == -1:
            return True
        elif playerY+directionY != self.height -1 and directionY == +1:
            return True
        else:
            return False
    def getTile(self,playerX,playerY,directionX,directionY):
        return self.worldArray[playerY+directionY][playerX+directionX]
    def getGround(self):
        return self.ground
    def saveState(self,playerX,playerY):
        f = open("saveFile.txt", "w")
        f.write(f"{self.length}\n")
        f.write(f"{self.height}\n")
        f.write(f"{playerX}\n")
        f.write(f"{playerY}\n")
        for x in range(0,len(self.worldArray)):
            for y in range(0,len(self.worldArray[x])):
                f.write(f"{self.worldArray[x][y].showId()}\n")
        f.close
    def loadSave(self): 
        f = open("saveFile.txt","r")
        saveArray = f.readlines()
        self.length = int(str(saveArray[0]).strip())
        self.height = int(str(saveArray[1]).strip())
        for y in range(0,self.height):
            self.worldArray.append([])
            for x in range(0,self.length):
                self.worldArray[y].append("")

        saveArrayIndex = 4
        for y in range(0,self.height):
            for x in range(0,self.length):
                for tileCheck in range(0,len(self.allTiles)):
                    if str(saveArray[saveArrayIndex]).strip() == self.allTiles[tileCheck].showId():
                        self.worldArray[y][x] = self.allTiles[tileCheck]
                saveArrayIndex += 1

        



    


        
            






    











    


    
