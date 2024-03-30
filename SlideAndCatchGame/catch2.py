# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:38:41 2024

@author: axeve
"""

import pygame, simpleGE

class Cup(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cup.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init()
        self.setImage("cafe.png")
        self.cup = Cup(self)
        self.sprites = [self.cup]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    