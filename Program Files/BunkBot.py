"""
Created on Fri Jan 11 10:03:00 2022

Updated on Wed Feb 02 16:00:00 2022

@author: Prabhas kumar
"""


# Impoerting lib.(s)

from ast import arguments
from time import sleep

import pyautogui

#import threading

#from tqdm import trange

import datetime as ddtt

import subprocess

import argparse



# Co-Ordinates

cord = {'taskbar': [476, 1079], 'win': [794, 1048], 'chrome': [1138, 411], 'edunext': [678, 627], 'login': [1336, 719], 'dashboard': [1781, 180], 'E-c': [34, 729], 'mic': [619, 808],\
        'cam': [717, 811], 'tab_cls': [587, 19], 'refresh': [107, 61], 1: [1308, 459], 'scroll': [1908, 1037], 2: [1308, 674], 3: [1330, 885], 4: [1310, 622], 5: [1307, 835],\
        'closer': [1889, 18], 'join': [1345, 631]}




sp = 3 # Waiting time gap between Clicks.


#Clicking 
def click(nm, d=sp):

    x, y = cord[nm] #Getting the cords

    pyautogui.moveTo(x,y, duration=1) #Moving to cords

    pyautogui.click() #clicking

    sleep(d) #Delay


def start(): # OPening the website

    #browser.get('https://dpspatna.edunexttech.com/Index')

    # click('taskbar')

    # click('win')

    # click('chrome')

    subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")

    sleep(sp)

    click('edunext')

    sleep(sp)

    click('login')

    click('dashboard')

    click('E-c')


def period(n): #Joining the class

    foo = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixed', 'Sevened', 'Eighth']
    
    print(f'Starting the {foo[n-1]} period.')

    click('refresh')
    
    if n > 3: click('scroll')

    click(n)

    click('mic')

    click('cam')

    click('join')


def close(): #Exiting the class

    click('tab_cls')

    click('refresh')

def close_win(): #Closing the Webbrowser

    click('closer')


# Main Program
def school(p=0, z=0):

    start()
    
    t, m = 0, 0


    # Times

    t1, t2, t3, t4, t5, t7, t8, t9, t10, t11 = [8, 8, 9, 10, 11, 8, 9, 9, 11, 12] #Hour
    m1, m2, m3, m4, m5, m7, m8, m9, m10, m11 = [0, 39, 19, 54, 29, 34, 14, 54, 24, 0] #Min


    while True:

        now = ddtt.datetime.now() #Current time
        
        # x donates the no. of period it has attended.

        # y donates wether it is on the class or not (0 = no, 1 = yes)


        if now.hour == t1 and now.minute >= m1 and p == 0 and z == 0: 
            
            period(1) 
            
            p += 1
            
            z = 1 
            
            t, m = t7, m7

        elif now.hour == t2 and now.minute > m2 and p == 1 and z == 0:

            period(2)

            p += 1

            z = 1

            t, m = t8, m8

        elif now.hour == t3 and now.minute > m3 and p == 2 and z == 0:

            period(3)

            p += 1

            z = 1

            t, m = t9, m9

        elif now.hour == t4 and now.minute > m4 and p == 3 and z == 0:

            click('refresh')
            
            click('login')

            click('dashboard')

            click('E-c')

            period(4)

            p += 1

            z = 1

            t, m = t10, m10

        elif now.hour == t5 and now.minute > m5 and p == 4 and z == 0:

            period(5)

            p += 1

            z = 1

            t, m = t11, m11


        if now.hour == t and now.minute > m and z == 1:

            close()

            z = 0

        if p == 5 and z == 0: #Ending Statement(s)            
                
            close_win(); break # Closing the program

    sleep(sp)





class Inputs:

    def __init__(self):
        HelP = {"Period": "It is used Specify the starting period of the Class. \
                     If the Status Input is set to Open (By default Value) then It \
                         will start the specified period Else it will wait till the \
                             specified period end time came and then countinue from there!",

                "Status": "It used to tell the program wether the curent specified \
                    period is already open & joined or not!, The Values are 'Open' & 'Close' only!"
                }


        
        parser = argparse.ArgumentParser(description = "BunkBot Program by Prabhas Kumar")

        parser.add_argument("-P", "-p", "--Period", "-p", help = HelP['Period'], required = False, default = "")
        parser.add_argument("-s", "-S", "--Status", help = HelP['Status'], required = False, default = "")

        argument = parser.parse_args()

        values = ["0", "Close"]

        if argument.Period: 
            print("You have Specified the starting period to: {0}".format(argument.Period))

            try: 
                
                foo = int(argument.Period)

                if foo > 5: raise RuntimeError("")

            except: 
                
                print("You have not specified the INtegral Value or the value exceds the no. of periods. Setting the default instead: 0")

                foo = 0

            values[0] = foo

        if argument.Status: 
            print("You have Specified status of the starting period strted: {0}".format(argument.Status))

            try: 
                
                foo = argument.Status

                if foo != "Open" and foo != "Close": raise RuntimeError("")

            except: 
                
                print("You have not specified the accepted Value. Setting the default instead: Close")

                foo = "Close"

            values[1] = foo

        self.Values = values

    
    def args(self):

        x, z = self.Values

        if z == "Close": z = 0

        elif z == "Open": z = 1

        else: z = 0

        return int(x), int(z)




# class bar:

#     def __init__(self):
        
#         self._right = True
    
#     def progress(self):
        
#         foo =  int(ddtt.datetime.now().hour), int(ddtt.datetime.now().minute)

#         if foo[0] >= 12 and foo[0] < 6: return 

#         left = ((12-foo[0]) *60 - foo[1]) *60

#         for i in trange(left, desc="Progress"): 
#             if self._right: break
            
#             else: sleep(1)

#     def stop(self): self._right = False



if __name__ == "__main__":

    
    INPUt = Inputs()

    p, z = INPUt.args()

    #print(p, z)
    
    #p, z = 0, 0

    
    #main = threading.Thread(target=school, name='Program', args=(p, z))
    #support = threading.Thread(target=progress, name='Support')

    print()

    #support.start()

    #main.start()

    #bar.progress()

    #main.join()

    #bar._stop()

    school(p, z)


    print('Thanks for using the Program!\n')

    while True:

        end = input("Close the progrma? [Y]es [n]o: ").lower()

        if end == 'n': sleep(3); print()

        elif end == 'y': break

        else: sleep(1)

    sleep(2)


'''
The End :)
'''
    
