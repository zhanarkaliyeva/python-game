#Game. The player has to put each fruit in the right house, avoiding the wolves.
import pygame

pygame.init()  # invokes pygame module

clock = pygame.time.Clock()  # invokes time module from pygame
screen = pygame.display.set_mode((700, 500))  # creates an application window at a certain resolution


key_up = False  # These default the button press variables to False (not pressed)
key_left = False
key_down = False
key_right = False

carryapple = False  # These are the variables for the picking up of the other objects by the player
carrybanana = False
carrypear = False
carrycherry=False
carrymashroom=False
carrymelon=False


background = pygame.Surface(screen.get_size())
background.fill((51, 102, 0)) # imports the game background

player = pygame.image.load('redcap.png')  # imports the player image

screen.blit(background,(0, 0))  # draw the background screen
playerPosition = pygame.Rect(0, 0, 40, 50)  # set player position (start x, start y, width, height)
screen.blit(player, playerPosition)  # draw the player marker

apple = pygame.image.load('apple.png')  # import apple image
applePosition = pygame.Rect(150, 50, 50, 60)  # set apple position
screen.blit(apple, applePosition)  # draw the apple

banana = pygame.image.load('banana.png')  # import banana
bananaPosition = pygame.Rect(60, 245, 50, 50)  # set banana position
screen.blit(banana, bananaPosition)  # draw banana

pear = pygame.image.load('pear.png')  # import pear image
pearPosition = pygame.Rect(150, 385, 50, 60)  # set pear position
screen.blit(pear, pearPosition)  # draw the pear

cherry=pygame.image.load('cherry.png')
cherryPosition=pygame.Rect(400,30,50,60)
screen.blit(cherry,cherryPosition)

mashroom=pygame.image.load('mashroom.png')
mashroomPosition=pygame.Rect(300,200,70,70)
screen.blit(mashroom,mashroomPosition)

melon=pygame.image.load('melon.png')
melonPosition=pygame.Rect(500,250,50,60)
screen.blit(melon, melonPosition)

wolf=pygame.image.load('wolf.png')
wolfPosition=pygame.Rect(500,400,10,10)
screen.blit(wolf,wolfPosition)

wolf1=pygame.image.load('wolf.png')
wolf1Position=pygame.Rect(70,150,10,10)
screen.blit(wolf1, wolf1Position)

wolf2=pygame.image.load('wolf.png')
wolf2Position=pygame.Rect(300,300,10,10)
screen.blit(wolf2, wolf2Position)

wolf3=pygame.image.load('wolf.png')
wolf3Position=pygame.Rect(450,150,10,10)
screen.blit(wolf3, wolf3Position)

wolf4=pygame.image.load('wolf.png')
wolf4Position=pygame.Rect(240,80,10,10)
screen.blit(wolf4,wolf4Position)

wolf5=pygame.image.load('wolf.png')
wolf5Position=pygame.Rect(10,440,10,10)
screen.blit(wolf5,wolf5Position)

applehouse=pygame.image.load('applehouse.png')
applehousePosition=pygame.Rect(650,0,50,50)
screen.blit(applehouse,applehousePosition)

bananahouse=pygame.image.load('bananahouse.png')
bananahousePosition=pygame.Rect(640,70,50,50)
screen.blit(bananahouse,bananahousePosition)

cherryhouse=pygame.image.load('cherryhouse.png')
cherryhousePosition=pygame.Rect(660,150,70,70)
screen.blit(cherryhouse,cherryhousePosition)

mashroomhouse=pygame.image.load('mashroomhouse.png')
mashroomhousePosition=pygame.Rect(640,250,60,60)
screen.blit(mashroomhouse,mashroomhousePosition)

melonhouse=pygame.image.load('melonhouse.png')
melonhousePosition=pygame.Rect(660,350,50,50)
screen.blit(melonhouse, melonhousePosition)

pearhouse=pygame.image.load('pearhouse.png')
pearhousePosition=pygame.Rect(660,450,30,30)
screen.blit(pearhouse,pearhousePosition)

def Intersect(x1,x2,y1,y2): # object collision formula  http://wiki.linuxformat.ru/wiki/LXF112:%D0%98%D0%B3%D1%80%D1%8B
    if (x1>x2-40) and (x1<x2+40) and (y1>y2-40) and (y1<y2+40):
        return 1
    else:
        return 0


pygame.display.update()  #display all elements



while (True):  # Start of while loop
    for event in pygame.event.get():  # This creates indefinate loop to keep program running unless QUIT is invoked
        if event.type == pygame.QUIT:
            pygame.quit();


        elif event.type == pygame.KEYDOWN:  # Start of KEYDOWN event (when a key is pressed)
            if event.key == pygame.K_RIGHT:  # States if a key is pressed then the related variable becomes True
                key_right = True
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_UP:
                key_up = True
            if event.key == pygame.K_DOWN:
                key_down = True
        elif event.type == pygame.KEYUP:  # Start of KEYUP event (when a key is not pressed)
            if event.key == pygame.K_RIGHT:  # States if a key is not pressed then the related variable becomes False
                key_right = False
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_UP:
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False

            if event.key == pygame.K_z:  # States if z key is pressed then the fruits will be picked up
                if carryapple == True:
                    carryapple = False
                elif playerPosition.left <= applePosition.right  and playerPosition.right >= applePosition.left and playerPosition.top <= applePosition.bottom and playerPosition.bottom >= applePosition.top:
                    carryapple = True

                if carrybanana == True:
                    carrybanana = False
                elif playerPosition.left <= bananaPosition.right and playerPosition.right >= bananaPosition.left and playerPosition.top <= bananaPosition.bottom and playerPosition.bottom >= bananaPosition.top:
                    carrybanana = True

                if carrypear == True:
                    carrypear = False
                elif playerPosition.left <= pearPosition.right and playerPosition.right >= pearPosition.left and playerPosition.top <= pearPosition.bottom and playerPosition.bottom >= pearPosition.top:
                    carrypear = True
                if carrycherry==True:
                    carrycherry=False
                elif playerPosition.left<=cherryPosition.right and playerPosition.right>=cherryPosition.left and playerPosition.top<=cherryPosition.bottom and playerPosition.bottom>=cherryPosition.top:
                    carrycherry=True

                if carrymashroom==True:
                    carrymashroom=False
                elif playerPosition.left<=mashroomPosition.right and playerPosition.right>=mashroomPosition.left and playerPosition.top<=mashroomPosition.bottom and playerPosition.bottom>=mashroomPosition.top:
                    carrymashroom=True

                if carrymelon==True:
                    carrymelon=False
                elif playerPosition.left<=melonPosition.right and playerPosition.right>=melonPosition.left and playerPosition.top<=melonPosition.bottom and playerPosition.bottom>=melonPosition.top:
                    carrymelon=True


        # collision of objects(wolf)
        if Intersect(playerPosition.x, wolfPosition.x, playerPosition.y, wolfPosition.y) == True:
            key_down=False
            key_left=False
            key_right=False
            key_up=False
            print 'You lose :('

        if Intersect(playerPosition.x, wolf1Position.x, playerPosition.y, wolf1Position.y) == True:
            key_down = False
            key_left = False
            key_right = False
            key_up = False
            print 'You lose :('

        if Intersect(playerPosition.x, wolf2Position.x, playerPosition.y, wolf2Position.y) == True:
            key_down=False
            key_left=False
            key_right=False
            key_up=False
            print 'You lose :('

        if Intersect(playerPosition.x, wolf3Position.x, playerPosition.y, wolf3Position.y) == True:
            key_down=False
            key_left=False
            key_right=False
            key_up=False
            print 'You lose :('

        if Intersect(playerPosition.x, wolf4Position.x, playerPosition.y, wolf4Position.y) == True:
            key_down=False
            key_left=False
            key_right=False
            key_up=False
            print 'You lose :('

        if Intersect(playerPosition.x, wolf5Position.x, playerPosition.y, wolf5Position.y) == True:
            key_down=False
            key_left=False
            key_right=False
            key_up=False
            print 'You lose :('

        if Intersect(applePosition.x,applehousePosition.x,applePosition.y, applehousePosition.y)==True and Intersect(bananaPosition.x, bananahousePosition.x, bananaPosition.y, bananahousePosition.y) == True and Intersect (cherryPosition.x,cherryhousePosition.x, cherryPosition.y,cherryhousePosition.y)==True and Intersect (mashroomPosition.x,mashroomhousePosition.x, mashroomPosition.y,mashroomhousePosition.y)==True and Intersect(melonPosition.x,melonhousePosition.x, melonPosition.y,melonhousePosition.y)==True and Intersect(pearPosition.x,pearhousePosition.x, pearPosition.y,pearhousePosition.y)==True:
            key_down = False
            key_left = False
            key_right = False
            key_up = False
            print 'You won!!!'




    screen.blit(background,playerPosition, playerPosition)  # erase
    screen.blit(background, applePosition, applePosition)
    screen.blit(background, bananaPosition, bananaPosition)
    screen.blit(background, pearPosition, pearPosition)
    screen.blit(background,cherryPosition,cherryPosition)
    screen.blit(background,mashroomPosition,mashroomPosition)
    screen.blit(background,melonPosition,melonPosition)
    screen.blit(background,wolfPosition,wolfPosition)
    screen.blit(background,wolf1Position,wolf1Position)
    screen.blit(background,wolf2Position,wolf2Position)
    screen.blit(background,wolf3Position,wolf3Position)
    screen.blit(background, wolf4Position, wolf4Position)
    screen.blit(background, wolf5Position, wolf5Position)
    screen.blit(background,applehousePosition,applehousePosition)
    screen.blit(background,bananahousePosition, bananahousePosition)
    screen.blit(background,cherryhousePosition,cherryhousePosition)
    screen.blit(background,mashroomhousePosition,mashroomhousePosition)
    screen.blit(background,melonhousePosition,melonhousePosition)
    screen.blit(background,pearhousePosition,pearhousePosition)

    #map

    if playerPosition.right >= 710:
        playerPosition.right = 710
    if playerPosition.left <= 0:
        playerPosition.left = 0
    if playerPosition.bottom >= 500:
        playerPosition.bottom = 500
    if playerPosition.top <= 0:
        playerPosition.top = 0

    #player movement

    if key_right == True:
        msElapsed = clock.tick(120)
        playerPosition = playerPosition.move(3, 0)
    if key_left == True:
        msElapsed = clock.tick(120)
        playerPosition = playerPosition.move(-3, 0)
    if key_down == True:
        msElapsed = clock.tick(120)
        playerPosition = playerPosition.move(0, 3)
    if key_up == True:
        msElapsed = clock.tick(120)
        playerPosition = playerPosition.move(0, -3)

    if carryapple == True:
        applePosition = playerPosition

    if carrybanana == True:
        bananaPosition = playerPosition

    if carrypear == True:
        pearPosition = playerPosition
    if carrycherry==True:
        cherryPosition=playerPosition

    if carrymashroom==True:
        mashroomPosition=playerPosition

    if carrymelon==True:
        melonPosition=playerPosition


    screen.blit(applehouse, applehousePosition)
    screen.blit(bananahouse, bananahousePosition)
    screen.blit(cherryhouse,cherryhousePosition)
    screen.blit(mashroomhouse,mashroomhousePosition)
    screen.blit(pearhouse,pearhousePosition)
    screen.blit(melonhouse,melonhousePosition)
    screen.blit(player, playerPosition)
    screen.blit(apple, applePosition)
    screen.blit(banana, bananaPosition)
    screen.blit(pear, pearPosition)
    screen.blit(cherry, cherryPosition)
    screen.blit(mashroom, mashroomPosition)
    screen.blit(melon, melonPosition)
    screen.blit(wolf, wolfPosition)
    screen.blit(wolf1, wolf1Position)
    screen.blit(wolf2, wolf2Position)
    screen.blit(wolf3, wolf3Position)
    screen.blit(wolf4, wolf4Position)
    screen.blit(wolf5, wolf5Position)


    pygame.display.update()