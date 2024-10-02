import random
def genuine_choice():
    player_choice = input("Enter a Choice (Number, Colour, Type, Range): ")
    options = ["Number", "Colour", "Type", "Range"]
    if player_choice not in options:
        print("Invalid choice. Please enter 'Number' , 'Colour' , 'Type' or 'Range'.")
        return genuine_choice() 
    else:
        return player_choice
def play_game(choice):
    if choice == "Number":
        player_choice = int(input("Enter a number (1-36): "))
        computer_choice = random.randint(1, 36)
        check_win(player=player_choice, computer=computer_choice, mode="Number",bet=bet_amount)
    elif choice == "Colour":
        player_choice = input("Enter a color (Red, Black): ").capitalize()
        computer_choice = random.choice(["Red", "Black"])
        check_win(player=player_choice,computer= computer_choice, mode="Colour", bet=bet_amount)
    elif choice == "Type":
        player_choice = int(input("Enter a number (1-36): "))
        computer_choice = random.randint(1, 36)
        check_win(player=player_choice, computer=computer_choice, mode="Type",bet=bet_amount)
    elif choice == "Range":
        player_choice = input("Enter a range [(1-6),(7-12),(13-18),(19-24),(25-30),(31-36)]")
        computer_choice = random.choice(["1-6","7-12","13-18","19-24","25-30","31-36"])
        check_win(player=player_choice, computer=computer_choice, mode="Range",bet=bet_amount)
    else:
        print("Invalid choice. Please try again.")
        return play_game(genuine_choice())
    print(f"You chose {player_choice}, Computer chose {computer_choice}.")
def check_win(bet,player, computer, mode):
    if mode == "Number":
        if player == computer:
            print("Congratulations! You win" , (bet * 2))
        else:
            print("Sorry, you lose.", (bet / 2))
    elif mode == "Colour":
        if player != computer:
            print("Sorry, you lose.", bet_amount / 2)
        else:
            print("Congratulations! You win ", bet_amount * 2)
    elif mode == "Type":
        if player%2 == 0 and computer%2 == 0:
            print("Congratulations! You win ", bet_amount * 2)
        if player%2 == 1 and computer%2 == 1:
            print("Congratulations! You win ", bet_amount * 2)
        if player%2 == 0 and computer%2 == 1:
            print("Sorry, you lose.", bet_amount / 2)
        if player%2 == 1 and computer%2 == 0:
            print("Sorry, you lose.", bet_amount / 2)
    elif mode == "Range":
        if player != computer:
            print("Sorry, you lose.", bet_amount / 2)
        else:
            print("Congratulations! You win ", bet_amount * 2)
    else:
        return(f"Invalid game mode: {mode}")
if __name__  == "__main__":
    bet_amount = int(input("Enter your bet amount: "))
    choice = genuine_choice()
    play_game(choice)