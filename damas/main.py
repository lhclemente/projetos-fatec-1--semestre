import pygame
import sys
from rules import CheckersGame 

pygame.init()

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
game = CheckersGame()
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Damas")


font = pygame.font.SysFont(None, 36)

def draw_board():
  
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def display_turn_info():
    
    text = font.render(f"Vez de: {game.turn}", True , BLUE)
    screen.blit(text, (10, 10))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

            if game.selected_piece:
                start_pos = game.selected_piece
                game.move_piece(start_pos, (row, col))
            game.select_piece((row, col))

    
    screen.fill(BLACK)

    
    draw_board()
    game.draw_pieces(screen, SQUARE_SIZE)

    
    display_turn_info()

    
    pygame.display.flip()
