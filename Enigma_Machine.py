###############################################################
# Author: Alexander Ogle                                      #
# Date: 19/6/2015 - 23/6/2015 (sub cipher/decipher completed) #
# Project: Enigma Machine                                     #
###############################################################
#To run the code, hit F5 and enter the following, then select "save", then "run": 
#cmd /k "C:\Python27\python.exe $(FULL_CURRENT_PATH)"

#import the functions which will be used! 
import em_functions
import time
import datetime
		 
#Ask whether to encode or decode
operation = str(raw_input("Would you like to encode or decode a message? (encode/decode) ")).lower()
while operation != "encode" and operation != "decode":
	operation = str(raw_input("Please indicate your preference from the available options (encode/decode) "))

if operation == "encode":
	#Ask user for message to encode
	message = str(raw_input("What would you like to encode? ")).lower()
	#Ask user for which cipher to use
	cipher = raw_input("What cipher would you like to use? (sub) ")
	while cipher != "sub":
		cipher = raw_input("Select from the available ciphers, please (sub):")
	cipher = str(cipher.lower())

	if cipher == "sub":
		#ask user for the 'A Key', which defines which letter is subbed for A
		key = str(raw_input("Enter an /A Key/, the letter which will be subbed for A "))
		#run this code which will encode it and stuff
		encoded_message = em_functions.cipher_sub(message, key)
		print ""
		em_functions.output_encoded(encoded_message)
		date = time.strftime("%H") + time.strftime("%M") + time.strftime("%S")
		time = time.strftime("%d") + time.strftime("%m") + time.strftime("%y")
		filename = date + "_" + time + ".txt"
		print filename
		file = open(filename,'w')
		file.seek(0)
		file.write(encoded_message)
		file.close()
	else: 
		print "Error 01"
	
if operation == "decode":
	#Ask user for message to decode
	message = str(raw_input("What would you like to decode? ")).lower()
	#Ask user for which cipher to use
	cipher = raw_input("What cipher should be decoded? (sub) ")
	while cipher != "sub":
		cipher = raw_input("Select from the available ciphers, please (sub):")
	cipher = str(cipher.lower())
	
	if cipher == "sub":
		#ask user for the 'A Key', which defines which letter is subbed for A
		key = str(raw_input("What is the /A Key/?"))
	#run this code which will decode it an stuff
	decoded_message = em_functions.decode_sub(message, key)
	print ""
	em_functions.output_encoded(decoded_message)
	