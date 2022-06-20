"""
This is a sudoku game using pygame.
It is solved using a backtracking algorithm.
Creator: Eden Candelas
"""
import pygame

from box_class import Cube
import solver

pygame.font.init()

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

BOX_SIDE = 60
WIDTH, HEIGHT = BOX_SIDE * 9, BOX_SIDE * 9 + 100
print(HEIGHT)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eden's Sudoku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

board = []

for y in range(0, BOX_SIDE*9, BOX_SIDE):
    row = []
    for x in range(0, BOX_SIDE*9, BOX_SIDE):
        row.append(Cube(x, y, BOX_SIDE, BOX_SIDE))
    board.append(row)

solver.print_board(board)

def draw_window():
    WIN.fill(WHITE)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            col.draw(WIN)
            if j % 3 == 0 and j != 0:
                pygame.draw.rect(WIN, BLACK, (col.x - 2, col.y - 2, 2, BOX_SIDE + 2), 0)
            if i % 3 == 0 and i != 0:
                pygame.draw.rect(WIN, BLACK, (col.x - 2, col.y - 2, BOX_SIDE + 2, 2), 0)
            elif i == len(board) - 1:
                pygame.draw.rect(WIN, BLACK, (col.x, col.y + BOX_SIDE - 2, BOX_SIDE + 4, 2), 0)
    pygame.display.update()

def handle_motion(pos):
    for i, row in enumerate(board):
        for j, col in enumerate(board):
            if board[i][j].is_over(pos):
                board[i][j].color = (225, 225, 225)
            else:
                board[i][j].color = WHITE

def get_number():
    pass

def main():
    run = True
    while run:
        draw_window()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEMOTION:
                handle_motion(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                get_number()


if __name__ == "__main__":
    main()

