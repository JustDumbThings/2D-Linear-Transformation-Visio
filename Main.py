from cmath import sin
from math import cos
import pygame 
import numpy.matlib 
import numpy as np 
import easygui

import Storeage as s

pygame.init()
clock = pygame.time.Clock()

Angle = s.Angle  
ScreenWidth = s.ScreenWidth
ScreenHight = s.ScreenHight


screen = pygame.display.set_mode((ScreenWidth, ScreenHight))
pygame.display.set_caption("Spin")
GameRun = True



def KeyListener():
    global GameRun, Paddle_L_Y, Paddle_R_Y, BallY

    keys = pygame.key.get_pressed()
    
    # Reaktion auf das Drücken der Tasten
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           GameRun = False

    if keys[pygame.K_m]:
            Mult = easygui.enterbox().split()
            print(Mult)
            Calc.Transform(Mult)
           

M1 = [	[2,0],
		[3,1]]


s.Transform = s.E 


# Sets the Input in relation to the middle of the screen input:[Horizontal,Vertical] Output:[Horizontal,Vertical]
class Calc():
    def New_Pos(OldX, OldY):
        NewX = OldX * s.Transform[0][0] + OldY * s.Transform[0][1]
        NewY = OldX * s.Transform[1][0] + OldY * s.Transform[1][1]
        New_Cord = Calc.Set_Origin([NewX, NewY])
        return(New_Cord)
    
    def Set_Origin (xy):  
            Origin = [ScreenWidth / 2 + xy[0], ScreenHight / 2 - xy[1]]
            return(Origin)
    
    def Transform(list):
        Mult = [[int(list[0]), int(list[1])],
                [int(list[2]), int(list[3])]]
        s.TransformNew = np.matmul(s.Transform,Mult)
        print(Mult)

class Draw:
    def Grid():
        Space = 30
        for i in range (int(ScreenWidth / Space) + 1):
            pygame.draw.line(screen,(255,255,255),Calc.New_Pos((i -int(ScreenWidth / Space/2)) * Space , -ScreenHight / 2), Calc.New_Pos((i -int(ScreenWidth / Space/2)) * Space , ScreenHight / 2))
            
        for i in range (int(ScreenHight/Space) + 1):
            pygame.draw.line(screen,(255,255,255), Calc.New_Pos(-ScreenWidth / 2,(i -int(ScreenHight / Space/2))* Space),Calc.New_Pos(ScreenWidth / 2, (i -int(ScreenHight / Space/2)) * Space))
        pygame.draw.line(screen,(255,255,255),Calc.Set_Origin([0,0]),Calc.Set_Origin([0,30]),3)
        pygame.draw.line(screen,(255,255,255),Calc.Set_Origin([0,0]),Calc.Set_Origin([30,0]),3)

    def Cube_rot():
        global Angle
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
                pygame.draw.circle(screen, (255,255,255), Calc.New_Pos(int((Offset[0])), int((Offset[1]))), 10)
            


    
while GameRun:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
   
    KeyListener()
   
    if np.array_equal(s.Transform, s.TransformNew) == False:
        for zeile in range(2):
            for spalte in range(2): 
                print(s.Transform[zeile][spalte] )
                if s.TransformNew[zeile][spalte] > s.Transform[zeile][spalte]:
                    s.Transform[zeile][spalte] = s.Transform[zeile][spalte] + (s.TransformNew[zeile][spalte] - s.Transform[zeile][spalte]) * 0.05 
                   
                else:
                    s.Transform[zeile][spalte] = s.Transform[zeile][spalte] - (s.Transform[zeile][spalte] - s.TransformNew[zeile][spalte]) * 0.05 

    screen.fill([0,0,0])

    # Spielfeld/figuren zeichnen
    
    Draw.Cube_rot()
    Draw.Grid()
    pygame.draw.line(screen,(255,255,255),Calc.New_Pos(0,0),Calc.New_Pos(50,100),10)
    # Fenster aktualisieren
    pygame.display.flip() 
    # Refresh-Zeiten festlegen
    clock.tick(25)
   

pygame.quit()