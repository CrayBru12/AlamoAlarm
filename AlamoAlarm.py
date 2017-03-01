#Import libraries
import time
import webbrowser
import random
import os



#This section checks if the user has the Alarm.txt file in the same area as alarm.py
if os.path.isfile("Alarm.txt") == False:
	print ("Alarm.txt not present. Creating file...")
	flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
	filecreate = os.open("Alarm.txt", flags)
	Alarm.txt.write("https://www.youtube.com/watch?v=dQw4w9WgXc")

#User Input to Set Alarm
print ("What time would you like to set the Alarm for?")
print ("Use this form.\nExample: 09:30")
Alarm = input("> ")


Time = time.strftime("%H:%M")

#To open text file
with open("Alarm.txt") as A:
	#reads content
	content = A.readlines()


#Every time that is not the alarm time
while Time != Alarm:
	
	print ("The time is " + Time)
	
	Time = time.strftime("%H:%M")
	
	#Prevention of flooding command line with time udates
	time.sleep(1)

#Alarm activation code
if Time == Alarm:

	print ("Hello, World! It is time to wake up!")
	#chooses a random link from Alarm file
	random_video = random.choice(content)
	webbrowser.open(random_video)