# It's a special function which will be called automatically when
# We create object of class

class Computer:
    # Constructor is used to initialize the default values
    def __init__(self, ram, rom, fps):
        print("It will be called automatically")
        self.ram = ram
        self.rom = rom
        self.fps = fps

    # Some code will be there
    def getRAM(self):
        print("RAM is",self.ram)

    def getROM(self):
        print("ROM is",self.rom)

    def getFps(self):
        print("FPS is",self.fps)

    def giveAllDetails(self):
        print(self.ram)
        print(self.rom)
        print(self.fps)
obj = Computer("4GB", "500GB", 200)

# obj.getRAM()
# obj.getROM()
# obj.getFps()

obj.giveAllDetails()