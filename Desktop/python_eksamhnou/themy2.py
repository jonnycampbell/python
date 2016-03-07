#!/usr/bin/env python

import pygame,sys,random,time
from pygame.locals import *


class Chessboard:

    def __init__(self,surface):
        self.box = ["","","","","","","","",""]
        self.surface = surface

    def draw(self):
        x = y = 0
        for i in range(0,3):
            for j in range(0,3):
                pygame.draw.rect(self.surface,(255,255,255),Rect((x,y),(50,50)),1)
                x += 50
            x = 0
            y += 50
            
    def insert(self):
        width = {0:25,1:75,2:125,3:25,4:75,5:125,6:25,7:75,8:125}
        height = {0:25,1:25,2:25,3:75,4:75,5:75,6:125,7:125,8:125}
        for i in range(0,9):
            if self.box[i] == "X":
                pygame.draw.circle(self.surface,(0,0,255),(width[i],height[i]),10)
            if self.box[i] == "O":
                pygame.draw.circle(self.surface,(255,0,0),(width[i],height[i]),10)

    def move(self,x,y):
        if x > 0 and x < 50:
            if y > 0 and y < 50:
                if self.box[0] == "":
                    self.box[0] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[3] == "":
                    self.box[3] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[6] == "":
                    self.box[6] = "O"
                    return True
            return False

        elif x > 50 and x < 100:
            if y > 0 and y < 50:
                if self.box[1] == "":
                    self.box[1] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[4] == "":
                    self.box[4] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[7] == "":
                    self.box[7] = "O"
                    return True
            return False

        elif x > 100 and x < 150:
            if y > 0 and y < 50:
                if self.box[2] == "":
                    self.box[2] = "O"
                    return True
            elif y > 50 and y < 100:
                if self.box[5] == "":
                    self.box[5] = "O"
                    return True
            elif y > 100 and y < 150:
                if self.box[8] == "":
                    self.box[8] = "O"
                    return True
            return False
        
        return False
            
    def check(self):
        if self.box[0] == "X" and self.box[1] == "X" and self.box[2] == "X": return True,"C"
        elif self.box[3] == "X" and self.box[4] == "X" and self.box[5] == "X": return True,"C"
        elif self.box[6] == "X" and self.box[7] == "X" and self.box[8] == "X": return True,"C"

        elif self.box[0] == "X" and self.box[3] == "X" and self.box[6] == "X": return True,"C"
        elif self.box[1] == "X" and self.box[4] == "X" and self.box[7] == "X": return True,"C"
        elif self.box[2] == "X" and self.box[5] == "X" and self.box[8] == "X": return True,"C"

        elif self.box[0] == "X" and self.box[4] == "X" and self.box[8] == "X": return True,"C"
        elif self.box[6] == "X" and self.box[4] == "X" and self.box[2] == "X": return True,"C"


        if self.box[0] == "O" and self.box[1] == "O" and self.box[2] == "O": return True,"P"
        elif self.box[3] == "O" and self.box[4] == "O" and self.box[5] == "O": return True,"P"
        elif self.box[6] == "O" and self.box[7] == "O" and self.box[8] == "O": return True,"P"

        elif self.box[0] == "O" and self.box[3] == "O" and self.box[6] == "O": return True,"P"
        elif self.box[1] == "O" and self.box[4] == "O" and self.box[7] == "O": return True,"P"
        elif self.box[2] == "O" and self.box[5] == "O" and self.box[8] == "O": return True,"P"
        
        elif self.box[0] == "O" and self.box[4] == "O" and self.box[8] == "O": return True,"P"
        elif self.box[6] == "O" and self.box[4] == "O" and self.box[2] == "O": return True,"P"

        return False,"N"

class Machine:

    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.move = None

    def attack(self):
        self.checktris("X")

    def defend(self):
        self.checktris("O")

    def do(self):
        if self.move == None: self.randomove()
        elif self.chessboard.box[self.move] != "": self.randomove()
        else: self.chessboard.box[self.move] = "X"
        self.move = None

    def randomove(self):
        while 1:
            move = random.randint(0,8)
            if self.chessboard.box[move] == "":
                self.chessboard.box[move] = "X"
                break        

    def checktris(self,simbol):
        if self.chessboard.box[0] == simbol and self.chessboard.box[1] == simbol and self.chessboard.box[2] == "": self.move = 2
        elif self.chessboard.box[0] == simbol and self.chessboard.box[1] == "" and self.chessboard.box[2] == simbol: self.move = 1
        elif self.chessboard.box[0] == "" and self.chessboard.box[1] == simbol and self.chessboard.box[2] == simbol: self.move = 0

        if self.chessboard.box[3] == simbol and self.chessboard.box[4] == simbol and self.chessboard.box[5] == "": self.move = 5
        elif self.chessboard.box[3] == simbol and self.chessboard.box[4] == "" and self.chessboard.box[5] == simbol: self.move = 4
        elif self.chessboard.box[3] == "" and self.chessboard.box[4] == simbol and self.chessboard.box[5] == simbol: self.move = 3

        if self.chessboard.box[6] == simbol and self.chessboard.box[7] == simbol and self.chessboard.box[8] == "": self.move = 8
        elif self.chessboard.box[6] == simbol and self.chessboard.box[7] == "" and self.chessboard.box[8] == simbol: self.move = 7
        elif self.chessboard.box[6] == "" and self.chessboard.box[7] == simbol and self.chessboard.box[8] == simbol: self.move = 6
        
        if self.chessboard.box[0] == simbol and self.chessboard.box[3] == simbol and self.chessboard.box[6] == "": self.move = 6
        elif self.chessboard.box[0] == simbol and self.chessboard.box[3] == "" and self.chessboard.box[6] == simbol: self.move = 3
        elif self.chessboard.box[0] == "" and self.chessboard.box[3] == simbol and self.chessboard.box[6] == simbol: self.move = 0

        if self.chessboard.box[1] == simbol and self.chessboard.box[4] == simbol and self.chessboard.box[7] == "": self.move = 7
        elif self.chessboard.box[1] == simbol and self.chessboard.box[4] == "" and self.chessboard.box[7] == simbol: self.move = 4
        elif self.chessboard.box[1] == "" and self.chessboard.box[4] == simbol and self.chessboard.box[7] == simbol: self.move = 1

        if self.chessboard.box[2] == simbol and self.chessboard.box[5] == simbol and self.chessboard.box[8] == "": self.move = 8
        elif self.chessboard.box[2] == simbol and self.chessboard.box[5] == "" and self.chessboard.box[8] == simbol: self.move = 5
        elif self.chessboard.box[2] == "" and self.chessboard.box[5] == simbol and self.chessboard.box[8] == simbol: self.move = 2

        if self.chessboard.box[0] == simbol and self.chessboard.box[4] == simbol and self.chessboard.box[8] == "": self.move = 8
        elif self.chessboard.box[0] == simbol and self.chessboard.box[4] == "" and self.chessboard.box[8] == simbol: self.move = 4
        elif self.chessboard.box[0] == "" and self.chessboard.box[4] == simbol and self.chessboard.box[8] == simbol: self.move = 0

        if self.chessboard.box[2] == simbol and self.chessboard.box[4] == simbol and self.chessboard.box[6] == "": self.move = 6
        elif self.chessboard.box[2] == simbol and self.chessboard.box[4] == "" and self.chessboard.box[6] == simbol: self.move = 4
        elif self.chessboard.box[2] == "" and self.chessboard.box[4] == simbol and self.chessboard.box[6] == simbol: self.move = 2
    
def run(computer,chessboard,screen):
    win = False
    player = True
    winner = ""

    while win is not True:

        ok = False

        screen.fill((0,0,0))
        chessboard.draw()
        chessboard.insert()

        if player is not True:
            computer.attack()
            if computer.move == None:
                computer.defend()
                computer.do()
            else: computer.do()        
            player = True
    
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player:
                        if chessboard.move(event.pos[0],event.pos[1]):
                            player = False
        
        for i in chessboard.box: 
            if  i == "":
                ok = True
                break 
          
        win,winner = chessboard.check()

        if ok == False: 
            win = True
            winner = "N"
    
        pygame.display.update()
    return winner	


pygame.init()
screen = pygame.display.set_mode((150,150))
pygame.display.set_caption("Tris")
font = pygame.font.SysFont("arial",30)

while 1:
    chessboard = Chessboard(screen)
    computer = Machine(chessboard)
    Winner = run(computer,chessboard,screen)

    if Winner == "C":
	screen.fill((255,255,255))
	text = font.render("Hai perso!!!",True,(0,0,0))
	screen.blit(text,(37,37+font.get_linesize()))
	pygame.display.update()
    elif Winner == "P":
	screen.fill((255,255,255))
	text = font.render("Hai vinto!!!",True,(0,0,0))
	screen.blit(text,(37,37+font.get_linesize()))
	pygame.display.update()
    elif Winner == "N":
	screen.fill((255,255,255))
	text = font.render("Pareggio...",True,(0,0,0))
	screen.blit(text,(37,37+font.get_linesize()))
	pygame.display.update()

    time.sleep(3)
