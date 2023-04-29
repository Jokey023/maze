from pygame import *
window = display.set_mode((1200, 800))
display.set_caption("Догонялки")
game = True
background = transform.scale(image.load("background.jpg"), (1200, 800))
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("jungles.ogg")
touch = mixer.Sound('kick.ogg')
Gold = mixer.Sound('money.ogg')
mixer.music.play()
font.init()
font = font.Font(None, 200)
victory = font.render('YOU WIN!', True, (0,0,0))
lose = font.render('YOU LOSE!', True, (0,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, speed, Image, x, y):
        super().__init__()
        self.image = transform.scale(image.load(Image), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def start(self):
        self.rect.x = 0
        self.rect.y = 0
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Main(GameSprite):
    def __init__(self, speed, Image, x, y):
        super().__init__(speed, Image, x, y)
    def move(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 1095:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 695:
            self.rect.y += self.speed
    def stop(self):
        self.speed = 0
class Enemy(GameSprite):
    def __init__(self, speed, Image, x, y, direction):
        super().__init__(speed, Image, x, y)
        self.direction = ''
    def move(self):
        if self.rect.x <= 750:
            self.direction = "right"
        if self.rect.x >= 1095:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))
    def stop(self):
        self.speed = 0
class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
Hero = Main(5, "hero.png", 0, 0)
enemy = Enemy(4, "cyborg.png", 900, 400, 'none')
wall1 = Wall(0, 255, 0, 100, 200, 600, 30)
wall2 = Wall(0, 255, 0, 100, 0, 30, 600)
wall3 = Wall(0, 255, 0, 250, 350, 300, 30)
wall4 = Wall(0, 255, 0, 240, 350, 30, 500)
wall5 = Wall(0, 255, 0, 700, 0, 30, 500)
gold = GameSprite(0, "treasure.png", 950, 100)
while game:
    clock.tick(FPS)
    window.blit(background, (0,0))
    wall1.draw()
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    keys_pressed = key.get_pressed()
    if sprite.collide_rect(Hero, enemy) or sprite.collide_rect(Hero, wall1) or sprite.collide_rect(Hero, wall2) or sprite.collide_rect(Hero, wall3) or sprite.collide_rect(Hero, wall4) or sprite.collide_rect(Hero, wall5):
        touch.play()
        window.blit(lose, (250,300))
        fail = False
        print('u bad')
    if sprite.collide_rect(Hero, gold):
        Gold.play()
        window.blit(victory, (250,300))
        Hero.stop()
        enemy.stop()
    Hero.move()
    enemy.move()
    gold.show()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()