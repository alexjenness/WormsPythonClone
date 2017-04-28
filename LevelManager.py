# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:11:44 2017

@author: rlwar
"""
import pygame
import Globals

from map import *
from vec2d import Vec2d
from Hud import Hud
from Camera import Camera
from player import Player

class LevelManager:
    
    entities = []
    mapSize = Vec2d(800,600)
    players = []
    turnPlayer = 0
    
    def __init__(self, window):
        self.level = None
        self.window = window
        self.windowWidth = 400
        self.windowHeight = 400
        self.camera = Camera(Vec2d(self.windowWidth,self.windowHeight))
        self.background = None 
        self.entitySurface = None 
        self.hudSurface = pygame.Surface((self.windowWidth, self.windowHeight), pygame.SRCALPHA)
        self.hud = Hud(self)
        
    def loadLevel(self, level):
        self.entities = []
        self.level = level
        if level == 1:
            self.loadedMap = Map1(self)
            
        self.background = pygame.Surface((self.loadedMap.width, self.loadedMap.height))
        self.background.fill((200,200,200,255))
        self.entitySurface = pygame.Surface((self.loadedMap.width, self.loadedMap.height), pygame.SRCALPHA)
        
    def addPlayer(self):
        player = Player(self, len(self.players))
        self.players.append(player)
        self.entities.append(player)
        
    def addEntity(self, ent):
        self.entities.append(ent)
        
    def playerTurnStart(self, index):
        self.turnPlayer = index
        self.camera.setFollowObject(self.players[self.turnPlayer])
        
    def removeEntity(self, ent):
        self.entities.remove(ent)
        
    def processEvent(self, event):
        if event == Globals.PLAYER_LEFT:
            self.players[self.turnPlayer].moveLeft()
        elif event == Globals.PLAYER_RIGHT:
            self.players[self.turnPlayer].moveRight()
        elif event == Globals.PLAYER_STOP:
            self.players[self.turnPlayer].stop()
        elif event == Globals.TALL_JUMP:
            self.players[self.turnPlayer].tallJump()
        elif event == Globals.LONG_JUMP:
            self.players[self.turnPlayer].longJump()
            
    def update(self, dT):
        if self.loadedMap == None:
            return
        
        self.hud.update(dT)
        
        for ent in self.entities:
            ent.update(dT)
            
        self.camera.update()
        
    def draw(self, drawTarget, dT):
        drawTarget.blit(self.background, (0,0))
        
        self.entitySurface.fill((0,0,0,0))
        self.loadedMap.draw(self.entitySurface)
        for ent in self.entities:
            ent.draw(self.entitySurface, dT)
        drawTarget.blit(self.entitySurface, (-self.camera.pos.x,-self.camera.pos.y))
        
        self.hudSurface.fill((0,0,0,0))
        
        self.hud.draw(self.hudSurface, dT)
        drawTarget.blit(self.hudSurface, (0,0))
        
        pygame.display.flip()
        
        
    def setWindowSize(self, width, height):
        self.windowWidth = width
        self.windowHeight = height
        self.camera.setSize(Vec2d(width, height))
        self.background = pygame.transform.scale(self.background, (self.windowWidth, self.windowHeight))
        self.entitySurface = pygame.transform.scale(self.entitySurface, (self.windowWidth, self.windowHeight))
        self.hudSurface = pygame.transform.scale(self.hudSurface, (self.windowWidth, self.windowHeight))
    