from Game_Card.Card import Card
from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Player import Player
from Game_Card.CardGame import CardGame
bet=0
# listbet=[]
war=CardGame()
war.print()
list1=war.list_players

for j in range(5):
    sum_bet = 0
    bet += 100
    sum_bet += (bet * war.players)
    listbet = []
    for i in range(len(list1)):

        list1[i].reduceAmount(bet)
        listbet.append(list1[i].getCard())

    ind_max=listbet.index(max(listbet))
    print(max(listbet))
    print(listbet)
    list1[ind_max].money += sum_bet
    print('And the winner is: ', list1[ind_max])
winner=0
max1 = 0
for i in range(len(list1)):
    if list1[i].money > max1:
        max1=list1[i].money
        winner = list1[i]


print('Winner Of The Game: ', winner)



























