import pygame
import enemies
import board
import towers


pygame.init()
board_cols = 4  
board_rows = 10  
tile_size = 80
size = width, height = board_cols * tile_size, board_rows * tile_size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True


game_board = board.Board(board_cols, board_rows, tile_size)


while running:
    fps = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with grass tiles
    for i in range(game_board.rows):
        for j in range(game_board.cols):
            tile_obj = game_board.array[i][j]  # Get the tile
            screen.blit(tile_obj.image, (j * game_board.tile_size, i * game_board.tile_size))

    currency = 500
    pygame.display.flip()

pygame.quit()