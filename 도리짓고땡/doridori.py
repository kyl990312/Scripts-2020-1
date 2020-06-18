from tkinter import*
from tkinter import font
from winsound import*
from card import*
from player import*
import random
import card

class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("1000x600")

        self.window.configure(bg = "green")

        p = PhotoImage(file="GodoriCards/table.gif")
        back = Label(self.window, image=p, height = 600, width = 1000)
        back.image = p
        back.pack()

        self.fontstyle = font.Font(self.window, size = 24, weight = 'bold',family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.LbetMoney = []
        self.setupButton()
        self.setupLabel()

        self.player = []
        self.player.append(Player("player1"))
        self.player.append(Player("player2"))
        self.player.append(Player("player3"))
        self.dealer = Player("dealer")
        self.betMoney = [0] * 3

        self.nCardsDealer = 0
        self.nCardsPlayer = 0
        self.LcardsPlayer = [[],[],[]]
        self.LcardsDealer = []
        self.LcardsBack = []
        self.playerCardText = [[],[],[]]
        self.dealerCardText=[]
        self.deckN = 0
        self.countDeal = 0
        self.window.mainloop()


    def setupButton(self):
        self.W5 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2,
                          command=lambda X=0: self.pressedB5(X))
        self.W5.place(x=50, y=500)
        self.W1 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2,
                          command=lambda X=0: self.pressedB1(X))
        self.W1.place(x=150, y=500)


        self.W52 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2,
                         command=lambda X=1: self.pressedB5(X))
        self.W52.place(x=300, y=500)
        self.W12 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2,
                          command=lambda X=1: self.pressedB1(X))
        self.W12.place(x=400, y=500)


        self.W53 = Button(self.window, text="5만", width=6, height=1, font=self.fontstyle2,
                         command=lambda X=2: self.pressedB5(X))
        self.W53.place(x=550, y=500)
        self.W13 = Button(self.window, text="1만", width=6, height=1, font=self.fontstyle2,
                          command=lambda X=2: self.pressedB1(X))
        self.W13    .place(x=650, y=500)

        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2,
                           command=self.pressedDeal)
        self.Deal.place(x=800, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=900, y=500)

        self.W5['state'] = 'disabled'
        self.W5['bg'] = 'gray'
        self.W52['state'] = 'disabled'
        self.W52['bg'] = 'gray'
        self.W53['state'] = 'disabled'
        self.W53['bg'] = 'gray'
        self.W1['state'] = 'disabled'
        self.W1['bg'] = 'gray'
        self.W12['state'] = 'disabled'
        self.W12['bg'] = 'gray'
        self.W13['state'] = 'disabled'
        self.W13['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'


    def setupLabel(self):
        global playerMoney

        for i in range(3):
            self.LbetMoney.append(Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan"))
            self.LbetMoney[i].place(x=100 + 250*i, y=450)
        self.LplayerMoney = Label(text=str(playerMoney) + '만', width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=700, y=450)
        self.LplayerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)


    def pressedB5(self, X):
        global playerMoney

        self.betMoney[X] += 5
        if self.betMoney[X] <= playerMoney:
            self.LbetMoney[X].configure(text = str(self.betMoney[X]) + '만')
            playerMoney -=5
            self.LplayerMoney.configure(text=str(playerMoney)+ '만')
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney[X] -= 5


    def pressedB1(self, X):
        global playerMoney

        self.betMoney[X] += 1
        if self.betMoney[X] <= playerMoney:
            self.LbetMoney[X].configure(text = str(self.betMoney[X]) + '만')
            playerMoney -= 1
            self.LplayerMoney.configure(text= str(playerMoney) + '만')
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney[X] -= 1


    def pressedDeal(self):
        if(self.countDeal==0):
            for i in range(3):
                self.player[i].reset()
            self.dealer.reset()
            self.cardDeck = [i for i in range(40)]
            random.shuffle(self.cardDeck)
            self.deckN = 0

            for i in range(3):
                newCard = Card(self.cardDeck[self.deckN])
                self.deckN += 1
                self.player[i].addCard(newCard)
                p = PhotoImage(file="GodoriCards/" + newCard.filename())
                self.LcardsPlayer[i].append(Label(self.window, image=p))

                self.LcardsPlayer[i][self.player[i].inHand() - 1].image = p
                self.LcardsPlayer[i][self.player[i].inHand() - 1].place(x=50 + i * 250, y=350)

                self.playerCardText[i].append(Label(self.window, text=str(self.player[i].cards[0].x), font=self.fontstyle2, bg="green", fg="cyan"))
                self.playerCardText[i][0].place(x=50 + i * 250, y=300)

            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.dealer.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsDealer.append(Label(self.window, image=p))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=300, y=100)

            b = PhotoImage(file="GodoriCards/cardback.gif")
            self.LcardsBack.append(Label(self.window, image=b))
            self.LcardsBack[0].image = b
            self.LcardsBack[0].place(x=300, y=100)

            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

        if (self.countDeal == 1):
            for n in range(3):
                for i in range(3):
                    newCard = Card(self.cardDeck[self.deckN])
                    self.deckN += 1
                    self.player[i].addCard(newCard)
                    p = PhotoImage(file="GodoriCards/" + newCard.filename())
                    self.LcardsPlayer[i].append(Label(self.window, image=p))

                    self.LcardsPlayer[i][self.player[i].inHand() - 1].image = p
                    self.LcardsPlayer[i][self.player[i].inHand() - 1].place(x=80 + n*30 + i * 250, y=350)

                    self.playerCardText[i].append(
                        Label(self.window, text=str(self.player[i].cards[n+1].x), font=self.fontstyle2, bg="green",
                              fg="cyan"))
                    self.playerCardText[i][n+1].place(x=80 + n*30 + i * 250, y=300)

            for i in range(3):
                a = Card(self.cardDeck[self.deckN])
                self.deckN += 1
                self.dealer.addCard(a)
                p = PhotoImage(file="GodoriCards/" + a.filename())
                self.LcardsDealer.append(Label(self.window, image=p))
                self.LcardsDealer[self.dealer.inHand() - 1].image = p
                self.LcardsDealer[self.dealer.inHand() - 1].place(x=330 + 30*i, y=100)

                b = PhotoImage(file="GodoriCards/cardback.gif")
                self.LcardsBack.append(Label(self.window, image=b))
                self.LcardsBack[i+1].image = b
                self.LcardsBack[i+1].place(x=330 + 30 * i, y=100)

            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

        if (self.countDeal == 2):
            for i in range(3):
                newCard = Card(self.cardDeck[self.deckN])
                self.deckN += 1
                self.player[i].addCard(newCard)
                p = PhotoImage(file="GodoriCards/" + newCard.filename())
                self.LcardsPlayer[i].append(Label(self.window, image=p))

                self.LcardsPlayer[i][self.player[i].inHand() - 1].image = p
                self.LcardsPlayer[i][self.player[i].inHand() - 1].place(x=170 + i * 250, y=350)

                self.playerCardText[i].append(
                    Label(self.window, text=str(self.player[i].cards[4].x), font=self.fontstyle2, bg="green",
                          fg="cyan"))
                self.playerCardText[i][4].place(x=170 + i * 250, y=300)

            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.dealer.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsDealer.append(Label(self.window, image=p))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=420, y=100)

            b = PhotoImage(file="GodoriCards/cardback.gif")
            self.LcardsBack.append(Label(self.window, image=b))
            self.LcardsBack[4].image = b
            self.LcardsBack[4].place(x=420, y=100)
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

        self.countDeal += 1

        self.W5['state'] = 'active'
        self.W5['bg'] = 'white'
        self.W52['state'] = 'active'
        self.W52['bg'] = 'white'
        self.W53['state'] = 'active'
        self.W53['bg'] = 'white'
        self.W1['state'] = 'active'
        self.W1['bg'] = 'white'
        self.W12['state'] = 'active'
        self.W12['bg'] = 'white'
        self.W13['state'] = 'active'
        self.W13['bg'] = 'white'
        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

        if(self.countDeal==3):
            self.checkWinner()


    def pressedAgain(self):
        self.window.destroy()
        self.__init__()


    def checkWinner(self):
        for i in range(5):
            self.LcardsBack[i].destroy()
            Label(self.window, text=str(self.dealer.cards[i].x), font=self.fontstyle2, bg="green", fg="cyan").place(
                x=300 + 30*i, y=0)

        self.scoreText = ['']*4
        self.intCards = [[],[],[],[]]
        self.score = [0] * 4
        self.scoreCheck = {100: '38광땡', 90: '광땡', 80: '땡', 70: '끗', 60: '망통'}

        #도리짓고땡 족보
        for i in range(4):
            if(i<3):
                cards = self.player[i].cards
            else:
                cards = self.dealer.cards

            cards.sort(key = lambda key:key.x)
            for n in range(5):
                self.intCards[i].append(cards[n].x)
            for j in range(4):
                if (self.intCards[i][j] == 1):
                    if (self.intCards[i][j+1] == 1 and 8 in self.intCards[i]):
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        self.scoreText[i] += '콩콩팔'
                        break
                    if (2 in self.intCards[i] and 7 in self.intCards[i]):
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        self.scoreText[i] += '삐리칠'
                        break

                    if (3 in self.intCards[i] and 6 in self.intCards[i]):
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        self.scoreText[i] += '물삼육'
                        break

                    if (4 in self.intCards[i] and 5 in self.intCards[i]):
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        del cards[self.intCards[i].index(5)]
                        self.intCards[i].remove(5)
                        self.scoreText[i] += '빽새오'
                        break

                    if (9 in self.intCards[i] and 10 in self.intCards[i]):
                        del cards[self.intCards[i].index(1)]
                        self.intCards[i].remove(1)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        del cards[self.intCards[i].index(10)]
                        self.intCards[i].remove(10)
                        self.scoreText[i] += '뺑구장'
                        break

                if (self.intCards[i][j] == 2):
                    if (self.intCards[i][j+1] == 2 and 6 in self.intCards[i]):
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        self.scoreText[i] += '니니육'
                        break

                    if (3 in self.intCards[i] and 5 in self.intCards[i]):
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(5)]
                        self.intCards[i].remove(5)
                        self.scoreText[i] += '이삼오'
                        break

                    if (8 in self.intCards[i] and 10 in self.intCards[i]):
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        del cards[self.intCards[i].index(10)]
                        self.intCards[i].remove(10)
                        self.scoreText[i] += '이판장'
                        break

                if (self.intCards[i][j] == 3):
                    if (self.intCards[i][j+1] == 3 and 4 in self.intCards[i]):
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        self.scoreText[i] += '심심새'
                        break

                    if (7 in self.intCards[i] and 10 in self.intCards[i]):
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        del cards[self.intCards[i].index(10)]
                        self.intCards[i].remove(10)
                        self.scoreText[i] += '삼칠장'
                        break

                    if (8 in self.intCards[i] and 9 in self.intCards[i]):
                        del cards[self.intCards[i].index(3)]
                        self.intCards[i].remove(3)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        self.scoreText[i] += '삼빡구'
                        break

                if (self.intCards[i][j] == 4):
                    if (self.intCards[i][j+1] == 4 and 2 in self.intCards[i]):
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        self.scoreText[i] += '살살이'
                        break

                    if (6 in self.intCards[i] and 9 in self.intCards[i]):
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        self.scoreText[i] += '사륙구'
                        break

                    if (7 in self.intCards[i] and 9 in self.intCards[i]):
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        self.scoreText[i] += '사칠구'
                        break

                if (self.intCards[i][j] == 5):
                    if (6 in self.intCards[i] and 9 in self.intCards[i]):
                        del cards[self.intCards[i].index(5)]
                        self.intCards[i].remove(5)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        self.scoreText[i] += '오륙구'
                        break

                    if (7 in self.intCards[i] and 8 in self.intCards[i]):
                        del cards[self.intCards[i].index(5)]
                        self.intCards[i].remove(5)
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        self.scoreText[i] += '오리발'
                        break

                if (self.intCards[i][j] == 6):
                    if (self.intCards[i][j+1] == 6 and 8 in self.intCards[i]):
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        self.scoreText[i] += '쭉쭉팔'
                        break

                if (self.intCards[i][j] == 7):
                    if (self.intCards[i][j+1] == 7 and 6 in self.intCards[i]):
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        del cards[self.intCards[i].index(7)]
                        self.intCards[i].remove(7)
                        del cards[self.intCards[i].index(6)]
                        self.intCards[i].remove(6)
                        self.scoreText[i] += '철철육'
                        break

                if (self.intCards[i][j] == 8):
                    if (self.intCards[i][j + 1] == 8 and 4 in self.intCards[i]):
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        del cards[self.intCards[i].index(8)]
                        self.intCards[i].remove(8)
                        del cards[self.intCards[i].index(4)]
                        self.intCards[i].remove(4)
                        self.scoreText[i] += '팍팍싸'
                        break

                if (self.intCards[i][j] == 9):
                    if (self.intCards[i][j + 1] == 9 and 2 in self.intCards[i]):
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        del cards[self.intCards[i].index(9)]
                        self.intCards[i].remove(9)
                        del cards[self.intCards[i].index(2)]
                        self.intCards[i].remove(2)
                        self.scoreText[i] += '구구리'
                        break

            if(self.scoreText[i] == ''):
                self.scoreText[i] += '노메이드'
                continue

            #광땡
            if(cards[0].x == 3 and cards[1].x == 8 and cards[0].value == 1 and cards[1].value == 1):
                self.score[i] = 100
                self.scoreText[i] += ' ' + self.scoreCheck[100]
                continue
            if(cards[0].x == 1 and cards[1].x == 8 and cards[0].value == 1 and cards[1].value == 1):
                self.score[i] = 90
                self.scoreText[i] += ' ' +'18' + self.scoreCheck[90]
                continue
            if (cards[0].x == 1 and cards[1].x == 3 and cards[0].value == 1 and cards[1].value == 1):
                self.score[i] = 90
                self.scoreText[i] +=' ' + '13' + self.scoreCheck[90]
                continue

            #땡
            if (cards[0].x == cards[1].x ):
                self.score[i] = 70 + cards[1].x
                self.scoreText[i] += ' ' + str(cards[0].x) + self.scoreCheck[80]
                continue

            #끗
            if ((cards[0].x + cards[1].x) % 10 != 0):
                self.score[i] = 60 + (cards[0].x + cards[1].x) % 10
                self.scoreText[i] += ' ' + str((cards[0].x + cards[1].x) % 10) + self.scoreCheck[70]
                continue

            #망통
            if ((cards[0].x + cards[1].x) % 10 == 0):
                self.score[i] = 60
                self.scoreText[i] += ' ' + self.scoreCheck[60]
                continue

        maxScore = max(self.score)
        overlab = 0

        for i in range(4):
            if self.score[i] == maxScore:
                overlab+=1

        global playerMoney

        for i in range(4):
            if self.score[i] == maxScore:
                if overlab > 1:
                    self.scoreText[i] += ' 무승부'
                else:
                    self.scoreText[i] += ' 승'
                    if i < 3:
                        playerMoney += self.betMoney[i] * 2
            else:
                self.scoreText[i] += ' 패'

        for i in range(3):
            print(self.scoreText[i])
            Label(self.window, text=self.scoreText[i], font=self.fontstyle, bg="green",
                  fg="cyan").place(x=50 + i * 250, y=250)

        Label(self.window, text=self.scoreText[3], font=self.fontstyle, bg="green",
              fg="cyan").place(x=300, y=50)

        self.W5['state'] = 'disabled'
        self.W5['bg'] = 'gray'
        self.W52['state'] = 'disabled'
        self.W52['bg'] = 'gray'
        self.W53['state'] = 'disabled'
        self.W53['bg'] = 'gray'
        self.W1['state'] = 'disabled'
        self.W1['bg'] = 'gray'
        self.W12['state'] = 'disabled'
        self.W12['bg'] = 'gray'
        self.W13['state'] = 'disabled'
        self.W13['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


playerMoney = 1000
BlackJack()