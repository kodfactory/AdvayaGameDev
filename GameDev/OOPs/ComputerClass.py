class Computer:
    # Some code will be there
    def getRAM(self):
        print("RAM is",self.ram)

    def getROM(self):
        print("ROM is",self.rom)

    def getFps(self):
        print("FPS is",self.fps)

obj = Computer()

obj.ram = "4GB"
obj.rom = "500GB"
obj.fps = "150"

obj.getRAM()
obj.getROM()
obj.getFps()


