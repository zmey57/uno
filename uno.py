import random


def draw_card(num, who):
    if who == 'player':
        for k in range(num):
            card = random.choice(deck)
            playerHand.append(card)
            deck.remove(card)
    if who == 'bot':
        for j in range(num):
            card = random.choice(deck)
            botHand.append(card)
            deck.remove(card)


def player_move():
    global up_card
    print('Your cards:', playerHand)
    wanna_play = input('What do you want to play? ')
    if wanna_play == '+4':
        color_pick = input('Choose a color: ')
        up_card = color_pick + '|+4'
        draw_card(4, 'bot')
    if wanna_play == 'Change Colour':
        color_pick = input('Choose a color: ')
        up_card = color_pick + '|Change Colour'
    up_card1 = up_card.split('|')
    wanna_play1 = wanna_play.split('|')
    if up_card1[0] == wanna_play1[0] or up_card1[1] == wanna_play1[1]:
        up_card = wanna_play
        playerHand.remove(wanna_play)


deck = []
colours = ["Red", "Green", "Blue", "Yellow"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Miss A Turn", "Reverse", "+2"]
playerHand, botHand = [], []

for z in range(2):
    for i in range(len(colours)):
        for x in range(len(numbers)):
            cardAdd = colours[i] + "|" + numbers[x]
            deck.append(cardAdd)
for i in range(len(colours)):
    cardAdd = colours[i] + "|0"
    deck.append(cardAdd)
for i in range(4):
    deck.append("+4")
    deck.append("Change Colour")

print('UNO!')

up_card = random.choice(deck)
deck.remove(up_card)
print(up_card)
draw_card(7, 'player')
draw_card(7, 'bot')
player_move()
print(up_card)
print(playerHand)
