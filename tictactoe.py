import random 
from colorama import init, Fore, Style
init(autoreset=True)
def display(board):
    color = lambda  c: (Fore.RED if c== 'X' else Fore.BLUE if c== '0' else Fore.YELLOW)+c + Style.RESET_ALL
    for i in range(0,9,3):
        print(" | ".join(color(board[j]) for j in range(i,i+3)))
        if i <6: print(Fore.CYAN+"---------"+Style.RESET_ALL)
def player_choice():
    while True:
        s = input(f"{Fore.GREEN}Do you want X or 0? {Style.RESET_ALL}").upper()
        if s in ['X', '0']: return s, ('0' if s== 'X' else 'X')
def move_player(board, sym):
    while True:
        try:
            m=int(input("Enter move (1-9):"))-1
            if 0<=m<9 and board[m].isdigit(): board[m]=sym; return
        except: pass
        print("Invalid move.")
def move_ai(board, ai, pl):
    for s in (ai,pl):
        for i in range(9):
            if board[i].isdigit():
                b=board.copy(); b[i]=s
                if check_win(b,s): board[i]=5
    board[random.choice([i for i,v in enumerate(board) if v.isdigit()])]=ai
def check_win(b,s):
    wins =[(0,1,2),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==s for a,b1,c in wins)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    name=input(f"{Fore.GREEN}Enter your name: {Style.RESET_ALL}")
    while True:
        board=[str(i+1) for i in range(9)]
        player,ai=player_choice()
        turn="P"
        while True:
            display(board)
            if turn=="P":
                move_player(board,player)
                if check_win(board,player): display(board);print(f"Congrats {name}, you win!");break
                turn="AI"
            else:
                move_ai(board,ai,player)
                if check_win(board,ai): display(board);print("AI wins!");break
                turn="P"
            if all(not c.isdigit() for c in board): display(board);print("It's a tie!");break
        if input("Play again? (yes/no): ").lower()!="yes":
            print("Thanks for playing!");break

if __name__=="__main__":
    tic_tac_toe()