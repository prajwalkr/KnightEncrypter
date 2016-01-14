import os
from knight import KnightEncrypter
from random import randint
from auth import auth

class Encrypt(KnightEncrypter):
	'''
		Contains the following attributes, apart from the parent class' attributes:
		encrypted_text - encrypted file text
		decryption_key - encryption key to decrypt the encrypted file later on
		text - the data of the file that is to be encrypted
	'''
	def __init__(self,ifile,ofile):
		KnightEncrypter.__init__(self,ifile,ofile)
		if self.error is None:					# If no errors found while loading tour data
			if os.path.exists(self.ifile):
				with open(self.ifile,'r') as f:		# Read file to encrypt
					self.text = ''.join(f.readlines())
			else:
				self.error = "Input file doesn't exist!"
			self.encrypted_text,self.decryption_key = self.encrypt(self.text)
			self.authorized_write()

	def encrypt(self,data):
		'''
			Returns encrypted string of the string "text"
		'''
		l = len(data)
		segments = [data[i:min(l,i + self.k)] for i in xrange(0,l,self.k)]
		encrypt_keys = []
		encrypted_segments = []
		for text in segments:
			tour_number = randint(0,len(self.tours) - 1)
			random_tour_sequence = self.tours[tour_number]
			encrypt_keys.append(str(tour_number))
			if len(text) < self.k:
				indices = [number for number in random_tour_sequence if number < len(text)]
				encrypted_segment = ''.join([text[index] for index in indices])
				encrypted_segments.append(encrypted_segment)
			else:
				encrypted_segments.append(''.join([text[index] for index in random_tour_sequence]))
		return ''.join(encrypted_segments),'.'.join(encrypt_keys)
	
	def authorized_write(self):
		password = auth()
		cryptic_password,password_key = self.encrypt(password)
		try: 
			with open(self.ofile,'w') as f:						# create/open an output file
				f.write('\n'.join([self.decryption_key,self.encrypted_text]))
				f.write('\n-k-' + ' '.join([cryptic_password,password_key]))
		except IOError:
			self.error = "Output file couldn't be created/opened. Check directory read/write permissions"



