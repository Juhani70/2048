
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


if __name__ == '__main__':
    print(f"Number of free cells is {len(freeCells(grid))}")
    print()
    printGrid(grid)

