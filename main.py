from cards import Cards
from players import Players


print("\nToday we play Poker! \n")

cards = Cards()
deck1 = cards.make_deck()


luke = Players("Luke")
slim = Players("Slim")

luke.hand = Cards().deal_cards(deck1,5)
slim.hand = Cards().deal_cards(deck1,5)

luke_sum = Cards().total_of_hand(luke.hand)
slim_sum = Cards().total_of_hand(slim.hand)

total = luke_sum+slim_sum

print("Total of both hands are: " + str(total) +"\n")

luke.hand = Cards().throw_cards(luke.hand,2)
slim.hand = Cards().throw_cards(slim.hand,2)

Cards().draw_cards(deck1,luke.hand,2)
Cards().draw_cards(deck1,slim.hand,2)


print()

luke.game_end(deck1)
slim.game_end(deck1)
print(Cards().throwaway_heap)