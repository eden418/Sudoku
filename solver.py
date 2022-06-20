def print_board(bo):
    for i in range(len(bo[0])):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')
            print(f" {bo[i][j]} ", end='')
        print()

def find_empty(bo):
    for i, row in enumerate(bo):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
    return None

def validate_num(bo, row, col, num):
    if num in bo[row]:
        return False
    if num in [bo[x][col] for x in range(len(bo[0]))]:
        return False
    box_x = row // 3 * 3
    box_y = col // 3 * 3
    for i in range(box_x, box_x+3):
        for j in range(box_y, box_y+3):
            if bo[i][j] == num:
                return False
    return True

def solve(bo):
    if not find_empty(bo):
        return True
    else:
        row, col = find_empty(bo)
        for i in range(1, 10):
            if validate_num(bo, row, col, i):
                bo[row][col] = i
                if solve(bo):
                    return True
                bo[row][col] = 0
        return False
