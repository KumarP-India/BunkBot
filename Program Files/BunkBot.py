"""
Created on Fri Jan 11 10:03:00 2022

Updated on Fri Feb 04 06:45:45 2022

@author: Prabhas kumar
"""


# Importing lib.(s)

from time import sleep # For time & Delay

import pyautogui # For Mouse & Cursor

#import threading

#from tqdm import trange

import datetime as ddtt # For Time

import subprocess # For Chrome

import argparse # For CMD or Terminal



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
    
    print(f'Starting the {foo[n-1]} period.') # Printing the message


    click('refresh')

    click('login')

    click('dashboard')

    click('E-c')

    click('refresh')

    
    if n > 3: click('scroll') # If the periods' link is not in the visible area of page, scroll down

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
def school(p=0, z=0): # p - Starting period, z - Status

    start() # Calling the func to open the website.
    
    t, m = 0, 0 # Creating two integral variables


    # Times

    t1, t2, t3, t4, t5, t7, t8, t9, t10, t11 = [8, 8, 9, 10, 11, 8, 9, 9, 11, 12] #Hour
    m1, m2, m3, m4, m5, m7, m8, m9, m10, m11 = [0, 39, 19, 54, 29, 34, 14, 54, 24, 0] #Min


    while True:

        now = ddtt.datetime.now() #Current time
        
        # p donates the no. of period it has attended.

        # z donates wether it is on the class or not (0 = no, 1 = yes)


        if now.hour == t1 and now.minute >= m1 and p == 0 and z == 0: 
            
            period(1) #Calling the func. Open excute the protocol of opening class
            
            p += 1 # Incresing the value if period varible as it has attended one more period
            
            z = 1  # Seting the Status to Yes (Whether it is in the class meeting?)
            
            t, m = t7, m7 # Setting the variables to the period ending time!

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

            close() # Calling the fuction to leave the class meeting room.

            z = 0  # Seting the Status to No (Whether it is in the class meeting?)

        if p == 5 and z == 0: #Ending Statement(s)            
                
            close_win(); break # Closing the program

    sleep(sp)





class Inputs: # The class for the optional comand prompts' or terminals' Input

    def __init__(self): 

        # Setting the help Messages to the Dictionary bounded to the self obj.
        HelP = {"Period": "It is used Specify the starting period of the Class. \
                     If the Status Input is set to Open (By default Value) then It \
                         will start the specified period Else it will wait till the \
                             specified period end time came and then countinue from there!",

                "Status": "It used to tell the program wether the curent specified \
                    period is already open & joined or not!, The Values are 'Open' & 'Close' only!"
                }


        
        parser = argparse.ArgumentParser(description = "BunkBot Program by Prabhas Kumar") # Creating the argument parser object

        # Adding the OPtional aruments
        parser.add_argument("-P", "-p", "--Period", "-p", help = HelP['Period'], required = False, default = "")
        parser.add_argument("-s", "-S", "--Status", help = HelP['Status'], required = False, default = "")

        argument = parser.parse_args() # Calling the inputs, if any!

        values = ["0", "Close"] # Default values, if no or unvalid input is given.

        if argument.Period: # If period arg. is given 
            print("You have Specified the starting period to: {0}".format(argument.Period)) # Printing message to let know of the change!

            try: # If any Error ocour then it reverts back to default, ie. don't change at all.
                
                foo = int(argument.Period) # Getting the input and converting the variable to int val.

                if foo > 5: raise RuntimeError("") # Raising the error if input is more than the max. no. of periods.

            except: # Code to run if error occur.
                
                # Printing the message for telling failure of changing the var.
                print("You have not specified the INtegral Value or the value exceds the no. of periods. Setting the default instead: 0")

                foo = 0 # Defult val.

            values[0] = foo # Adding the final value to the list.

        if argument.Status:  # If status arg. is given 
            print("You have Specified status of the starting period strted: {0}".format(argument.Status)) # Printing message to let know of the change!

            try: # If any Error ocour then it reverts back to default, ie. don't change at all.
                
                foo = argument.Status # Geting the input.

                if foo != "Open" and foo != "Close": raise RuntimeError("") # Raising error if Unvalid input is given!

            except: # Code to run if error occur.
                
                # Printing the message for telling failure of changing the var.
                print("You have not specified the accepted Value. Setting the default instead: Close")

                foo = "Close" # Defult val.

            values[1] = foo # Adding the final value to the list.

        self.Values = values # Sending the values to the list bounde to Python's Classes' self obj.

    
    def args(self): # Func. to return the inputs or defualt var.

        x, z = self.Values # Calling the values.

        # Converting Status var's Human readble Str. val. to Integral Binary! 
        if z == "Close": z = 0

        elif z == "Open": z = 1

        else: z = 0


        return int(x), int(z) # Returniing the values




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

    
    INPUt = Inputs() # Calling the Inputs class & bounding it to obj. INPUt

    p, z = INPUt.args() # Calling the func to get the values from Inputs class

    #print(p, z)
    
    #p, z = 0, 0

    
    #main = threading.Thread(target=school, name='Program', args=(p, z))
    #support = threading.Thread(target=progress, name='Support')

    print() # Empty line

    #support.start()

    #main.start()

    #bar.progress()

    #main.join()

    #bar._stop()

    school(p, z) # Calling the main program with the input values.


    print('Thanks for using the Program!\n') # Ending Statement!

    while True: # Final Confirmation Loop.

        end = input("Close the progrma? [Y]es [n]o: ").lower() # Question

        if end == 'n': sleep(3); print() # If ans. is no, wait 3 sec. and re-ask the question

        elif end == 'y': break # Else, if asn. is yes, exit the loop.

        else: sleep(1)

    sleep(2) # Wait 2 sec. to prppoerly clear the background low level files.


'''
The End :)
'''
