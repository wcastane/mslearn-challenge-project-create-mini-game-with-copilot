import random

# La Rock gana a las Scissors.
# Las Scissors ganan al Paper.
# El Paper gana a la Rock.

# El jugador podrá elegir una de las tres opciones, rock, paper o scissors, y se le debería advertir en caso de introducir una opción no válida.
# En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
# Al final de cada ronda, el jugador elegirá si vuelve a jugar.
# Muestra la puntuación del jugador al final del juego.
# El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            score += 1
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Your final score is {score}.")

play_game()