#Import libraries
import time
import webbrowser
import random
import os



#This section checks if the user has the Alarm.txt file in the same area as alarm.py
if os.path.isfile("Alarm.txt") == False:
	print "Alarm.txt not present. Creating file..."
	flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
	filecreate = os.open("Alarm.txt", flags)
	with os.fdopen(fisierCreat, 'w') as fileCreated:
	    fileCreated.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#User Input to Set Alarm
print "What time would you like to set the Alarm for?"
print "Use this form.\nExample: 09:30"
Alarm = raw_input("Alarm Set> ")


#I first need to state the Time variable so it's usable in the while-loop
Time = time.strftime("%H:%M")

#This opens the text file with the youtube links
with open("YT.txt") as f:
	#the urls are stored in the content variable 
	content = f.readlines()


#When the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:
	
	print "The time is " + Time
	
	#Restating the Time variable allows the time to refresh
	#When I tried keeping the variable outside of the loop it just repeated the inital time
	Time = time.strftime("%H:%M")
	
	#This keeps the loop from flooding the command line with updates of the time :P
	time.sleep(1)

#If the Time variable is equal to the Alarm string, this code activates
if Time == Alarm:

	print "Time to Wake up!"
	#from the variable content, a random link is chosen and then that link is stored in random_video variable
	random_video = random.choice(content)
	#Using the webbrowser library, it opens this youtube video link.
	#The videos are varius aphex twin songs
	webbrowser.open(random_video)