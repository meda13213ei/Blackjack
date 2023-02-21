### This code is sole work of Phanindra Medapati and can be duplicated upon written consent from me ###

import random
import art
print(art.logo)
def hitcards(player_score, player1_cards, dealer_score, dealer_cards):
  a = input("Do you want to hit or stand?:").lower()
  while a == "hit":
    temp = random.choice(cards)
    if temp == "A":
      if player_score <= 10:
        player1_cards.append(11)
        player_score = sum(player1_cards)
        print(f"Your cards are {player1_cards}    Currentscore = {player_score}")
      elif player_score > 10:
        player1_cards.append(1)
        player_score = sum(player1_cards)
        print(f"Your cards are {player1_cards}    Currentscore = {player_score}")
    if temp != "A":
      player1_cards.append(temp)
      player_score = sum(player1_cards)
      print(f"Your cards are {player1_cards}    Currentscore = {player_score}")
    if player_score > 21:
      print("Player lose! Dealer_wins")
      break
    elif player_score == 21:
      a = "stand"
    elif player_score < 21:
      a = input("Do you want to hit or stand?:").lower()
      continue
  if a == "stand":
    print(f"Dealer cards are {dealer_cards}")
    while sum(dealer_cards) < 17:
      dealer_cards.append(random.choice(cards))
      dealer_score = sum(dealer_cards)
      print(f"Dealer cards are {dealer_cards}     Dealer score = {dealer_score}")
      break
    if dealer_score >= 17 and dealer_score <= 21:
      if dealer_score > player_score:
        print("player busted. dealer wins")
      elif player_score > dealer_score:
        print("player wins! dealer bust")
    if dealer_score > 21:
      print("player wins! dealer bust")
    if dealer_score == player_score:
      print("It's a draw")

proceed = input("Do you want to play Blackjack today? y or n:").lower()
cards = ["A",2,3,4,5,6,7,8,9,10,10,10,10]
player1_cards = []
dealer_cards = []
player_score = dealer_score = 0
if proceed == "y": 
  for index in range (0,2):
    randomplayercard = random.choice(cards)
    if randomplayercard == "A":
      player1_cards.append(11)
    else:
      player1_cards.append(randomplayercard)
    randomdealercard = random.choice(cards)
    if randomdealercard == "A":
      dealer_cards.append(11)
    else:
      dealer_cards.append(randomdealercard)
    
player_score = sum(player1_cards)
dealer_closed_cards = ["?"]*2
dealer_closed_cards[0]=dealer_cards[0]
print(f"Your cards are {player1_cards}    Currentscore = {player_score}")
print(f"Dealer cards are {dealer_closed_cards}")
if len(player1_cards) == 2 and player_score == 21:
  print("You hit a Blackjack! You win")
else:
    hitcards(player_score, player1_cards, dealer_score, dealer_cards)
  