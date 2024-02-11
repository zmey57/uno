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
    print('Your cards:', playerHand)
    wanna_play = input('What do you want to play?')


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
print(deck)
print(len(deck))
