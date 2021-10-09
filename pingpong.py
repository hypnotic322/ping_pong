from pygame import *
from GameSprite import GameSprite
from Player import Player

def pause(window):
    run = True
    font1 = font.Font(None, 35)
    while run:
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_p:
                    run = False

        window.blit(font1.render('PAUSE!', True, (180, 0, 0)), (300, 200))
        display.update()
def game():
    #Игровая сцена:
    back = (200, 255, 255) # цвет фона (background)
    win_width = 600
    win_height = 500
    window = display.set_mode((win_width, win_height))
    

    #флаги отвечающие за состояние игры
    run = True
    finish = False
    clock = time.Clock()
    FPS = 60

    racket1 = Player('racket.png', 30, 200, 4, 50, 150, win_width, win_height, window) # при созданни спрайта добавляется еще два параметра
    racket2 = Player('racket.png', 520, 200, 4, 50, 150, win_width, win_height, window)
    ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50, win_width, win_height, window)
    speed_x = 3
    speed_y = 3
    font.init()
    font1 = font.Font(None, 35)
    lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
    lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_p:
                    pause(window)
        if finish != True:
            window.fill(back)
            racket1.reset()
            racket2.reset()
            ball.reset()
            if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1

            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed_y *= -1
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            racket2.update_r()
            racket1.update_l()
            # если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (200, 200))
                
            # если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
            if ball.rect.x > win_width:
                finish = True
                window.blit(lose2, (200, 200))
                

        display.update()
        clock.tick(FPS)
if __name__ == '__main__':
    game()



