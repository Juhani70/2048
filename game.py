import random

def initGrid(size: int) -> list:
    '''Initiliaze grid with two number
    
    size: grid width and height'''
    grid = []

    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        grid.append(line)

    # Init grid with two numbers
    for i in range(2):
        addNumber(grid, freeCells(grid))
    
    return grid


def freeCells(grid: list) -> list:
    '''Function return list of empty cells. Empty cells in gris are 0.
    
    grid: grid to find and list empty cells'''

    freeCells = []

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                freeCells.append({'x': i, 'y': j})
    
    return freeCells


def printGrid(grid: list) -> None:
    '''Print grid in the screen
    
    
    grid: grid to print'''

    for i in range(4):
        line = ''
        for j in range(4):
            line += f"\t{grid[i][j]}"
        print(line)
    print()


def randomNumber() -> int:
    '''Draw the number either 2 or 4. The probability of number 2 is 80%.'''

    # if random.random() < 0.8:
    #     return 2
    # else:
    #     return 4

    return random.choices([2, 4], weights=(80, 20))[0]


def addNumber(grid: list, freeCells: list) -> None:
    '''Add number to the free cell on the grid
    
    grid: grid where to add number
    freeCells: list of grid's free cells'''
    
    rndCell = random.choices(freeCells)
    grid[rndCell[0].get('x')][rndCell[0].get('y')] = randomNumber()


def slide(grid: list, direction: int) -> None:
    '''Slide move cells to selected direction
    
    directions:
        0: up
        1: down
        2: left
        3: right'''

    pass


def compactGrid(grid: list, direction: int) -> None:
    '''Move numbers and remove zeros between them.
    
    grid: Game board\n
    directions:
        0: up
        1: down
        2: left
        3: right'''
    
    # If direction is not known return grid with doing nothing
    if direction not in [0, 1, 2, 3]:
        print("Direcion unknown!")
        return

    # Iterate through the rows or columns of the grid
    # Direction left or right iteration row by rows
    if direction in [2, 3]:
        if direction == 2: # direction left
            for  row in grid:
                i = 0

                while i < len(row) - 1:
                    #If cell is empty ...
                    if row[i] == 0:
                        # find next cell witch not ...
                        for j in range(i + 1, len(row)):
                            if row[j] != 0:
                                # and swap them
                                row[i], row[j] = row[j], row[i]
                                break
                    i += 1
        else: # direction == 3 right
            for  row in grid:
                i = len(row) - 1

                while i >= 0:
                    #If cell is empty ...
                    if row[i] == 0:
                        # find next cell witch not ...
                        for j in range(i - 1, -1, -1):
                            if row[j] != 0:
                                # and swap them
                                row[i], row[j] = row[j], row[i]
                                break
                    i -= 1
    
    else: # Direction up or down
        if direction == 0: # up
            for j in range(0,len(grid)):
                for i in range(0, len(grid)):
                    #If cell is empty ...
                    if grid[i][j] == 0:
                        # find next cell witch not ...
                        for k in range(i + 1, len(grid)):
                            if grid[k][j] != 0:
                                # and swap them
                                grid[k][j], grid[i][j] = grid[i][j], grid[k][j]
                                break
        else: # direction == 1 down
            for j in range(len(grid) - 1, -1, -1):
                for i in range(len(grid) - 1, -1, -1):
                    #If cell is empty ...
                    if grid[i][j] == 0:
                        # find next cell witch not ...
                        for k in range(i - 1, -1, -1):
                            if grid[k][j] != 0:
                                # and swap them
                                grid[k][j], grid[i][j] = grid[i][j], grid[k][j]
                                break
                    
        
def combineGrid(grid: list, direction: int) -> None:
    '''Combine numbers and add zeros to end.
    
    grid: Game board\n
    directions:
        0: up
        1: down
        2: left
        3: right'''
        

if __name__ == '__main__':
    grid = initGrid(4)

    for add in range(5):
        addNumber(grid, freeCells(grid))

    printGrid(grid)

    compactGrid(grid, 1)

    printGrid(grid)
