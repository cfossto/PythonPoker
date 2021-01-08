from cards import Cards
from players import Players

print("\nToday we play Poker! \n")

slim = Players("Slim")
luke = Players("Luke")

deck = Cards().make_deck()

print(deck)

print("\n Today's players are {} and {}. Good luck! \n \n".format(slim.name,luke.name))

