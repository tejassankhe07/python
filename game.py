# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:55:13 2018

@author: tejas sankhe
"""
import random

#player choice 
print ("palyer choice 1:rock 2:paper 3:scissor")
playerchoice= raw_input ("Enter player choice")
print "player choice :  " + playerchoice
playerchoice=playerchoice.lower()





#select random choice for cpu
cpuoption= ['rock','paper','scissor']
cpuchoice= random.choice(cpuoption)
print "computer choice "+ cpuchoice

#game alogrithm 
if cpuchoice==playerchoice:
    print "Game is Tie"
    quit()
if playerchoice == cpuoption[0]:
    if cpuchoice == cpuoption[2]:
        print("Palyer win")
    else:
        print("cpu win")
elif playerchoice == cpuoption[1]:
    if cpuchoice == cpuoption[0]:
        print("Palyer win")
    else:
        print("cpu win")
elif playerchoice == cpuoption[2]:
    if cpuchoice == cpuoption[1]:
        print("Palyer win")
    else:
        print("cpu win")
