import pygame
import time
pygame.init()

#players
player1 = input('Enter player 1 name: ')
player2 = input('Enter player 2 name: ')
chand = int(input('How many goals do you want to play?? '))

#cheching gate lol
name = input('Enter a word less than 8 charachters (and please write all uppercase): ')

if len(name)>=8:
    print('Sorry you entered ', len(name), ' characters and that is out of limit')
    time.sleep(5)
    pygame.quit()

for i in name:
    if i.islower():
        print('Sorry you entered lowercase!')
        time.sleep(5)
        pygame.quit()
        break

#Informations
width = 10
height = 100
w_text = len(name)*15
h_text = 38
x1 = 80
y1 = 350
x2 = 920
y2 = 350
xt = 90
yt = 350
yb1 = 400
yb2 = 400
vel = 5
vel_ball = 6
text_font = pygame.font.SysFont("Arial", 30)
smallfont = pygame.font.SysFont("comicsansms" , 25)
wow = 1
woow = 2
s1 = 0
s2 = 0

#Display
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Text_Ball")

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text , True , color)
    elif size == "medium":
        textSurface = pygame.font.SysFont("Arial",(255,255,255), 30) 
    elif size == "large":
        textSurface = text_font.render(text , True , color) 
    return textSurface , textSurface.get_rect()

def draw_text(text, font, text_col, x, y):
    img = font.render(text,True,text_col)
    win.blit(img, (x,y))

def message_to_screen(msg,color,y_displace=0,x_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (win.get_width()/2+x_displace) , ((win.get_height()/2) + y_displace)
    win.blit(textSurf,textRect)

#main code ( The base )
run = True
while run:
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #for player 2
    if keys[pygame.K_UP]and y2 > 0:
        y2 -= vel
        yb2 -= vel
    if keys[pygame.K_DOWN]and y2 < 700:
        y2 += vel
        yb2 += vel

    #for player 1
    if keys[pygame.K_w] and y1 > 0:
        y1 -= vel
        yb1 -= vel
    if keys[pygame.K_s]and y1 < 700:
        y1 += vel
        yb1 += vel

    #ball
    if (yt <= (y1+height) and yt > yb1) and (xt <= x1 and xt >= (x1-width)):
        wow = 1
        woow = 1
    elif (yt >= (y1) and yt <= yb1) and (xt <= x1 and xt >= (x1-width)):
        wow = 1
        woow = 2
    
    if (yt <= (y2+height) and yt > yb2) and (xt >= (x2-w_text) and xt <= (x2)):
       wow = 2
       woow = 1
    elif (yt >= (y2) and yt <= yb2) and (xt >= (x2-w_text) and xt <= (x2)):
       wow = 2
       woow = 2
    



    #if yt

    if wow == 1:
        xt += vel_ball
    
    elif wow == 2:
        xt -= vel_ball
    
    if yt <= 0:
        woow = 1

    elif yt >= 800-h_text:
        woow = 2
    
    if woow == 1:
        yt += vel_ball
    elif woow == 2:
        yt -= vel_ball

    #scores
    if xt>= 1000:
        s2 += 1
        wow = 2
    
    elif xt <= 0:
        s1 += 1
        wow = 1

    message_to_screen(str(s1),(255,255,255),-200,-100,"small")
    message_to_screen(str(s2),(255,255,255),-200, 100,"small")

    if s2 == chand:
        looser = player2 + ' lost'
        message_to_screen(looser,(255,255,255),-100,100)
        pygame.display.update()
        time.sleep(5)
        break
    
    elif s1 == chand:
        looser = player1 + ' lost'
        message_to_screen(looser,(255,255,255),-100,-100)
        pygame.display.update()
        time.sleep(5)
        break
    
    win.fill((0,0,0))       #Drawing
    message_to_screen(player1,(255,255,255),-255,-100,"small")
    message_to_screen(player2,(255,255,255),-255,100,"small")
    pygame.draw.line(win,(176, 253, 174),(500,0),(500,800),5)
    pygame.draw.rect(win, (255, 154, 200), (x1,y1,width,height))
    pygame.draw.rect(win, (154, 192, 255), (x2,y2,width,height))
    draw_text(name, text_font, (255,255,255), xt, yt)
    pygame.display.update()

pygame.quit()