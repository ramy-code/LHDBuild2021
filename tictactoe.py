board = [["","",""],["","",""],["","",""]]
def print_board():
    for line in board:
        for el in line:
            if (el != "X" and el != "O"):
                print(" |   |",end="")
            else:
                print(" | "+el+" |",end="")
        print("\n--------------------")
    

def play():
    position_X = int(input("Player X : Pick a number between 1 and 9 to play in")) - 1
    position_O = int(input("Player O : Pick a number between 1 and 9 to play in")) - 1
    board[int(position_X/3)][position_X%3] = "X"
    board[int(position_O/3)][position_O%3] = "O"

def compute_position():
    for i in range(0,3):
        j=0
        if(board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2] and board[i][j+1] == board[i][j+2]):
            return board[i][j]
    for j in range(0,3):
        i=0
        if(board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j] and board[i+1][j] == board[i+2][j]):
            return board[i][j]
    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[1][1]==board[2][2]):
        return board[0][0]
    if(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[1][1]==board[2][0]):
        return board[0][2]

# Main Loop
turn = 0
while(turn<5):
    play()
    print_board()
    winner = compute_position()
    if(winner == "X" or winner == "O"):
        print("Congratulations "+ winner + " you won!")
        exit()
    turn += 1
if(turn==4):
    print("It's a draw !")
    
