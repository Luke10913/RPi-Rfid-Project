import MFRC522
import RPi.GPIO as GPIO
import rfidread
import time
import mysql
while True:
	print ("Please select one of the following")
	print (" 1 - New Item Entry")
	print (" 2 - Lookup Entry")
	print (" 3 - Delete Entry")
	Selection = input('Selection Number = ')
	if 1 <= Selection <= 3:
		if(Selection==1):
			print ("New Item Entry Selected")
			print ("Please Scan Card")
			uid = 0
			while uid == 0:
				uid=rfidread.uidread()
				print ("Your Card UID = "+uid)
			itemname = raw_input('Please Enter Item Name = ')
			itemlocation = raw_input('Please Enter Item Location = ')
			mysql.newentry(uid, itemname, itemlocation)
			print ("Item written to database...hopefully.")
		if(Selection==2):
			print ("Lookup Entry")
		if(Selection==3):
			print ("Delete Entry")
	else:
		print ("Invalid Entry")

