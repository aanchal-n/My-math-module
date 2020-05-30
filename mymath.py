#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:21:36 2019

@author: aanchalnarendran
"""

def circle_circumference_calc(radius):
    circumference = 2*3.14*r
    return circumference
    
def circle_area_calc(radius):
    area = 3.14*(radius**2)
    return area
    
def square_area_calc(side):
    area = side*side
    return area
    
def square_perimeter_calc(side):
    perimeter = 4*side
    return per
    
def rectangle_area_calc(length,breadth):
    area = length*breadth
    return area
    
def rectangle_perimeter(length,breadth):
    perimeter = 2*(length+breadth)
    return perimeter
    
def sphere_volume(radius):
    volume = (4*3.14*(radius**3))/4
    return volume
    
def sphere_surface_area(radius):
    surface_area = 4*3.14*(radius**2)
    return surface_area
    
def cube_volume(side):
    volume = side**3
    return volume
    
def cube_surface_area(side):
    surface_area = 6*(side**2)
    return surface_area
    
def cuboid_surface_area(length,breadth,height):
    surafce_area = 2*(length*breadth + breadth*height + length*height)
    return surface_area
    
def cuboid_volume(length,breadth,height):
    volume = length*breadth*height
    return volume
    
def cylinder_volume(radius,height):
    volume = 3.14*(radius**2)*height
    return volume
    
def cylinder_surface_area(radius,height):
    surface_area = 2*3.14*(radius**2)+ 3.14*radius*((radius**2 + height**2)**0.5)
    return surface_area
    
def cone_surface_area(radius,slant_height):
    surface_area = 3.14*(radius**2)+3.14*radius*((radius**2 + height**2)**0.5)
    return surface_area
    
def cone_volume(radius,height):
    volume = (3.14*(radius**2)*height)/3
    return volume
    
def pyramid_area(length,width,height):
    surface_area = lenght*width + length*(((width/2)**2 + height**2)**0.5) + width*(((length/2)**2 + height**2)**0.5)
    return surface_area
    
def pyramid_volume(length,width,height):
    volume = length*width*height/3
    return volume
    
def triangle_perimeter(side1,side2,side3):
    perimeter = side1 + side2 + side3
    return perimeter
    
def triangle_area(side1, side2, side3):
    perimeter_half = (triangle_perimeter(side1,side2,side3))/2
    area = (p*(p-side1)*(p-side2)*(p-side3))**0.5
    return area
    
def main():
    print("welcome to my math module")
    print("For circle related computation,enter 1")
    print("For square related computation,enter 2")
    print("For rectangle related computation,enter 3")
    print("for triangle related computation,enter 4")
    print("For sphere related computation,enter 5")
    print("For cube related computation,enter 6")
    print("For cuboid related computation,enter 7")
    print("For cylinder related computation,enter 8")
    print("For cone related computation,enter 9")
    print("for pyramid related computation,enter 10")
    choice = int(input("enter your choice"))
    
    if choice == 1:
        radius_val = int(input("enter the radius"))
        print("to compute cicrcumference,enter 1")
        print("to compute area, print 2")
        internal_choice = int(input("enter your choice"))
        if internal_choice == 1:
            print("circumference is",circle_circumference_calc(radius_val))
        elif internal_choice == 2:
            print("area is",circle_area_calc(radius_val))
        else:
            print("wrong option")
            
    elif choice == 2:
        side = int(input("enter the side"))
        print("to compute perimeter,enter 1" )
        print("to compute area,enter 2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("perimeter is",square_perimeter_calc(side))
        elif internal_choice==2:
            print("area is",square_area_calc(side))
        else:
            print("wrong option")
            
    elif choice==3:
        length = int(input("enter the length"))
        breadth = int(input("enter the breadth"))
        print("to compute perimeter, enter 1")
        print("to compute area, enter 2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("perimeter is",rectangle_perimeter(length,breadth))
        elif internal_choice==2:
            print("area is", rectangle_area_calc(length,breadth))
        else:
            print("wrong option")
            
    elif choice==4:
        side1 = int(input("enter side 1"))
        side2 = int(input("enter side 2"))
        side3 = int(input("enter side 3"))
        print("for computation of perimeter, enter 1")
        print("for computation of area,enter 2")
        internal_choice = int(input("Enter your choice"))
        if internal_choice == 1:
            print("the perimeter is",triangle_perimeter(side1,side2,side3))
        elif internal_choice == 2:
            print("the area is",triangle_area(side1,side2,side3))
        else:
            print("wrong option")
            
    elif choice==5:
        radius = int(input("enter radius"))
        print("for computation of area, enter1")
        print("for computation of area, enter 2")
        internal_choice=int(input("enter your choice"))
        if internal_choice==1:
            print("the area is",sphere_surface_area(r))
        elif internal_choice==2:
            print("the volume is",sphere_volume(r))
        else:
            print("wrong choice")
            
    elif choice==6:
        side = int(input("enter the side"))
        print("to compute surface area, enter 1")
        print("to compute volume,enter 2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("the surface area of cube",cube_surface_area(a))
        elif internal_choice==2:
            print("the volume is",cube_volume(a))
        else:
            print("wrong choice")
            
    elif choice==7:
        len = int(input("enter the length"))
        bre = int(input("enter the breadth"))
        hei = int(input("enter the height"))
        print("to compute surface area,enter 1")
        print("to compute volume, enter 2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("the surface area is", cuboid_surface_area(len,bre,hei))
        elif internal_choice==2:
            print("the volume is",cuboid_volume(len,bre,hei))
        else:
            print("wrong choice")
            
    elif choice==8:
        radius = int(input("enter radius"))
        height = int(input("enter height"))
        print("to compute surface area,enter 1")
        print("to compute volume, enter2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("surface area is",cylinder_surface_area(radius,height))
        elif internal_choice==2:
            print("volume is",cylinder_volume(radius,height))
        else:
            print("wrong choice")
            
    elif choice==9:
        radius = int(input("enter the radius"))
        height = int(input("enter the height"))
        print("to compute surface area,enter1")
        print("to compute volume,enter2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("the surface area is",cone_surface_area(radius,height))
        elif internal_choice==2:
            print("the volume is",cone_volume(radius,height))
        else:
            print("wrong choice")
    elif choice==10:
        b_len = int(input("enter base length"))
        b_wid = int(input("enter base width"))
        height = int(input("enter height"))
        print("top compute surface area,enter 1")
        print("to compute volume,enter2")
        internal_choice = int(input("enter your choice"))
        if internal_choice==1:
            print("surface area is",pyramid_area(b_len,b_wid,height))
        elif internal_choice==2:
            print("volume is",pyramid_volume(b_len,b_wid,height))
        else:
            print("wrong choice")
    else:
        print("wrong option")
main()

        
