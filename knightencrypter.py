from scripts.encrypter import Encrypt
from scripts.decrypter import Decrypt
from scripts.help import *
from sys import argv
import timeit

def main(args):
	try:
		choice = args[0].lower()
		if choice.lower() == "help":
			Help()
			return
		input_file = args[1]
		output_file = args[2]
	except:	
		print "\nUsage: knight.pyc [decrypt][encrypt] <input_file> <output_file>\n"
		return
	if choice.lower() == 'encrypt':
		print '\n------------Encrypt mode--------------\n'
		response = Encrypt(input_file,output_file)
		if response.error is None:
			print "\nFile successfully encrypted!\n"
		else:
			print response.error
	elif choice.lower() == 'decrypt':
		print '\n------------Decrypt mode--------------\n'
		response = Decrypt(input_file,output_file)
		if response.error is None:
			print "\nFile successfully decrypted!\n"
		else:
			print response.error
	else:
		print "Supported commands: [encrypt][decrypt]"

main(argv[1:])
