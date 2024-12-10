import pygame

SELECTED_COLOR = (0, 255, 0) 
DARK_GREY = (50, 50, 50)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CROWN_COLOR = (255, 215, 0)  

class CheckersGame:
    def __init__(self):
        self.turn = "RED"  
        self.selected_piece = None  
        self.board = self.create_board()  
        self.must_jump = False  

    def create_board(self):
        
        board = [[None] * 8 for _ in range(8)]

        
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 != 0:
                    if row < 3:
                        board[row][col] = {"color": "RED", "king": False}  
                    elif row > 4:
                        board[row][col] = {"color": "GREEN", "king": False} 

        return board

    def switch_turn(self):
        
        if not self.must_jump:
            self.turn = "GREEN" if self.turn == "RED" else "RED"

    def is_valid_move(self, start_pos, end_pos):
       
        start_piece = self.board[start_pos[0]][start_pos[1]]
        end_piece = self.board[end_pos[0]][end_pos[1]]

        
        if start_piece is None:
            return False

        row_diff = abs(start_pos[0] - end_pos[0])
        col_diff = abs(start_pos[1] - end_pos[1])

        
        if row_diff == 1 and col_diff == 1 and end_piece is None:
            return True

        
        if row_diff == 2 and col_diff == 2:
            middle_row = (start_pos[0] + end_pos[0]) // 2
            middle_col = (start_pos[1] + end_pos[1]) // 2
            middle_piece = self.board[middle_row][middle_col]

            
            if middle_piece is not None and middle_piece["color"] != start_piece["color"]:
                return True

        return False

    def select_piece(self, pos):
        row, col = pos
        piece = self.board[row][col]

        
        if piece is not None and piece["color"] == self.turn:
            self.selected_piece = pos
        else:
            self.selected_piece = None  

    def promote_to_king(self, pos):
        piece = self.board[pos[0]][pos[1]]
        if piece["color"] == "RED" and pos[0] == 7:  
            piece["king"] = True
        elif piece["color"] == "GREEN" and pos[0] == 0:  
            piece["king"] = True

    def check_for_chain_jump(self, end_pos):
        
        piece = self.board[end_pos[0]][end_pos[1]]
        directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]  

        for dr, dc in directions:
            new_row = end_pos[0] + dr
            new_col = end_pos[1] + dc

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.is_valid_move(end_pos, (new_row, new_col)):
                    return True

        return False

    def move_piece(self, start_pos, end_pos):
       
        if self.is_valid_move(start_pos, end_pos):
            piece = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = None  
            self.board[end_pos[0]][end_pos[1]] = piece  

            
            if abs(start_pos[0] - end_pos[0]) == 2:
                middle_row = (start_pos[0] + end_pos[0]) // 2
                middle_col = (start_pos[1] + end_pos[1]) // 2
                self.board[middle_row][middle_col] = None  

                
                if self.check_for_chain_jump(end_pos):
                    self.selected_piece = end_pos
                    self.must_jump = True  
                else:
                    self.must_jump = False
                    self.switch_turn()  
            else:
                self.must_jump = False
                self.switch_turn()  

            self.promote_to_king(end_pos)  

    def draw_pieces(self, screen, square_size):
        
        radius = square_size // 2 - 10
        shadow_offset = 5

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None:
                    center = (col * square_size + square_size // 2, row * square_size + square_size // 2)

                    
                    pygame.draw.circle(screen, DARK_GREY, (center[0] + shadow_offset, center[1] + shadow_offset), radius + 2)

                    
                    color = RED if piece["color"] == "RED" else GREEN
                    pygame.draw.circle(screen, BLACK, center, radius + 2)
                    pygame.draw.circle(screen, color, center, radius)

                    
                    if piece["king"]:
                        pygame.draw.circle(screen, CROWN_COLOR, center, radius // 2)

                    
                    if self.selected_piece == (row, col):
                        pygame.draw.circle(screen, SELECTED_COLOR, center, radius + 4, 4)
