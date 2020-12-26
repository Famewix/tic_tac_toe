# Creator Famewix
# https://github.com/Famewix
# date: 26.12.2020

import time


def display(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])


# Global vars
brd = list('---------')


def char_choice():
    actual = False
    choice = ['X','O']
    while actual == False:
        ques = input('Which one would you choose(O or X): ').upper()
        if ques == 'X' or ques == 'O':
            actual = True
            other = choice[choice.index(ques)-1] # cheaks for player 2
            print('You have choosed ' + ques + ' \nso the other player is ' + other )
            
        elif ques != 'X' or ques != 'O':
            print("Sorry i don't understand")
            actual = False
    return ques, other


def player_one():
    actual = False
    while actual == False:
        try:
            position = (int(input('choose a position(1-9)[Player 1]: '))-1)
            if position in range(0, 10) and brd[position] == '-': # cheaks if position is already filled
                brd[position] = a
                display(brd) # displays the board
                actual = True
            else:
                print('Position already filled, chose another one')
                actual = False
            if position not in range(0, 10):
                print('Position not found, try again.')
                actual = False
        except ValueError:
            print("You can't use String!!!")
            actual = False


def player_two():
    actual = False
    while actual == False:
        try:
            position = (int(input('choose a position(1-9)[Player 2]: '))-1)
            if position in range(0, 10) and brd[position] == '-': # cheaks if position is already filled
                brd[position] = b
                display(brd) # displays the board
                actual = True
            else:
                print('Position already filled, chose another one')
                actual = False
            if position not in range(0, 10):
                print('Position not found, try again.')
                actual = False
        except ValueError:
            print("You can't use String!!!")
            actual = False


def win_lose():
    res = False

    y = 'Player1'
    z = 'Player2'
    print("!!Num Pad formation!!")
    while res == False:

        player_one() # func call

        if (brd[0] == brd[1] == brd[2] == a) or (brd[3] == brd[4] == brd[5] == a) or (brd[6] == brd[7] == brd[8] == a):
            res = True
            print(y + ' has won!!!')
            break  # check win
        elif (brd[0] == brd[3] == brd[6] ==a) or (brd[1] == brd[4] == brd[7] == a) or (brd[2] == brd[5] == brd[8] == a):
            print(y + ' has won!!!')
            res = True # checks column
            break  # check win
        elif (brd[0] == brd[4] == brd[8] == a) or (brd[2] == brd[4] == brd[6] == a):
            print(y + ' has won!!!')
            res = True # checks corner to corner
            break  # check win
        elif brd[0] != '-' and brd[1] != '-' and brd[2] != '-' and brd[3] != '-' and brd[4] != '-' and brd[5] != '-' and brd[6] != '-' and brd[7] != '-' and brd[8] != '-':
            print("It's a TIE...")
            break

        time.sleep(0.5)

        player_two() # func call

        if (brd[0] == brd[1] == brd[2] == b) or (brd[3] == brd[4] == brd[5] == b) or (brd[6] == brd[7] == brd[8] == b):
            res = True # checks row
            print(z + ' has won!!!')
            break  # check win
        elif (brd[0] == brd[3] == brd[6] ==b) or (brd[1] == brd[4] == brd[7] == b) or (brd[2] == brd[5] == brd[8] == b):
            print(z + ' has won!!!')
            res = True # checks column
            break  # check win
        elif (brd[0] == brd[4] == brd[8] == b) or (brd[2] == brd[4] == brd[6] == b):
            print(z + ' has won!!!')
            res = True # checks corner to corner
            break  # check win


a, b = char_choice()
display(brd)
win_lose()
