import os
import subprocess

def choice():
    global answer
    answer = input("(y/n) ").strip().lower()

def pick_color():
    global color
    color = input("\nColor: #").strip().lower()
    if color == "":
        print("")
    else:
        print("")
        os.system("printf '\e]4;1;%s\a\e[0;41m   \n   \n\e[m' '#"+color+"'")
        print("")
        print("\nIs this the color you want?", end="")
        choice()
        if answer == "y":
            pass
        elif answer == "n":
            pick_color()
        else:
            choice()

def options():
    global color
    global line
    global component

    #User Inputs
    mode = input("\nMode (static, breathe): ").strip().lower()
    pick_color()
    speed = ""
    if mode != "static":
        speed = input("\nSpeed (1-5):").strip().lower()
    brightness = input("\nBrightness (0-5):").strip().lower()

    #Assigns attributes to the values
    if mode != "":
        mode = " --mode=" + mode
    if color != "":
        color = " --color=" + color
    if speed != "":
        speed = " --speed=" + speed
    if brightness != "":
        brightness = " --brightness=" + brightness
    line =component + mode + color + speed + brightness + " "


finalline = "cm-rgb-cli set "
unactive_elements = 0

enable_component = input("\nEnable the Logo? (y/n) ").strip().lower()
if enable_component == "y":
    component = "logo"
    options()
    finalline += line
else:
    unactive_elements += 1

enable_component = input("\nEnable the Fan? (y/n) ").strip().lower()
if enable_component == "y":
    component = "fan"
    options()
    finalline += line
else:
    unactive_elements += 1

enable_component = input("\nEnable the Ring? (y/n) ").strip().lower()
if enable_component == "y":
    component = "ring"
    options()
    finalline += line
else:
    unactive_elements += 1

if unactive_elements == 3:
    print("\nNo inputs. All RGB will be turned off")
    os.system("cm-rgb-cli set logo --mode=off save")
else:
    finalline += "save"
    print("\nThis line will be executed :\n\n" + finalline + "\n")
    os.system(finalline)
