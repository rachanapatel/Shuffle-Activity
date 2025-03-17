from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]


# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    new_deck = []
    while (len(new_deck) < 52):
        cards = deck_of_cards[randint(0,len(deck_of_cards) -1)]
        new_deck.append(cards)
    print(new_deck)

    return (new_deck)
    
shuffle_deck(deck_of_cards)
