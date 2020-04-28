
nCols = 8
nRows = 8
empySpace = 0
p1RegPiece = 1
p2RegPiece = 2
p1KingPiece = 3
p2KingPiece = 4
p1 = 1
p2 = 2

moveUpRight_g = 0
moveUpLeft_g = 1
moveDownRight_g = 2
moveDownLeft_g = 3

jumpUpRight_g = 0
jumpUpLeft_g = 1
jumpDownRight_g = 2
jumpDownLeft_g = 3


class GameBoard:
    p1Piece = 'x'
    p1King = 'X'
    p2Piece = 'o'   
    p2King = 'O'
    blank = ' '

    # 1 = player 1
    # 2 = player 2
    # 3 = player 1 kinged
    # 4 = player 2 kinged 

    gameBoard = [
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [2,0,2,0,2,0,2,0],
    [0,2,0,2,0,2,0,2],
    [2,0,2,0,2,0,2,0]]

    vertSym = ['A', 'B', 'C', 'D', 'E','F','G','H']
    vertSym2 = ['a', 'b', 'c', 'd', 'e','f','g','h']
    horzSym = ['1', '2', '3', '4', '5','6','7','8']


#FUNCTIONS

    def setPlayerOneSymms(self,word):
        self.p1Piece = word
        self.p1King = word.upper()

    def setPlayerTwoSymms(self,word):
        self.p2Piece = word
        self.p2King = word.upper()

    def announcePlayerSymms(self):
        print("Player One will be: %s" % self.p1Piece)
        print("Player Two will be: %s" % self.p2Piece)

    def drawBoard(self):

        print("\n   ---------------------------------")
        print("   To Move: XX>XX (ex. C1>D2)")
        print("   ---------------------------------")
        for x in range(nRows):
            print("\n   ---------------------------------")
            print(self.vertSym[nRows - x - 1] + '  |', end='')
            for y in range(nCols):
                symbol = '*'
                
                if(self.gameBoard[x][y] == empySpace):
                    symbol = self.blank            
                elif(self.gameBoard[x][y] == p1RegPiece):
                    symbol = self.p1Piece
                elif(self.gameBoard[x][y] == p2RegPiece):
                    symbol = self.p2Piece
                elif(self.gameBoard[x][y] == p1KingPiece):
                    symbol = self.p1King
                elif(self.gameBoard[x][y] == p2KingPiece):
                    symbol = self.p2King
                else:
                    symbol = '?'
                


                #main print symbol
                print( ' ' + symbol + ' |', end='')

        print("\n   ---------------------------------")
        print("     1   2   3   4   5   6   7   8  ")

   

    def getVertIndex(self,word):
        #need to translate the char here to an index
        for x in range(len(self.vertSym)):
            if(word == self.vertSym[x]):
                return len(self.vertSym) - (x + 1)
        #im lazy and dont know to uppers yet
        for x in range(len(self.vertSym2)):
            if(word == self.vertSym2[x]):
                return len(self.vertSym2) - (x + 1)

        return -1


    def getHorzIndex(self,word):
        #need to translate the char here to an index
        for x in range(nRows):
            if(word[0] == self.horzSym[x]):
                return x
        return -1


    def areValidPiecesSelected(self,x1,y1,x2,y2,player):
        sourcePiece = self.gameBoard[x1][y1]
        tarSpace = self.gameBoard[x2][y2]
        #They must be moving their piece
        if(player == p1):
            if(sourcePiece != p1RegPiece and sourcePiece != p1KingPiece):
                print("Please select your own piece to move - %d" % sourcePiece)
                return False

        if(player == p2):
            if(sourcePiece != p2RegPiece and sourcePiece != p2KingPiece):
                print("Please select your own piece to move - %d" % sourcePiece)
                return False

        #They must be moving to a blank piece
        if(tarSpace != 0):
            print("Please select an empty space to move your piece to.")
            return False

        return True 

#returns the direction of the given coords and if valid for moving
    def getMoveDirection(self, x1, y1, x2, y2):
        if(x1 - x2) == 1:
            if(y1 - y2) == -1:
                return moveUpRight_g
            elif (y1 - y2) == 1:
                return moveUpLeft_g
        elif(x1 - x2) == -1:
            if(y1 - y2) == -1:
                return moveDownRight_g
            elif (y1 - y2) == 1:
                return moveDownLeft_g
        else:
            return -1

#returns the direction of the given coords and if valid for jumping
    def getJumpDirection(self, x1, y1, x2, y2):
        if(x1 - x2) == 2:
            if(y1 - y2) == -2:
                return jumpUpRight_g
            elif (y1 - y2) == 2:
                return jumpUpLeft_g
        elif(x1 - x2) == -2:
            if(y1 - y2) == -2:
                return jumpDownRight_g
            elif (y1 - y2) == 2:
                return jumpDownLeft_g
        else:
            return -1


#Can this piece MOVE "down and right" on the board
    def canMoveDownRight(self, x, y):
        #set target coords
        x2 = x + 1
        y2 = y + 1

        #check bounds
        if(x2 >= nRows):
            return False
        elif (y2 >= nCols):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece MOVE "down and right" on the board
    def canMoveDownLeft(self, x, y):
        #set target coords
        x2 = x + 1
        y2 = y - 1

        #check bounds
        if(x2 >= nRows):
            return False
        elif (y2 < 0):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece MOVE "up and right" on the board
    def canMoveUpRight(self, x, y):
        #set target coords
        x2 = x - 1
        y2 = y + 1
        print("coord post %d %d" % (x2,y2))
        #check bounds
        if(x2 < 0):
            return False
        elif (y2 >= nCols):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece MOVE "up and right" on the board
    def canMoveUpLeft(self, x, y):
        #set target coords
        x2 = x - 1
        y2 = y - 1

        #check bounds
        if(x2 < 0):
            return False
        elif (y2 < 0):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece JUMP "down and right" on the board
    def canjumpDownRight(self, x, y, player):
        #set target coords
        x2 = x + 2
        y2 = y + 2

        #check bounds
        if(x2 >= nRows):
            return False
        elif (y2 >= nCols):
            return False
        
        if not self.isEnemyPieceAt(player, x+1, y+1):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece JUMP "down and right" on the board
    def canjumpDownLeft(self, x, y, player):
        #set target coords
        x2 = x + 2
        y2 = y - 2

        #check bounds
        if(x2 >= nRows):
            return False
        elif (y2 < 0):
            return False

        if not self.isEnemyPieceAt(player, x+1, y-1):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece JUMP "up and right" on the board
    def canjumpUpRight(self, x, y, player):
        #set target coords
        x2 = x - 2
        y2 = y + 2

        #check bounds
        if(x2 < 0):
            return False
        elif (y2 >= nCols):
            return False

        if not self.isEnemyPieceAt(player, x-1, y+1):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

#Can this piece JUMP "up and right" on the board
    def canjumpUpLeft(self, x, y, player):
        #set target coords
        x2 = x - 2
        y2 = y - 2

        #check bounds
        if(x2 < 0):
            return False
        elif (y2 < 0):
            return False

        if not self.isEnemyPieceAt(player, x-1, y-1):
            return False
        else:
            if self.gameBoard[x2][y2] == 0:
                return True
            else:
                return False

    

#Determines if the MOVE is valid
#Checks if they selected the correct pieces/spaces,
#Then checks if they are MOVING in the correct direction.
    def isValidMove(self,x1,y1,x2,y2,player):
        print("validating move")
        if(not self.areValidPiecesSelected(x1,y1,x2,y2,player)):
            return False

        sourcePiece = self.gameBoard[x1][y1]
        moveDir = self.getMoveDirection(x1, y1, x2, y2)

        print("player is moving in direction %d " % moveDir)

        if moveDir == -1:
            return False

        
        
        if(player == p1 and sourcePiece == p1RegPiece):          
            if moveDir == moveDownRight_g:
                return self.canMoveDownRight(x1,y1)
            elif moveDir == moveDownLeft_g:
                return self.canMoveDownLeft(x1,y1)

        elif(player == p2 and sourcePiece == p2RegPiece):
            print("player 2 moving")
            if moveDir == moveUpRight_g:
                return self.canMoveUpRight(x1, y1)
            elif moveDir == moveUpLeft_g:
                return self.canMoveUpLeft(x1, y1)
            print("player 2 cant move")

        elif((player == p1 and sourcePiece == p1KingPiece) or (player == p2 and sourcePiece == p2KingPiece)):
            if moveDir == moveDownRight_g:
                return self.canMoveDownRight(x1,y1)
            elif moveDir == moveDownLeft_g:
                return self.canMoveDownLeft(x1,y1)
            elif moveDir == moveUpRight_g:
                return self.canMoveUpRight(x1, y1)
            elif moveDir == moveUpLeft_g:
                return self.canMoveUpLeft(x1, y1)
        
        print("Invalid movement direction")
        return False     

#Determines if the JUMP is valid
#Checks if they selected the correct pieces/spaces,
#Then checks if they are JUMPING in the correct direction.
    def isValidJump(self,x1,y1,x2,y2,player):
                
        if(not self.areValidPiecesSelected(x1,y1,x2,y2,player)):
            return False

        sourcePiece = self.gameBoard[x1][y1]
        jumpDir = self.getJumpDirection(x1,y1,x2,y2)

        if jumpDir == -1:
            return False

        #Check if movement direction is valid - since we know they are targeting their piece and an empty space all we have left to deterimine is if the direction is correct.
        if(player == p1 and sourcePiece == p1RegPiece):          
            if jumpDir == jumpDownRight_g:
                return self.canjumpDownRight(x1,y1,player)
            elif jumpDir == jumpDownLeft_g:
                return self.canjumpDownLeft(x1,y1,player)

        elif(player == p2 and sourcePiece == p2RegPiece):
            if jumpDir == jumpUpRight_g:
                return self.canjumpUpRight(x1, y1,player)
            elif jumpDir == jumpUpLeft_g:
                return self.canjumpUpLeft(x1, y1,player)

        elif((player == p1 and sourcePiece == p1KingPiece) or (player == p2 and sourcePiece == p2KingPiece)):
            if jumpDir == jumpDownRight_g:
                return self.canjumpDownRight(x1,y1,player)
            elif jumpDir == jumpDownLeft_g:
                return self.canjumpDownLeft(x1,y1,player)
            elif jumpDir == jumpUpRight_g:
                return self.canjumpUpRight(x1, y1,player)
            elif jumpDir == jumpUpLeft_g:
                return self.canjumpUpLeft(x1, y1,player)
        else:
            print("Invalid movement direction")
            return False   

       

#we know the command is a move if our difs between x's and y's are 1 or -1
    def isCommandMove(self, x1, y1, x2, y2):
        if(x1 - x2 == 1 or x1 - x2 == -1):
            if(y1 - y2 == 1 or y1 - y2 == -1):
                return True
        print("command wasnt move")
        return False

#we know the commmand is a jump if our difs between x's and y's are 2 or -2
    def isCommandJump(self, x1, y1, x2, y2):
        if(x1 - x2 == 2 or x1 - x2 == -2):
            if(y1 - y2 == 2 or y1 - y2 == -2):
                return True
        print("command wasnt jump")
        return False     



#Checks for if there is an enemy piece at the given location
    def isEnemyPieceAt(self,player,x,y):
        tarPiece = self.gameBoard[x][y]
        if(player == 1 or player == 3):
            if(tarPiece == 2 or tarPiece == 4):
                return True
        elif(player == 2 or player == 4):
            if(tarPiece == 1 or tarPiece == 3):
                return True
        else:
            return False      

#Does the work of actually moving the pieces on the game board
#Also, kings the piece if it moves to the end of the baord and is not kinged already
    def movePiece(self,x1,y1,x2,y2,player):
        self.gameBoard[x2][y2] = self.gameBoard[x1][y1]
        self.gameBoard[x1][y1] = 0

        if(player == p1):
            if(x2 == 7 and self.gameBoard[x2][y2] == p1RegPiece):
                self.gameBoard[x2][y2] = p1KingPiece
                print("Kinging player 1 piece")

        if(player == p2 and self.gameBoard[x2][y2] == p2RegPiece):
            if(x2 == 0):
                self.gameBoard[x2][y2] = p2KingPiece
                print("Kinging player 2 piece")


#Does the work of actually moving the pieces on the game board
#Also, kings the piece if it moves to the end of the baord and is not kinged already
    def jumpPiece(self,x1,y1,x2,y2,player):
        self.gameBoard[x2][y2] = self.gameBoard[x1][y1]
        self.gameBoard[x1][y1] = 0

        jumpDir = self.getJumpDirection(x1,y1,x2,y2)

        if jumpDir == jumpUpLeft_g:
            self.gameBoard[x1-1][y1-1] = 0
        elif jumpDir == jumpUpRight_g:
            self.gameBoard[x1-1][y1+1] = 0
        elif jumpDir == jumpDownRight_g:
            self.gameBoard[x1+1][y1+1] = 0
        elif jumpDir == jumpDownLeft_g:
            self.gameBoard[x1+1][y1-1] = 0
        else:
            print("something went terribly wrong... run... RUN!!!!")

        if(player == p1):
            if(x2 == 7 and self.gameBoard[x2][y2] == p1RegPiece):
                self.gameBoard[x2][y2] = p1KingPiece
                print("Kinging player 1 piece")

        if(player == p2 and self.gameBoard[x2][y2] == p2RegPiece):
            if(x2 == 0):
                self.gameBoard[x2][y2] = p2KingPiece
                print("Kinging player 2 piece")




    def canPieceJump(self, player, x, y):
        sourcePiece = self.gameBoard[x][y]
        if(player == p1):
            if sourcePiece == p1RegPiece :
                return (self.canjumpDownLeft(x,y,player) or self.canjumpDownRight(x,y,player))
            elif sourcePiece == p1KingPiece :
                return (self.canjumpUpLeft(x,y,player) or self.canjumpUpRight(x,y,player) or self.canjumpDownRight(x,y,player) or self.canjumpDownLeft(x,y,player))
            else:
                return False
        elif(player == p2):
            if sourcePiece == p2RegPiece :
                return (self.canjumpUpLeft(x,y,player) or self.canjumpUpRight(x,y,player))
            elif sourcePiece == p2KingPiece :
                return (self.canjumpUpLeft(x,y,player) or self.canjumpUpRight(x,y,player) or self.canjumpDownRight(x,y,player) or self.canjumpDownLeft(x,y,player))
            else:
                return False
        else:
            return False
                

    def canCurrentPlayerJump(self,player):
        print("Can current Player jump?")
        for x in range(nRows):
            for y in range(nCols):
                piece = self.gameBoard[x][y]

                if player == p1 and (piece == p1RegPiece or piece == p1KingPiece):
                    if self.canPieceJump(player,x,y):
                        print("player one should have jumped")
                        return True
                elif player == p2 and (piece == p2RegPiece or piece == p2KingPiece):
                    if self.canPieceJump(player,x,y):
                        print("player two should have jumped")
                        return True
                else:
                    continue


    def isGameOver(self):
        numP1Pieces = 0
        numP2Pieces = 0
        for x in range(nRows):
            for y in range(nCols):
                piece = self.gameBoard[x][y]

                if piece == p1RegPiece or piece == p1KingPiece:
                    numP1Pieces += 1
                elif piece == p2RegPiece or piece == p2KingPiece:
                    numP2Pieces += 2

        if numP1Pieces == 0:
            return 1
        elif numP2Pieces == 0:
            return 2
        else:
            return 0

                
            

    

 

    
