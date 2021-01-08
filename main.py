from cards import Cards
from players import Players

print("\nToday we play Poker! \n")

luke = Players("Luke")
slim = Players("Slim")


deck1 = Cards().make_deck()

print(deck1)

luke.hand = Cards().deal_cards(deck1,5)
slim.hand = Cards().deal_cards(deck1,5)

print(luke.name)
print(luke.hand)
print(slim.name)
print(slim.hand)