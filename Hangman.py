from itertools import groupby
import sys


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


c = 0


def replay_game():
    while True:
        print('\n')
        decision = input("Please enter Y to play again or any other key to Quit: ")
        if decision == 'Y' or decision == 'y':
            main()
        else:
            sys.exit()


actual_name = []

counter = 0

char = ''

aa = []
bb = []
cc = []


def compare(list1, list2):
    for i in list1[:]:
        if i in list2:
            list2.remove(i)
    return list2


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
                # print(censor(actual_name, actual_name))
                start_game()
                c += 1


def start_game():
    game_start = False
    while not game_start:
        start = input("Press enter to Start the game \n")
        if start == '':
            game_starts()
            game_start = True

        else:
            print("")


def game_starts():
    global aa, bb, cc, counter
    actual_word = list(actual_name)

    hidden_name = []
    not_in_list = []

    head1 = []
    tail1 = []

    aa.clear()
    bb.clear()
    cc.clear()

    for k, g in groupby(actual_word, key=lambda s: s.startswith(' ')):
        if k:
            head1.append(list(g))
        else:
            tail1.append(list(g))

    out = [u for u in tail1]

    for i in out:
        sub_result = []
        for j in i:
            sub_result.append('_')
        hidden_name.append(sub_result)

    # print("OUT: ", out)
    # print("HIDDEN: ", hidden_name)

    is_game_over = False
    attempts = 0
    max_attempts = 5

    temp = []
    temp2 = []

    while not is_game_over:
        print('you have {} left over. '.format((max_attempts - attempts)))

        # hidden_string = [''.join(chars) for chars in hidden_name]
        hidden_string = ''.join(str(hidden_name))
        # hidden_string = ''.join(hidden_name)
        print('you Result is :  {} '.format(hidden_string))

        print('    |----------|    ')
        print('    |          |    ')
        print('    |         ' + (' O' if attempts > 0 else ''))
        print('    |         ' + ('/ \\' if attempts > 1 else ''))
        print('    |         ' + (' |' if attempts > 2 else ''))
        print('    |         ' + ('/ \\' if attempts > 3 else ''))
        print(' ----------     ')

        if attempts > 4:
            print('attempts: ', attempts)
            print("Game Over. :(")
            print('ACTUAL WORD: ', out)
            print('HIDDEN WORD: ', hidden_name)
            replay_game()
        else:
            char = input("please enter your word: ").lower()
            counter = 0
            if len(char) > 1 or char == '':
                print("please enter one letter at a time")

            elif char in aa:
                print("character already exists")

            elif (char in sublist for sublist in out):
                for list_counter, sublist in enumerate(out):
                    for sublist_counter, i in enumerate(sublist):
                        character = sublist[sublist_counter]
                        if character == char:
                            hidden_name[list_counter][sublist_counter] = character
                            temp.append(character)
                            aa = list(set(temp))
                            if out == hidden_name:
                                print("Congrats, you win")
                                is_game_over = True
                                print('ACTUAL WORD: ', out)
                                print('HIDDEN WORD: ', hidden_name)
                                replay_game()
                        elif character != char:
                            temp2.append(char)
                            bb = list(set(temp2))

                            cc = compare(aa, bb)

            if char in cc:
                if counter == 1:
                    break

                elif char not in aa and char in not_in_list:
                    print("character already exists in not given list {}".format(cc))
                    counter += 1
                else:
                    if char not in aa:
                        not_in_list.append(char)
                        print("Sorry wrong word {}".format(cc))
                        attempts += 1
                        counter += 1


def main():
    print("====== Welcome to the Hangman Game ======")
    while True:
        # if c == 1:
        #     break
        while True:
            player1 = input("Please enter the name of player1. ")
            if player1 == '':
                print("Name of Player 1 cannot be blank")
            else:
                break
        while True:
            player2 = input("Please enter the name of player2. ")
            if player2 == '':
                print("name of Player2 cannot be blank")
            else:
                break
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


if __name__ == '__main__':
    main()
