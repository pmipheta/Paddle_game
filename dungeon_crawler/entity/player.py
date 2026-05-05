import random
class Player:
    def __init__(self, game_map):
        self.hp = 5
        # self.attack = attack

        while True:
            row = random.randint(0, len(game_map.map) - 1)
            col = random.randint(0, len(game_map.map[0]) - 1)

            if game_map.can_move(row, col):
                self.row = row
                self.col = col
                break