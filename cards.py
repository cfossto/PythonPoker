import random

class Cards():


    def make_deck(self):

        # Empty list of numbers. Filled in for loop
        numbers = []
        colors = ["clubs","hearts","diamonds","spades"]
        
        # Fill Numbers list with numbers
        for num in range(1,14):
            numbers.append(num)
    

        # Empty deck, filled with for loop later.
        #deck = []

        random.shuffle(colors)
        random.shuffle(numbers)
        # Make 13 of each color and append to deck
        deck = dict(zip(colors,numbers))



        print("Deck - shuffled and ready! \n ")

        return deck


    def deal_cards(self,deck,amount_of_cards):

        card_round = []

        for cards in range(0,amount_of_cards):
            card_round.append(deck[cards])
            print("Dealt: {}".format(deck[cards]))
            deck.pop(cards)
        
        print("\n {} cards left. \n ".format(len(deck)))

        return card_round

    def draw_cards(self,deck, hand, amount):

        hand.append(self.deal_cards(deck,amount))
        return hand

    
    def throw_cards(self,hand):
    
        hand.sort()
        hand.pop()
        hand.pop()

        return hand