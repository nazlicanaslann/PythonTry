# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:33:37 2022

@author: spoiltheart
"""
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black') #background color
t.speed(0) #speed
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1) #Circle with left side
    t.fd(1)
    for j in range (2):
        t.left(2) #Circle with left side
        t.circle(100) 
        #endless circle