from scripts.encrypt import *
from scripts.decrypt import *
from scripts.help import *
from sys import argv
def main(args):
	try:
		choice = args[0].lower()
		if choice.lower() == "help":
			Help()
			return
		input_file = args[1]
		output_file = args[2]
	except:	
		print "Usage: knight.pyc [decrypt][encrypt] <input_file> <output_file>"
		return
	if choice.lower() == 'encrypt':
		print '\n------------Encrypt mode--------------\n'
		print Encrypt(input_file,output_file)
	elif choice.lower() == 'decrypt':
		print '\n------------Decrypt mode--------------\n'
		print Decrypt(input_file,output_file)
	else:
		print "Supported commands: [encrypt][decrypt]"

main(argv[1:])
