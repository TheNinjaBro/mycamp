#!/usr/bin/env python3

"""
File: rps.py
Name:Donovan Coen

A rock-paper-scissors game against the CPU
Concepts covered: Random, IO, if/else, printing
"""

import random
import sys

def greeting(): 
    print ("Welcome to Rock Paper Sisors!")
    print ("You will play Rock, Paper, Sisors against a CPU opponent")

def main():
    p1 = (input("Pick Rock, Paper, or Sisors by typing r/p/s: "))
    print (p1)
    
    ai_guess()
    
        
def ai_guess():
    
    random = random.randint(1,3)

    if (random == 1):
        p2 = r
    if (random == 2):
        p2 = p
    if (random == 3):
        p2 = s
    
    checkWin(p1, p2)

    

def checkWin(p1, p2):
    if (p1 == p2):
        print ("Draw. You and the CPU picked the same answer")
        print (" The game will automaticly restart in 3 seconds")
        time.sleep(3)
        main()
    
    
        
    
   
if __name__ == "__main__":
    greeting()
    main()
    
