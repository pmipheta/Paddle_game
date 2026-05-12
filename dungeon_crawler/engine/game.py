from dungeon_crawler.entity.player import Player
from dungeon_crawler.ui.render import render
from dungeon_crawler.engine.map import Map
from dungeon_crawler.entity.enemy import Enemy
from dungeon_crawler.entity.Door import Door
def handle_move():
    move = input("Enter walk: ").lower()
    return move

def update_move(player,maps,move):
    new_row = player.row
    new_col = player.col


    if move == 'w':
        new_row -=1 
    elif move == 's':
        new_row +=1
    elif move == 'd':
        new_col +=1
    elif move == 'a':
        new_col -=1

    if maps.can_move(new_row,new_col):
        player.row = new_row
        player.col = new_col

def combat(player,enemy):
    player.hp -= enemy.attack
    print(f"player have hp : {player.hp}")
    return player.hp


def check_collision(player,enemies):
    for enemy in enemies:
        if player.row == enemy.row and player.col == enemy.col:
            return enemy
    return False
        
def run():
    maps = Map()
    player = Player(maps)
    
    enemy_list = []
    for i in  range(8):
        enemy = Enemy(maps,player,enemy_list)
        enemy_list.append(enemy)
    door = Door(maps, player, enemy_list)
    gaming = True
    while gaming:
        render(maps.map,player,enemy_list,door)
        move = handle_move()
        update_move(player,maps,move)

        for enemys in enemy_list:
            enemys.move(maps,enemy_list,player)
        
        if player.row == door.row and player.col == door.col:
            render(maps.map, player, enemy_list, door)
            print("\n🎉 You Escaped! YOU WIN! 🎉")
            gaming = False
            break


        hit_enemy = check_collision(player,enemy_list)

        if hit_enemy :
            print(f"player: {player.row},{player.col}")

            for index, e in enumerate(enemy_list):
                print(f"Enemy {index + 1}: {e.row},{e.col}")

            print("Fight")
            combat(player,hit_enemy)

            if player.hp <=0 :
                print("Game Over")
                gaming = False    
            else:
                input("press to continue game.... : ")    

