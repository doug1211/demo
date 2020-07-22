import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("No_Good_Right.wav")

display_width = int(800)
display_height = int(600)

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

hero_width = 69
hero_height = 69

enemy_width = 73
enemy_height = 73

pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Running block")
clock = pygame.time.Clock()

heroImg = pygame.image.load("hero.png")
# hero px 72x72 from uihere.com/free-cliparts/spacecraft-clip-art-spaceship-png-file-1095751

pygame.display.set_icon(heroImg)

enemyImg = pygame.image.load("badguy.png")
# badGuy px 100x100 pngfuel.com/free-png/cuzxn


def enemy_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def quit_game():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objetcs(msg, small_text)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 60)
        TextSurf, TextRect = text_objetcs("Space Racer", largeText)
        TextRect.center = (display_width / 2), (display_height / 2)
        gameDisplay.blit(TextSurf, TextRect)

        button("Shoot!", 200, 350, 100, 50, green, bright_green, game_loop)
        button("Quit", 450, 350, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(5)

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 60)
        TextSurf, TextRect = text_objetcs("Pause", largeText)
        TextRect.center = (display_width / 2), (display_height / 2)
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 200, 350, 100, 50, green, bright_green, unpause)
        button("Quit", 450, 350, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(5)

def hero(x,y):
    gameDisplay.blit(heroImg, [x, y])

def enemy(e_x, e_y):
    gameDisplay.blit(enemyImg, [e_x, e_y])

def text_objetcs(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 60)
    TextSurf, TextRect = text_objetcs(text, largeText)
    TextRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(1)

    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 60)
        TextSurf, TextRect = text_objetcs("You Crashed", largeText)
        TextRect.center = (display_width / 2), (display_height / 2)
        gameDisplay.blit(TextSurf, TextRect)

        button("Play again", 200, 350, 120, 50, green, bright_green, game_loop)
        button("Quit", 450, 350, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(5)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)

    x = int((display_width / 2.2))
    y = int((display_height - 2 * 40))

    #  Vel sirve para el metodo 2 de movimiento de Hero:
    #  vel = 50
    x_change = 0
    y_change = 0

    e_startx = random.randrange(0,display_width)
    e_starty = -60
    enemy_speed = 3

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Metodo 2 para moverse presionando las teclas repetidas veces y con limites en la pantalla
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_LEFT] and x > vel:
            #     x -= vel
            # if keys[pygame.K_RIGHT] and x < display_width - hero_width - vel:
            #     x += vel
            # if keys[pygame.K_UP] and y > vel:
            #     y -= vel
            # if keys[pygame.K_DOWN]and y < display_height - hero_height - vel:
            #     y += vel

# Metodo 1 para moverse continiamente solo presionando una vez la tecla - limite de la pantalla en BOUNDERIES CODE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill(white)

        enemy(e_startx, e_starty)

        e_starty += enemy_speed

        hero(x, y)
        enemy_dodged(dodged)

        if e_starty > display_height:
            e_starty = 0 - (enemy_width - 3)
            e_startx = (random.randrange(0, display_width + 3) - enemy_width)
            dodged += 1

            if dodged < 10:
                enemy_speed = 5
            elif dodged < 20:
                enemy_speed = 7
            elif dodged < 30:
                enemy_speed = 9
            elif dodged < 50:
                enemy_speed = 15
        # TODO agregar el metodo de incrementar mas objetos para subir de nivel

# BOUNDERIES
        if x > (display_width-hero_width) or x < 0 or y > (display_height-(hero_height/50)) or y < (0 - (hero_height*2)):
            crash()

        if (e_startx >= x and e_startx < (x + hero_width)) or (x >= e_startx and x < (e_startx + enemy_width)):
            if (e_starty >= y and e_starty < (y + hero_height)) or (y >= e_starty and y < (e_starty + enemy_height)):
                crash()

        pygame.display.update()
        clock.tick(80)

game_intro()
game_loop()
pygame.quit()
quit()