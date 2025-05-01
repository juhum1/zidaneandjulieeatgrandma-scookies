import pygame
import sys
import enemies
import board
import towers
import menu
import random
import start_screen
import projectile
import faulthandler; faulthandler.enable()

pygame.mixer.pre_init(44100, -16, 2, 4096)
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
wave_cleared = True
enemies_spawned = 0
enemy_spawned_time = pygame.time.get_ticks()
enemy_moved_time = pygame.time.get_ticks()
tower_attack_time = pygame.time.get_ticks()
is_paused = False
paused_start_time = 0
paused_total_time = 0
remove = False

enemies_arr = [enemies.Goblin, enemies.Skeleton, enemies.Witch, enemies.Necromancer, enemies.Bat, enemies.Slime, enemies.Bandit, enemies.FireImp]


pygame.mixer.init()
pygame.mixer.music.load("assets/pvz.wav")
pygame.mixer.music.set_volume(0.5)
wave_sfx = pygame.mixer.Sound("assets/wave.mp3")
wave_sfx.set_volume(0.5)
#pygame.mixer.music.play(-1)


def handle_wave(wave_num, game_board, menu, cur_time, tile_size, enemy_spawned_time, enemy_moved_time, tower_attack_time, enemies_spawned, wave_begin_time, wave_cleared):
    enemies_to_spawn = 10 + 5 * (wave_num - 1)
    move_rate = max(400, 1000 - 100 * (wave_num - 1))
    spawn_rate = max(500, 2000 - 100 * (wave_num - 1))

    game_board.tower_attack()

    if cur_time - enemy_moved_time >= move_rate:
        wave_cleared = menu.update_health(game_board.move_enemies(game_board))
        enemy_moved_time = cur_time
    
    if cur_time - enemy_spawned_time >= spawn_rate:
        if enemies_spawned < enemies_to_spawn:
            if wave_num < 4:
                game_board.add_enemy(
                    enemies_arr[random.randint(0, 3)](),
                    0,
                    random.randint(0, game_board.cols - 1)
                )

            else:
                game_board.add_enemy(
                    enemies_arr[random.randint(0, len(enemies_arr) - 1)](),
                    0,
                    random.randint(0, game_board.cols - 1)
                )
            enemy_spawned_time = cur_time
            enemies_spawned += 1
            enemy_moved_time = cur_time

    menu.update_currency(game_board.death())

    wave_done = game_board.wave_over(enemies_to_spawn, spawn_rate, cur_time - wave_begin_time)
    return wave_done, enemy_spawned_time, enemy_moved_time, enemies_spawned, wave_cleared

while running:
    fps = clock.tick(45)
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
                pygame.mixer.music.stop()
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
            
            if menu.play_again(event.pos[0], event.pos[1]):
                game_board.clear_board()
                wave = 1
                wave_cleared = True
                enemies_spawned = 0
                enemy_spawned_time = pygame.time.get_ticks()
                enemy_moved_time = pygame.time.get_ticks()
                tower_attack_time = pygame.time.get_ticks()
                is_paused = False
                paused_start_time = 0
                paused_total_time = 0
                remove = False
                
            if menu.quit(event.pos[0], event.pos[1]):
                pygame.quit()
                sys.exit()

    if not is_paused:
        screen.fill((255, 255, 255))
        # background
        for i in range(game_board.rows):
            for j in range(game_board.cols):
                tile_obj = game_board.array[i][j]
                screen.blit(tile_obj.image, (j * tile_size, i * tile_size))
                pygame.draw.rect(screen, (0, 0, 0), (j * tile_size, i * tile_size, tile_size, tile_size), 1)

        if wave == 0:
            start_game = start_screen.draw(game_board, menu, tile_size)
            if start_game:
                    
                    wave += 1 
                    pygame.mixer.music.play(-1)
                    menu.set_wave(wave)
                    wave_begin_time = cur_time
        else:

            wave_done, enemy_spawned_time, enemy_moved_time, enemies_spawned, wave_cleared = handle_wave(
                wave, game_board, menu, cur_time, tile_size, enemy_spawned_time, 
                enemy_moved_time, tower_attack_time, enemies_spawned, wave_begin_time, wave_cleared
            )
            if wave_done:
                wave_sfx.play()

                wave += 1
                enemies_spawned = 0
                wave_begin_time = pygame.time.get_ticks()
                menu.set_wave(wave)
            
            if wave_cleared == False:
                is_paused = True

            # draw projectiles
            for proj in game_board.projectiles[:]:
                proj.draw(screen)
                proj.move()
                if proj.check_collision(game_board) or not proj.alive:
                    game_board.projectiles.remove(proj)

            # draw enemies and towers
            for i in range(game_board.rows):
                for j in range(game_board.cols):
                    item = game_board.array[i][j].item
                    if isinstance(item, towers.Tower):
                        screen.blit(item.sprite_surface, (j * tile_size, i * tile_size))
                    elif isinstance(item, enemies.Enemy):
                        screen.blit(pygame.image.load(item.sprite), (j * tile_size, i * tile_size))

            menu.draw()

    if not wave_cleared:
        pygame.draw.rect(screen, (0, 0, 0), (width/2 - 150, height/2 - 75, 300, 150))
        font = pygame.font.Font(None, 36)
        screen.blit(font.render("Game Over!", True, (255, 255, 255)), (width/2 - 70, height/2 - 70))
        font = pygame.font.Font(None, 30)
        screen.blit(font.render("Do you want to play again?", True, (255, 255, 255)), (width/2 - 130, height/2 - 40))
        pygame.draw.rect(screen, (128, 128, 128), (width/2 - 110, height/2 + 30, 70, 30))
        pygame.draw.rect(screen, (128, 128, 128), (width/2 + 40, height/2 + 30, 70, 30))
        screen.blit(font.render("QUIT", True, (255, 255, 255)), (width/2 - 100, height/2 + 36))
        screen.blit(font.render("OK", True, (255, 255, 255)), (width/2 + 58, height/2 + 36))
        
        
    pygame.display.flip()

pygame.quit()
