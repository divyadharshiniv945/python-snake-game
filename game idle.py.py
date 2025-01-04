# python snake game
import pygame
import random
pygame.init()
# screen
w=500
h=500
a=pygame.display.set_mode((w,h))
a.fill((100,255,100))
# score font
game_font=pygame.font.SysFont(None,35)
score=0

# snake body
x=232
y=234
width=15
height=15
vel=10
dir_x=0
dir_y=0
grow=0
snakelist=[[x,y]] 
len_of_thesnake=1


jump=True
jumpcount=10
# food  
food_x=50
food_y=100
food_width=15
food_height=15



run=True  
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         run=False
    #  Snake movements  
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
          dir_x=0
          dir_x-=vel 
          dir_y=0
    if keys[pygame.K_RIGHT]:
        dir_x=0
        dir_x+=vel
        dir_y=0
    if keys[pygame.K_UP]:
        dir_y=0
        dir_y-=vel
        dir_x=0
    if keys[pygame.K_DOWN]:
        dir_y=0
        dir_y+=vel
        dir_x=0
    if keys[pygame.K_SPACE]:
        jump=True
        y-=jumpcount**2
    # Wrap snake around the screen
    if x < 0:
        x = w
    elif x > w:  
        x = 0
    if y < 0:
        y =h
    elif y > h:
        y = 0
    # update snake head position
    x=x+dir_x
    y=y+dir_y
    # Add the new head position to the snake
    snakelist.append([x, y]) 
    if len(snakelist) > len_of_thesnake:
        del snakelist[0]
    # snake eats itself
    for segment in snakelist[:-1]: 
        if segment == [x, y]:
             run =False
    

    a.fill((100,255,100))


    apple=pygame.draw.rect(a,(255,0,0),(food_x,food_y,food_width,food_height))
    
    for segment in snakelist:
        pygame.draw.rect(a, (0, 50, 0), (segment[0], segment[1], width,height))
    
    snake=pygame.draw.rect(a,(0,50,0),(x,y,width,height))
    
    # collision between snake and food 
    if snake.colliderect(apple) :
          len_of_thesnake += 1
          score+=1
          food_x=random.randint(0,w-food_width)
          food_y=random.randint(0,h-food_height)
    # adding score
    score_text= game_font.render("Score: " + str(score), True, (0, 0, 0)) 
    a.blit(score_text, [0, 0 ])
         

    pygame.display.update()  
        
   
pygame.quit()

