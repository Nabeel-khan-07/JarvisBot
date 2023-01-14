from os import  startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappMsg(name,message):

    startfile("C:\\Users\\kn392\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    sleep(10) 
    
    click(x=105, y=140)

    sleep(1)

    write(name)

    sleep(1)

    click(x=380, y=311)

    sleep(1)

    click(x=585, y=303)

    sleep(1)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\kn392\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    sleep(10) 
    
    click(x=105, y=140)

    sleep(1)

    write(name)

    sleep(1)

    click(x=380, y=311)

    sleep(1)

    click(x=1709, y=65)

def WhatsappChat(name):

    startfile("C:\\Users\\kn392\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    sleep(10) 
    
    click(x=105, y=140)

    sleep(1)

    write(name)

    sleep(1)

    click(x=380, y=311)

    sleep(1)    

def WhatsappVideocall(name):
   
    startfile("C:\\Users\\kn392\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    sleep(10) 
    
    click(x=105, y=140)

    sleep(1)

    write(name)

    sleep(1)

    click(x=380, y=311)

    sleep(1)    

    click(x=1662, y=76)

def WhatsappStatus():

    startfile("C:\\Users\\kn392\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
   
    sleep(10)

    click(x=397, y=77)

    sleep(1)

    click(x=249, y=265)

