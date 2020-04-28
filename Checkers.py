import gameBoard


#TODO
#generic bug fixes insert more here
#Add lower case requirement for piece name
#Add to upper case for kinged pieces


def parseCommand(board,word, player, coords,isRunning):
    if(word == "x"):
        isRunning = False
    if(len(word) != 5):
        print("Too many characters detected")
        return 0
    if(word[2] != '>'):
        print("Please separate your command with the > symbol")
        return 0

    coords[0] = board.getVertIndex(word[0])
    if(coords[0] == -1):
        print("Invalid first character")
        return 0
    coords[1] = board.getHorzIndex(word[1])     
    if(coords[1] == -1):
        print("invalid second character")
        return 0
        
    coords[2] = board.getVertIndex(word[3])
    if(coords[2] == -1):
        print("Invalid fourth character")
        return 0
        
    coords[3] = board.getHorzIndex(word[4])     
    if(coords[3] == -1):
        print("Invalid fifth character")
        return 0
        

    print("1s:(%d,%d)" % (coords[0],coords[1]))
    print("2s:(%d,%d)" % (coords[2],coords[3]))
    return 1

#return values
# 0 = player moved
# 1 = player jumped
# 2 = invalid movement
# 3 = Tried to move but jump is avialable 
def processCommand(board, player, x1, y1, x2, y2):
    print("processing command...")
    if(board.isCommandMove(x1,y1, x2, y2)):
        if(board.canCurrentPlayerJump(player)):
            return 3
        elif (board.isValidMove(x1,y1,x2,y2,player)):
            print("Player tried to move and it is a valid move so lets move them")
            board.movePiece(x1,y1,x2,y2,player)
            return 0
        else:
            return 2
    elif(board.isCommandJump(x1, y1, x2, y2)):
        if(board.isValidJump(x1, y1, x2, y2, player)):
            print("Player tried to jump and it is a valid jump so lets mote them and remove the piece they jumped")
            board.jumpPiece(x1,y1,x2,y2, player)
            return 1
    else:
        print("Invalid movement attempted")
        return 2

    


def main():
    p1 = 1
    p2 = 2
    curPTurn = p1
    board = gameBoard.GameBoard()

    symm = input("What character will Player One be?  ")
    board.setPlayerOneSymm(symm)
    symm = input("What character will Player Two be?  ")
    board.setPlayerTwoSymm(symm)
    isRunning = True
    curMsg = ""
    while(isRunning):
        
        board.drawBoard()
        print()
        if(curPTurn == p1):
            print("it is %s's turn" % board.p1Piece)
        elif(curPTurn == p2):
            print("it is %s's turn" % board.p2Piece)

        print(curMsg)
        curMsg = ""
        command = input("Enter Command:")


        changeTurn = True
        coords = [0,0,0,0]
        if(parseCommand(board, command, curPTurn, coords,isRunning)):
            x1 = coords[0]
            y1 = coords[1]
            x2 = coords[2]
            y2 = coords[3]
            print("1s:(%d,%d)" % (x1,y1))
            print("2s:(%d,%d)" % (x2,y2))
            
            result = processCommand(board, curPTurn, x1, y1, x2, y2)
            print("the result was %d" % result)
            if(result == 0):
                print("moving...")
                changeTurn = True
            elif(result == 1):
                print("jumping...")
                #if they jumped and can jump again let them know
                if(board.canPieceJump(curPTurn,x2,y2)):
                    curMsg = "%s is able to jump again!" % curPTurn
                    print(x2)
                    print(y2)
                    changeTurn = False
                else:
                    changeTurn = True
            elif(result == 2):
                curMsg ="invalid movement attempted"
                changeTurn = False
            elif result == 3:
                curMsg = "A jump is available and must be taken"
                changeTurn = False
        else:
            changeTurn = False
            print("invalid input - probably an unneeded message since we type so fucking much all the gosh darn freaking time so just shut the fuck up and let me play the damn game")
        

        result = board.isGameOver()
        if result == 1:
            print("Congratulations player one you have won the game")
            isRunning = False
        elif result == 2:
            print("Congratulations player two you have won the game")
            isRunning = False


        if(changeTurn):
            if(curPTurn == p1):
                curPTurn = p2
            else:
                curPTurn = p1
        
        print()
        print()
        print()
        print()
        print()
        print()

            

    
    print("Main loop ended. Press any key to terminate.")

main()