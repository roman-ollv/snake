from random import randrange

def create_board(coordinates):
    board = []
    for _ in range(10):
        board.append(["."] * 10)
    for x, y in coordinates:
        board[x][y] = "x"
    for row in board:
        print(" ".join(row))
    return board
    
def food(board, coordinates):
    while True:
        food_x = randrange (10)
        food_y = randrange (10)
        print(food_x,food_y)
        if (food_x, food_y) not in coordinates:
            board[food_x][food_y] = "}"
            return board
            

def movement(board,coordinates, direction):
    x = coordinates[-1][0]
    y = coordinates[-1][1]
    if direction == "w":
        y -=1
        coordinates.append((x,y))
        print(create_board(coordinates))
    elif direction == "e":
        y += 1
        coordinates.append((x,y))
        print(create_board(coordinates))
    elif direction == "n":
        x -= 1
        coordinates.append((x,y))
        print(create_board(coordinates))
    elif direction == "s":
        x += 1
        coordinates.append((x,y))
        print(create_board(coordinates))   
    elif direction == "end":
        print ("game over")
        exit()
#    try:
 #       direction != "n" or direction != "s" or direction != "w" or direction != "e" or direction != "end"
  #  except ValueError:
   #     raise ValueError ("Choose the direction : 'n' , 's', 'w', 'e': ")
    #return coordinates

#    if (x,y) in coordinates:
 #       raise ValueError ("Snake bites itself. Game over")
  #  elif x > 10 or  y > 10 or x < 0 or  y < 0:
   #     raise ValueError ( "Wall crash. Game over")

#    if board[x][y] != "}":
 #       del coordinates[0]
  #      coordinates.insert(0, ".")
   #     return coordinates
    #else:
     #   board = food(board, coordinates)
     #   return coordinates
        
def game():       
    coordinates = [(0,0), (0,1), (0,2)]
    board = create_board(coordinates) 
    while True:
        direction = str(input("Choose thr direction: 'w' = 'west', 'e' = 'east', 's' = 'south', 'n' = 'north' \nTo leave the game type 'end'"))
        board = food(board, coordinates)
        print(board)
        coordinate = movement(board,coordinates, direction)
#        print(create_board(coordinates))
game()