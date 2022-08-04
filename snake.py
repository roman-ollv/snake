from random import randrange

def create_board(coordinates):
    board = []
    for _ in range(10):
        board.append(["."]* 10)
    for x, y in coordinates:
        board[x][y] = "x"         
    for row in board:
        print(" ".join(row))
    return board  

def food(board,coordinates):
    while True:
        food_x = randrange (10)
        food_y = randrange (10)
        print(food_x, food_y)
        if (food_x, food_y) not in coordinates:
            board[food_x][food_y] = "}"
            return board

def movement(board, coordinates, direction, food):
    x = coordinates[-1][0]
    y = coordinates[-1][1]
    if direction == "w":
        y -=1
    elif direction == "e":
        y += 1
    elif direction == "n":
        x -= 1
    elif direction == "s":
        x += 1 
    elif direction == "end":
        print ("game over")
        exit()
    try:
        direction != "n" or direction != "s" or direction != "w" or direction != "e" or direction != "end"
    except ValueError:
        raise ValueError ("Choose the direction : 'n' , 's', 'w', 'e': ")

    if [x,y] in coordinates:
        raise ValueError ("Snake bites itself. Game over")
    elif x > 10 or  y > 10 or x < 0 or  y < 0:
        raise ValueError ( "Wall crash. Game over")
    else:
        coordinates.append([x,y])
        tail = coordinates[0]
        if board[x][y] == "}":
            board = food(board,coordinates)
            return coordinates
        else:
            board[tail[0]][tail[1]] = "."
            coordinates.remove(coordinates[0])
            return coordinates

def game():
    coordinates = [[0,0],[0,1],[0,2]]
    board = create_board(coordinates)
    board = food(board, coordinates)
    print(board)
    while True:
        board = create_board(coordinates)
        direction = input ("Choose thr direction: 'w' = 'west', 'e' = 'east', 's' = 'south', 'n' = 'north' \nTo leave the game type 'end'")
        move = movement(board,coordinates,direction, food)
game()
