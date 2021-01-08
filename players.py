class Players():

    name = ""
    hand = []

    def __init__(self,name):
        self.name = name

    def game_end(self,hand):

        self.hand = []
        return self.hand