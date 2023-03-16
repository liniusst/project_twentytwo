# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deckAfter a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
from typing import List
import random


class Card:
    def __init__(self, suits_list: List[str], card_value_list: List[str]) -> None:
        self.suits_list = suits_list
        self.card_value_list = card_value_list

    def get_card_value(self) -> str:
        random_card_value = random.choice(card_value_list)
        return f"{random_card_value} of "

    def get_card_suit(self) -> str:
        random_suit = random.choice(suit_list)
        return f"{random_suit}"

    def get_random_card(self) -> str:
        suit = self.get_card_suit()
        value = self.get_card_value()
        card = value + suit
        return card


class Deck(Card):
    def __init__(self) -> None:
        self.card_deck = []

    def get_card_deck(self):
        card_desk = []
        for s in suit_list:
            for v in range(1, 14):
                self.card_desk.append(s, v)


suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_value_list = ["A", "2", "3", "4", "5",
                   "6", "7", "8", "9", "10", "J", "Q", "K"]

x = Deck(suits_list=suit_list, card_value_list=card_value_list)
# y = Card()
print(x.get_card_deck())
