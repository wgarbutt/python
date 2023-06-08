import random


def setup_game():
    with open('words.txt', 'r') as wl:
        words = wl.readlines()
        global correct_count
        correct_count = 0
        list_length = len(words)
        num = random.randint(0,list_length - 1)
        word = words[num].strip()
        board = ["_", "_", "_", "_", "_"]
        used_letters = []
        print("#################################\n#" '\x1b[6;30;42m' + " Welcome to Will's wordfinder! " + '\x1b[0m' + "#\n#################################")
        print("\nTry and guess this word!")
    return word, board, used_letters

word, board, used_letters  = setup_game()


while True:
    correct_count = board.count('_')
    while correct_count > 0:
        #print(word)
        print(" ".join(board))
        print("\nGuesses: " + " ".join(used_letters))
        user_input = input("Enter a new letter: ")
        user_input = user_input.lower()
        if len(user_input) == 1 and user_input.isalpha():
            if user_input in word and user_input not in used_letters:
                index_location = []
                for i in range(len(word)):
                    if word[i] == user_input:
                        index_location.append(i)
                for index in index_location:
                    board[index] = user_input
                correct_count += len(index_location)
                used_letters.append(user_input)
            elif user_input not in used_letters:
                used_letters.append(user_input)
        else:
            print('Enter a single letter to continue.')
            continue   
        correct_count = board.count('_')
    print("Congratulations " + '\x1b[6;30;42m' + word + '\x1b[0m' + " was the correct word!")
    play_again = input("Do you want to play again? (Y/N): ")

    if play_again.upper() == "Y":
        word, board, used_letters  = setup_game()
    else:
        break
