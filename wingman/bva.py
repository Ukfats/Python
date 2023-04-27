import speech_recognition as sr
import sounddevice as dev
import subprocess

#IMPORTANT: uses google for the transciption of voice>text so an internet connection is required!.
#Limitations are how well the google recognition can make out words, some words are complicated and not all mics are clear.

#Get a list of connected audio devices, sequencial number on that list is the "device_index=" number 
#e.g: number 10 on the list would be "device_index=9"
#print(sr.Microphone.list_microphone_names())

#dictlist=[]
r = sr.Recognizer()
mic = sr.Microphone(device_index=9)

with mic as source:
    audio = r.listen(source,timeout=None)
    phrase=(r.recognize_google(audio))

#Output phrase to terminal for debug.    
#line=print(phrase)

# Initialize Dictionary #
#Usage:
#Edit dictionary key to the "voice command" being spoken.
#Edit the dictionary value to the command you want to run.
#Format = {'voice_command_phrase' : 'keyboard_command_permormed'}
command_list = {
             'inventory' : 'Super_L', 
             'skills' : 'F12', 
             'pause' : 'F12'
            }

#Convert voice command into keyboard command.
subprocess.call ('xdotool key --clearmodifiers '+ (command_list[phrase])+ '', shell=True)
