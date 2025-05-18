theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',}
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'x'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("it's your turn," + turn + ".move to which place?")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("that place is already filled.\nMove to which place?")
            continue
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame over. \n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] ==theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] ==theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] ==theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break