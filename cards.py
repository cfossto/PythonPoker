import random

class Cards():

    throwaway_heap = []

    def make_deck(self):

        # Empty list of numbers. Filled in for loop
        numbers = []
        colors = ["clubs","hearts","diamonds","spades"]
        
        # Fill Numbers list with numbers
        for num in range(1,14):
            numbers.append(num)
    

        # Empty deck, filled with for loop later.
        deck = []
        # Make 13 of each color and append to deck
        for number in numbers:
            for color in colors:
                deck.append("{} of {}".format(number,color))

        random.shuffle(deck)

        print("Deck - shuffled and ready! \n ")

        return deck


    def deal_cards(self,deck,amount_of_cards):

        card_round = []

        for cards in range(0,amount_of_cards):
            card_round.append(deck[cards])
            print("Dealt: {}".format(deck[cards]))
            deck.pop(cards)
        
        self.throwaway_heap.append(card_round)
        
        print("\n {} cards left. \n ".format(len(deck)))

        return card_round

    def draw_cards(self,deck, hand, amount):

        pick = self.deal_cards(deck,amount)

        for cards in pick:
            hand.append(cards)
        
        self.throwaway_heap.append(pick)

        return hand

    
    def throw_cards(self,hand,throw_count):
    
        hand.sort()

        self.throwaway_heap.append(hand[-2:])
        self.throwaway_heap.pop()
        self.throwaway_heap.pop()

        hand.pop()
        hand.pop()

        return hand

    def total_of_hand(self,hand):
        
        totalList = []
        for cards in hand:

            accessCards = cards.split()
            totalList.append(int(accessCards[0]))

        total = 0

        for num in totalList:

            total += num

        print("Sum of hand is: " + str(total))

        return total

    def card_end(self, deck):
        
        heap = self.throwaway_heap
        
        for card in heap:
            deck.append(card)
        
        print(heap)
        

        print(len(deck))