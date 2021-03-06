from random import randrange
import random
class Deck:
    def __init__(self, num_decks = 8):
        self.cards = ["ace",2,3,4,5,6,7,8,9,10,10,10,10] * 4 * num_decks
        self.cutoff = randrange(64, 64*3)
        self.num_decks = num_decks
    #@property
    def hit(self):
        card = random.choice(self.cards)
        self.cards.remove(card) 
        return card
    #@property
    def shuffle(self):
        # check if need to shuffle
        if self.num_decks*52 - len(self.cards) > self.cutoff:
            print("shuffled")
            self.cards = ["ace",2,3,4,5,6,7,8,9,10,10,10,10] * 4 * self.num_decks
            self.cutoff = randrange(64, 64*3)
        return

    
######################
## Strategy for Aces
######################
def ace(total, target):
    if total + 11 > 21:
        return 1
    # if ace gets to my target
    elif total + 11 > target:
        return 11
        
    else:
        return 11
    
######################
## Dealer Aces
######################    
    
def dealer_ace(total, dealer_ace_count):
    if dealer_ace_count == 0 and total+11 < 22:
        return 11
    else: 
        return 1
    
#######################
### Play Game
#######################

def game(deck, target):
    deck.shuffle()

##########################    
## initial hands
##########################    
    dealer_total = 0
    my_total = 0
    my_cards = []
    dealer_cards = []
    dealer_ace_count = 0

    for i in range(2):
    ## player hit
        new_card = deck.hit()
        if new_card == "ace":
            new_card = ace(my_total, target)
        my_cards.append(new_card)
        my_total = sum(my_cards)
        
    ## dealer hit        
        dealer_card = deck.hit()
        if dealer_card == "ace":
            dealer_card = dealer_ace(dealer_total, dealer_ace_count)
            dealer_ace_count += 1
        dealer_cards.append(dealer_card)
        dealer_total = sum(dealer_cards)
    print("Initial hand: ", my_total)
    print("Dealer initial hand: ", dealer_total)
    ## check if initial blackjack
    if my_total == 21 or dealer_total == 21:
        return(int(my_total == 21))
    if my_total == 21 and dealer_total == 21:
        return(0)
#####################    
#### hit sequence    
####################
    condition = False
    stop_hit = False
    stop_dealer_hit = False

    while dealer_total < 21 and my_total < 21 and not condition:
        ### my turn
        if my_total < target:
            new_card = deck.hit()
            if new_card == "ace":
                new_card = ace(my_total, target)
            my_cards.append(new_card)
            my_total = sum(my_cards)
            ## bust
            if my_total > 21:
                print("I busted, whoops", my_total)
                return 0
        else:
            stop_hit = True
        ### dealer turn    
        if dealer_total < 17:
            dealer_card = deck.hit()
            if dealer_card == "ace":
                dealer_card = dealer_ace(dealer_total, dealer_ace_count)
                dealer_ace_count += 1
            dealer_cards.append(dealer_card)
            dealer_total = sum(dealer_cards)
            ### dealer bust
            if dealer_total > 21: 
                print("Dealer busted, I win: ", dealer_total)
                return 1
        else:
            stop_dealer_hit = True
        if stop_hit and stop_dealer_hit:
            break
    print("dealer: ", dealer_total)
    print("Me:", my_total)     
    if my_total > 21:
        return 0
    elif dealer_total > 21:
        return 1
    ## blackjack
    elif my_total == 21 and dealer_total != 21:
        return 1
    elif dealer_total == 21 and my_total != 21:
        return 0
    elif dealer_total == 21 and my_total == 21:
        return 0
    elif my_total > dealer_total:
        return 1
    elif my_total < dealer_total:     
        return 0
    else:
        # tie
        return .5