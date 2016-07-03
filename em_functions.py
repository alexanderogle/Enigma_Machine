def cipher_sub(str, n):
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	#make everything lower case to simplify things (really only works for English)
	print ""
	print str
	key_index = alpha.index(n)
	#generate the substitution alphabet
	#create an empty list first
	alpha_sub = []
	#then order the alpha according to the key (n)
	#loop through alpha from the key to the end, and append that to alpha_sub
	for i in range(len(alpha[key_index:len(alpha)])):
		alpha_sub.append(alpha[key_index+i])
	#then loop through alpha from the beginning to the key, appending alpha_sub 
	for i in range(0, key_index):
		alpha_sub.append(alpha[i])
	#now we encode the message
	encoded_message = []
	for i in str:
		#check to make sure it's a letter
		if i.isalpha():
			encoded_message.append(alpha_sub[alpha.index(i)])
		else:
			encoded_message.append(i)
	#convert the list 'encoded_message' into a str
	str_encoded_message = ''
	for i in range(len(encoded_message)):
		str_encoded_message = str_encoded_message + encoded_message[i]
	encoded_message = str_encoded_message
	#print out the information necessary for decoding
	print ""
	print "A Key = %s" % (key_index)
	print "<",
	for letter in alpha_sub:
			print letter,
	print ">"
	return encoded_message

def decode_sub(str, n):
	#this code is nearly identical to the cipher_sub function
	alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	#make everything lower case to simplify things (really only works for English)
	print ""
	print str
	key_index = alpha.index(n)
	#generate the substitution alphabet
	#create an empty list first
	alpha_sub = []
	#then order the alpha according to the key (n)
	#loop through alpha from the key to the end, and append that to alpha_sub
	for i in range(len(alpha[key_index:len(alpha)])):
		alpha_sub.append(alpha[key_index+i])
	#then loop through alpha from the beginning to the key, appending alpha_sub 
	for i in range(0, key_index):
		alpha_sub.append(alpha[i])
	#now we decode the message
	decoded_message = []
	for i in str: 
		if i.isalpha():
			decoded_message.append(alpha[alpha_sub.index(i)])
		else:
			decoded_message.append(i)
	#convert decoded message to a usable string
	str_decoded_message = ''
	for i in range(len(decoded_message)):
		str_decoded_message = str_decoded_message + decoded_message[i]
	decoded_message = str_decoded_message
	#print out the information necessary for decoding
	print ""
	print "A Key = %s" % (key_index)
	print "<",
	for letter in alpha_sub:
			print letter,
	print ">"
	return decoded_message
	
def output_encoded(str):
	for i in str:
		print i,

def empty(x):
	#Use this function to generate an empty array, filled with 0s!
	array_x = []
	for i in range(x):
		 array_x.append(0)
	return array_x
		 
def alpha_index(str):
	if len(str) != 1:
		print "That's not a letter!"
	elif str.isalpha():
		#find the index associated with this letter in the alphabet!
		alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		alpha_index = alpha.index(str)
		return alpha_index
		
