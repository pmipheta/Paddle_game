import random
class Door:
    def __init__(self, game_map,player,enemies):
       
    
        while True:
            row = random.randint(0, len(game_map.map) - 1)
            col = random.randint(0, len(game_map.map[0]) - 1)

            if game_map.can_move(row, col) and  not (row == player.row and col == player.col) and not any(e.row == row and e.col == col for e in enemies):
                self.row = row
                self.col = col
                break