def censor(text, word):
    word_list = text.split()
    stars = '*' * len(word)
    index = 0
    for i in word_list:

        if i == word:
            word_list[index] = stars
        index += 1

    result = ' '.join(word_list)

    return result


actual_name = []
c = 0


def user_input(player):
    less_than_one_char = False
    while not less_than_one_char:
        global actual_name
        global c
        if c >= 1:
            break
        else:
            actual_name = input("{} please enter the word. ".format(player))
            actual_name = actual_name.lower()
            if actual_name == '' or len(actual_name) <= 1:
                print("Cannot be empty or less than 1 character")
            else:
                print(censor(actual_name, actual_name))
                start_game()
                c += 1


def start_game():
    gameStart = False
    while not gameStart:
        start = input("Press enter to Start the game \n")
        if start == '':
            gameStarts()
            gameStart = True

        else:
            print("")


def gameStarts():
    global remaining
    actual_word = list(actual_name)
    hidden_name = []

    for i in actual_word:
        if i == ' ':
            actual_word.remove(' ')
        hidden_name.append('_')

    print(hidden_name)

    isGameOver = False
    attempts = 0
    max_attempts = 4

    # stop = 30
    # second = 0
    # # print('> Stopwatch Started.')
    # while stop > second:
    #     if second < stop:
    #         second = second + 1
    #         time.sleep(1)
    #         # sys.stdout.write(str(second))
    #     else:
    #         second += 1
    #         time.sleep(1)
    #         # sys.stdout.write(str(second))

    while not isGameOver:

        print('you have {} left over. '.format((max_attempts - attempts + 1)))

        hiddenString = ' '.join(hidden_name)
        print('you current word is {}  : '.format(hiddenString))

        print('    |----------|    ')
        print('    |          |    ')
        print('    |         ' + (' O' if attempts > 0 else ''))
        print('    |         ' + ('/ \\' if attempts > 1 else ''))
        print('    |         ' + (' |' if attempts > 2 else ''))
        print('    |         ' + ('/ \\' if attempts > 3 else ''))
        print(' ----------     ')

        if all("_" == i for i in actual_word):
            print("Congrats, you win")
            isGameOver = True
        else:
            char = input("please enter your word: ").lower()

            if len(char) > 1 or char == '':
                print("please enter one letter at a time")
            elif char in actual_word:
                for i in range(len(actual_word)):
                    character = actual_word[i]
                    if character == char:
                        hidden_name[i] = actual_word[i]
                        actual_word[i] = '_'
            elif char in hidden_name:
                for i in range(len(hidden_name)):
                    character = hidden_name[i]
                    if character == char:
                        print("character already exists")
            elif attempts == 4:
                print('attempts: ', attempts)
                print("Game Over. :(")
                break
            else:
                attempts += 1

    print('ACTUAL WORD: ', actual_name)
    print('HIDDEN WORD: ', hidden_name)


while True:
    player1 = input("Please enter the name of player1. ")
    player2 = input("Please enter the name of player2. ")
    if player1 == player2:
        print("Both names are not suppose to be the same")
    else:
        while True:
            first_player = input("Please choose who wants to enter the words first.  "
                                 "\nPress 'A' for player 1 \nPress 'B' for player 2\n")

            if first_player == 'A' or first_player == 'a':
                user_input(player1)
                break
            elif first_player == 'B' or first_player == 'b':
                user_input(player2)
                break
            else:
                print("Please Press either A or B")