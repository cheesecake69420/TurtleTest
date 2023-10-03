"""
    Author: Joshua Sucala 
    Date:   10/2/2023
    Class:  MCSCI-270
    Desc:   Program for drawing lines & circles utilizing the turtle library!
"""

import turtle
import math
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    length = (2 * math.pi * r) / 360
    for i in range(360):
        t.fd(length)
        t.lt(1)

def arc(t,angle):
    length = (2 * math.pi * 50) / 360
    for i in range(angle):
        t.fd(length)
        t.lt(1)

arc(bob,90)

turtle.mainloop()
