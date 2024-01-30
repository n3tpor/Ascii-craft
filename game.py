from player import *
from world import *

class Game():
    def __init__(self):
        self.world = World()
        self.player = Player(self.world)
    def play(self):
        while True: 
            worldType = input("Generate new world or load save: n/l")
            if worldType in ("n","l"):
               break

        if worldType == "n":
            while True:
                worldLength = input("How long would you like the world to be:")
                worldHeight = input("How tall would you like the world to be:")
                if int(worldLength) >= 3 and int(worldHeight) >= 3:
                    break
                print("Invalid size, world must be at least 3 x 3")

            self.world = World(int(worldLength),int(worldHeight))
            self.player = Player(self.world)
            self.world.generateWorld()
            self.player.spawn("new")
        elif worldType == "l":
            self.world.loadSave()
            self.player.spawn("loaded")

        self.world.displayWorld()
        while True:
            playerCommand = input("Enter a command:")
            if playerCommand == "x":
                break
            else:
                self.player.command(playerCommand)
                if self.player.checkState() == False:
                    print("YOU DIED")
                    activeGame = Game()
                    activeGame.play()
                    break
                

activeGame = Game()
activeGame.play()
