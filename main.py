import pygame
pygame.init()


class Brick:
    def __init__(self, xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    def draw(self):
        if self.alive:
            pygame.draw.rect(screen,(255,0,23),(self.xpos, self.ypos, 50,20))
    def collide(self,x,y):
        if self.alive:
            if x+20>self.xpos and x<self.xpos+50 and y+20>self.ypos and y<self.ypos+20:
                self.alive = False
                return True
    
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("breakout")
clock = pygame.time.Clock()


doExit = False
px = 300
py = 450

bx = 200
by = 200

bVx = 5
bVy = 5

#Bricks
b1 = Brick(20,20)
b2 = Brick(100,100)
b3 = Brick(200,200)
while not doExit: #pygame loop ----
    
    #Input and Output section ----
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True

    keys = pygame.key.get_pressed()
    if keys [pygame.K_a]:
        px -= 5
    if keys [pygame.K_d]:
        px += 5
    
    #physics section ----
    #makes the ball move with velocity
    bx += bVx
    by += bVy
    
    #collision section ----
    #ball bounces off walls
    if bx < 0 or bx+20 > 700:
        bVx *=-1
    if by < 0 or by+20 > 500:
        bVy *=-1
        
    #bounce ball off paddle
    if by+20 > py and bx+20 > px and bx < px+100:
        bVy *=-1
        
    if b1.collide(bx,by):
        bVy*=-1
    if b2.collide(bx,by):
        bVy*=-1
    if b3.collide(bx,by):
        bVy*=-1
    #render section ----
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (px,py, 100, 20)) #paddle
    pygame.draw.rect(screen, (255,255,255), (bx,by, 20, 20)) #ball
    
    
    b1.draw()
    b2.draw()
    b3.draw()
    
    
    
    pygame.display.flip() 



pygame.quit() #end of pygame loop ----
