def check(password):
	if password.lower() == 'exit':
		return "Cannot have keyword 'exit' as password"
	if ' ' in password:
		return "Your password cannot contain spaces"
	return 'ok'

def auth():
	print "\nThe Knight requests a password which has to be used during decryption."
	password = raw_input("Enter 'exit' to abort or a password to continue: ")
	while password.lower() != 'exit':
		pass_check = check(password)
		if pass_check == 'ok':
			return password
		password = raw_input(pass_check)
	return ''

def auth_decrypt(passkey):
	print "\nThe Knight requires a decryption password [You may enter 'exit' to terminate]"
	password = raw_input("Enter the decryption key: ")
	while password != "exit" and passkey != password:
		password = raw_input("Nope, you got the key wrong. Enter again: ")
	if password == "exit":
		print "Process terminated...\n"
		exit(0)