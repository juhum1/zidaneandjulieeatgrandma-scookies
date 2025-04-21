import pygame
import enemies
import board
import towers
import menu
import random

pygame.init()
board_cols = 4  
board_rows = 10  
tile_size = 80
width, height = board_cols * tile_size * 2, board_rows * tile_size
width += 100
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
running = True


game_board = board.Board(board_cols, board_rows, tile_size)
menu = menu.Menu(screen, board_cols * tile_size, width, height, 500)

wave = 0
enemies_spawned = 0
enemy_spawned_time = pygame.time.get_ticks()
enemy_moved_time = pygame.time.get_ticks()
is_paused = False
paused_start_time = 0
paused_total_time = 0
remove = False

while running:
    fps = clock.tick(120)
    cur_time = pygame.time.get_ticks() - paused_total_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if menu.buy_tower(event.pos[0], event.pos[1]):  
            #     # change coloring of the selected tower on menu, change to green
            #     print("Tower selected")
                

            # else:
            #     if menu.selected_tower:
            #         success = menu.place_tower(game_board, event.pos[0], event.pos[1])
            #         if success:
            #             print("Tower placed")
            menu.buy_tower(event.pos[0], event.pos[1])
            menu.place_tower(game_board, event.pos[0], event.pos[1])
            if menu.click_menu_bar(event.pos[0], event.pos[1]):
                is_paused = not is_paused
                if is_paused:
                    paused_start_time = pygame.time.get_ticks()
                else:
                    paused_time = pygame.time.get_ticks() - paused_start_time
                    paused_total_time += paused_time
                    enemy_spawned_time -= paused_time
                    enemy_moved_time -= paused_time
            # need to fix so works for all waves
            if menu.click_restart_button(game_board, event.pos[0], event.pos[1]) and is_paused:
                cur_time = enemy_spawned_time = enemy_moved_time = pygame.time.get_ticks()
                paused_start_time = paused_total_time = 0
                enemies_spawned = 0
                is_paused = False
                menu.currency = 500
            
            if menu.click_remove(event.pos[0], event.pos[1]):
                remove = not remove
            elif remove:
                menu.update_currency(menu.remove_tower(game_board, event.pos[0], event.pos[1]))
                remove = False
            else:
                pass

                
    if not is_paused:
        if wave == 0:
            #separate screen with welcome to tower defense game and introduction
            wave += 1 
            wave_1_begin_time = cur_time
     

        if wave == 1:
            for i in range(game_board.rows):
                for j in range(game_board.cols):
                    tile_obj = game_board.array[i][j]  
                    screen.blit(tile_obj.image, (j * tile_size, i * tile_size))
                    pygame.draw.rect(screen, (0, 0, 0), (j * game_board.tile_size, i * game_board.tile_size, game_board.tile_size, game_board.tile_size), 1)
                    if isinstance(tile_obj.item, towers.Tower):   # drawing towers 
                        screen.blit(tile_obj.item.sprite_surface, (j * tile_size, i * tile_size))
                    if isinstance(tile_obj.item, enemies.Enemy):    #drawing enemies
                        screen.blit(pygame.image.load(tile_obj.item.sprite), (j * tile_size, i * tile_size))
            
            enemies_to_spawn = 10
            spawn_rate = 2000
            move_rate = 1500

            if spawn_rate < move_rate:  # enemies may collide at spawn
                running = False
            
            if cur_time - enemy_moved_time >= move_rate:
                wave_cleared = menu.update_health(game_board.move_enemies())
                enemy_moved_time = cur_time

            if cur_time - enemy_spawned_time >= spawn_rate:
                if (enemies_spawned < enemies_to_spawn):
                    game_board.add_enemy(enemies.Goblin(), random.randint(0, 3))
                    enemy_spawned_time = cur_time        
                    enemies_spawned += 1
                    enemy_moved_time = cur_time
            
            game_board.tower_attack()
            menu.update_currency(game_board.death())
            if game_board.wave_over(enemies_to_spawn, spawn_rate, cur_time - wave_1_begin_time):
                wave += 1
                #game_board.clear_board()


        if wave == 2:
            for i in range(game_board.rows):
                for j in range(game_board.cols):
                    tile_obj = game_board.array[i][j]  
                    screen.blit(tile_obj.image, (j * tile_size, i * tile_size))
                    pygame.draw.rect(screen, (0, 0, 0), (j * game_board.tile_size, i * game_board.tile_size, game_board.tile_size, game_board.tile_size), 1)
                    if isinstance(tile_obj.item, towers.Tower):   # drawing towers 
                        screen.blit(tile_obj.item.sprite_surface, (j * tile_size, i * tile_size))
                    if isinstance(tile_obj.item, enemies.Enemy):    #drawing enemies
                        screen.blit(pygame.image.load(tile_obj.item.sprite), (j * tile_size, i * tile_size))


        menu.draw()
    
       
        
            
    pygame.display.flip()


pygame.quit()
