from cards import Cards
from players import Players

print("\nToday we play Poker! \n")

deck1 = Cards().make_deck()

luke = Players("Luke")
slim = Players("Slim")

print(deck1)

luke.hand = Cards().deal_cards(deck1,5)