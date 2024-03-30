# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:13:49 2024

@author: axeve

Alexis Evans
CS 120 
Prof Harris
Mar 29, 2024
Slide and Catch Game 

"""
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("cafe.png")
        self.sprites = []
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
