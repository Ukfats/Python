import subprocess

#value "dictaphone" would save
phrase = ('testphrase1')

# Initialize Dictionary #
#Usage:
#Edit dictionary key to the "voice command" being spoken.
#Edit the dictionary value to the command you want to run.
test_list = {
             'testphrase1' : 'Super_L', 
             'testphrase2' : 'F12', 
             'testphrase3' : 'F12'
            }

#Compares the spoken phrase to the dictionary list and calls xdotool to run the associated command.
subprocess.call ('xdotool key --clearmodifiers '+ (test_list[phrase])+ '', shell=True)
