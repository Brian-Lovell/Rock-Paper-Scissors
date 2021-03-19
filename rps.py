import random

import time

from colorama import init, Fore, Back, Style

init(autoreset=True)

# Available game moves for human and computer players

moves = ['rock', 'paper', 'scissors']

# Functions for use Colorama to change colors


def print_red(string):
    print(Fore.WHITE + Back.RED + string)
    time.sleep(2)


def print_cyan(string):
    print(Style.DIM + Fore.BLACK + Back.CYAN + string)
    time.sleep(2)


def print_yellow(string):
    print(Fore.BLACK + Back.YELLOW + string)
    time.sleep(2)


def print_black(string):
    print(Back.WHITE + Fore.BLACK + string)
    time.sleep(2)


#  Player class is the parent class to all other players

class Player():
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# This function determine who wins


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# This function validiates user input, response must equal items in list.


def valid_input(prompt, options, verify):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response
        print_red(verify)


#  AI Player class that selects move randomly


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


#  AI Player class that learns and copies from the other Player


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


#  AI Player class that picks a random move, then cycles through the move list

class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            try:
                index = moves.index(self.my_move)
                index = index + 1
                return (moves[index])
            except IndexError:
                return (moves[0])

    def learn(self, my_move, their_move):
        self.my_move = my_move


# Human player class, allows you to play against computer

class HumanPlayer(Player):
    def move(self):
        return valid_input(Style.DIM + Fore.BLACK + Back.CYAN +
                           "Rock, Paper, or Scissors? \n", moves,
                           "Please type in Rock, Paper, Or Scissors")

#  Game class the controls playing the rps game.


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print_cyan("Game Tied!")
        else:
            if (beats(move1, move2)):
                print_black("Player 1 Wins the round!")
                self.p1_score += 1
            else:
                print_black("Player 2 Wins the round!")
                self.p2_score += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def determine_score(self, p1, p2):
        p1_string = str(self.p1_score)
        p2_string = str(self.p2_score)
        p1_final = "Final Score for Player 1:{} \n"
        p2_final = "Final Score for Player 2:{} \n"
        print_yellow(p1_final.format(p1_string))
        print_yellow(p2_final.format(p2_string))
        if self.p1_score == self.p2_score:
            print_yellow("No winnner! It's a draw!")
        else:
            if self.p1_score > self.p2_score:
                print_yellow("Player 1 Wins the game!")
            else:
                print_yellow("Player 2 Wins the game!")

    def play_game(self):
        self.rounds = 3
        print_cyan("Game start!")
        for round in range(self.rounds):
            print_yellow(f"Round {round}:")
            print_black(f"Player 1 Score {self.p1_score}")
            print_black(f"Player 2 Score {self.p2_score}")
            self.play_round()
        self.determine_score(self.p1_score, self.p2_score)
        print_red("Game over!")
        menu_function()


def menu_function():
    menu_choices = ["starter", "easy", "medium", "hard", "exit"]
    print_black("Welcome to Rock Paper Scissors!")
    print_black("Type Starter, Easy, Medium, or Hard to Begin!")
    print_black("Type Exit to quit")
    game_mode = valid_input("Please select a game mode \n", menu_choices,
                            "Please type in starter, easy, medium,"
                            " hard or exit.")
    if game_mode == "starter":
        print("Starter Mode Selected")
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif game_mode == "easy":
        print("Easy Mode Selected")
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    elif game_mode == "medium":
        print("Medium Mode Selected")
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    elif game_mode == "hard":
        print("Hard Mode Selected")
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif game_mode == "exit":
        print("Thanks for playing!")
        exit()


menu_function()


# if __name__ == '__main__':
#     game = Game(HumanPlayer(), CyclePlayer())
#     game.play_game()
