import random
import sys

# note: face cards are all revalued to 10 for this version of blackjack
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Bet:
    def __init__(self):
        self.bet = [0]

    def bet(self):
        pass  # not sure I need this

    def __str__(self):
        return f"The current bet is: {self.bet}"


class Deck:
    def __init__(self):
        self.all_deck_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_deck_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_deck_cards)

    def deal(self):
        return self.all_deck_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_player_cards = []
        self.player_chips = [250]

    def add_one(self, new_card):
        self.all_player_cards.append(new_card)

    # def com_tot(self):
    #     self.add_one(new_deck.deal())
    def __str__(self): return f"Player name {self.name} has {self.player_chips}"


def print_human_cards():
    for card in human.all_player_cards:
        print(card)


def print_computer_cards():
    for card in computer.all_player_cards:
        print(card)


def player_add_one_func():
    global human_total
    human.add_one(new_deck.deal())
    ace_choice()
    human_total = sum(card.value for card in human.all_player_cards)


# computer add card
def com_add_one_func():
    global computer_total
    computer.add_one(new_deck.deal())
    ace_choice()
    computer_total = sum(card.value for card in computer.all_player_cards)


# prompts the player if they want any aces to be 11 or 1
def ace_choice():
    if card.value == 11:
        ace_val = int(input(f"{human.name} would you like your Ace to be 1 or 11? "))
        card.value = ace_val
        print(f"Your Ace has been updated to {ace_val}!")


# deals the 4 hole cards to both players and shows 2 from player and 1 from computer
def hole_func():
    hole_cards = True
    while hole_cards:
        human.add_one(new_deck.deal())
        computer.add_one(new_deck.deal())
        if len(human.all_player_cards) >= 2 and len(computer.all_player_cards) >= 2:
            return computer.all_player_cards and human.all_player_cards  # todo i need this?
            # hole_cards = False


def player_turn_func():
    global player_turn
    global human_total
    while player_turn:
        action = input(f"Your total card value is {human_total}\nWould you like to HIT or STAND? ").lower()
        if action == "hit":
            print("\n" * 100)
            player_add_one_func()
            ace_choice()
            # print_human_cards()
            if human_total > 21:
                print('\n')
                print(f"{human.name} you are BUST and you lost your bet!")
                player_turn = False
                return human_total
            elif human_total <= 21:
                continue

        else:
            if action == "stand":
                print("\n" * 100)
                print(f"{human.name} is standing with a total of {human_total} and a bet of {bet_amount}")
                print("\n")
                player_turn = False
                return human_total


def computer_turn_func():
    global computer_turn
    global computer_total
    global player_won
    while computer_turn:
        print("The computer will draw another card...")  # todo need to move this
        com_add_one_func()
        print_computer_cards()
        print(f"Computers total card value is: {computer_total}")
        print("\n")
        if computer_total > 21:
            player_won = True
            print(f"Computer is BUST with {computer_total}!\nCongratulations you beat the computer!")
            computer_turn = False
        elif computer_total > human_total:
            print(f"Computer WON with {computer_total}!\nBetter luck next time!")
            computer_turn = False
        else:
            continue


# GAME LOGIC
human = Player("Reginald")
computer = Player("Computer")

new_deck = Deck()
new_deck.shuffle()
print('\n')
print(f"Your current account balance is {str(human.player_chips[0])}")
bet_amount = int(input(f"{human.name} please make your bet for the upcoming game: "))
print("\n")

hole_func()
print("Computer has drawn 2 cards")
print(f"One card is hidden and one is: {computer.all_player_cards[0]}")
print("\n")
print(f"Your current bet is: {bet_amount}\nThese are your current cards:")
print_human_cards()
for card in human.all_player_cards:
    ace_choice()
print("\n")

human_total = sum(card.value for card in human.all_player_cards)
computer_total = sum(card.value for card in computer.all_player_cards)

player_won = False
player_turn = True
player_turn_func()
human_total = sum(card.value for card in human.all_player_cards)
if human_total > 21:
    sys.exit()

computer_turn = True
computer_turn_func()

if player_won:
    human.player_chips[0] += bet_amount * 2


# todo add safety to the inputs being wrong
# todo add to bet class add and subtract bet methods
# todo check line 99
# todo make the ace choice function display cards better
# todo reduce the use of global variables
# todo add a minimum bet
# todo add a dealer stands at 17 statement
# todo add an option to continue the game and carry on playing
# todo add name input
# todo add colour using
# todo dbl check all the names/variables and see if they could be better
# todo sort it into modules
# todo add ability to accept multiple players
