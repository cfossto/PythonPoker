from cards import Cards
from players import Players

print("\nToday we play Poker! \n")

deck1 = Cards().make_deck()

luke = Players("Luke")
slim = Players("Slim")

print(luke.hand)


print(deck1)


luke.hand = Cards().deal_cards(deck1,5)
slim.hand = Cards().deal_cards(deck1,5)

print(luke.hand)
print(slim.hand)

luke.hand = Cards().throw_cards(luke.hand)
slim.hand = Cards().throw_cards(slim.hand)

print(luke.hand)
print(slim.hand)

Cards().draw_cards(deck1,luke.hand,2)
Cards().draw_cards(deck1,slim.hand,2)

print(luke.hand)
print(slim.hand)