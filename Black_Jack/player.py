class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        # ace는 1혹은 11로 모두 사용 가능
        # 일단 11로 계산한 후 21이 넘어가면 1로 인정
        val = 0
        aceNum = 0
        for c in self.cards:
            if c.getValue() == 1:
                aceNum+= 1
        for c in self.cards:
            if not c.getValue() == 1:
                val += c.getValue()

        for i in range(1,aceNum+1,1):
            if val+11 > 21:
                val += 1
            else: val += 11

        return val


