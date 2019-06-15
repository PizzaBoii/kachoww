import pygame
import pygame.freetype
import time
pygame.init()

path = '' # you will have to have this image path on your PC
display_width = 8000
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0, 0, 0)
white = (255, 255, 255)
color = (0,0,0)

clock = pygame.time.Clock()
crashed = False


def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_object(text,font):
    textSurface = font.render(text,True,black)
    return (textSurface,textSurface.get_rect())

def message_display(message,cords):
    large_text=pygame.font.Font('freesansbold.ttf',50)
    Textsurf,TextRect=text_object(message,large_text)
    TextRect.center=(cords)
    gameDisplay.blit(Textsurf,TextRect)





x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

car_speed = 0
side_x=' '
side_y=' '
vs=0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                side_x='left'
                path ='' #you will have to have this imagine path on your pc




            elif event.key == pygame.K_d:
                side_x='right'
                path =' ' #you will have to have this imagine path on your pc




            elif event.key== pygame.K_w:
                y=y-5
            elif event.key == pygame.K_s:
                y+= 5
            elif event.key==pygame.K_SPACE:
                path =  #you will have to have this imagine path on your pc
                side_x = " "
            elif event.key == pygame.K_DOWN:
                vs-=0.5
            elif event.key == pygame.K_UP:
                vs += 0.5

        ######################
    ##


    gameDisplay.fill(white)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 8
    if pressed[pygame.K_s]:
        y += 8


    if side_x=='left': #x_change>-15
        x_change-=vs

    if side_x=='right':#and x_change<15
       x_change+=vs

    if side_x==" ":
        x_change=x_change*0.9


    x += x_change
    ##
    carImg = pygame.image.load(path)

    car(x, y)
    if x>1700:

        x=0
    if x<0:
        x=1700


    message_display(f"({int(x)},{int(y)})- speed of the car:{int(x_change)}", (500, 24))
    message_display(f"speed rate -      {vs}", (1500, 24))


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
