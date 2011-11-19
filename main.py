#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import random
import os

class PuyoGame(object):
    MAX_COLOMN = 13
    MAX_RAW = 6
    MAX_COLORS = 5

    def __init__(self):
        self.GameField = [[0 for i in xrange(self.MAX_RAW)] for j in xrange(self.MAX_COLOMN)]
        self.mainPuyo = {"x":self.MAX_RAW/2-1 ,"y":0 ,"color":random.randint(1 ,self.MAX_COLORS)}
        self.subPuyo = {"x":self.MAX_RAW/2 ,"y":0 ,"color":random.randint(1 ,self.MAX_COLORS)}
        self.onPuyo = 1 #onPuyo parameter mods meens; 0:top ,1:right ,2:bellow ,3:left
        self.chaining = False

    def move(self ,dx):
        """
        move main and sub Puyos to dx
        if it isn't moveable area,return false
        """
        if self.mainPuyo == None:
            return False
        if self.is_moveable(self.mainPuyo["x"]+dx ,self.mainPuyo["y"]) and \
           self.is_moveable(self.subPuyo["x"]+dx ,self.subPuyo["y"]):
            self.mainPuyo["x"] += dx
            self.subPuyo["x"] += dx
            return True
        else:
            return False


    def turn(self ,left=False):
        """
        turn Puyo couple;change subPuyo possision
        if left arg is True ,turnig left
        default setting is turnig right
        """
        if self.mainPuyo == None:
            return False
        if self.onPuyo%4 == 0:
            if left:
                if self.is_moveable(self.mainPuyo["x"]-1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]-1
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.onPuyo -= 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"]+1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["x"] +=1
                    self.onPuyo -= 1
                    return True
                else:
                    return False
            else:
                if self.is_moveable(self.mainPuyo["x"]+1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]+1
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.onPuyo += 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"]-1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["x"] -=1
                    self.onPuyo += 1
                    return True
                else:
                    return False
        elif self.onPuyo%4 == 1:
            if left:
                if self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]-1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]-1
                    self.onPuyo -= 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]+1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["y"] -=1
                    self.onPuyo -= 1
                    return True
                else:
                    return False
            else:
                if self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]+1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]+1
                    self.onPuyo += 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]-1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["y"] -=1
                    self.onPuyo += 1
                    return True
                else:
                    return False
        elif self.onPuyo%4 == 2:
            if left:
                if self.is_moveable(self.mainPuyo["x"]+1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]+1
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.onPuyo -= 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"]-1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["x"] -=1
                    self.onPuyo -= 1
                    return True
                else:
                    return False
            else:
                if self.is_moveable(self.mainPuyo["x"]-1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]-1
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.onPuyo += 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"]+1 ,self.mainPuyo["y"]):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["x"] +=1
                    self.onPuyo += 1
                    return True
                else:
                    return False
        else:
            if left:
                if self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]+1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]+1
                    self.onPuyo -= 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]-1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["y"] -=1
                    self.onPuyo -= 1
                    return True
                else:
                    return False
            else:
                if self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]-1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]-1
                    self.onPuyo += 1
                    return True
                elif self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]+1):
                    self.subPuyo["x"] = self.mainPuyo["x"]
                    self.subPuyo["y"] = self.mainPuyo["y"]
                    self.mainPuyo["y"] +=1
                    self.onPuyo += 1
                    return True
                else:
                    return False

    def check_chain(self):
        """
        if 4 Puyos are combined,remove their from GameField
        and return True else False
        """
        def inner_cc(x ,y ,checked=set()):
            if len(checked) == 0:
                return inner_cc(x ,y ,set([(x ,y)]))
            else:
                if x == 0:
                    raws = [x ,x+1]
                elif x == self.MAX_RAW-1:
                    raws = [x-1 ,x]
                else:
                    raws = [x-1 ,x ,x+1]
                if y == 0:
                    colomns = [y ,y+1]
                elif y == self.MAX_COLOMN-1:
                    colomns = [y-1 ,y]
                else:
                    colomns = [y-1 ,y ,y+1]
                chain_poses = set([(i ,j) for i in raws for j in colomns if self.GameField[y][x] == self.GameField[j][i] and abs(i-x+j-y)==1])
                if chain_poses.issubset(checked):
                    return checked
                checked.update(chain_poses)
                [inner_cc(psx ,psy ,checked) for psx ,psy in chain_poses]
                return checked
        chained = False
        for y in xrange(len(self.GameField)):
            for x in xrange(len(self.GameField[y])):
                if self.GameField[y][x] == 0:
                    continue
                combs = inner_cc(x ,y)
                if len(combs) >= 4:
                    for rx ,ry in combs:
                        self.GameField[ry][rx] = 0
                    chained = True
        return chained

    def drop(self):
        """
        if you call this method,drop Puyos that is possible to drop on field
        if no Puyos are dropped,this method return False
        """
        dropped = False
        for y in xrange(self.MAX_COLOMN):
            for x in xrange(self.MAX_RAW):
                if self.GameField[y][x] == 0:
                    continue
                if self.is_moveable(x ,y+1):
                    self.GameField[y+1][x] = self.GameField[y][x]
                    self.GameField[y][x] = 0
                    dropped = True
        if dropped:
            self.drop()
        return dropped

    def next(self):
        """
        this method will progress game
        """
        if not self.chaining:
            if self.mainPuyo == None:
                self.mainPuyo = {"x":self.MAX_RAW/2-1 ,"y":0 ,"color":random.randint(1 ,self.MAX_COLORS)}
                self.subPuyo = {"x":self.MAX_RAW/2 ,"y":0 ,"color":random.randint(1 ,self.MAX_COLORS)}
                self.onPuyo = 1
                return 0
            elif self.is_moveable(self.mainPuyo["x"] ,self.mainPuyo["y"]+1) and \
               self.is_moveable(self.subPuyo["x"] ,self.subPuyo["y"]+1):
                self.mainPuyo["y"] += 1
                self.subPuyo["y"] += 1
                return -1
            else:
                self.GameField[self.mainPuyo["y"]][self.mainPuyo["x"]] = self.mainPuyo["color"]
                self.GameField[self.subPuyo["y"]][self.subPuyo["x"]] = self.subPuyo["color"]
                self.mainPuyo = self.subPuyo = None
                if self.drop():
                    self.chaining = True
                    return 0
                if self.check_chain():
                    self.chaining = True
                else:
                    self.chaining = False
                if self.GameField[0][self.MAX_RAW/2-1] != 0 or self.GameField[0][self.MAX_RAW/2] != 0:
                       return -2
        else:
            if self.drop():
                return
            if self.check_chain():
                self.chaining = True
            else:
                self.chaining = False
                if self.GameField[0][self.MAX_RAW/2-1] != 0 or self.GameField[0][self.MAX_RAW/2] != 0:
                    return -2
        return 0


    def is_moveable(self ,x ,y):
        """
        return arg's possision is moveable or not
        """
        if (0 <= x < self.MAX_RAW) and (0 <= y < self.MAX_COLOMN) and (self.GameField[y][x] == 0):
            return True
        else:
            return False

def LoadImage(name):
    """
    load image from file name and change sxale
    """
    path = os.path.join("img" ,name)
    image = pygame.image.load(path).convert_alpha()
    rect = image.get_rect()
    image = pygame.transform.scale(image ,(32 ,32))
    return image

def main():
    pygame.init()
    screen = pygame.display.set_mode((6*32 ,13*32))
    pygame.display.set_caption("Puyo2")
    clock = pygame.time.Clock()
    spend_time = 0
    puyo2 = PuyoGame()
    colors = {1:LoadImage("b.gif") ,2:LoadImage("g.gif") ,3:LoadImage("r.gif")
              ,4:LoadImage("y.gif") ,5:LoadImage("p.gif") ,6:LoadImage("e.gif")}
    while 1:
        clock.tick(60)
        spend_time += 1
        if spend_time%60 == 0 or (spend_time%30 == 0 and puyo2.chaining):
            puyo2.next()
         screen.fill((0 ,0 ,0))
        for y in xrange(len(puyo2.GameField)):
            for x in xrange(len(puyo2.GameField[y])):
                if puyo2.GameField[y][x] != 0:
                    screen.blit(colors[puyo2.GameField[y][x]] ,(x*32 ,y*32))
        if puyo2.mainPuyo != None:
            screen.blit(colors[puyo2.mainPuyo["color"]] ,(puyo2.mainPuyo["x"]*32 ,puyo2.mainPuyo["y"]*32))
            screen.blit(colors[puyo2.subPuyo["color"]] ,(puyo2.subPuyo["x"]*32 ,puyo2.subPuyo["y"]*32))
        pygame.display.flip()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_DOWN] and spend_time%6 == 0 and not puyo2.chaining:
            puyo2.next()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_LEFT:
                    puyo2.move(-1)
                if event.key == K_RIGHT:
                    puyo2.move(1)
                if event.key == K_UP:
                    puyo2.turn()
                if event.key == K_z:
                    puyo2.turn(left = True)
                if event.key == K_x:
                    puyo2.turn()

if __name__  == '__main__':
    main()
