class Card:
    def __init__(self,n):
        self.value = n%13 + 1
        self.x = n//13
        self.fileName = ''
        self.GetName()

    def GetName(self):
        if self.x == 0:
            self.fileName = "cards/Clubs"+str(self.value)+".png"
        elif self.x == 1:
            self.fileName = "cards/Spades"+str(self.value)+".png"
        elif self.x == 2:
            self.fileName = "cards/Hearts"+str(self.value)+".png"
        elif self.x == 3:
            self.fileName = "cards/Diamonds" + str(self.value)+".png"
