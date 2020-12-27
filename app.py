#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:50:04 2020

@author: ashish
"""

import pygame,sys

pygame.init()

window = pygame.display.set_mode((550,550))
pygame.display.set_caption('Tic-Tac-Toe')

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

first = pygame.draw.rect(window, white, (25,25,150,150))
second = pygame.draw.rect(window, white,(200,25,150,150))
third = pygame.draw.rect(window, white,(375,25,150,150))

forth = pygame.draw.rect(window, white,(25,200,150,150))
fifth = pygame.draw.rect(window, white,(200,200,150,150))
sixth = pygame.draw.rect(window, white,(375,200,150,150))

seventh = pygame.draw.rect(window, white,(25,375,150,150))
eight = pygame.draw.rect(window, white,(200,375,150,150))
nine = pygame.draw.rect(window, white,(375,375,150,150))


player_turn = 'rect'

while True:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            
            if first.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(50,50,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(100,100),50)
                    player_turn="rect"
                
            if second.collidepoint(position):
                 if player_turn=="rect":
                     pygame.draw.rect(window,red,(225,50,100,100))
                     player_turn="circle"
                 else:
                     pygame.draw.circle(window,green,(275,100),50)
                     player_turn="rect"
                     
            if third.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(400,50,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(450,100),50)
                    player_turn="rect"
                    
            if forth.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(50,225,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(100,275),50)
                    player_turn="rect"
                    
            if fifth.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(225,225,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(275,275),50)
                    player_turn="rect"
                    
            if sixth.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(400,225,100,100))
                    player_turn="circle"
                else:
                     pygame.draw.circle(window,green,(450,275),50)
                     player_turn="rect"
                     
            if seventh.collidepoint(position):
                 if player_turn=="rect":
                     pygame.draw.rect(window,red,(50,400,100,100))
                     player_turn="circle"
                 else:
                     pygame.draw.circle(window,green,(100,450),50)
                     player_turn="rect"
                
            if eight.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(225,400,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(275,450),50)
                    player_turn="rect"
                    
            if nine.collidepoint(position):
                if player_turn=="rect":
                    pygame.draw.rect(window,red,(400,400,100,100))
                    player_turn="circle"
                else:
                    pygame.draw.circle(window,green,(450,450),50)
                    player_turn="rect"
            
    
    pygame.display.update()