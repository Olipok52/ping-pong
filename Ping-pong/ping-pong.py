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

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    player.update_r()
    player.reset()
    player2.update_l()
    player2.reset()

    clock.tick(FPS)
    display.update()