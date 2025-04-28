import pygame
import enemies
import board
import towers
import menu
import random
import start_screen

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

start_screen = start_screen.Start_Screen(screen, width, height)
game_board = board.Board(board_cols, board_rows, tile_size)
menu = menu.Menu(screen, board_cols * tile_size, width, height, 500)

start_game = False
wave = 0
enemies_spawned = 0
enemy_spawned_time = pygame.time.get_ticks()
enemy_moved_time = pygame.time.get_ticks()
is_paused = False
paused_start_time = 0
paused_total_time = 0
remove = False

enemies_arr = [enemies.Witch, enemies.Witch, enemies.Witch]

def handle_wave(wave_num, game_board, screen, menu, cur_time, tile_size, enemy_spawned_time, enemy_moved_time, enemies_spawned, wave_begin_time):
    enemies_to_spawn = 10 + 5 * (wave_num - 1)
    spawn_rate = max(500, 2000 - 100 * (wave_num - 1))  
    move_rate = max(400, 1500 - 100 * (wave_num - 1))   

    for i in range(game_board.rows):
        for j in range(game_board.cols):
            tile_obj = game_board.array[i][j]
            screen.blit(tile_obj.image, (j * tile_size, i * tile_size))
            pygame.draw.rect(screen, (0, 0, 0), (j * tile_size, i * tile_size, tile_size, tile_size), 1)
            if isinstance(tile_obj.item, towers.Tower):
                screen.blit(tile_obj.item.sprite_surface, (j * tile_size, i * tile_size))
            elif isinstance(tile_obj.item, enemies.Enemy):
                screen.blit(pygame.image.load(tile_obj.item.sprite), (j * tile_size, i * tile_size))

    if cur_time - enemy_moved_time >= move_rate:
        wave_cleared = menu.update_health(game_board.move_enemies(game_board))
        enemy_moved_time = cur_time

    if cur_time - enemy_spawned_time >= spawn_rate:
        if enemies_spawned < enemies_to_spawn:
            #game_board.add_enemy(enemies.Goblin(), 0, random.randint(0, game_board.cols - 1))
            if (wave_num // 2 + 1 <= len(enemies_arr) - 1):
              game_board.add_enemy(enemies_arr[random.randint(0, wave_num // 2 + 1)](), 0, random.randint(0, game_board.cols - 1))
            else:
               game_board.add_enemy(enemies_arr[random.randint(0, len(enemies_arr) - 1)](), 0, random.randint(0, game_board.cols - 1))
            enemy_spawned_time = cur_time
            enemies_spawned += 1
            enemy_moved_time = cur_time

    game_board.tower_attack()
    menu.update_currency(game_board.death())

    wave_done = game_board.wave_over(enemies_to_spawn, spawn_rate, cur_time - wave_begin_time)
    return wave_done, enemy_spawned_time, enemy_moved_time, enemies_spawned

while running:
    fps = clock.tick(120)
    cur_time = pygame.time.get_ticks() - paused_total_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_screen.click_start(event.pos[0], event.pos[1]) 

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

            if menu.click_restart_button(game_board, event.pos[0], event.pos[1]) and is_paused:
                cur_time = enemy_spawned_time = enemy_moved_time = pygame.time.get_ticks()
                paused_start_time = paused_total_time = 0
                enemies_spawned = 0
                is_paused = False
                menu.currency = 500
                menu.health = 500
                wave = 0
            
            if menu.click_remove(event.pos[0], event.pos[1]):
                remove = not remove
            elif remove:
                menu.remove_tower(game_board, event.pos[0], event.pos[1])
                remove = False
            else:
                pass

                
    if not is_paused:
        if wave == 0:
            start_game = start_screen.draw(game_board, menu, tile_size)
            if start_game:
                    wave += 1 
                    menu.set_wave(wave)
                    wave_begin_time = cur_time
        else:
            wave_done, enemy_spawned_time, enemy_moved_time, enemies_spawned = handle_wave(wave, game_board, screen, menu, cur_time, tile_size, enemy_spawned_time, enemy_moved_time, enemies_spawned, wave_begin_time)
            if wave_done:
                wave += 1
                enemies_spawned = 0
                wave_begin_time = pygame.time.get_ticks()
                menu.set_wave(wave)


            menu.draw()
            for proj in game_board.projectiles[:]:  
                proj.move()
                proj.draw(screen)
                if proj.check_collision() or not proj.alive:
                    game_board.projectiles.remove(proj)
                
    pygame.display.flip()


pygame.quit()
