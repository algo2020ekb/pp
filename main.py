from pygame import*
from random import randint
from time import time as timer


# сцена
w, h = 500, 500
window = display.set_mode((w,h))
display.set_caption("Pee-Poo")
clock = time.Clock()

# переменные
lost = 0
score = 0
font.init()
font_txt = font.SysFont("Arial", 36)

# win = font_win_lose.render("YOU WIN", True, (47, 143, 0))
# lose = font_win_lose.render("YOU LOSE", True, (180, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < w - self.size_y - 5:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < w - self.size_y - 5:
            self.rect.y += self.speed
    


class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > h:
            self.rect.x = randint(0, w-80)
            self.rect.y = 0
            lost += 1


left = Player("left.png", 5, 250, 10, 50, 5)
right = Player("right.png", 485, 250, 10, 50, 5)


# игровой цикл
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
    if not finish:
        window.fill((157,236,87))

        left.update_left()
        right.update_right()

        left.reset()
        right.reset()


      
        display.update()
    clock.tick(30)