import pygame

#NEWEST VERSION
#IDEAS
#BUTTON THAT MAKES A SOLID BLOCK WHERE YOU ARE AND TELEPORTS YOU TO YOUR SPAWNPOINT
#SMOOTHER CAMERA SCROLL THAT SHOWS MORE OF THE SCREEN ON THE DIRECTION YOU'RE FACING
pygame.init()
screen = pygame.display.set_mode((1400, 1000))
done = False
is_blue = True
onGround = False
ySpeed = 0
xSpeed = 0
blocks = []
wall = False
prevX = 10
prevY = 10
wallJump = 0
wallSide = "none"
stage = 1
levelRendered = False
checkPoints = []
deathBlocks = []
bullets = []
moveBlocks = []

clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class block():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        blocks.append(self)

class exitBlock():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def endLevel(self):
        global stage, blocks
        if player.x in range(self.x - 60, self.x + 60) and player.y in range(self.y - 60, self.y + 60):
            stage += 1
            player.x = 60
            player.y = 0
            blocks = []
            levelRendered = False

class checkPoint():
    def __init__(self, x, y, used):
        self.x = x
        self.y = y
        self.used = used
        checkPoints.append(self)

class danger():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        deathBlocks.append(self)

class bullet():
    def __init__(self, startX, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.startX = startX
        bullets.append(self)

class movingBlock():
    def __init__(self, startX, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.startX = startX
        moveBlocks.append(self)

player = player(500, 0, (0, 255, 255))


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and (onGround == True or wallSide != "none"):
                        ySpeed = 20
                        if wallSide == "left":
                            xSpeed -= 20
                        elif wallSide == "right":
                            xSpeed += 20
                        onGround = False
                        wallJump = 100
            
        
        #if levelRendered == False:
            #I found this code online at http://pygame.org/project-Rect+Collision+Response-1061-.html and edited it to work with my code 
        if stage == 1:
            level = [
        "           W          W                       ",
        "           W          W                       ",
        "        C  W    WWWW  W                       ",
        "        W  W     W W       E                  ",
        "        W  WWW   W W     WWW                  ",
        "        W  W     W W                          ",
        "        W  W     WWW                          ",
        "        W  W                                  ", 
        "        W  W                                  ",
        "        W                                     ",
        "        W                                     ",
        "        WWWWW                                 ",
        "                                              ",
        "                                              ",
        "                                              ",
        "                                              ",
        ]
            pygame.display.set_caption("Jumping and wall jumping")

        elif stage == 2:
            level = [
        "          W                                       ",
        "          W                                       ",
        "          W                                       ",
        "          W            C                          ",
        "          W            W                          ",
        " C        W   W    W       W                      ",
        " W        W   W            W                      ",
        "              W            W                      ",
        "                           W                      ",
        "                           W   W                 E",
        "                               W              WWWW",
        "         W                     W        W         ",
        "                               W        W         ",
        "                               W                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        ]
            pygame.display.set_caption("Checkpoints")
            
        elif stage == 3:
            level = [
        "     W            D                               ",
        " C   W            D                               ",
        " W   W             D     D                        ",
        " WD  W   D   W      D                             ",
        " W   W   D   W                  D            E    ",
        " W   W   D   W                  D       WWWWWW    ",
        " W   W   D   W   D    C   DDD   D                 ",
        " W  DW   D   W     WWWWWWW  W   D     W           ",
        " W   W   D   W              W                     ",
        " W   W                      W       W             ",
        " W                          W                     ",
        " WD   C                     W     W               ",
        " WWWWWW                     W                     ",
        "                                                  ",
        "                                                  ",
        ]
            pygame.display.set_caption("A little danger")

        elif stage == 4: #My little brother designed the level below on graph paper, which i then translated into the game.
            level = [
        "                         W           W            ",
        "                         W     C     WE           ",
        "                        DW    WW     WW           ",
        "                        DW   DW       W           ",
        " C                      DW    W       W           ",
        "WWW                     DWD   WD      W           ",
        "                        DW    W       W           ",
        "       Q      D      D  DW    W       W           ",
        "              W      W  DW   DW       W           ",
        "              W      W  DW    W      DW           ",
        "DDDDDDDDDDDDDDW      W  DW    W       W           ",
        "                     W  DWD   W                   ",
        "                     W  DW    W                   ",
        "                              W       W           ",
        "                      R    C                      ",
        "                           W                      ",
        ]
            pygame.display.set_caption("Moving Platforms")

        elif stage == 5:
            level = [
        "W       W                         W               ",
        "W       W                         W               ",
        "W       W                    C    W               ",
        "W       W                    9    W               ",
        "W           W      QQQ      W     W               ",
        "W           WDDDDDDDDDDDDDDW      W               ",
        "WC          W7                    W               ",
        " WWWWWWWWWWWW                     W               ",
        " D                     R          W               ",
        " D  E                             W               ",
        "          Q                       W               ",
        "                DDDDDDDDDDDDDDDDDDD               ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        ]
            pygame.display.set_caption("Bullets")
        elif stage == 6:
            level = [
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        " C                                                ",
        " W  WWW W W WWW    WWW W   W WW                   ",
        "     W  W W W      W   WW  W W W                  ",
        "     W  WWW WWW    WWW W W W W W                  ",
        "     W  W W W      W   W  WW W W                  ",
        "     W  W W WWW    WWW W   W WW  E                ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        "                                                  ",
        ]
            pygame.display.set_caption("End")

            # Parse the level string above. W = wall, E = exit
        if levelRendered == False:
            bx = by = 0
            lastCheckPoint = checkPoint(500, 0, False)
            for row in level:
                for col in row:
                    if col == "W":
                        block(bx, by, (0, 255, 20))
                    if col == "E":
                        door = exitBlock(bx, by, (255, 255, 255))
                    if col == "C":
                        checkPoint(bx, by, False)
                    if col == "D":
                        danger(bx, by)
                    if col == "1" or col == "2" or col == "3" or col == "4" or col == "5":
                        bullet(bx, bx, by, int(col))
                        block(bx, by, (0, 255, 20))
                    if col == "6" or col == "7" or col == "8" or col == "9" or col == "0":
                        bullet(bx, bx, by, (-1 * int(col)) + 4)
                        block(bx, by, (0, 255, 20))
                    if col == "Q":
                        movingBlock(bx, bx, by, 3)
                    if col == "R":
                        movingBlock(bx, bx, by, -3)
                    bx += 60
                by += 60
                bx = 0
            levelRendered = True
            #Everything below I made myself
        wallSide = "none"
        

        if onGround == True:
            wallSide = "none"
         
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if xSpeed > -10:
                if wallSide != "right":
                    xSpeed -= 2
        if pressed[pygame.K_RIGHT]:
            if xSpeed < 10:
                if wallSide != "left":
                    xSpeed += 2

        if xSpeed > 0:
            xSpeed -= 1
        elif xSpeed < 0:
            xSpeed += 1

        player.x += xSpeed

        if onGround == False:
            ySpeed -= 1
            player.y -= ySpeed

        #I'm really proud of the loops below, specifically this first one, as they were difficult to make work. Most of them have to do with collision, which was a difficult problem.
        for i in blocks:
            if player.x in range(i.x - 60, i.x + 60) and player.y in range(i.y - 60, i.y + 60):

                if prevY in range(i.y - 59, i.y + 59) and prevX not in range(i.x - 59, i.x + 59):
                    if player.x < i.x + 30:
                        player.x = i.x - 61
                        wallSide = "left"
                        xSpeed = 0
                    elif player.x > i.x + 30:
                        player.x = i.x + 60
                        wallSide = "right"
                        xSpeed = 0
                    else:
                        wallSide = "none"

                if prevX in range(i.x - 60, i.x + 60) and prevY not in range(i.y - 60, i.y + 60):
                    if player.y > i.y + 30:
                        player.y = i.y + 60
                        ySpeed = 0
                    else:
                        player.y = i.y - 60
                        onGround = True
                        
                if prevX in range(i.x - 60, i.x + 60) and prevY in range(i.y - 60, i.y + 60):
                    if player.y < i.y + 30:
                        player.y = i.y - 60
                        onGround = True
                    else:
                        player.y = i.y + 60
                        ySpeed = 0
                    

            if player.y == i.y - 60 and player.x in range(i.x - 60, i.x + 60):
                onGround = True
                ySpeed = 0
                break
            else:
                onGround = False

        if wallSide != "none" and ySpeed < -2:
            ySpeed = -2

        if player.y > 1100:

            player.x = lastCheckPoint.x
            player.y = lastCheckPoint.y
        if player.y < 0:
            player.y = 0
            ySpeed = 0

        prevX = player.x
        prevY = player.y

        screen.fill((0, 0, 0))
        for i in blocks:
            pygame.draw.rect(screen, i.color, pygame.Rect(i.x - (player.x - 500), i.y, 60, 60))

        for i in checkPoints:
            if player.x in range(i.x - 60, i.x + 60) and player.y in range(i.y - 60, i.y + 60):
                lastCheckPoint.x = i.x
                lastCheckPoint.y = i.y
                
            pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(i.x - (player.x - 500), i.y, 60, 60))

        for i in deathBlocks:
            if player.x in range(i.x - 60, i.x + 60) and player.y in range(i.y - 60, i.y + 60):
                player.x = lastCheckPoint.x
                player.y = lastCheckPoint.y - 10
                ySpeed = 0
                
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i.x - (player.x - 500), i.y, 60, 60))

        for i in bullets:
            if player.x in range(i.x - 60, i.x + 30) and player.y in range(i.y - 45, i.y + 30):
                player.x = lastCheckPoint.x
                player.y = lastCheckPoint.y - 10
                ySpeed = 0

            if i.direction < 0:
                if i.x < i.startX + (i.direction*190):
                    i.x = i.startX
                i.x -= 10
            if i.direction > 0:
                if i.x > i.startX + i.direction*190:
                    i.x = i.startX
                i.x += 10
                    
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i.x - (player.x - 500), i.y, 30, 30))

        for i in moveBlocks:
            if player.x in range(i.x - 60, i.x + 60) and player.y in range(i.y - 60, i.y + 10):
                player.y = i.y - 60
                ySpeed = 0
                player.x += i.direction
                onGround = True
                break
            
        for i in moveBlocks:
            if i.direction < 0:
                if i.x < i.startX + (i.direction*120):
                    i.direction = -1*i.direction
            if i.direction > 0:
                if i.x > i.startX + i.direction*120:
                    i.direction = -1*i.direction
            i.x += i.direction
                    
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(i.x - (player.x - 500), i.y, 60, 10))

        pygame.draw.rect(screen, player.color, pygame.Rect(500, player.y, 61, 60))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(door.x - (player.x - 500), door.y, 60, 60))
        if player.x in range(door.x - 60, door.x + 60) and player.y in range(door.y - 60, door.y + 60):
            levelRendered = False
            blocks = []
            stage += 1
            player.x = 60
            player.y = 0
            xSpeed = 0
            checkPoints = []
            deathBlocks = []
            bullets = []
            moveBlocks = []
            xSpeed = 0
            
        pygame.display.flip()
        clock.tick(60)
        













 






