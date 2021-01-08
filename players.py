class Players():

    name = ""

    def __init__(self,name):
        self.name = name

    def make_hand(self, card_round):
        hand = []
        amount = len(card_round)//2
        print(amount)

        for cards in range(0,amount):
            hand.append(card_round[cards])
            card_round.pop(cards)
        
        print(self.name+" has {}".format(hand))
        return hand