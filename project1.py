import random

choices = ['snake','water','gun']

def show_choices():
    print("Please select one option:")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")

def main():   
    print(89*'-','Snake, Water, Gun Game',88*'-')
    print("Welcome to this game")
    asking = input("Do you want to play game (yes/no): ").lower()
    computer_score = 0
    play_score = 0
    
    if asking == 'yes':
        show_choices()
        while True:
            computer_choice = random.choice(choices)
            player_choice = input("Enter your choice here(snake/water/gun): ").lower()
            
            if player_choice not in choices:
                print("please enter valid choice")
                continue
            
            print(f"You choose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            
            if player_choice == 'snake' and computer_choice == "snake":
                print("It's a draw")
            elif player_choice == 'water' and computer_choice == "water":
                print("It's a draw")
            elif player_choice == 'gun' and computer_choice == "gun":
                print("It's a draw")
            elif player_choice == 'water' and computer_choice == "snake":
                print("Computer win")
                computer_score += 1
            elif player_choice == 'snake' and computer_choice == "water":
                print("You win")
                play_score += 1
            elif player_choice == 'water' and computer_choice == "gun":
                print("You win")
                play_score += 1
            elif player_choice == 'gun' and computer_choice == "water":
                print("Computer win")
                computer_score += 1
            elif player_choice == 'gun' and computer_choice == "snake":
                print("You win")
                play_score += 1
            elif player_choice == 'snake' and computer_choice == "gun":
                print("Computer win")
                computer_score += 1
            
            print(f"Your score: {play_score}")
            print(f"Computer score: {computer_score}")

            play_again = input('Do you want to play again?(yes/no): ').lower()
            if play_again != 'yes':
                print("Thank you! please come back again")
                break

        print(f"your final score: {play_score}")
        print(f"Computer final score: {computer_score}")
        if play_score > computer_score:
            print("congratulations! you win")
        elif play_score == computer_score:
            print("match draws")
        else:
            print("better luck next time!")

    elif asking == 'no':
        print("Its okay! see you again")
    else:
        print("Please enter valid choice")

main()
