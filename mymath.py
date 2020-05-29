#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:21:36 2019

@author: aanchalnarendran
"""

def circlecirc(r):
    circum= 2*3.14*r
    return circum
def circlearea(r):
    a=3.14*(r**2)
    return a
def squarearea(a):
    area=a*a
    return area
def squareper(a):
    per=4*a
    return per
def rectarea(l,b):
    area=l*b
    return area
def rectperm(l,b):
    per=2*(l+b)
    return per
def spherev(r):
    v=(4*3.14*(r**3))/4
    return v
def spheresa(r):
    sa=4*3.14*(r**2)
    return sa
def cubevol(a):
    v=a**3
    return v
def cubesa(a):
    v=6*(a**2)
    return v
def cuboidsa(a,b,c):
    sa=2*(a*b + b*c + a*c)
    return sa
def cuboidvol(a,b):
    v=a*a*b
    return v
def cylinderv(r,h):
    v=3.14*(r**2)*h
    return v
def cylindersa(r,h):
    sa=3.14*(r**2)+ 3.14*r*((r**2 + h**2)**0.5)
    return sa
def conesa(r,s):
    sa=3.14*(r**2)+3.14*r*s
    return sa
def conevol(r,s):
    v= (3.14*(r**2)*s)/3
    return v
def pyramidarea(b,h,s):
    sa=2*b*s + b**2
    return sa
def pyramidvolume(b,h):
    v=((b**2)*h)/3
    return v
def prismsa(b,h,l,s):
    sa= b*h + 2*l*s + l*b
    return sa
def prismvol(b,h,l):
    vol=b*h*l
    return vol
def main():
    print("welcome to my math module")
    print("For circle related computation,enter1")
    print("For square related computation,enter2")
    print("For rectangle related computation,enter3")
    print("For sphere related computation,enter4")
    print("For cube related computation,enter5")
    print("For cuboid related computation,enter6")
    print("For cylinder related computation,enter7")
    print("For cone related computation,enter8")
    print("for pyramid related computation,enter9")
    print("for prism related computation,enter10")
    n=int(input("enter your choice"))
    if n==1:
        r=int(input("enter the radius"))
        print("to compute cicrcumference,enter1")
        print("to compute area, print2")
        e=int(input("enter your choice"))
        if e==1:
            print("circumference is",circlecirc(r))
        elif e==2:
            print("area is",circlearea(r))
        else:
            print("wrong option")
    elif n==2:
        r=int(input("enter the side"))
        print("to compute perimeter,enter 1" )
        print("to compute area,enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("perimeter is",squareper(r))
        elif e==2:
            print("area is",squarearea(r))
        else:
            print("wrong option")
    elif n==3:
        l=int(input("enter the length"))
        b=int(input("enter the breadth"))
        print("to compute perimeter, enter1")
        print("to compute area, enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("perimeter is",rectperm(l,b))
        elif e==2:
            print("area is", rectarea(l,b))
        else:
            print("wrong option")
    elif n==4:
        r=int(input("enter radius"))
        print("for computation of area, enter1")
        print("for computation of area, enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("the area is",spheresa(r))
        elif e==2:
            print("the volume is",spherev(r))
        else:
            print("wrong choice")
    elif n==5:
        a=int(input("enter the side"))
        print("to compute surface area, enter 1")
        print("to compute volume,enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("the surface area of cube",cubesa(a))
        elif e==2:
            print("the volume is",cubevol(a))
        else:
            print("wrong choice")
    elif n==6:
        l=int(input("enter the length"))
        b=int(input("enter the breadth"))
        h=int(input("enter the height"))
        print("to compute surface area,enter 1")
        print("to compute volume, enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("the surface area is", cuboidsa(l,b,h))
        elif e==2:
            print("the volume is",cuboidvol(l,b,h))
        else:
            print("wrong choice")
    elif n==7:
        r=int(input("enter radius"))
        h=int(input("enter height"))
        print("to compute surface area,enter 1")
        print("to compute volume, enter2")
        e=int(input("enter your choice"))
        if e==1:
            print("surface area is",cylindersa(r,h))
        elif e==2:
            print("volume is",cylinderv(r,h))
        else:
            print("wrong choice")
    elif n==8:
        r=int(input("enter the radius"))
        s=int(input("enter the side"))
        print("to compute surface area,enter1")
        print("to compute volume,enter2")
        e=int(input("enter your choice"))
        if e==1:
            print("the surface area is",conevol(r,s))
        elif e==2:
            print("the volume is",conevol(r,s))
        else:
            print("wrong choice")
    elif n==9:
        b=int(input("enter base"))
        h=int(input("enter height"))
        s=int(input("enter side"))
        print("top compute surface area,enter 1")
        print("to compute volume,enter2")
        e=int(input("enter your choice"))
        if e==1:
            print("surface area is",pyramidarea(b,h,s))
        elif e==2:
            print("volume is",pyramidvolume(b,h))
        else:
            print("wrong choice")
    elif n==10:
        b=int(input("enter the base"))
        h=int(input("enter the height"))
        l=int(input("enter the length"))
        s=int(input("enter the side"))
        print("to compute surface area,enter1")
        print("to compute volume,enter 2")
        e=int(input("enter your choice"))
        if e==1:
            print("the surface area is", prismsa(b,h,l,s))
        elif e==2:
            print("the volume is",prismvol(b,h,l))
        else:
            print("wrong option")
    else:
        print("wrong option")
main()

        