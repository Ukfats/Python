import speech_recognition as sr
import sounddevice as dev
global mic_stream
global mic_input

'''
Run to get a list of connected audio devices, sequencial number on that list is the "device_index=" number 
e.g: number 10 on the list would be "device_index=9"
'''
#print(sr.Microphone.list_microphone_names())

dictlist=[]
r = sr.Recognizer()
mic = sr.Microphone(device_index=9)

with mic as source:
    audio = r.listen(source,timeout=None)

dictlist.append (r.recognize_google(audio))
line=print(dictlist)

#Edit location as needed.
with open('/home/user/scripts/Python/BVA/dictated.txt', 'a+') as file:
    for line in dictlist:
        file.write("%s\n" % line)
        file.close()

#print(testlist) #output test
