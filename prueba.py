import random
#directions
N, S, E, W = 1, 2, 4, 8

#direction with values
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}

#opposite direction
OPPOSITE = {E: W, W: E, N: S, S: N}


def generate_maze(width, height):
    #create matrix filled with 0s
    grid = []
    for _ in range(height):
        row = [0] * width
        grid.append(row)
    
    #depth first algortithm starting at top left corner
    stack = [(0, 0)]

    while stack:
        cx, cy = stack[-1]
        directions = [N, S, E, W]
        random.shuffle(directions)
        moved = False

        for direction in directions:
            nx, ny = cx + DX[direction], cy + DY[direction]

            if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == 0:
                grid[cy][cx] |= direction
                grid[ny][nx] |= OPPOSITE[direction]
                stack.append((nx, ny))
                moved = True
                break
        
        if not moved:
            stack.pop()

    return grid

def visual_maze(grid, width, height):
    maze = []
    for y in range(height):
        row = ["|"]

        for x in range(width):
            cell = grid[y][x]
            
            # Check if there's an open passage to the South (S)
            if cell & S != 0:
                row.append(" ")
            else:
                row.append("_")

            # Check if there's an open passage to the East (E)
            if cell & E != 0:
                # Check if there's a connection to the South (S) in the next cell
                if x + 1 < width and (grid[y][x] | grid[y][x + 1]) & S != 0:
                    row.append(" ")
                else:
                    row.append("_")
            else:
                row.append("|")

        maze.append(row)
    maze[height-1][width*2] = avatar
    maze[0][0] = 'o'
    return(maze)

def display_maze(maze):
    print(" " + "_" * (width * 2 - 1))
    for i in range(len(maze)):
        maze[i] = ''.join(maze[i])
    print('\n'.join(maze))

def play_game(maze, curr_position, prev_char):
    move = input('Next move: ')
    maze[curr_position[0]][curr_position[1]] = prev_char
    if move == 'w':
        if maze[curr_position[0]-1][curr_position[1]] != "_" and maze[curr_position[0]-1][curr_position[1]] != "|":
            curr_position[0] -=1
        else:
            print("Invalid move")
    elif move == 'a':
        if maze[curr_position[0]][curr_position[1]-1] != "|":
            curr_position[1] -=1
        else:
            print("Invalid move")
    elif move == 's':
        if curr_position[0] != height-1 and curr_position != width*2 :
            if prev_char != "_":
                curr_position[0] +=1
            else:
                print("Invalid move")
    elif move == 'd':
        if curr_position[0] != height-1 and curr_position != width*2 :
            if maze[curr_position[0]][curr_position[1]+1] != "|":
                curr_position[1] +=1
            else:
                print("Invalid move")
    prev_char = maze[curr_position[0]][curr_position[1]]
    maze[curr_position[0]][curr_position[1]] = avatar
    print_maze = maze[:]
    display_maze(print_maze)
    return maze, curr_position, prev_char

print("JUEGO DEL LABERINTO")
print("""En este juego tu podrias elegir tu avatar y el tamaño del laberinto.
        
La meta es llegar a la salida esquivando las barreras, tu avatar empezara jugando 
en la esquina inferior derecha y la salida se encuentra en la esquina superior izquierda.
      
Para desplazarate puedes usar los comandos a, w, d, s. 
      
Para desplazarte a la derecha "a", para desplazarte a la izquierda "d", para desplazarte hacia abajo "s" y para arriba "w".  
          
¡Mucho exito!""")
avatar = input('Elija un su avatar (un unico caracter del teclado): ')
width = height = int(input('Ingrese dimensiones de su laberinto: '))  # Width and Height of the maze
grid = generate_maze(width, height)
maze = visual_maze(grid,width,height)
print_maze = maze[:]
display_maze(print_maze)
curr_position = [height-1, width*2]
prev_char = "|"

while maze[0][0]== 'o': 
    maze, curr_positionm, prev_char = play_game(maze, curr_position, prev_char)  

print("Lo has logrado!!")   