import speech_recognition as sr
import sounddevice as dev
import subprocess
from playsound import playsound

#IMPORTANT: uses google for the transciption of voice>text so an internet connection is required!.
#Limitations are how well the google recognition can make out words, some words are complicated and not all mics are clear.

#Get a list of connected audio devices, sequencial number on that list is the "device_index=" number 
#e.g: number 10 on the list would be "device_index=9"
#print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
mic = sr.Microphone(device_index=9)

while True:
    with mic as source:
        try:
         audio = r.listen(source,timeout=None)
         phrase=(r.recognize_google(audio))
         
         #Usage:
         #Edit dictionary key to the "voice command" being spoken.
         #Edit the dictionary value to the command you want to run.
         #Format = {'voice_command_phrase' : 'keyboard_command_permormed'}
         command_list = {
             'inventory' : 'Super_L', 
             'gear' : 'F12', 
             'skills' : 'F12'
            }
         #Convert voice command into keyboard command.
         subprocess.call ('xdotool key --clearmodifiers '+ (command_list[phrase])+ '', shell=True)
        
        except:
         sr.UnknownValueError
