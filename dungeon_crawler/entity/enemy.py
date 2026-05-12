import random
class Enemy:
    def __init__(self,game_map,player,enemies):
        self.hp = 1
        self.attack = 1
        self.vision = 3
        while True:
            row = random.randint(0,len(game_map.map)-1)
            col = random.randint(0,len(game_map.map[0])-1)

            if game_map.can_move(row, col) and not (row == player.row and col == player.col) and not any(e.row == row and e.col == col for e in enemies) :
                self.row = row
                self.col = col
                break
    
    def move(self,game_map,enemies,player):
        distance = ((abs(player.row - self.row))**2 + (abs(player.col-self.col))**2)**0.5

        if distance <= self.vision:
            if self.row < player.row:
                move_row , move_col = 1, 0
            elif self.row > player.row :
                move_row , move_col = -1,0
            elif self.col < player.col:
                move_row , move_col = 0 ,1 
            elif self.col > player.col:
                move_row , move_col = 0 ,-1
            else:
                move_row,move_col = 0 ,0
        else:
            direction = [(-1,0),(1,0),(0,1),(0,-1)]

            move_row , move_col = random.choice(direction)
        new_row = self.row + move_row
        new_col = self.col +move_col

        if not game_map.can_move(new_row,new_col):
            return 
            
        for e in enemies:
            if e != self and e.row == new_row and e.col == new_col:
                return 
                
        self.row = new_row
        self.col = new_col