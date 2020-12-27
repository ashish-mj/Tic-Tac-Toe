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

first = pygame.draw.rect(window, white, (25,25,150,150))
second = pygame.draw.rect(window, white,(200,25,150,150))
third = pygame.draw.rect(window, white,(375,25,150,150))

forth = pygame.draw.rect(window, white,(25,200,150,150))
fifth = pygame.draw.rect(window, white,(200,200,150,150))
sixth = pygame.draw.rect(window, white,(375,200,150,150))

seventh = pygame.draw.rect(window, white,(25,375,150,150))
eight = pygame.draw.rect(window, white,(200,375,150,150))
nine = pygame.draw.rect(window, white,(375,375,150,150))


while True:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            
            if first.collidepoint(position):
                pygame.draw.rect(window,red,(50,50,100,100))
                
            if second.collidepoint(position):
                pygame.draw.rect(window,red,(225,50,100,100))
                
            if third.collidepoint(position):
                pygame.draw.rect(window,red,(400,50,100,100))
                
            if forth.collidepoint(position):
                pygame.draw.rect(window,red,(50,225,100,100))
                
            if fifth.collidepoint(position):
                pygame.draw.rect(window,red,(225,225,100,100))
                
            if sixth.collidepoint(position):
                pygame.draw.rect(window,red,(400,225,100,100))
                
            if seventh.collidepoint(position):
                pygame.draw.rect(window,red,(50,400,100,100))
                
            if eight.collidepoint(position):
                pygame.draw.rect(window,red,(225,400,100,100))
                
            if nine.collidepoint(position):
                pygame.draw.rect(window,red,(400,400,100,100))
            
            
    
    pygame.display.update()