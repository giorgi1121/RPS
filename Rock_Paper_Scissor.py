# import modules
import random
import sys
import pygame
from art import draw


# main function which calls other functions and uses while loop
def main():
    # we defined music_file and give it as a parameter to
    # play_music function which plays that music.
    music_file = "Queen - We Will Rock You (Official Video) (mp3cut.net) (1).mp3"
    play_music(music_file)

    # defined variable required_points and gave it the value of required function
    # this function prompts user required points for win
    print("=" * 40)
    print("WELCOME TO THE GAME!")
    required_points = required()

    # defined variable level and gave it the value of game_level function
    # this function prompts user to choose LEVEL1 or LEVEL2
    level = game_level()

    # call game_rules function with parameter of level which gives user rules
    game_rules(level)

    # while loop which is the main engine of the program
    while True:

        # defined variable player_points and computer_points
        # as initialize points of player and computer
        player_points = 0
        computer_points = 0
        # user can choose 2 different level, so
        # if user choose level 1 then we use game_level_1 function,
        # otherwise we use game_level_2 function.

        if level == "1":
            game_level_1(required_points, player_points, computer_points)
        else:
            game_level_2(required_points, player_points, computer_points)

        # we use play_again function which ask user
        # if he/she wants to play again or not.
        # if user does not want play anymore, then program will be finished.

        if play_again(level) == "yes":
            required_points = required()
            level = game_level()
        else:
            break

# game_level_1 function is function for playing game on level1
# we give that function 3 different parameters:
# required_points, player_points and computer_points.


def game_level_1(required_points, player_points, computer_points):
    # inside the function we use while loop with win function.
    # while win function returns True than program prompts user for choice,
    # at the same time computer makes choice and
    # program calculates the score for both.
    # loop will break if user write "stop" or someone reach required points.
    while win(required_points, player_points, computer_points):
        player_choice = player(level="1")
        available_choices = ["Rock", "Paper", "Scissor"]
        computer_choice = random.choice(available_choices)
        if player_choice == computer_choice:
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("It's Tie")
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rock" and computer_choice == "Scissor":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Paper" and computer_choice == "Rock":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Scissor" and computer_choice == "Paper":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rules":
            print("=" * 40)
            game_rules(level="1")
            print("=" * 40)

        elif player_choice == "Stop":
            sys.exit()

        else:
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Computer wins!")
            computer_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)


# game_level_2 function is function for playing game on level2
# we give that function 3 different parameters:
# required_points, player_points and computer_points.
def game_level_2(required_points, player_points, computer_points):
    # inside the function we use while loop with win function.
    # while win function returns True than program prompts user for choice,
    # at the same time computer makes choice and
    # program calculates the score for both.
    # loop will break if user write "stop" or someone reach required points.
    # difference from game_level_1 is that here we have more available_choices.
    while win(required_points, player_points, computer_points):
        player_choice = player(level="2")
        available_choices = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        computer_choice = random.choice(available_choices)
        if player_choice == computer_choice:
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("It's Tie")
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rock" and computer_choice == "Scissor":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rock" and computer_choice == "Lizard":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Paper" and computer_choice == "Rock":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Paper" and computer_choice == "Spock":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Scissor" and computer_choice == "Paper":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Scissor" and computer_choice == "Lizard":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Lizard" and computer_choice == "Paper":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Lizard" and computer_choice == "Spock":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Spock" and computer_choice == "Scissor":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Spock" and computer_choice == "Rock":
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rules":
            print("=" * 40)
            game_rules(level="2")
            print("=" * 40)

        elif player_choice == "Stop":
            sys.exit()

        else:
            print("Player choice: " + player_choice + draw(player_choice))
            print("Computer choice: " + computer_choice + draw(computer_choice))
            print("Computer wins!")
            computer_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)


# win function has 3 different parameters:
# required_points, player_points and computer_points.
# this function will be called when someone reach required points
# and returns True and False bools.
def win(required_points, player_points, computer_points):
    if int(player_points) == required_points:
        print("*" * 40)
        print("Player wins!!!!!!")
        print("CONGRATULATION!!!!!")
        print("*" * 40)
        return False

    elif int(computer_points) == required_points:
        print("*" * 40)
        print("Computer wins!!!!!")
        print("Sorry, try again")
        print("*" * 40)
        return False

    return True


# player function has 1 parameter - level.
# According to level, this function prompts user to make a choice.
# try/except statements help us to catch any errors.
def player(level):
    while True:
        try:
            if level == "1":
                print("=" * 40)
                available_choices = ["Rock", "Paper", "Scissor", "Rules", "Stop"]
                player_choice = input("Rock, Paper, Scissor: ").title().strip()
            else:
                print("=" * 40)
                available_choices = ["Rock", "Paper", "Scissor", "Lizard", "Spock", "Rules", "Stop"]
                player_choice = input("Rock, Paper, Scissor, Lizard, Spock: ").title().strip()

            if player_choice in available_choices:
                return player_choice
            else:
                raise ValueError("YOUR CHOICE IS NOT APPROPRIATE")
        except ValueError:
            print("YOUR CHOICE IS NOT APPROPRIATE")
            pass


# This function greets the user and asks the needed required points to win.
# try/except statements help us to catch any errors.
def required():
    while True:
        try:
            print("=" * 40)
            return int(input("Please, enter the required points: "))
        except ValueError:
            print("YOU SHOULD INPUT INTEGER")


# play_again function has 1 parameter - level.
# it defines available answers.
# function asks user if he/she wants to play again or not.
# if user choose rules, then program calls game_rules function according to level.
# otherwise it returns user's answer and catches errors.
def play_again(level):
    available_answers = ["yes", "no", "rules"]
    while True:
        try:
            answer = str(input("Do you want to play again? YES/NO: ")).lower()
            try:
                if answer in available_answers:
                    if answer == "rules":
                        game_rules(level)
                        continue
                    else:
                        return answer
                else:
                    raise ValueError
            except ValueError:
                print("YOU SHOULD INPUT YES OR NO")
        except ValueError:
            print("YOU SHOULD INPUT YES OR NO")


# play_music takes 1 parameter called music_file
# and plays that music.
def play_music(music_file):
    pygame.mixer.init()
    clock = pygame.time.Clock()
    music = pygame.mixer.Sound(music_file)
    music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(10)


# game_level function has 2 available levels.
# it asks user to choose LEVEL1 or LEVEL2 and returns users answer
# try/except statements catches errors.
def game_level():
    available_levels = ["1", "2"]
    while True:
        try:
            level = input("Choose LEVEL: ").lower().strip()
            if level in available_levels:
                return level
            else:
                raise ValueError
        except ValueError:
            print("YOU SHOULD CHOOSE 1 OR 2")


# game_rules function has 1 parameter - level.
# according to level it prints game rules.
def game_rules(level):
    if level == "1":
        print("""Rules: Rock wins against scissors; 
       paper wins against rock; 
       and scissors wins against paper.
             """)

    elif level == "2":
        print("""The rules: Scissors cuts paper, 
          paper covers rock, 
          rock crushes lizard, 
          lizard poisons Spock, 
          Spock smashes scissors, 
          scissors decapitates lizard, 
          lizard eats paper, 
          paper disproves Spock, 
          Spock vaporizes rock, 
          and as it always has, rock crushes scissors.""")


if __name__ == '__main__':
    main()
