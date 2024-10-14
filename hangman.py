
import random
words = ["banana", "apple", "grape"]
 
def hangman():
    game_word = random.choice(words)
    show_word = []
    lives = 5 
    execute_loop = True

    for _ in game_word:
        show_word += "_"


    print("======== HANGMAN ========")
    print(f"Guess the word: {"".join(show_word)}")
    print(f"Lives: {lives}")

    while execute_loop:
        user_letter = input("Enter a letter: ").lower()
        if user_letter not in game_word:
            lives -= 1
        index = 0
        for letter in game_word:
            if letter == user_letter:
                show_word[index] = user_letter
            index += 1
        
        print(f"Guess the word: {"".join(show_word)}")
        print(f"Lives: {lives}")


        if lives < 5: print("    |    ")
        if lives < 4: print("    0    ")
        if lives < 3: print("   /|\\  ")
        if lives < 2: print("    |    ")
        if lives == 0:print("   / \\  ")

        if "_" not in show_word:
            print("You won") 
            execute_loop = False
        if lives == 0:  
            print("You lost")
            print(f"The word was: {game_word}")
            execute_loop = False 

play = True
while play:
    ask_to_play = input(" Do you wanna play hangman? ").lower()
    if ask_to_play == "yes" or ask_to_play == "y":
        hangman()
    elif ask_to_play == 'no' or ask_to_play == "n":
        break
    else:
        print("Please enter 'yes' or 'no' ")
