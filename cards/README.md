# SIMULATING DECK OF CARDS

## INTRODUCTION

In this project, i will simulate a real-world deck of cards in an object-oriented paradigm.


```
from random import shuffle

# declare a class

class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
```

We declare a class in python called `DeckOfCards`. Immediately after, we declare our `__init__(self)` function.
This is a special function and everytime an object of class is instantiated, the class `DeckOfCards` will be invoked automatically. Another point to notice
is the use of `self`. `self` refers to the object itself. We pass the `self` keyword to every function within the class so that we wouldn't have to 
manually pass the instantiated object at run-time. Lastly, is the `self._deck = []`. The explanation is that we need a container to store all 52 deck of cards.
And since the `__init__ function runs everytime an object is instantiated, we basically hook the container to each insyantiated object so that they have an independent
set of 52 cards.

The purpose of using undescore in `self._deck` is to make it a private attribute. This to to avoid altering the value of the deck attribute at un-time by the user.


Now, let's build the deck

```
class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
        
    def _card(self, suit, value):
        return {suit: suit, value: value}
    
    def build_deck(self):
        for suit in ('❤', '♠️', '♦️', '♣️'):
            for value in ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'):
                self._deck.append(self._card(suit, value))
```

First, we create a private _card function that will take 2 inputs, card suit and card value and then return a dictionary with keys suit and value.
`build_deck()` will fill the deck container fo us with the 52 cards. I have used the a double for loop so that it iterates 52 times and with each iteration, the loop
will append the suit and the value to the _deck container.

So the logic is this: We first pass the suit and value to the `_card` function so that it returns a consistent format, then we append to our deck container.

Now let's add a function to shuffle deck.

```
from random import shuffle

class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
        self._dealt_cards = []
        
    def _card(self, suit, value):
        return {suit: suit, value: value}
    
    def build_deck(self):
        for suit in ('❤', '♠️', '♦️', '♣️'):
            for value in ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'):
                self._deck.append(self._card(suit, value))
                
    def shuffle_deck(self):
        shuffle(self._deck) # shuffle function works in place
        
```

What i did here is to import `shuffle` from the random module and give it the deck container to shuffle.

Now let's see how to deal cards from the deck, keep track of the dealt cards, and remove the dealt cards from the actual container

```
from random import shuffle

class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
        
    def _card(self, suit, value):
        return {suit: suit, value: value}
    
    def build_deck(self):
        for suit in ('❤', '♠️', '♦️', '♣️'):
            for value in ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'):
                self._deck.append(self._card(suit, value))
                
    def shuffle_deck(self):
        shuffle(self._deck) # shuffle function works in place
        
        
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
```

I have added three new functions. The first 2 which are relaed are used to deal the cards. The `deal_card` function accepts no parameters
and will pop out a card from the beginning of the deck. If you llok out the `__init__ function, there is another private propert added. It will contain the dealt
cards. Basically, the deal_card function will pop out the card from the beginning of the deck, append it to the _dealt_cards array and return the card.

I have also added the `deal_cards` function which internally uses the `self_card` function. It helps deal more card at once. So you specify the number of cards
as an argument and it checks for the lenght of the deck to see of you have the number of cards you are asking for and the returns the card in an array.

The last function is the `rebuild_deck` function. Once you invoke this function, it will first empty the containers and he rebuild the deck for you.

Next, i will implement some 'dunder methods', the define getters functions for the two properties `self._deck` and `self.dealt_cards` so that users can access the 
properties but could never alter the values


```
from random import shuffle

class DeckOfCards:
    # declare init function
    def __init__(self):
        self._deck = []
        
        
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

        
    def _card(self, suit, value):
        return {suit: suit, value: value}
    
    def build_deck(self):
        for suit in ('❤', '♠️', '♦️', '♣️'):
            for value in ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'):
                self._deck.append(self._card(suit, value))
                
    def shuffle_deck(self):
        shuffle(self._deck) # shuffle function works in place
        
        
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
```

Looking at the beginning of class, you can see i have added some stuffs. First is `@property'. It is special wrapper function called a decorator. through this,
we can define getters and setters. Below the getters functions, i added some special and reserved methods represented using an underscore. They are called 
'dunder methods'.

The first method `__str__` is responsible for things like printing the object or casting it into a str() function to change the object's type. Through this method,
you can control the behaviour of the class.

The next one is the `__repr__` function is responsible for the representation of the object. `__repr__` and `__str__` are very similar. You can implement it
to run a variable or object without a print statement.

The last one is `__len__` function that is used to return the length of the deck.

## Example output if function is run

```
deck = DeckOfCards()

print(deck._card('Ace', 2))

print(deck.deal_cards(45))
```

__Output__

```
{'Ace': 'Ace', 2: 2}
Not enough cards 
```














