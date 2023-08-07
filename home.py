import time
import os
import socket
import psutil
import tkinter as tk
import requests
import time
import calendar
import datetime

from one import ONE
from two import TWO
#from three import THREE
from four import FOUR
from five import FIVE
from terminal import TER
from weather import wea
from calender import ttt
from my_Calculator import cal
from Drive_Memory import dmem 
from Drive_Open import dopn
from usbDetect import usb

import datetime

e = datetime.datetime.now()

battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""

░█████╗░░█████╗░████████╗░█████╗░██╗░░░██╗███████╗░░░░░░░█████╗░░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░██║██╔════╝░░░░░░██╔══██╗██╔════╝
██║░░██║██║░░╚═╝░░░██║░░░███████║╚██╗░██╔╝█████╗░░█████╗██║░░██║╚█████╗░
██║░░██║██║░░██╗░░░██║░░░██╔══██║░╚████╔╝░██╔══╝░░╚════╝██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░╚██╔╝░░███████╗░░░░░░╚█████╔╝██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░░░░░╚════╝░╚═════╝░
""")
print("WELCOME "+l_n)
#print("")
print("The Date is: "+time.strftime("%m/%d/%y"))
print ("The time is now: %s:%s:%s" % (e.hour, e.minute, e.second))
print("The Battery Level is: ", end=' ')
print(battery.percent)
print(" ")

print("")
print("Basic Functions : ")
print("""
[1] To Open Browser
[2] To Open Text Editor
[3] Shut Down OS
[4] To Open Terminal
[5] Calender
[6] Calculator
[7] Weather Forecast 
""")

print(" ")
                                        
print("Network Functions : ")
print("""
[8] Internet Connectivity Status
[9] Internet Speed Status
[10] Saved Wifi Networks Details
[11] Switch Wifi
""")

print(" ")
                                        
print("File Managment Functions : ")
print("""
[12] Open File Explorer
[13] Show Drive Memory
[14] Open Drive

""")

print(" ")
                                        
print("Input/Output Management : ")
print("""
[15] Open CD Drive
[16] USB Detection

""")

while(1):
    select = input("[?]: ")

    if select == '1':
        os.system("python brows.py")
        
    if select == '2':
        os.system("python edit.py")
        
    if select == '3':
        print("Shutiing Down .... ")
        os.system("shutdown /s /t 2")
        
    if select == '4':
        TER()
    if select =='5':
        ttt()
    if select =='6':
        cal()
    if select =='7':
        wea()
    if select == '8' :
        ONE()
    if select == '9' :
        TWO()
    if select == '10' :
        os.system('cmd /c "netsh wlan show network"')
    if select == '11' :
        FIVE()
    if select == '12' :
        os.system("python file.py")
    if select == '13':
        dmem()
    if select == '14':
        dopn()
    if select == '15':
        os.system('cmd /c "Explorer "G:""')
    if select =='16':
        usb()