import random

print("Welcome to the Rock, Paper and Scissors game!!!")


# checks if it should return game or games
def game_s(number):
    if number == 1:
        return "game"
    else:
        return "games"


# function to get the amount of rounds to be played
def get_round():
    round_input = input("How many rounds do you want to play? ")

    overall_rounds = round_input
    if round_input.isdigit() and int(round_input) > 0:
        rounds = int(round_input)
        play(rounds, overall_rounds)
    else:
        print("Invalid number of rounds")
        get_round()


# the game loop to go through all the rounds, count wins, losses, and draws
def play(rounds, overall_rounds):
    won = 0
    lost = 0
    draw = 0
    valid_input = False

    while rounds > 0:
        print(f"Round {int(overall_rounds) - rounds + 1} of {overall_rounds}")
        player_input = input("Choose rock, paper, or scissors: ")
        player_input = player_input.lower()

        # player insta wins with this secret code ( Hidden Code To Insta Win This Game
        if player_input == "hctiwtg" and taehc_wolla is True:
            won = int(overall_rounds)
            lost = 0
            draw = 0
            rounds = 0
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")

        elif player_input == "hctiltg":
            lost = int(overall_rounds)
            won = 0
            draw = 0
            rounds = 0
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")

        elif player_input == "rock" or player_input == "r" or player_input == "1":
            valid_input = True
            player_input = 1
            rounds -= 1

        elif player_input == "paper" or player_input == "p" or player_input == "2":
            valid_input = True
            player_input = 2
            rounds -= 1

        elif player_input == "scissors" or player_input == "s" or player_input == "3":
            valid_input = True
            player_input = 3
            rounds -= 1
        else:
            print("Invalid input")
            valid_input = False

        if valid_input:
            bot = random.randint(1, 3)

            if bot == 1:
                if player_input == 1:
                    draw += 1
                    print("Bot chose rock \n you draw")
                elif player_input == 2:
                    won += 1
                    print("Bot chose rock \n you won")
                elif player_input == 3:
                    lost += 1
                    print("Bot chose rock \n you lost")
            elif bot == 2:
                if player_input == 1:
                    lost += 1
                    print("Bot chose paper \n you lost")
                elif player_input == 2:
                    draw += 1
                    print("Bot chose paper \n you draw")
                elif player_input == 3:
                    won += 1
                    print("Bot chose paper \n you won")
            elif bot == 3:
                if player_input == 1:
                    won += 1
                    print("Bot chose scissor \n you won")
                elif player_input == 2:
                    lost += 1
                    print("Bot chose scissor \n you lost")
                elif player_input == 3:
                    draw += 1
                    print("Bot chose scissors \n you draw")
    if rounds == 0:
        if 1 < won == int(overall_rounds) and won > 1:
            print("#######################################################################\n"
                  "░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                  "░░░█░░░░░░░░░█░░░░░░░░░█░░░\n"
                  "░░░██░░░░░░░█▒█░░░░░░░██░░░\n"
                  "░░░█▒█░░░░░█▒▒▒█░░░░░█▒█░░░\n"
                  "░░░█▒▒█░░░█▒▒▒▒▒█░░░█▒▒█░░░\n"
                  "░░░█▒▒▒█░█▒▒▒▒▒▒▒█░█▒▒▒█░░░\n"
                  "░░░█▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒█░░░\n"
                  "░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░\n"
                  "░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░\n"
                  "░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░\n"
                  "░░░█████████████████████░░░\n"
                  "░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                  f"You have Won a perfect game in the best of {str(overall_rounds)}")

            rounds -= 1
        elif 1 < lost == int(overall_rounds):
            print("#######################################################################\n"
                  "████████████████\n"
                  "█░░░░░░░░░░░░░░█\n"
                  "█░░▄▀▄▀▄▀▄▀▄▀░░█\n"
                  "█░░▄▀░░░░░░░░░░█\n"
                  "█░░▄▀░░█████████\n"
                  "█░░▄▀░░░░░░░░░░█\n"
                  "█░░▄▀▄▀▄▀▄▀▄▀░░█\n"
                  "█░░▄▀░░░░░░░░░░█\n"
                  "█░░▄▀░░█████████\n"
                  "█░░▄▀░░█████████\n"
                  "█░░▄▀░░█████████\n"
                  "█░░░░░░█████████\n"
                  "████████████████\n"
                  f"You lost all {str(overall_rounds)} rounds!!!")
            rounds -= 1
        elif won > lost:
            print(
                "#######################################################################\n"
                f" You have Won the best of {str(overall_rounds)}!!! \n You won {str(won)} {game_s(won)} \n"
                f" You lost {str(lost)} {game_s(lost)} \n and you've drawn in {str(draw)} {game_s(draw)}")
            rounds -= 1
        elif won == lost:
            print(
                "#######################################################################\n"
                f" You have Drawn in the best of {str(overall_rounds)}!!! \n You won {str(won)} {game_s(won)} \n"
                f" You lost {str(lost)} {game_s(lost)} \n and you've drawn in {str(draw)} {game_s(draw)}")
            rounds -= 1
        else:
            print(
                "#######################################################################\n"
                f" You have Lost the best of {str(overall_rounds)}!!! \n You won {str(won)} {game_s(won)} \n"
                f" You lost {str(lost)} {game_s(lost)} \n and you've drawn in {str(draw)} {game_s(draw)}")
            rounds -= 1
        input("#######################################################################")
        restart = input("do you want to restart the game? (y/n): ")
        if restart == "y":
            get_round()


# read backwards
taehc_wolla = True

get_round()
