from knight import KnightEncrypter
import os
from itertools import izip
from auth import authorize_decryption

class Decrypt(KnightEncrypter):
	'''
		Contains the following attributes, apart from the parent class' attributes:
		decrypted_text - decrypted file text
		decryption_keys - encryption keys used to encrypt segments of the file before(it will be stored in the file)
		text - the data of the file that is to be encrypted
	'''
	def __init__(self,ifile,ofile):
		KnightEncrypter.__init__(self,ifile,ofile)
		if self.error is None:
			if os.path.exists(self.ifile):
				self.decryption_keys = []
				self.text = ''
				self.load_encrypted_data()
			else:
				self.error = "Input file doesn't exist!"
			if self.error is None and self.authenticated():
				self.decrypted_text = self.decrypt(self.text,self.decryption_keys)
				self.write_back()

	def load_encrypted_data(self):
		with open(self.ifile,'r') as f:
			encryption_key_line = True
			for line in f:
				if encryption_key_line:
					try:
						self.decryption_keys = map(int,line[:len(line) - 1].split('.'))
					except:
						self.error = 'File data invalid!'
						break
					encryption_key_line = False
				elif len(line) > 3 and line[:3] == '-k-':
					try:
						self.cryptic_password, password_key = line[3:].split()
						self.password_encryption_keys = map(int,password_key.split('.'))
						self.text = self.text[:-1]
					except:
						self.error = 'File data invalid!'
						break
				else:
					self.text += line

	def authenticated(self):
		password = self.decrypt(self.cryptic_password,self.password_encryption_keys)
		authorize_decryption(password)
		return True

	def decrypt(self,text,decryption_keys):
		l = len(text)
		decrypted_bits = []
		encrypted_segments = [text[i:i+min(self.k,l)] for i in xrange(0,l,self.k)]
		for tour_index,encrypted_segment in izip(decryption_keys,encrypted_segments):
			tour_sequence = self.tours[tour_index]
			decrypted_bit = [None for _ in range(len(encrypted_segment))]
			i = 0
			for number in tour_sequence:
				if number < len(encrypted_segment):
					decrypted_bit[number] = encrypted_segment[i]
					i += 1
			decrypted_bits.append(''.join(decrypted_bit))
		return ''.join(decrypted_bits)
		
	def write_back(self):
		try:
			with open(self.ofile,'w') as f:
				f.write(self.decrypted_text)
		except IOError:
			self.error = "Output file couldn't be created/opened. Check directory read/write permissions"