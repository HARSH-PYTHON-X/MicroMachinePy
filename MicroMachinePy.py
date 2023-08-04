from time import sleep
from tkinter import *
import pyautogui as pg
import pydirectinput as pd
import cv2
import pyttsx3
import speech_recognition
import random

import math

print("using __MicroMachinePy__")

def random_int (start = 1, end = 9) :
    ran = random.randint(start, end)
    
    return ran

def choose_random (choose_from, length = 1) :
    ran = ''.join(random.sample(choose_from, length))

    return ran

def _SQUARE_ROOT_ (num) :
    root = num ** 0.5
    return root

def _random_ (_choices_, _no_of_output_ = 1) :
    outcome = ''.join(random.sample(_choices_, _no_of_output_))
    
    return outcome

def _LCM_ (x, y) :
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

def _HCF_ (x, y) :
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf 

# LSA , TSA, VOLUME

def _CUBOID_TSA_ (l, b, h) :
    TSA = 2 * (l * b + b * h + h * l)
    return TSA

def _CUBOID_LSA_ (l, b, h) :
    LSA = 2 * h (l + b)
    return LSA

def _CUBOID_VOLUME_ (l, b, h) :
    VOLUME = l * b * h
    return VOLUME

# CUBE

def _CUBE_TSA_ (side) :
    TSA = 6 * side * side
    return TSA

def _CUBE_LSA (side) :
    LSA = 4 * side * side
    return LSA

def _CUBE_VOLUME_ (side) :
    VOLUME = side * side * side
    return VOLUME

# CYLINDER

def _CYLINDER_TSA_ (r, h) :
    TSA = 2 * 3.14 * r * (r + h)
    return TSA

def _CYLINDER_LSA_ (r, h) :
    LSA = 2 * 3.14 * r * h
    return LSA

def _CYLINDER_VOLUME_ (r, h) :
    VOLUME = 3.14 * r * r * h
    return VOLUME

# SPHERE

def _SPHERE_TSA_ (r) :
    TSA = 4 * 3.14 * r * r
    return TSA

def _SPHERE_VOLUME_ (r) :
    VOLUME = 4 / 3 * 3.14 * r * r * r
    return VOLUME

# HEMISPHERE

def _HEMISPHERE_TSA_ (r) :
    TSA = 3 * 3.14 * r * r
    return TSA

def _HEMISPHERE_LSA_ (r) :
    LSA = 2 * 3.14 * r * r
    return LSA

def _HEMISPHERE_VOLUME_ (r) :
    VOLUME = 2 / 3 * 3.14 * r * r * r
    return VOLUME

# CONE

def _CONE_find_l (r, h) :
    l = (r * r + h * h) ** 0.5
    return l

def _CONE_find_r (l, h) :
    r = (h * h - l * l) ** 0.5
    return r

def _CONE_find_h (l, r) :
    h = (l * l - r * r) ** 0.5
    return h

def _CONE_TSA_ (r, l) :
    TSA = 3.14 * r * (r + l)  
    return TSA

def _CONE_LSA_ (r, l) :
    TSA = 3.14 * r * l

def _CONE_VOLUME_ (r, h) :
    VOLUME = 1 / 3 * 3.14 * r * r * h
    return VOLUME

# EQUATIONS

def check_solutions_of_linear_equation_in_two_variables (a1x, a1y, a1c, a2x, a2y, a2c) :
    x1 = a1x / a2x
    x2 = a1y / a2y
    x3 = a1c / a2c

    if x1 == x2 != x3 :
        return "no solution"

    elif x1 != x2 :
        return "one solution"

    elif x1 == x2 == x3 :
        return "infinite solutions"
    


def area_of_right_angle_traingle (base, height) :
    area = 0.5 * base * height

    return area


def check_common_AP (list_AP) :
    D1 = list_AP[1] - list_AP[0]
    D2 = list_AP[3] - list_AP[2]

    if D1 == D2 :
        return "0"
    
    elif D1 != D2 :
        return "1"

# PHYSICS

const_G = 0.00000000006

const_g_equator = 9.8
const_g_pole = 10

def momentum_of (mass, velocity) :
    momentum = mass * velocity
    return momentum

def kinetic_energy_of_obj_from_height (mass, height) :
    kinetci_energy = mass * height
    return kinetci_energy

def kinetic_energy_of_obj (mass, velocity) :
    kinetic_energy = 1 / 2 * mass * velocity * velocity
    return kinetic_energy

def find_height_from_time (time_taken_from_down_to_up_and_up_to_down) :
    height = time_taken_from_down_to_up_and_up_to_down * time_taken_from_down_to_up_and_up_to_down * 4.9
    return height





#! EXTRA


def speak (txt) :
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
