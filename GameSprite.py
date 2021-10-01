from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
       #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height, win_width, win_height, window): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height
        self.window = window
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height)) # вместе 55,55 - параметры
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
