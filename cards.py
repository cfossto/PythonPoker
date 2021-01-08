import random

class Cards():


    def make_deck(self):

        colors = ["clubs","hearts","diamonds","spades"]
        numbers = []
        for num in range(1,14):
            numbers.append(num)
    
        deck = []

        for nums in numbers:
            for color in colors:
                deck.append("{} of {}".format(nums,color))


        random.shuffle(deck)
        print("Deck - shuffled and ready! \n ")

        return deck


    def deal_cards(self,deck,amount_of_cards):

        card_round = []

        for cards in range(0,amount_of_cards):
            card_round.append(deck[cards])
            # print("Dealt: {}".format(deck[cards]))
            deck.pop(cards)
        
        print("{} cards left.".format(len(deck)))

        return card_round