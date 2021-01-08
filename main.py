from cards import Cards
from players import Players
import re


print("\nToday we play Poker! \n")

deck1 = Cards().make_deck()

luke = Players("Luke")
slim = Players("Slim")


luke.hand = Cards().deal_cards(deck1,5)
slim.hand = Cards().deal_cards(deck1,5)

Cards().throw_cards(luke.hand)
Cards().throw_cards(slim.hand)

Cards().draw_cards(deck1,luke.hand,2)
Cards().draw_cards(deck1,slim.hand,2)

print(luke.hand)

luke_total = Cards().total_of_hand(luke.hand)
slim_total = Cards().total_of_hand(slim.hand)