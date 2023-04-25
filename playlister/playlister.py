import subprocess
import random
import time
from termcolor import colored

'''
Loops through Youtube playlists.
My first attempt at a re-write in Python, the original file is a bash script.

Attempted to use Python modules to handle the keyboard and mouse actions (mouse, keyboard, pynput.mouse, pynput.keyboard).
Never managed to get them working, Python calls them as shell(sh) commands which aren't recognised while using os.system 
and subprocess.Popen.

As a workaround I put the Linux 'xdotool' commands in lists and called those.
'''

#Playlist locations.
playlist = [
  'xdotool mousemove 668 875 click --repeat 2 1', 
  'xdotool mousemove 897 867 click --repeat 2 1', 
  'xdotool mousemove 1307 875 click --repeat 2 1',    
  'xdotool mousemove 1539 865 click --repeat 2 1'
  ]
ranlist = random.choice(playlist) 

#Duration locations.
dcoord=[
  'xdotool mousemove 380 895 click --repeat 2 1',
  'xdotool mousemove 419 895 click --repeat 2 1',
  'xdotool mousemove 484 895 click --repeat 2 1',
  'xdotool mousemove 594 895 click --repeat 2 1',
  'xdotool mousemove 755 895 click --repeat 2 1',
  'xdotool mousemove 999 895 click --repeat 2 1',
  'xdotool mousemove 1209 895 click --repeat 2 1'
  ]
rancoord = random.choice(dcoord)

#Looping function for "Stage5"
def looper():
 timer1=(random.randint(27, 39))
 timer2=(random.randint(147, 623))
 timer3=(random.randint(218, 461))
 timer4=(random.randint(117, 346))
 
 time.sleep(timer1)
 for i in range (1):
  time.sleep (6)
  subprocess.Popen((rancoord),shell=True)
  time.sleep (5) 
  #subprocess.Popen(('xdotool key --clearmodifiers k'),shell=True)
 
 time.sleep(timer2)
 for i in range (1):
  time.sleep (7)
  subprocess.Popen((rancoord),shell=True)
  time.sleep (6) 
  subprocess.Popen(('xdotool key --clearmodifiers k'),shell=True)

 time.sleep (timer3)
 for i in range (1):
  time.sleep (5)
  subprocess.Popen((rancoord),shell=True)
  time.sleep (5) 
  subprocess.Popen(('xdotool key --clearmodifiers k'),shell=True)
  time.sleep (timer4)
  subprocess.Popen(('xdotool mousemove 460 919 click --repeat 2 1'),shell=True)
  print (colored("Stage Complete: LOOPER", 'blue', attrs=['blink']))
  looper()

#Stage1: VPN randomiser stage.
subprocess.Popen(("python vpnswitch.py"),shell=True)
time.sleep (10)
print(colored("Stage Complete: VPN", 'green', attrs=['blink']))

#Stage2: User Agent randomiser stage.
time.sleep(3)
subprocess.Popen(('xdotool mousemove 1827 193 click --repeat 2 1'),shell=True)
time.sleep(3)
subprocess.Popen(('xdotool mousemove 1623 555 click --repeat 2 1'),shell=True)
time.sleep(3)
#subprocess.Popen(('xdotool mousemove 1827 193 click --repeat 2 1'),shell=True)
print(colored("Stage Complete: USER AGENT", 'green', attrs=['blink']))

#Stage3: Opening Site stage.
subprocess.Popen(('xdotool mousemove 542 230 click --repeat 2 1'),shell=True)
time.sleep(5)
subprocess.Popen(('xdotool mousemove 568 483 click --repeat 2 1'),shell=True)
time.sleep(10)
subprocess.Popen(('xdotool mousemove 870 716 click --repeat 2 1'),shell=True)
time.sleep(10)
print(colored("Stage Complete: OPEN SITE", 'yellow', attrs=['blink']))

#Stage4: Selecting random playlist stage and sleep.
timerl=(random.randint(31, 53))
time.sleep(8)
for i in range (1):
  subprocess.Popen((rancoord),shell=True)
  time.sleep(timerl)
print(colored("Stage: PLAYLIST", 'yellow', attrs=['blink']))

#Stage5: Randomly move around video before moving to next video.
looper()
print(colored("Stage Complete: LOOPER", 'blue', attrs=['blink']))
