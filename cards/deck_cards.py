from random import shuffle

# declare a class

class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
        self._dealt_cards = []
        
    @property
    def deck(self):
        return self._deck
    
    def dealt_cards(self):
        return self._dealt_cards
    
    def __str__(self) -> str:
        return f'A deck of {len(self._deck)} cards'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __len__(self):
        return len(self._deck)

    # build the deck
    
    def _card(self, suit, value):
        return {suit: suit, value: value}
    
    def build_deck(self):
        for suit in ('❤', '♠️', '♦️', '♣️'):
            for value in ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'):
                self._deck.append(self._card(suit, value))
                
    def shuffle_deck(self):
        shuffle(self._deck) # shuffle function works in place
        
    # deal cards
    def deal_card(self):
        card = self._deck.pop(0) # to pop from the beginning
        self._dealt_cards.append(card)
        return card
    
    def deal_cards(self, number):
        hand = []
        
        if number > len(self._deck):
            return 'Not enough cards'
        
        for _ in range(number):
            hand.append(self.deal_card())
            
        return hand
    
    
    def rebuild_deck(self):
        self._deck.clear()
        self._dealt_cards.clear()
        
        return self.build_deck()
    

deck = DeckOfCards()

print(deck._card('Ace', 2))

print(deck.deal_cards(45))