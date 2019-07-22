import threading
import _thread
import time
from datetime import date
import datetime
import re
import csv
from pygame import mixer

stop_flag = 0

def help() :
    print("setalarm \t\t: adds alarm in list of alarms")
    print("\tUsage \t: setalarm hh:mm:ssAM/PM \"<message>\"")
    print("getalarm \t\t: displays list of alarms")
    print("\tUsage \t: getalarm")
    print("deletealarm \t\t: delete alarm from list of alarms")
    print("\tUsage \t: deletealarm <alarm number>")
    print("stop \t\t: stop alarm")
    print("\tUsage \t: stop")
    print("help \t\t: displays list of commands")
    print("\tUsage \t: help")
    print("exit \t\t: exit application")
    print("\tUsage \t: exit")

def Set_alarm(cmd) :
   try:
        tm = re.match('(((0[0-9])|(1[0-2])):[0-5][0-9]:[0-5][0-9](A|P)M)$', cmd[1])
        if tm is not None:
            fo = open("writeData.csv", "a")
            fo.writelines(cmd[1] +" " + cmd[2] + "\n")
            fo.close()
        else:
            print("Time Is Invalid")
            
   except ValueError:
        pass


def Get_alarm() :
    fo = open("writeData.csv", "r")
    linenu = 1
    for lines in fo:
        print("%d. %s" %(linenu ,lines))
        linenu += 1
    fo.close()

def Delete_alarm(cmd) :
    flag = 0
    infile = open('writeData.csv','r').readlines()
    with open('writeData.csv','w') as outfile:
        for index,line in enumerate(infile):
            if index != (int(cmd[1],10) - 1):
                outfile.write(line)
            else:
                flag = 1
        if flag == 0:
            print("Invalid Line Number")
        
        outfile.close()

def compare():
    global stop_flag
    now = datetime.datetime.now()
    d_today = now.strftime("%I:%M:%S%p")
    
    fo = open("writeData.csv", "r")
    for lines in fo:
        if lines.find(d_today) != -1:
            mixer.music.play()
            stop_flag = 1
    fo.close()
    if stop_flag != 0:
        stop_flag += 1
    if stop_flag == 30:
        stop_flag = 0
        mixer.music.stop()
    threading.Timer(1, compare).start()


print("This Program Is For Alarm Operations..............................")
help()
mixer.init()
mixer.music.load("mysong.mp3")
threading.Timer(1, compare).start()
#compare()

while 1:
    x = input("->")
    cmd = re.split("\s" , x)
    if(cmd[0] == "help"):
        if(len(cmd) == 1):
            help()
        else:
            print("Invalid Arguments")
        
    elif(cmd[0] == "setalarm"):
        if(len(cmd) == 3):
            Set_alarm(cmd)
        else:
            print("Invalid Arguments")
        
    elif(cmd[0] == "getalarm"):
        if(len(cmd) == 1):
            Get_alarm()
        else:
            print("Invalid Arguments")
            
    elif(cmd[0] == "deletealarm"):
        if(len(cmd) == 2):
            Delete_alarm(cmd)
        else:
            print("Invalid Arguments")

    elif(cmd[0] == "exit"):
        if(len(cmd) == 1):
            print("Application is sutting down....")
            mixer.music.stop()
            break
        else:
            print("Invalid Arguments")

    elif(cmd[0] == "stop"):
        if(len(cmd) == 1):
            mixer.music.stop()
            break
        else:
            print("Invalid Arguments")

    elif(cmd[0] == ""):
        ()
    
    else :
        print("Invalid Command")   
    
