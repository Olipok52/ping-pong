from pygame import *

window = display.set_mode((700,600))
display.set_caption("Ping-pong")
background = transform.scale(image.load("background.jpg"), ((700,600)))

clock = time.Clock()
FPS = 60    

class GameSprits(sprite.Sprite):
    def __init__(self, sprite, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite), ((size_x,size_y)))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprits):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 530:
            self.rect.y += self.speed
    
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 530:
            self.rect.y += self.speed

player = Player('Ракетка.png', 10, 250, 20, 100, 6)
player2 = Player('Ракетка.png', 670, 250, 20, 100, 6)
krug = GameSprits('Мяч.png',250, 200, 100, 100, 3)

font.init()
font1 = font.SysFont('Arial', 24)

player1_win = font1.render(
'',1, (255,0,0))

player2_win = font1.render(
'',1, (0,255,0))

speed_x = 3
speed_y = 3

start_x = 5
start_y = 5
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        if sprite.collide_rect(player, krug) or sprite.collide_rect(player2, krug):
            speed_x *= -1 
        krug.rect.x += speed_x
        krug.rect.y += speed_y
        
        if krug.rect.y < 5:
            speed_y *= -1
        
        if krug.rect.y > 480:
            speed_y *= -1
        
        if krug.rect.x > 650:
            player2_win = font1.render(
                    'Игрок 1 выйграл', 1 ,(255,255,255)
                )
            finish = True
        
        if krug.rect.x < -70:
            player1_win = font1.render(
                    'Игрок 2 выйграл', 1 ,(255,255,255)
                )
            finish = True
        
        window.blit(background, (0,0))
        player.update_r()
        player.reset()
        player2.update_l()
        player2.reset()
        krug.reset()
        window.blit(player2_win,(250,250))
        window.blit(player1_win,(250,250))

        clock.tick(FPS)
        display.update()
