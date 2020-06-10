from tkinter import*
from tkinter import font
from winsound import*
from Player import*
from cards import*
import random

def find(lst, key):
    for i in lst:
        if i == key:
            return True
    return False

class TexmasHoldemPoker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")
        self.window.configure(bg = "green")

        self.fontstyle = font.Font(self.window,size = 24, weight = 'bold', family = 'Consolas')
        self.fontstyle2 = font.Font(self.window, size = 16, weight = 'bold', family = "Consolas")

        self.player = Player()
        self.dealer = Player()
        self.playerLCards = []
        self.dealerLCards = []
        self.commonCards = []
        self.commonLCards = []
        self.dealN = 0

        self.cards = [i for i in range(4*13)]
        random.shuffle(self.cards)
        self.cardN = 0

        self.SetupBotton()
        self.SetLabel()
        self.winLabel= None
        self.playerScoreLabel= None
        self.dealerScoreLabel= None

        self.window.mainloop()

    def SetupBotton(self):
        self.checkButt = Button(self.window, text = 'Check', width = 6, height = 1, font= self.fontstyle2,command = self.CheckProcess)
        self.checkButt.place(x = 50, y = 500)
        self.bet1Butt = Button(self.window, text = 'Bet x1',width = 6, height =1, font = self.fontstyle2,command = self.Betx1Process)
        self.bet1Butt.place(x = 150, y = 500)
        self.bet2Butt = Button(self.window, text = 'Bet x2',width = 6, height = 1, font = self.fontstyle2,command = self.Betx2Process)
        self.bet2Butt.place(x = 250, y = 500)

        self.dealButt = Button(self.window, text = 'Deal',width  = 6, height = 1, font = self.fontstyle2,command = self.DealProcess)
        self.dealButt.place ( x = 600, y = 500)
        self.againButt = Button(self.window,text = "Again", width = 6, height = 1, font = self.fontstyle2, command = self.Reset)
        self.againButt.place(x = 700, y = 500)

        self.checkButt['state'] = 'disabled'
        self.checkButt['bg'] = 'gray'
        self.bet1Butt['state'] = 'disabled'
        self.bet1Butt['bg'] = 'gray'
        self.bet2Butt['state'] = 'disabled'
        self.bet2Butt['bg'] = 'gray'
        self.againButt['state'] = 'disabled'
        self.againButt['bg'] = 'gray'

    def SetLabel(self):
        self.betLabel =Label(text ='$' + str(self.player.betMoney) , width = 4, height = 1, font = self.fontstyle, bg = "green",fg = 'cyan' )
        self.betLabel.place(x = 150, y = 450)
        self.moneyLabel = Label(text ='$'+str(self.player.ownMoney), width = 5, height = 1, font = self.fontstyle, bg= 'green', fg = 'cyan')
        self.moneyLabel.place(x = 650,y = 450)


    def DealProcess(self):
        # 첫번째 Deal
        if self.dealN == 0:
            # 딜러카드
            self.DealDealerCard()
            self.SetDealerCard()
            self.DealDealerCard()
            self.SetDealerCard()

            # 플레이어 카드
            self.DealPlayerCard()
            self.SetPlayerCard()
            self.DealPlayerCard()
            self.SetPlayerCard()
        elif self.dealN == 1:
            self.DealCommonCard()
            self.SetCommonCard()
            self.DealCommonCard()
            self.SetCommonCard()
            self.DealCommonCard()
            self.SetCommonCard()

        elif 1 < self.dealN < 4:
            # 공통 카드
            self.DealCommonCard()
            self.SetCommonCard()

        # 버튼 관리
        self.checkButt['state'] = 'active'
        self.checkButt['bg'] = 'gray94'
        self.bet1Butt['state'] = 'active'
        self.bet1Butt['bg'] = 'gray94'
        self.bet2Butt['state'] = 'active'
        self.bet2Butt['bg'] = 'gray94'

        self.dealButt['state'] = 'disabled'
        self.dealButt['bg'] = 'gray'

        self.dealN += 1

    def DealDealerCard(self):
        newCard = Card(self.cards[self.cardN])
        self.cardN += 1
        self.dealer.SetCard(newCard)

    def DealPlayerCard(self):
        newCard = Card(self.cards[self.cardN])
        self.cardN += 1
        self.player.SetCard(newCard)

    def DealCommonCard(self):
        newCard = Card(self.cards[self.cardN])
        self.cardN += 1
        self.commonCards.append(newCard)

    def SetDealerCard(self):
        p = PhotoImage(file = 'cards/b2fv.png')
        self.dealerLCards.append(Label(self.window,image = p))
        idx = len(self.dealerLCards)-1
        self.dealerLCards[idx].image = p
        self.dealerLCards[idx].place(x = 100*self.dealer.cardN + 50, y = 50)
        PlaySound('sounds/cardFlip1.wav',SND_FILENAME)

    def SetPlayerCard(self):
        p = PhotoImage(file=self.player.cards[self.player.cardN - 1].fileName)
        self.playerLCards.append(Label(self.window, image=p))
        idx = len(self.playerLCards) - 1
        self.playerLCards[idx].image = p
        self.playerLCards[idx].place(x=100 * self.player.cardN + 50, y=350)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def SetCommonCard(self):
        idx = len(self.commonCards)-1
        p = PhotoImage(file = self.commonCards[idx].fileName)
        self.commonLCards.append(Label(self.window,image = p))
        self.commonLCards[idx].image = p
        self.commonLCards[idx].place(x = 150 + idx*100,y = 200)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def Betx1Process(self):
        # 플레이어 베팅금액 조정
        self.player.Bet(2)
        if self.player.ownMoney<0:
            self.player.ownMoney = 1000
            self.Reset()


        if self.dealN == 4:
            self.EndGame()
            return

        # 라벨 조정
        self.betLabel.configure(text = '$' + str(self.player.betMoney))
        self.moneyLabel.configure(text='$' + str(self.player.ownMoney))

        # 버튼 조정
        self.dealButt['state'] = 'active'
        self.dealButt['bg'] = 'gray94'

        self.bet1Butt['state'] = 'disabled'
        self.bet1Butt['bg'] = 'gray'
        self.bet2Butt['state'] = 'disabled'
        self.bet2Butt['bg'] = 'gray'
        self.checkButt['state'] = 'disabled'
        self.checkButt['bg'] = 'gray'

    def Betx2Process(self):
        # 플레이어 베팅금액 조정
        self.player.Bet(3)
        if self.player.ownMoney < 0:
            self.player.ownMoney = 1000
            self.player.betMoney = 0
            self.bet1Butt['state'] = 'disabled'
            self.bet1Butt['bg'] = 'gray'
            self.bet2Butt['state'] = 'disabled'
            self.bet2Butt['bg'] = 'gray'

            return

        if self.dealN == 4:
            self.EndGame()
            return

        # 라벨 조정
        self.betLabel.configure(text='$' + str(self.player.betMoney))
        self.moneyLabel.configure(text='$' + str(self.player.ownMoney))



        # 버튼 조정
        self.dealButt['state'] = 'active'
        self.dealButt['bg'] = 'gray94'

        self.bet1Butt['state'] = 'disabled'
        self.bet1Butt['bg'] = 'gray'
        self.bet2Butt['state'] = 'disabled'
        self.bet2Butt['bg'] = 'gray'
        self.checkButt['state'] = 'disabled'
        self.checkButt['bg'] = 'gray'

    def EndGame(self):
        # 딜러 카드 공개
        p=PhotoImage(file = self.dealer.cards[0].fileName)
        self.dealerLCards[0].configure(image = p)
        self.dealerLCards[0].image = p
        p = PhotoImage(file=self.dealer.cards[1].fileName)
        self.dealerLCards[1].configure(image=p)
        self.dealerLCards[1].image = p

        self.player.cards += self.commonCards
        self.dealer.cards += self.commonCards
        self.playerNum = 0
        self.dealerNum = 0

        # 플레이어 점수계산
        playerscore = 12
        if self.CheckLoyalStraitFlush(self.player.cards,0):
            playerscore = 0
        elif self.CheckBackStraitFlush(self.player.cards,0):
            playerscore = 1
        elif self.CheckStraitFlush(self.player.cards,0):
            playerscore = 2
        elif self.CheckPoker(self.player.cards,0):
            playerscore = 3
        elif self.CheckFullHouse(self.player.cards,0):
            playerscore = 4
        elif self.CheckFlush(self.player.cards,0):
            playerscore = 5
        elif self.CheckMountain(self.player.cards,0):
            playerscore = 6
        elif self.CheckBackStrait(self.player.cards,0):
            playerscore = 7
        elif self.CheckStrait(self.player.cards,0):
            playerscore = 8
        elif self.CheckTriple(self.player.cards,0):
            playerscore = 9
        elif self.CheckTwoPair(self.player.cards,0):
            playerscore = 10
        elif self.CheckOnePair(self.player.cards,0):
            playerscore = 11


        # 딜러의 점수 계산
        dealerscore = 12
        if self.CheckLoyalStraitFlush(self.dealer.cards,1):
            dealerscore = 0
        elif self.CheckBackStraitFlush(self.dealer.cards,1):
            dealerscore = 1
        elif self.CheckStraitFlush(self.dealer.cards,1):
            dealerscore = 2
        elif self.CheckPoker(self.dealer.cards,1):
            dealerscore = 3
        elif self.CheckFullHouse(self.dealer.cards,1):
            dealerscore = 4
        elif self.CheckFlush(self.dealer.cards,1):
            dealerscore = 5
        elif self.CheckMountain(self.dealer.cards,1):
            dealerscore = 6
        elif self.CheckBackStrait(self.dealer.cards,1):
            dealerscore = 7
        elif self.CheckStrait(self.dealer.cards,1):
            dealerscore = 8
        elif self.CheckTriple(self.dealer.cards,1):
            dealerscore = 9
        elif self.CheckTwoPair(self.dealer.cards,1):
            dealerscore = 10
        elif self.CheckOnePair(self.dealer.cards,1):
            dealerscore = 11


        # 승패
        self.win =''
        if playerscore<dealerscore:
            self.win = "Win"
        elif playerscore == dealerscore:
            if playerscore == 12:
                self.playerNum = self.player.GetNoPairScore()
                self.dealerNum = self.dealer.GetNoPairScore()
                if self.playerNum > self.dealerNum:
                    self.win = "Win"

                else:
                    self.win = 'Push'
            elif playerscore == 3:
                if self.player.GetPokerSocre(self.commonCards) > self.dealer.GetPokerSocre(self.commonCards):
                    self.win = 'Push'
                elif self.player.GetPokerSocre(self.commonCards) == self.dealer.GetPokerSocre(self.commonCards):
                    self.win = "Push"
                else:
                    self.win = "Lose"
            else:
                self.win = "Push"
        else:
            self.win = "Lose"

        # 베팅 금액 배당
        if self.win == "Win":
            self.player.ownMoney += (self.player.betMoney + self.player.betMoney //2)
        if self.win == "Push":
            self.player.ownMoney += self.player.betMoney

        # 라벨설정
        self.winLabel = Label(self.window, text = self.win,font = self.fontstyle2,bg = 'green', fg = 'red')
        self.winLabel.place(x = 700, y = 300)
        scoreLst = ["Loyal Strait Flush","Back Strait Flush", "Strait Flush", "Poker","Full House","Flush", "Mountain",
                    "Back Strait","Strait","Triple","TwoPair","One Pair","No Pair"]
        self.playerScoreLabel = Label(self.window,text = scoreLst[playerscore]+str(self.playerNum),
                                      font = self.fontstyle2,bg = 'green',fg = 'cyan')
        self.playerScoreLabel.place(x = 400, y = 400)
        self.dealerScoreLabel = Label(self.window,text = scoreLst[dealerscore]+str(self.dealerNum),
                                      font = self.fontstyle2,bg = 'green',fg = 'cyan')
        self.dealerScoreLabel.place(x = 400, y = 100)

        # 버튼설정
        self.bet1Butt['state'] = 'disabled'
        self.bet1Butt['bg'] = 'gray'
        self.bet2Butt['state'] = 'disabled'
        self.bet2Butt['bg'] = 'gray'
        self.checkButt['state'] = 'disabled'
        self.checkButt['bg'] = 'gray'
        self.dealButt['state'] = 'disabled'
        self.dealButt['bg'] = 'gray'

        self.againButt['state'] = 'active'
        self.againButt['bg'] = 'gray94'

    def CheckLoyalStraitFlush(self,cards,tag):
        for i in range(len(cards)-1):
            if cards[i].x != cards[i+1].x:
                return False
        cardVals = [c.x for c in cards]
        if not find(cardVals,1):
            return False
        if not find(cardVals,13):
            return False
        if not find(cardVals,12):
            return False
        if not find(cardVals,11):
            return False
        if not find(cardVals, 10):
            return False
        if tag == 0:
            self.playerNum = 1
        else:
            self.dealerNum = 1
        return True

    def CheckBackStraitFlush(self,cards,tag):
        for i in range(len(cards)-1):
            if cards[i].x != cards[i+1].x:
                return False
        cardVals = [c.x for c in cards]
        if not find(cardVals,1):
            return False
        if not find(cardVals,2):
            return False
        if not find(cardVals,3):
            return False
        if not find(cardVals,4):
            return False
        if not find(cardVals, 5):
            return False

        if tag == 0:
            self.playerNum = 1
        else:
            self.dealerNum = 1
        return True

    def CheckStraitFlush(self,cards,tag):
        for i in range(len(cards)-1):
            if cards[i].x != cards[i+1].x:
                return False
        cardVals = [c.x for c in cards]
        cardVals.sort()
        cnt = 0
        for i in range(len(cardVals)-1):
            if cardVals[i] +1 != cardVals[i+1]:
                cnt = 0
            else:
                cnt +=1
        if cnt > 4:
            if tag == 0:
                self.playerNum = 1
            else:
                self.dealerNum = 1
            return True
        else:
            return False

    def CheckPoker(self,cards,tag):
        cardVals = [c.value for c in cards]
        for i in range(13,0,-1):
            if cardVals.count(i+1) == 4:
                if tag == 0:
                    self.playerNum = i
                else:
                    self.dealerNum = i
                return True
        return False

    def CheckFullHouse(self,cards,tag):
        cardVals = [c.value for c in cards]
        n = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(13,0,-1):
            if cardVals.count(i + 1) == 3:
                cnt1= 3
                n = i
                if tag == 0:
                    self.playerNum = i
                else:
                    self.dealerNum = i
                break

        for i in range(n,0,-1):
            if cardVals.count(i) == 2:
                cnt2 = 2
                break

        if cnt1 == 3 and cnt2 == 2:
            return True
        return False

    def CheckFlush(self,cards,tag):
        cardXs = [c.x for c in cards]
        for i in range(3):
            if cardXs.count(i) == 5:
                if tag == 1:
                    self.playerNum = i
                else:
                    self.dealerNum = i
                return True
        return False

    def CheckMountain(self,cards,tag):
        cardVals = [c.value for c in cards]
        if not find(cardVals, 1):
            return False
        if not find(cardVals, 13):
            return False
        if not find(cardVals, 12):
            return False
        if not find(cardVals, 11):
            return False
        if not find(cardVals, 10):
            return False
        if tag == 0:
            self.playerNum = 1
        else:
            self.dealerNum = 1
        return True

    def CheckBackStrait(self,cards,tag):
        cardVals = [c.value for c in cards]
        if not find(cardVals, 1):
            return False
        if not find(cardVals, 2):
            return False
        if not find(cardVals, 3):
            return False
        if not find(cardVals, 4):
            return False
        if not find(cardVals, 5):
            return False
        if tag == 0:
            self.playerNum = 1
        else:
            self.dealerNum = 1
        return True


    def CheckStrait(self,cards,tag):
        cardVals = [c.value for c in cards]
        cardVals.sort()
        cnt = 0
        for i in range(len(cardVals) - 1):
            if cardVals[i] + 1 != cardVals[i + 1]:
                cnt = 0
            else:
                cnt += 1
        if cnt > 4:
            if tag == 0:
                self.playerNum = 1
            else:
                self.dealerNum = 1
            return True
        else:
            return False

    def CheckTriple(self,cards,tag):
        cardVals = [c.value for c in cards]
        for i in range(13,0,-1):
            if cardVals.count(i) == 3:
                if tag == 0:
                    self.playerNum = i
                else:
                    self.dealerNum = i
                return True
        return False

    def CheckTwoPair(self,cards,tag):
        cardVals = [c.value for c in cards]
        cnt= 0
        for i in range(13, 0, -1):
            if cardVals.count(i) == 2:
                if(cnt == 0):
                    if tag == 0:
                        self.playerNum = i
                    else:
                        self.dealerNum = i
                cnt += 1
        if cnt >=2 :
            return True
        return False

    def CheckOnePair(self,cards,tag):
        cardVals = [c.value for c in cards]
        for i in range(13, 0, -1):
            if cardVals.count(i) == 2:
                if tag == 0:
                    self.playerNum = i
                else:
                    self.dealerNum = i
                return True
        return False

    def Reset(self):
        # 플레이어 리셋
        self.player.Reset()

        # 딜러 리셋
        self.dealer.Reset()

        # 라벨 리셋
        self.SetLabel()
        for l in self.commonLCards:
            l.destroy()
        self.commonLCards.clear()
        for l in self.dealerLCards:
            l.destroy()
        self.dealerLCards.clear()
        for l in self.playerLCards:
            l.destroy()
        self.playerLCards.clear()

        if not self.winLabel is None:
            self.winLabel.destroy()
        if not self.playerScoreLabel is None:
            self.playerScoreLabel.destroy()
        if not self.dealerScoreLabel is None:
            self.dealerScoreLabel.destroy()

        # 버튼 리셋
        self.againButt['state'] = 'disabled'
        self.againButt['bg'] = 'gray'
        self.dealButt['state'] = 'active'
        self.dealButt['bg'] = 'gray94'

        # 기타 리셋
        self.dealN = 0
        self.cards = [i for i in range(4 * 13)]
        random.shuffle(self.cards)
        self.cardN = 0
        self.commonCards.clear()

    def CheckProcess(self):
        self.player.ownMoney += self.player.betMoney
        self.Reset()


TexmasHoldemPoker()
