import random
from typing import List, NamedTuple
from abc import ABC, abstractmethod


class Card(NamedTuple):
    value: int
    suit: str

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck(ABC):

    @abstractmethod
    def get_card(self) -> Card:
        pass

    @abstractmethod
    def remove_card(self, card: Card) -> None:
        pass


class CardDeck52(Deck):
    def __init__(self):
        self.card_deck = self.generate_card_deck()

    @staticmethod
    def generate_card_deck() -> List[Card]:
        card_deck = []
        for value in (2, 3, 4, 5, 6, 7, 8, 9, 10, "Валет", "Дама", "Король", "Туз"):
            for suit in ("clubs", "diamonds", "hearts", "spades"):
                card_deck.append(Card(value=value, suit=suit))
        return card_deck

    def get_card(self) -> Card:
        return random.choice(self.card_deck)

    def remove_card(self, card: Card) -> None:
        self.card_deck.remove(card)

    def __str__(self):
        print(f"Колода карт:{self.card_deck}")


class PlayerInterface(ABC):
    @abstractmethod
    def take_turn(self, deck: Deck):
        pass

    @abstractmethod
    def add_card_to_hand(self, card: Card) -> None:
        pass


class ScoreCalculator:
    @staticmethod
    def calculate_score(card: Card, current_score: int) -> int:
        return {
            "Туз": 11 if current_score + 11 <= 21 else 1,
            "Король": 4,
            "Дама": 3,
            "Валет": 2,
        }.get(card.value, card.value)


class PlayerBlackJack(PlayerInterface):
    def __init__(self):
        self.score = 0
        self.hand_cards = []

    def add_card_to_hand(self, card: Card) -> None:
        self.hand_cards.append(card)
        self.add_score(card)

    def add_score(self, card: Card) -> None:
        self.score += ScoreCalculator.calculate_score(card, self.score)

    def take_turn(self, deck: Deck) -> None:
        card = deck.get_card()
        deck.remove_card(card)
        self.add_card_to_hand(card)


class Player(PlayerBlackJack):
    def __init__(self, deck):
        super().__init__()
        for _ in range(2):
            self.take_turn(deck)


class BotBlackJack(PlayerBlackJack):
    def play(self, deck: Deck, target_score: int) -> None:
        while self.score <= target_score and self.score < 21:
            self.take_turn(deck)
            print(self.score)
            print(self.hand_cards)


def black_jack_play():
    deck = CardDeck52()
    player = Player(deck)
    bot_player = BotBlackJack()

    player.play(deck)
    if player.score < 22:
        bot_player.play(deck, player.score)
        if bot_player.score > 21:
            return f"Вы выиграли с {player.score} очками. У бота перебор {bot_player.hand_cards} {bot_player.score} очков"

        return f"Бот Выиграл с картами {bot_player.hand_cards} - {bot_player.score}очков" if bot_player.score > player.score \
            else f"Вы выиграли с картами {player.hand_cards} - {player.score} очков"

    return f"Бот Выиграл. У вас 'перебор'"

