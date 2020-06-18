class Card:
    def __init__(self, temp: object) -> object:
        if(temp % 4 == 0):
            self.value = 1
        else:
            self.value = temp % 4 + 1
        self.x = temp // 4 + 1

    def getValue(self):
        if self.value > 10:
            return 10
        else:
            return self.value

    def filename(self):
        return str(self.x) + '.' +str(self.value) + ".gif"