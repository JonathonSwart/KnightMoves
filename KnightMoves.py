#Jonathon Swart
#This program will calculate how many moves it takes a knight to capture a king
#from various positions
#June 4, 2020

#Place the knight on the chess board
def SetKnight():
    global knightx
    global knighty
    knightx = int(knight[1])
    knighty = int(knight[3])
    board[knightx-1][knighty-1] = 'h'

    
#Place the king on the chess board 
def SetKing():
    global kingx
    global kingy
    kingx = int(king[1])
    kingy = int(king[3])
    board[kingx-1][kingy-1] = 'x'

def KnightMoves():
    
    global end_loop
    
    #2 up 1 left
    if x > 1 and y > 0:
        if board[x-2][y-1] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x-2)
        positionList.append(y-1)
        
    #2 up 1 right
    if x > 1 and y < 7:
        if board[x-2][y+1] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x-2)
        positionList.append(y+1)
            
    #2 down 1 left
    if x < 6 and y > 0:
        if board[x+2][y-1] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x+2)
        positionList.append(y-1)
        
    #2 down 1 right
    if x < 6 and y < 7:
        if board[x+2][y+1] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x+2)
        positionList.append(y+1)

    #2 left 1 down
    if x < 7 and y > 1:
        if board[x+1][y-2] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x+1)
        positionList.append(y-2)

    #2 left 1 up
    if x > 0 and y > 1:
        if board[x-1][y-2] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x-1)
        positionList.append(y-2)


    #2 right 1 down
    if x < 7 and y < 6:
        if board[x+1][y+2] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x+1)
        positionList.append(y+2)

    #2 right 1 up
    if x > 0 and y < 6:
        if board[x-1][y+2] == 'x':
            end_loop = True
        #append positions to a list
        positionList.append(x-1)
        positionList.append(y+2)




#Open text file
filename = "knight.txt"
inFile = open(filename, "r")

#the first line is the position of the king
king = inFile.readline()

#set knight coordinates to a variable
knight = inFile.readline()

#print knight moves
print ("Knight Moves")
print ("------------")
print ()

while knight != "":
    #The chess board
    board = [[ '-' for i in range(8) ] for j in range(8)]
    SetKing()
    SetKnight()
    moves = 0  #counter for moves
    
    end_loop = False
    while end_loop == False:
        positionList = []
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                for sqr in board[x][y]:
                    if sqr == 'h':
                        KnightMoves()
                                    
                    if end_loop == True:
                        break
                if end_loop == True:
                    break
            if end_loop == True:
                break


        counter1 = 0
        counter2 = 1

        
        while counter1 != len(positionList):
            x = positionList[counter1]
            y = positionList[counter2]

            board[x][y] = 'h'

            
            counter1 += 2
            counter2 += 2

        moves += 1
        
    #print amount of moves taken
    print ("It takes",str(moves),"moves for the knight at ("+str(knightx)+","+str(knighty)+") to capture the king at ("+str(kingx)+","+str(kingy)+").")
    
    knight = inFile.readline()
    


















