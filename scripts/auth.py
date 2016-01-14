def auth():
	print "\nThe Knight requests a password which has to be used during decryption."
	response = raw_input("Enter 'exit' to abort or a password to continue: ")
	if response.lower() == 'exit':
		print "\nEncryption cancelled by user!\n"
		exit(0)
	return response

def authorize_decryption(passkey):
	print "\nThe Knight requires a decryption password [You may enter 'exit' to terminate]"
	password = raw_input("Enter the decryption key: ")
	while password != "exit" and passkey != password:
		password = raw_input("Nope, you got the key wrong. Enter again: ")
	if password == "exit":
		print "\nDecryption cancelled by user!\n"
		exit(0)