board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    
    for i in range(len(board)):
        # sudoku board is made up of 3x3 squares
        # this is to break up rows
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        # board[0] = len of rows
        for j in range(len(board[0])):
            # checking to make sure it is not the 0th colum
            # 0 % 3 === 0 and would print out on the edge
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # as opposed to default line ending of \n
            # at the end of the line, print the line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
#print_board(board)

"""
    Given a board, and number, and a position,
    is the new board layout valid? This requires
    checking the row, the colum, and the individual
    square/space.
    
    board is the given board
    number is the digit being input as a guess/answer
    position is a tuple with (x, y) or (row, column) or (i, j) indexing
"""
def is_move_valid(board, number, position):
    # check row
    # looking for two of the same numbers in the first row
    for i in range(len(board[0])):
        # position will be a tuple with (i,j) indexing
        if board[position[0]][i] == number and position[1] != i:    # dont check what we just inserted
            return False

    # check column
    for i in range(len(board)):
        # checking if our current "x" value is equal to the number we inserted
        if board[i][position[1]] == number and position[0] != i:    # skipping position we just inserted 
            return False
        
    # now check 3x3 box for same number
    # first determine which of the boxes we are in
    box_x = position[1] // 3    
    box_y = position[0] // 3
    
    # multiply by 3 to get to the correct index, squares/boxes are 3x3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            # within the correct 3x3 square, check to see if given "number" is repeated
            if board[i][j] == number and (i, j) != position:
                # if we find a digit that matches "number" (input) then not valid input
                return False
    
    # made it through all the checks
    return True
    
"""
    Given a board, find empty square. empty = 0
"""
def find_empty(board):
    # iterate through the rows
    for i in range(len(board)):
        # iterate through the columns
        for j in range(len(board[0])):
            # if the number in the space is 'empty' (0) return tuple of "position"
            if board[i][j] == 0:
                return (i, j)   # tuple of (row, col) this is position
    # need "None" for solve method check
    return None
            
#print(find_empty(board))

# getting to end means the board was solved!
def solve(board):
    
    find_Empty_Spot = find_empty(board)
    # no empty spaces were found
    if not find_Empty_Spot:
        # board is solved!
        return True
    else:
        # found an empty spot (0), board is not complete
        row, col = find_Empty_Spot
    
    # try each digit 1-10 as a solution
    for i in range(1,10):
        # if the board is in a valid state, try new digit
        if is_move_valid(board, i, (row, col)):
            # if move was sucessful, update i
            board[row][col] = i
            # check to see if we are done
            if solve(board):
                return True
            # solve did not work, reset index/value
            board[row][col] = 0
    return False
            


print_board(board)
solve(board)
print_board(board)



