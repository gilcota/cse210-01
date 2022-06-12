# Assignment: Wk 01 Prove Developer - A simple Tic-Tac-Toe Game
# Author: Mahonri Gil

# main function
def main():
    gb = [1,2,3,4,5,6,7,8,9]
    player = "X"
    playing = True
    
    while player != False:
        select(gb, player)

        player = winner(gb, player, playing)

# shows the actual board game values
def showboard(gb):

    """
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """
    print(f"\n{gb[0]}|{gb[1]}|{gb[2]}")
    print(f"-+-+-")
    print(f"{gb[3]}|{gb[4]}|{gb[5]}")
    print(f"-+-+-")
    print(f"{gb[6]}|{gb[7]}|{gb[8]}\n")

# defines if there is a winner or if it is a draw
def winner(gb, player, playing):
    while True:
        if (gb[0] == "O" and gb[1] == "O" and gb[2] == "O") or (gb[0] == "X" and gb[1] == "X" and gb[2] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break
        
        elif (gb[3] == "O" and gb[4] == "O" and gb[5] == "O") or (gb[3] == "X" and gb[4] == "X" and gb[5] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break
        
        elif (gb[6] == "O" and gb[7] == "O" and gb[8] == "O") or (gb[6] == "X" and gb[7] == "X" and gb[8] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break
        
        elif (gb[0] == "O" and gb[3] == "O" and gb[6] == "O") or (gb[0] == "X" and gb[3] == "X" and gb[6] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break

        elif (gb[1] == "O" and gb[4] == "O" and gb[7] == "O") or (gb[1] == "X" and gb[4] == "X" and gb[7] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break

        elif (gb[2] == "O" and gb[5] == "O" and gb[8] == "O") or (gb[2] == "X" and gb[5] == "X" and gb[8] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break

        elif (gb[0] == "O" and gb[4] == "O" and gb[8] == "O") or (gb[0] == "X" and gb[4] == "X" and gb[8] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break

        elif (gb[2] == "O" and gb[4] == "O" and gb[6] == "O") or (gb[2] == "X" and gb[4] == "X" and gb[6] == "X"):
            showboard(gb)
            print(f"Good game. Thanks for playing!")
            playing = False
            return playing
            break

        elif (gb[0] == "O" or gb[0] == "X") and (gb[1] == "O" or gb[1] == "X") and (gb[2] == "O" or gb[2] == "X") and (gb[3] == "O" or gb[3] == "X") and (gb[4] == "O" or gb[4] == "X") and (gb[5] == "O" or gb[5] == "X") and (gb[6] == "O" or gb[6] == "X") and (gb[7] == "O" or gb[7] == "X") and (gb[8] == "O" or gb[8] == "X"):
            showboard(gb)
            print(f"Game over, it's a draw!")
            playing = False
            return playing
            break

        else:
            playing = True
            break
        
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    
    return player
        
# changes player turn
def select(gb, player):
    
    showboard(gb)

    position = int (input(f"{player}'s turn to choose a square (1-9): "))
    
    gb[position - 1] = player
    
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

    return player

# Call main to start this program
if __name__ == "__main__":
    main()