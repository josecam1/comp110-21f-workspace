"""This is a project about creating a game set."""

__author__ = "730410369"

from random import randint
SMILES = "\U0001F603"
adventure_points_path_one: int = 1
adventure_points_path_two: int = 1
adventure_points_path_three: int = 0
points = int(adventure_points_path_one) + int(adventure_points_path_two) + int(adventure_points_path_three)
player: str = ""


def main() -> None:
    """The main function."""
    greet()


def greet() -> None:
    """This function greets the player."""
    print("You are about to play a game that involves guessing numbers and coinflips correctly and even making arrays. This might be hard at first but just make sure to keep trying and you'll get the hang of it.")
    player = str(input("What is your name? "))
    print(f"Welcome, { player }!")
    print("By selecting to take the first path, you will prompted to try and guess a randomly generated number from 1 to 10. However, the number changes with every new guess! Type 1 to play this mode.")
    print("By opting to take the second path, you will be asked to try and guess if a coin landed on heads or tails. Type 2 to play this mode.")
    print("By choosing to take the third path, you will partake in the creation of a lovely array of a character of your choice. Type 3 to play this mode. ")
    print("By electing to take the fourth path, you will finish this session of gameplay. Type 4 to finish your game. Hope you had fun! ")
    start = int(input("Where do you want to start? "))
        
    def path_one():
        """The first of all the paths."""
        print("An acquintance challenges you to guess their number as quick as possible. However, How many tries will it take you be able to beat this challenge?")
        print("Get ready to guess!")
        adventure_points_path_one = 1
        counts = 0
        while counts == 0: 
            random_integer: int = randint(1, 10)
            guess = input("Guess a integer between 1 and 10.")
            guess = int(guess)
            if guess == random_integer:
                print("Congrats!")
                retry = int(input("Do you want to play again? Type 1 if yes or type 2 if not. "))
                if retry == 1:
                    print("Thanks for playing!")
                    print(adventure_points_path_one)
                    main()
                else:
                    print("Goodbye!")
                    print(SMILES)
                    print(adventure_points_path_one)
                    counts = counts + 1
            else:
                input("Try again!")
                print(adventure_points_path_one)
                adventure_points_path_one = adventure_points_path_one + 1

    def path_two():
        """The second of all the paths."""
        print("A friend is asking your help for an experiment of theirs. They want to see how many tries it take you to correctly guess the result of a coin toss. Will you be lucky and guess correctly first try?")
        adventure_points_path_two = 1
        random_coin: int = randint(1, 2)
        coin_guess = input("Type 1 if it's heads or type 2 if it's tails. ")
        coin_guess = int(coin_guess)
        if coin_guess == random_coin:
            adventure_points_path_two = adventure_points_path_two + 1
            print("You were right!")
            retry = int(input("Do you want to play again? Type 1 if yes or type 2 if not. "))
            if retry == 1:
                print("Thanks for playing!")
                print(adventure_points_path_two)
                main()
            else:
                print("Goodbye!")
                print(SMILES)
                print(adventure_points_path_two)
        else: 
            print("You were wrong.")
            retry = int(input("Do you want to play again? Type 1 if yes or type 2 if not. "))
            if retry == 1:
                print("Thanks for playing!")
                print(adventure_points_path_two)
                main()
            else:
                print("Goodbye!")
                print(SMILES)
                print(adventure_points_path_two)
        
    def path_three(): 
        """The third of all the paths."""
        adventure_points_path_three = 0
        print("This game will create an array of letters for visual purposes.")

        def path_square(character: str, length: int):
            """This determines the character desired and how long the player wants it."""
            i = 0
            j = 0
            empty = ""
            while i < length:
                while j < length:
                    empty = empty + character
                    j += 1
                print(empty)
                i += 1
        adventure_points_path_three += 1

        path_square(input("What character do you want to make a square of? "), int(input("What do you want the length of the square to be? ")))

    def path_four():
        """This function says goodbye to the player."""
        print("Well, guess that concludes your gaming session. Hope you had fun guessing and what not. Make sure to like and subscribe and hit that notification bell!")
        print(points)

    if start == 1:
        path_one()
    elif start == 2:
        path_two()
    elif start == 3:
        path_three()
    else:
        path_four()


if __name__ == "__main__":
    main()