
class Player:
    def __init__(self):
        self.betMoney = 10
        self.ownMoney = 990
        self.cards = []
        self.cardN = 0

    def Bet(self, n):
        self.ownMoney += self.betMoney
        self.betMoney *= n
        self.ownMoney -= self.betMoney

    def SetCard(self,card):
        self.cards.append(card)
        self.cardN+=1

    def GetNoPairScore(self,cards):
        mVal = 0
        for i in cards:
            if i.value > mVal:
                mVal = i.value
                if i.value == 1:
                    mVal = 14
        return mVal

    def GetPokerSocre(self,cards):
        if cards[0].value != cards[1].value:
            return cards[0].value
        else:
            return cards[4].value

    def Reset(self):
        self.cards.clear()
        self.betMoney = 10
        self.cardN = 0
        self.ownMoney -= 10

