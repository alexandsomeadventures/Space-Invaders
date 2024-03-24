import pygame
import random
import math
from pygame import mixer #for music and sounds
pygame.init()#initializing pygame  library(without this,won't work)

#we need to create screen(like window) for game
screen=pygame.display.set_mode((800,600))#add another () inside ().  you have to write 2 values inside for width and height(first comes width,second comes height)

#after running these 3 lines,python will once execute the code and exit the program. one way to make prevent this- create loop(while True)

#while True:
#   pass

#you can open Task Manager just for your window to be there

pygame.display.set_caption('Space Invaders')#name of game

background= pygame.image.load('background.png')#new cool background. we need to put it in loop to make it appear constantly


#--- SOUNDS ---
mixer.music.load('background.wav')#adding background music
mixer.music.play(-1)#playing the music. However, if we don't put anything inside play(),the music won't play continiously.

#The play() method of the Pygame mixer module is used to start playing a sound.
# The second argument of the play() method determines how many times the sound should be played.
# If you pass -1 as the second argument to play(),
# it means that the sound should be played in an infinite loop until you explicitly stop it.






#when creating icon in pycharm, it is better to import image with png format
icon = pygame.image.load('abduction.png')#firstly we need to load image and then display it
pygame.display.set_icon(icon)#please choose image that is 32 bits and 32 pixels. also if it is not in your current python project,transfer it there to be able to use it in your game file

#---ADDING IMAGES TO GAME---
#here, in adding image to our game, you can use image with 64 pixels. we need to place our image at center of the window
#Therefore, we need to know coordinates of middle using coordinates of window(800,600)

player_image = pygame.image.load('space.png')
#BIG NOTE: Please never forget - after downloading an image, it is better to put it in python project folder or file manually
# in app 'File Explorer' since otherwise,python will show an error that it hasn't found such an image IN ITS DIRECTORY


#let's also make enemy for our object to shoot:
enemy_speed_variable=2.5
enemy_image=[]
enemy_imageX= []
enemy_imageY= []
enemy_imageX_change=[]
enemy_imageY_change=[]
number_of_enemies=6#we can later change the value if we want to increase amount of enemies

for i in range(number_of_enemies):#the loop is gonna run 6 times, so it means we will create 6 enemies
    #elements-such as x, y, Xchange,Ychange- of our enemies will each be stored in separate list
    enemy_image.append(pygame.image.load('alien.png'))
    enemy_imageX.append(random.randint(0,735))
    enemy_imageY.append(random.randint(50,150))
    enemy_imageX_change.append(enemy_speed_variable)
    enemy_imageY_change.append(40)
    # enemy_image=pygame.image.load('alien.png')
    # enemy_imageX= random.randint(0,735) #when game starts we want our enemy to appear in random places
    # enemy_imageY= random.randint(50,150)
    # enemy_imageX_change=2.5
    # enemy_imageY_change=40
#but now there is another problem. Before, we were working with only one enemy code. Now that we have changed data type of enemy variables to lists, python is not able to execute actions with them that we've written below
#plus we have 6 enemies. python doesn't know which one we're calling.That's why we need to use indexes and iterate each of them


#but we also want our enemy to move to random positions instead of staying constantly in same place.
#That's why we import random library


#but we also want to create multiple enemies, so look above



#now let's create position for our image using x and y coordinates

player_imageX= 370
player_imageY= 480
player_imageX_change=0
#we want it to appear not exactly in the middle, but below. somewhere in middle of width and lower than center point.
#the half of 800 is 400 which is center of x axis, but we don't give that value since we have to consider image as well,
# which may not fit perfectly

#now let's create function def player():

def player(x,y):#add here x and y variables for new coordinates, which will help us with moving our object

    screen.blit(player_image,(x,y))#blit allows us to draw our image on window of our game
    #blit requires two parameters- 1)image itself 2) write another() and inside write x,y coordinates of image.
    #Quick Note: don't forget to put commas inside brackets()


#create same function for the enemy:

def enemy(x,y,enemy_i):

    screen.blit(enemy_image[enemy_i],(x,y))

#now let's create shooting bullets at our enemy
#so x coordinate of our bullet is equal to that of our spaceship
#bullet's starting position is in our object. wherever the ship moves, bullets will come out of our object.
#as we shoot bullet,the bullet is going up(away from us) which means its y coordinate value decreases.




#let's display score:
score = 0#each time user kills enemy, score will be increased

#we want it to appear in the top left corner:
scoreX=10
scoreY=10

#we also need to set up font of the text
font= pygame.font.Font('freesansbold.ttf',32)#2 parameters. 1)what type of font we want 2)size of our font

def score_display(x,y):
    score_variable= font.render('SCORE: '+str(score),True,(255,255,255))

    # the reason we don't use screen.blit but render is because we have to create surface for text. Images already have surfaces,but texts
    #firstly need to be rendered so that surfaces would be created for them. Only then, you can treat texts same as images
    #in other words,images already have their size,font,color,and etc. while these properties for texts are done manually
    #for example you just wrote random text. Logically you have to put color for it, change its size, or alter the font/style of it

    #first parameter for text that is displayed, second for antialiasing(explained below),third for color.

    #This argument is the "antialias" flag which determines whether or not to apply antialiasing when rendering the text.
    # Antialiasing is a technique used in computer graphics to smooth jagged edges and make text or graphics
    # appear more smooth and less pixelated.

    # When True is passed as the second argument, antialiasing is enabled, and the text will be rendered with smooth edges.
    # If False is passed, then antialiasing will be disabled, and the text will be rendered with sharp edges.

    # So in this case, passing True enables antialiasing for the text in the score_variable,
    # which will make the text appear smoother and more readable.

    screen.blit(score_variable,(x,y))

#---GAME OVER---

font_gameover= pygame.font.Font('freesansbold.ttf',80)

def game_over_text():
    GAME_OVER=font_gameover.render('GAME OVER',True,(255,255,255))
    screen.blit(GAME_OVER,(200,250))



bullet_image=pygame.image.load('bullet_1.png')
bullet_imageX= 0
bullet_imageY= 480#why 480? because our ship is always on y = 480. our object can change its x position but y is always same.
bullet_imageX_change=0
bullet_imageY_change=10
bullet_state= 'ready'# if our object doesn't shoot(when you don't see bullet on screen), the bullet status is ready ,
# otherwise when it is being shot, it is on file abd being"fired"



def fire_bullet(x,y): #this is going to be called whenever we press space button on keyboard
    global bullet_state
    #we said that this func activates when we press spacebar,which means we shoot a bullet. That means we have to change status of our bullet
    bullet_state= 'fire'
    screen.blit(bullet_image,(x+16,y+10))#python always takes x y coordinates of center of an object to left hand side.
    #so x y coordinates of our ship-which are 370,480- are actually left side of our ship.
    # in order to start our bullet from nose of our ship(center),we should add some amount for both x and y

#collision detection
#now we will have to know whether our bullet hit the enemy or not:

def iscollided(enemyX_value,enemyY_value,bulletX_value,bulletY_value):
    # distance= ((enemyX_value-bulletX_value)**2 + (enemyY_value-bulletY_value)**2)**0.5
    distance=math.sqrt(math.pow(enemyX_value-bulletX_value,2)+math.pow(enemyY_value-bulletY_value,2))
    #check out on google for equation that solves for distance. it is formula
    #inside math.pow, there are 2 parameters. first requires a number or a value , second requires power to which we are going to increase the value we wrote in 1st parameter.

    if distance <27:#why 27? Well,actually, we just chose this number by testing our code. Thus, we came to conclusion that when distance is less than 27,it means the bullet has hit the enemy
        return True
    return False






second_score=0
running = True
#while loop is main root of our game since actions that we want to implement should be put inside of it
#everythin that is related to inside of our window game should be in loop
while running:
    # now let's create background for window of our game
    screen.fill((140, 50, 255))  # inside brackets write () and then inside of that write 3 paremeters(RGB- red, green,blue). basically,everything else consists of these 3 colors
    # maximum in one parameter above you can write up to 255 (0-255) not more than that. the higher number, the more pure the color
    # for example 255 in first parameter means pure red(it is like you mix 3 colors)
    # if you want to know how to get parameters of specific color(say yellow) you can google- RGB converter(website- rapidtables or else)


    # player_imageX += 0.1#this will move our object 0.1 square  right each iteration in loop(continiously)
    # player_imageY -= 0.1#this will move our object 0.1 square up each iteration in loop(continiously)


    #adding and putting background in loop:
    screen.blit(background,(0,0))#always choose background that covers your whole window. in our case, our window is 800x600, which is why
    #we looked for background with 800x600 parameters. then write (0,0). The reason why we didn't write 800,600 is because these are coordinates
    #of our right lower corner. We want our background to start from left upper corner. It is going to spread and fill whole window anyway
    #since it is 800x600. Remember, don't forget width and height of an object since it has its own amount of space.
    #background,due to parameters, takes whole window as its space so that's why we write 0,0.

    #you might ask why our objects move so slow now after adding only background? That's because our background file is heavy(224kb)
    #Due to having big size of background as a file, our while loop becomes slower, thus leading to ineffectiveness in movement of our objects.
    #we just have to increase values for moving our objects. Instead of enemyimageX_change=0.3 or playerImageX_change=0.3,write 5 or more.




    for event in pygame.event.get():#all of the events -actions- will be stored in pygame.event.get()
        # we want to make so that when user closes the window of game(at the top in right corner ) the game is gonna stop
        if event.type == pygame.QUIT:#we are checking whether user quits the game or not
            running = False

        #check whether pressed keystroke is left or:
        if event.type == pygame.KEYDOWN: #this means that action was pressing a key on keyboard. if keystroke was pressed,python will enter this condition
            if event.key == pygame.K_LEFT:#checks whether pressed key is left arrow key or not
                player_imageX_change = -5
            elif event.key == pygame.K_RIGHT:
                player_imageX_change = 5
            elif event.key == pygame.K_SPACE:#if user presses spacebar,we shoot a bullet

                #there is one more problem. if we press spacebar while the bullet is fired and ship is being moved, it is going to copy X position of ship which is moving and appear in other position
                #we need to make sure bullet can only be fired when status is 'ready':
                if bullet_state == 'ready':
                    #1)For songs/music use mixer.music.2) For sound effects or short sounds, use mixer.Sound
                    bullet_sound= mixer.Sound('laser.wav')
                    bullet_sound.play()#we dont add '-1' since once we shoot a bullet, the sound effect won't stop playing
                    bullet_imageX=player_imageX#solving our second problem mentioned somewhere below
                    #thus bulletX won't follow the ship when it moves every time. when we press space,
                    # the bullet is gonna take x coordinate of ship the moment user wanted to fire bullet and the bullet is gonna go on that only X position
                    fire_bullet(bullet_imageX,bullet_imageY)




        #in pygame.KEYDOWN, keydown means - pressing key, and when we remove our finger from pressing that key, it is know as key up:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # let's create variable for changing movement of our x,y coordinates
                player_imageX_change = 0
    player_imageX += player_imageX_change
    #now let's set boundaries for our object so that it doesn't get out of the window:
    if player_imageX<=0:
        player_imageX=0
    elif player_imageX>=736:
        player_imageX=736#the reason why we don't write 800 here is because we also have to consider width of our object.
        #our objects is 64 pixels,which means it takes 64 squares as its width. player_imageX is x coordinate of our object,
        #so when the object reaches x = 800, it will get out of the boundary anyway because of THE WIDTH. we have to subtract object width
        #from x width = 800-64 = 736. when x =736, the other side of spaceship will be touched by boundary,thus preventing it from going any further
    if score-second_score>=10:
        second_score+=10
        enemy_speed_variable+=1
    for i in range(number_of_enemies):
        #Game Over screen:
        if enemy_imageY[i]>=440:#don't forget to consider weight of enemy! that's why we wrote '440'
            for elem in range(number_of_enemies):
                enemy_imageY[elem]=2000#if enemies reach our ship or Y line where our ship is, then it is game over. At that moment, we want all of our ships to disappear from the screen
            game_over_text()
            break
        enemy_imageX[i] += enemy_imageX_change[i]
        if enemy_imageX[i]<=0:
            enemy_imageX_change[i] = enemy_speed_variable
            enemy_imageY[i] += enemy_imageY_change[i]
        elif enemy_imageX[i]>=736:
            enemy_imageX_change[i] = -enemy_speed_variable
            enemy_imageY[i] += enemy_imageY_change[i]
        #we put collision here inside this loop since thus we will know which specific enemy has been hit
        # COLLISION DETECTION
        collision_variable = iscollided(enemy_imageX[i], enemy_imageY[i], bullet_imageX, bullet_imageY)
        if collision_variable:  # if the function returns true, logically this condition will work
            hit_sound= mixer.Sound('explosion.wav')
            hit_sound.play()
            bullet_imageY = 480
            bullet_state = 'ready'
            score += 1
            enemy_imageX[i] = random.randint(0, 735)
            enemy_imageY[i] = random.randint(50, 150)
            # if we write enemy_imageX = random.randint(0, 800) , this will cause error since remember we wrote this?:
            # elif enemy_imageX >= 736:
            #     enemy_imageX_change = -2.5
            #     enemy_imageY += enemy_imageY_change
            # we did this so that when enemy reaches boundary,it goes a bit down. However, when our bullet collides with enemy, the enemy's X respawns in range 0-800
            # so when python chooses random integer(let's say-760),it checks condition with boundary.
            # Thus when an enemy respawns when x =736-800, it doesn't even have chance to go left. It immediately goes down
            # to prevent this write random.randint(0, 735)  so that python respawns our enemy in random position but not in range x = 736-800
        enemy(enemy_imageX[i], enemy_imageY[i],i)#i is third parameter for python to understand which enemy out of 6 we want to appear on the screen



    # so what we want to do is when enemy hits right boundary,it changes its direction in opposite side. so for example
    # when hitting left boundary,enemy will push away and go in right side direction.
    #   Bullet Movement:
    if bullet_state == 'fire': # keyword 'is' executes the same purpose as '=='. It checks whether 2 objects are equal
        fire_bullet(bullet_imageX ,bullet_imageY)
        bullet_imageY -= bullet_imageY_change
    #so far it was okay,but there are two problems: 1)we can fire only one bullet
    # 2)when the bullet is shot,it should move in the direction it started with,
    # but in our case, when we shoot a bullet and then move our ship somewhere else, bullet (while getting away)moves to the position where our ship moved


    if bullet_imageY <=0:#when it reaches the boundary,the bullet is gonna reset to its initial vertical position(y=480)
        # and status is going to be 'ready'again
        bullet_state = 'ready'
        bullet_imageY=480



    #now we will have to change name/title of our game




    player(player_imageX,player_imageY)#in order to activate our image on screen, we put it in loop(thus it never disappears)
    score_display(scoreX,scoreY)
#But if we run the code, we will see that colors are not applied. Nothing changed.That is because we are not updating our window
    pygame.display.update()#updating the window

#dont forget these two lines= pygame.init() and pygame.display.update()

#Now, we want to create movement for our object(space.png). For example, the current coordinates of our object are 370,480.
#If we add or subtract some amount from x or y values, the position of our object will be changed,thus leading to movement of our player

#1)now, we will have to move our object according to user's keyboard(whether he presses on left arrow key or right arrow key)
#2)we will also have to put boundaries for our game so that our object doesn't move outside the window


#For collision detection pygame actually has a method called 'colliderect' which detects collision between rectangles.
# So, if you want to check if the enemy rectangle has collided with the bullet rectangle,
# instead of checking the distance between the two for every frame, you just write:
# if enemy_rectangle.colliderect(bullet_rectangle)
#     [whatever you want to do when the enemy collides with a bullet, or vice versa]


#now, we have to add sound effects and (background)music to our game with file extension .wav

#DONE