import pygame
import time
from Tile import *
from Player import *
from Button import *


pygame.init()

# surface_sz = width = height = 480   # Desired physical surface size, in pixels.
width = 1280
height = 720
size = width, height
screen = pygame.display.set_mode(size)
mouse = pygame.mouse.get_pos()
numberOfPlayers = 0

# Scherm opdelen in 16 stukken
if not width == height:
    offset = (width-height)/2
else:
    offset = 0
unit = int(height/16)

#Background 1
unscaled_bg = pygame.image.load("assets\\title3.png")
bg = pygame.transform.scale(unscaled_bg,size)

#Background 2
unscaled_bg2 = pygame.image.load("assets\\title2.png")
bg2 = pygame.transform.scale(unscaled_bg2,size)

# A color is a mix of (Red, Green, Blue)
# <color> = (r, g, b)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (100,100,100)
LIGHTGRAY = (200,200,200)
RED = (200,80,80)
BRIGHTRED = (255,0,0)
GREEN = (80,200,80)
BRIGHTGREEN = (0,255,0)
BLUE = (80,80,200)
YELLOW = (200,200,80)
PINK = (200,100,100)
BRIGHTBLUE = (51,153,255)

# Doorloopbare lijst aan kleuren voor spelerTiles en normale Tiles
PlayerColors = [RED,GREEN,BLUE,YELLOW]
TileColors = [LIGHTGRAY,GRAY]

# Spelerplaatjes in doorloopbare lijst
pimg = player_images = [
        pygame.transform.scale(pygame.image.load("assets\\player1.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player4.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player2.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player3.png"),(int(unit/2), int(unit/2)))
        ]


# Alle Buttons:
# TITLE SCREEN
#Start
button1 = Button("START!", GREEN, (180, 300, 250, 75),((180+125), (300+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 300, 250, 75), ((850+125), (300+(75/2))))

#Instructions
button12 = Button("INSTRUCTIONS", PINK,(490, 300, 300, 75), ((490+150), (300+(75/2)))) #changed size

#Player amount selection screen
#1 Player
button3 = Button("1 PLAYER", WHITE, (180, 250, 250, 75),((180+125), (250+(75/2))))

#2 Players
button4 = Button("2 PLAYERS", WHITE, (515, 250, 250, 75),((515+125), (250+(75/2))))

#3 Players
button5 = Button("3 PLAYERS", WHITE, (850, 250, 250, 75),((850+125), (250+(75/2))))

#4 Players
button6 = Button("4 PLAYERS", WHITE, (515, 350, 250, 75), ((515+125), (350+(75/2))))

# GAME SCREEN
# Exitbutton game
button7 = Button("EXIT", RED,(1020, 640, 250, 75), ((1020+125), (640+(75/2))))

# Roll dice
button8 = Button("Roll Dice", BLUE,(10,640,250,75),((10+125),(640+(75/2))))

# Pop-up screen
button9 = Button("Are you sure you want to quit?", WHITE, (340, 235, 600, 250), ((340+300), (150+125)))

# Keep playing
button10 = Button("Keep playing", GREEN,(350,425,250,50),((350+125),(425+25)))

# Exit anyway
button11 = Button("Quit", RED,(680,425,250,50),((680+125),(425+25)))

#instructionscreen
#start
button13 = Button("START!", GREEN, (180, 550, 250, 75),((180+125), (550+(75/2))))

#back
button14 = Button("BACK", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))



def build_board():
    board = []
    startTiles = []
    pc = 0
    tc = 1
    for j in range(16):
        for i in range(16):
            if (j == 0 and i == 0) or (j == 0 and i == 14) or (j == 14 and i == 0) or (j == 14 and i == 14):
              board.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
              startTiles.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
              pc += 1
            elif (j == 1 and i == 7) or (j == 14 and i == 7):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,0))
            elif (j == 7 and i == 1) or (j == 7 and i == 14):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,1))
            elif j == 1:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                tc += 1
            elif j == 14:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
            elif i == 1:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
            elif i == 14:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
    return board, startTiles

def playerInit(humans,startTiles,names = None): #give names as a list, in order of players
    players = []
    pnr = 0
    if names is None:
        while pnr < 4:
            if pnr < humans:
                players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],True,"Human Player %s" % (pnr+1)))
            else:
                players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],False,"CPU Player %s" % (pnr+1)))
            pnr += 1
    return players


def findNewTile(current,board,n):
    X1 = current.Position.X - 1
    Y1 = current.Position.Y - 1
    if n < 0:
        if Y1 == 0:
            if X1+n <= 0:
                X2 = 0
                Y2 = 0 - (n + X1)
            else:
                X2 = X1+n
                Y2 = Y1
        elif Y1 == 13:
            if X1-n >= 13:
                X2 = 13
                Y2 = 13 - (n-(X1-13))
            else:
                X2 = X1-n
                Y2 = Y1
        if 0<Y1<13:
            if X1 == 0:
                if Y1+n >= 13:
                    Y2 = 13
                    X2 = n - (13-Y1)
                else:
                    Y2 = Y1+n
                    X2 = X1
            elif X1 == 13:
                if Y1-n <= 0:
                    Y2 = 0
                    X2 = 13 - (n - Y1)
                else:
                    Y2 = Y1-n
                    X2 = X1

    elif n > 0:
        if Y1 == 0:
            if X1+n >= 13:
                X2 = 13
                Y2 = n - (13- X1)
            else:
                X2 = X1+n
                Y2 = Y1
        elif Y1 == 13:
            if X1-n <= 0:
                X2 = 0
                Y2 = 13 - (n-X1)
            else:
                X2 = X1-n
                Y2 = Y1
        if 0<Y1<13:
            if X1 == 0:
                if Y1-n <= 0:
                    Y2 = 0
                    X2 = n-Y1
                else:
                    Y2 = Y1-n
                    X2 = X1
            elif X1 == 13:
                if Y1+n >= 13:
                    Y2 = 13
                    X2 = 13 - (n - (13-Y1))
                else:
                    Y2 = Y1+n
                    X2 = X1
    else: # if user somehow gets a 0 roll
        X2,Y2 = X1,Y1
    if X2 != 7:
        X2 += 1
    if Y2 != 7:
        Y2 += 1
    for tile in board:
        if tile.Position.X == X2 and tile.Position.Y == Y2:
            return tile


def switchScreen(screen,optionalArg = None):
    if optionalArg is None:
        screen.run()
    else:
        screen.run(optionalArg)