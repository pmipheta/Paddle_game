def render(game_map,player,enemies,door):
    
    print("\n" * 5)  

    for r in range(len(game_map)):
        row_str = ""
        for c in range(len(game_map[0])):
            if r == player.row and c == player.col:
                row_str += "@"
            elif any(e.row == r and e.col == c for e in enemies):
                row_str += "E"
            elif r == door.row and c == door.col:
                row_str += "X"
            else:
                row_str += game_map[r][c]
        print(row_str)