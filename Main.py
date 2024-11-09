from cmath import sin
from math import cos
import pygame
from pygame.locals import*
import numpy.matlib 
import numpy as np 

pygame.init()

black   = ( 0, 0, 0)

ScreenWidth = 800
ScreenHight = 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHight))
pygame.display.set_caption("Spin")
GameRun = True

clock = pygame.time.Clock()

def KeyListener():

    global GameRun

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False

Transform = [[1,2],
             [2,1]]
Angle = 0

# Sets the Input in relation to the middle of the screen input:[Horizontal,Vertical] Output:[Horizontal,Vertical]


class Draw:
    def Grid():
        Space = 30
        for i in range (int(ScreenWidth / Space) + 1):
            pygame.draw.line(screen,(255,255,255),Draw.New_Pos((i -int(ScreenWidth / Space/2)) * Space , -ScreenHight / 2), Draw.New_Pos((i -int(ScreenWidth / Space/2)) * Space , ScreenHight / 2))
            
        for i in range (int(ScreenHight/Space) + 1):
            pygame.draw.line(screen,(255,255,255), Draw.New_Pos(-ScreenWidth / 2,(i -int(ScreenHight / Space/2))* Space),Draw.New_Pos(ScreenWidth / 2, (i -int(ScreenHight / Space/2)) * Space))
        pygame.draw.line(screen,(255,255,255),Draw.Set_Origin([0,0]),Draw.Set_Origin([0,30]),3)
        pygame.draw.line(screen,(255,255,255),Draw.Set_Origin([0,0]),Draw.Set_Origin([30,0]),3)

    def New_Pos(OldX, OldY):
        NewX = OldX * Transform[0][0] + OldY * Transform[0][1]
        NewY = OldX * Transform[1][0] + OldY * Transform[1][1]
        New_Cord = Draw.Set_Origin([NewX, NewY])
        return(New_Cord)
    
    def Set_Origin (xy):  
        Origin = [ScreenWidth / 2 + xy[0], ScreenHight / 2 - xy[1]]
        return(Origin)
    
while GameRun:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
   
    KeyListener()
   
    

    screen.fill(black)

    # Spielfeld/figuren zeichnen
    
   
    StartPos =  [   [-50,  50, 50, -50, -50,  50,  50, -50],   #x 
                    [-50, -50, 50,  50, -50, -50,  50,  50],   #y
                    [ 50,  50, 50,  50, -50, -50, -50, -50]    #z
                ]

    P = [   [1, 0, 0],
            [0, 1, 0],   
            [0, 0, 0]    
        ]
   
    Angle += 0.1
    
    
    RZ =     [   
                [cos(Angle), -sin(Angle), 0],
                [sin(Angle), cos(Angle), 0],
                [0, 0, 1]
            ]
    RX =    [   
        
                [1, 0, 0],
                [0,cos(Angle), -sin(Angle)],
                [0,sin(Angle), cos(Angle)]
            ]
    RY =    [   
        
                [cos(Angle), 0, -sin(Angle)],
                [0,1, 0],
                [sin(Angle), 0 , cos(Angle)]
            ]

    for i in range(8):
        z = [StartPos[0][i], StartPos[1][i], StartPos[2][i]]
        l = np.matmul(RX,z)
        l = np.matmul(RZ,l)
        l = np.matmul(RY,l)
        
        Offset = np.matmul(P,l)     
    
        for i in range(8):
            pygame.draw.circle(screen, (255,255,255), Draw.New_Pos(int((Offset[0])), int((Offset[1]))), 10)
        
   
    Draw.Grid()
    pygame.draw.line(screen,(255,255,255),Draw.New_Pos(0,0),Draw.New_Pos(0,100),10)
    # Fenster aktualisieren
    pygame.display.flip() 
    # Refresh-Zeiten festlegen
    clock.tick(25)
   

pygame.quit()