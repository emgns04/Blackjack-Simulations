from random import randrange
class Deck:
    def __init__(self):
        self.cards = ["ace",2,3,4,5,6,7,8,9,10,10,10] * 4 * 8
        self.cutoff = randrange(64, 64*3)