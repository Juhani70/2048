import random

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def freeCells(grid: list) -> list:
    '''Function return list of empty cells. Empty cells in gris are 0.'''

    freeCells = []

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                freeCells.append({'x': i, 'y': j})
    
    return freeCells


def printGrid(grid: list) -> None:
    '''Print grid in the screen'''

    for i in range(4):
        line = ''
        for j in range(4):
            line += f"\t{grid[i][j]}"
        print(line)
    print()


def randomNumber() -> int:
    '''Draw the number either 2 or 4. The probability of number 2 is 80%.'''

    if random.random() < 0.8:
        return 2
    else:
        return 4


def addNumber(grid: list, freeCells: list) -> None:
    '''Add number to the free cell on the grid'''
    
    rndCell = random.choices(freeCells)
    grid[rndCell[0].get('x')][rndCell[0].get('y')] = randomNumber()


if __name__ == '__main__':
    print(f"Number of free cells is {len(freeCells(grid))}")
    print()
    printGrid(grid)

    for i in range(5):
        addNumber(grid, freeCells(grid))

    printGrid(grid)

