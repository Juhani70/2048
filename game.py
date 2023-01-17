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


if __name__ == '__main__':
    grid = initGrid(4)

    print(f"Number of free cells is {len(freeCells(grid))}")
    print()
    printGrid(grid)

    for i in range(5):
        addNumber(grid, freeCells(grid))

    printGrid(grid)

