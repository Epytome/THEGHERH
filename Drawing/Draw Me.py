import pygame
import random

# Initialize game engine
pygame.init()

# Window
width = 800
height = 600
SIZE = (width, height)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0 )
WHITE2 = (210, 210, 210)
MAROON = (128, 0, 0)


''' Make Stars '''
stars = []
for i in range(300):
    x = random.randrange(1, width)
    y = random.randrange(1, height)
    r = random.randrange(2, 3)
    stars.append([x, y, r, r])


'''Make Clouds'''
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 800)
    y = random.randrange(-50, 100)
    loc = [x, y]
    clouds.append(loc)




def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for s in stars:
        s[1] -= -4

        if s[1] > 410:
           s[0] = random.randrange(0, 800)
           s[1] = random.randrange(-400, 0)



    for c in clouds:
        c[0] -= -3

        if c[0] > 900:
            c[0] = random.randrange(-800, -100)
            c[1] = random.randrange(-50, 200)
             
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' stars '''
    for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)


    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


    
    ''' grass '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    '''snowMAN'''
    pygame.draw.ellipse(screen, WHITE2, [100 , 500, 60, 60])
    pygame.draw.ellipse(screen, WHITE2, [105, 460, 50, 50])
    pygame.draw.ellipse(screen, WHITE2, [110, 430, 40, 40])
    pygame.draw.ellipse(screen, BLACK, [126, 492, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 500, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 484, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 476, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [132, 445, 8, 8])
    pygame.draw.ellipse(screen, BLACK, [120, 445, 8, 8])


    ''' house '''
    pygame.draw.rect(screen, MAROON, [400, 300, 200, 100])
    pygame.draw.polygon(screen, WHITE2,[[380, 300], [500, 240], [620, 300]])
    pygame.draw.rect(screen, BLACK, [460, 320, 45, 80])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)

    '''clouds'''
    for c in clouds:
        draw_cloud(c)


    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)





    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
