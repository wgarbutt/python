import random


def setup_game():
    with open('word_list.txt', 'r') as wl:
        words = wl.readlines()
        global correct_count
        correct_count = 0
        list_length = len(words)
        num = random.randint(0,list_length - 1)
        word = words[num].strip()
        board = ["_" for i in range(len(word))]
        used_letters = []
        print("#################################\n#" '\x1b[6;30;42m' + " Welcome to Will's wordfinder! " + '\x1b[0m' + "#\n#################################")
        print("\nTry and guess this word!")
    return word, board, used_letters

word, board, used_letters  = setup_game()


while True:
    correct_count = board.count('_')
    while correct_count > 0:
        print(" ".join(board))
        print("\nGuesses: " + " ".join(used_letters))
        user_input = input("Enter your guess: ")
        if len(user_input) == len(word):
            if user_input == word:
                board = list(word)
                break
            else:
                print('\x1b[6;30;41m' + " Nope! That isnt the word we are looking for, try again! " + '\x1b[0m' )
        elif len(user_input) == 1 and user_input.isalpha():
            if user_input in used_letters:
                print("You already guessed that letter. Try again.")
            elif user_input in word:
                for i in range(len(word)):
                    if word[i] == user_input:
                        board[i] = user_input
                used_letters.append(user_input)
            else:
                used_letters.append(user_input)
        else:
            print("Invalid input. Please enter a valid letter or the entire word.")
            continue   
        correct_count = board.count('_')
    print("Congratulations " + '\x1b[6;30;42m' + word + '\x1b[0m' + " was the correct word!")
    play_again = input("Do you want to play again? (Y/N): ")

    if play_again.upper() == "Y":
        word, board, used_letters  = setup_game()
    else:
        break