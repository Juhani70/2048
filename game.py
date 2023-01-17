
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


if __name__ == '__main__':
    print(f"Number of free cells is {len(freeCells(grid))}")
    print(grid)

