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

first = pygame.Rect(25,25,150,150)
second = pygame.Rect(200,25,150,150)
third = pygame.Rect(375,25,150,150)

forth = pygame.Rect(25,200,150,150)
fifth = pygame.Rect(200,200,150,150)
sixth = pygame.Rect(375,200,150,150)

seventh = pygame.Rect(25,375,150,150)
eight = pygame.Rect(200,375,150,150)
nine = pygame.Rect(375,375,150,150)

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(window,white,first)
    pygame.draw.rect(window,white,second)
    pygame.draw.rect(window,white,third)
    
    pygame.draw.rect(window,white,forth)
    pygame.draw.rect(window,white,fifth)
    pygame.draw.rect(window,white,sixth)
    
    pygame.draw.rect(window,white,seventh)
    pygame.draw.rect(window,white,eight)
    pygame.draw.rect(window,white,nine)
    
    
    pygame.display.flip()