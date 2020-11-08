import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1900, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders   Tutorial")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player1 player1
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        #pixel colision prevent

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 15

    def __init__(self, x, y, health1=100, health2=100, health3=100):
        self.x = x
        self.y = y
        self.health1 = health1
        self.health2 = health2
        self.health3 = health3
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown1()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health1 -= 10
                obj.health2 -= 10
                obj.health3 -= 10
                self.lasers.remove(laser)

    def cooldown1(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def cooldown2(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 3

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player1(Ship):
    def __init__(self, x, y, health1=100):
        super().__init__(x, y, health1)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health1 = health1



    def move_lasers(self, vel, objs):
        self.cooldown2()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health1/self.max_health1), 10))



class Player2(Ship):
    def __init__(self, x, y, health2=100):
        super().__init__(x, y, health2)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health2 = health2

    def move_lasers(self, vel, objs):
        self.cooldown2()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health2/self.max_health2), 10))

class Player3(Ship):
    def __init__(self, x, y, health3=100):
        super().__init__(x, y, health3)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health3 = health3

    def move_lasers(self, vel, objs):
        self.cooldown2()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health3/self.max_health3), 10))



class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    points = 0
    run = True
    FPS = 60
    level = 0
    defense = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1
    #every time press key, move 5 pixels

    player_vel = 10
    laser_vel_player = 20
    laser_vel_enemy = 5

    player1 = Player1(300, 730)
    player2 = Player2(300, 530)
    player3 = Player3(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Defense: {defense}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player1.draw(WIN)
        player2.draw(WIN)
        player3.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

        player1.draw(WIN)
        player2.draw(WIN)
        player3.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        #to pozwala trzymać zegar niezależnie od szybkości kompa
        redraw_window()

        if defense <= 0 or player1.health1 <= 0:
            lost = True
            lost_count += 1
        if defense <= 0 or player2.health2 <= 0:
            lost = True
            lost_count += 1
        if defense <= 0 or player3.health3 <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x - player_vel > 0: # left
            # block move out of the screen
            player1.x -= player_vel
        if keys[pygame.K_d] and player1.x + player_vel + player1.get_width() < WIDTH: # right
            player1.x += player_vel
            #get_width oblicza szerokość obiektu na prawo w celu nie chowania się poza ekran
        if keys[pygame.K_w] and player1.y - player_vel > 0: # up
            player1.y -= player_vel
        if keys[pygame.K_s] and player1.y + player_vel + player1.get_height() + 15 < HEIGHT: # down
            # +15 bo lewy górny pixel( żeby obiekt się nie chował
            player1.y += player_vel
        if keys[pygame.K_t]:
            player1.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP4] and player2.x - player_vel > 0:  # left
            # block move out of the screen
            player2.x -= player_vel
        if keys[pygame.K_KP6] and player2.x + player_vel + player2.get_width() < WIDTH:  # right
            player2.x += player_vel
            # get_width oblicza szerokość obiektu na prawo w celu nie chowania się poza ekran
        if keys[pygame.K_KP8] and player2.y - player_vel > 0:  # up
            player2.y -= player_vel
        if keys[pygame.K_KP5] and player2.y + player_vel + player2.get_height() + 15 < HEIGHT:  # down
            # +15 bo lewy górny pixel( żeby obiekt się nie chował
            player2.y += player_vel
        if keys[pygame.K_p]:
            player2.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_j] and player3.x - player_vel > 0:  # left
            # block move out of the screen
            player3.x -= player_vel
        if keys[pygame.K_l] and player3.x + player_vel + player3.get_width() < WIDTH:  # right
            player3.x += player_vel
            # get_width oblicza szerokość obiektu na prawo w celu nie chowania się poza ekran
        if keys[pygame.K_i] and player3.y - player_vel > 0:  # up
            player3.y -= player_vel
        if keys[pygame.K_k] and player3.y + player_vel + player3.get_height() + 15 < HEIGHT:  # down
            # +15 bo lewy górny pixel( żeby obiekt się nie chował
            player3.y += player_vel
        if keys[pygame.K_n]:
            player3.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel_enemy, player1)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player1):
                player1.health1 -= 5
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                defense -= 1
                enemies.remove(enemy)

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel_enemy, player2)


            if collide(enemy, player2):
                player2.health2 -= 1
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                defense -= 1
                enemies.remove(enemy)

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel_enemy, player3)


            if collide(enemy, player3):
                player3.health3 -= 5
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                defense -= 1
                enemies.remove(enemy)

        player1.move_lasers(-laser_vel_player, enemies)
        player2.move_lasers(-laser_vel_player, enemies)
        player3.move_lasers(-laser_vel_player, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()


# rekord : 19