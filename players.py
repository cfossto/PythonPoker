from cards import Cards

class Players():

    name = ""
    age = ""
    hand = []

    def __init__(self,name):
        self.name = name

    def game_end(self,deck):
        # Cards return to deck
        for card in self.hand:
            deck.append(card)

        heap = Cards().throwaway_heap
        print(heap)
        heap_len = len(heap)

        ## Return heap to deck. Fix this problem ##

        print(len(heap)) 
        print(len(deck))