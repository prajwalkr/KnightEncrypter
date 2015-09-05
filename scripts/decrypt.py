from os.path import *
from auth import auth_decrypt

def Decrypt(ifile,ofile,x = 3,y = 10):
	try:																	# Open encrypted file
		with open(join(dirname(__file__),ifile),'r') as f:
			__ = 0
			keys = pkeys = []												# get the sequence of keys in this
			text = ''														# get the encrypted data in this
			k = x*y
			for line in iter(f):
				if len(line) > 3 and line[:3] == '-k-':
					try:
						password,pkey = line[3:].split()
						pkeys = map(int,pkey.split('.'))
						text = text[:len(text) - 1]
					except:
						return 'File data invalid!'
					break
				if __ == 0:
					try:
						keys = map(int,line[:len(line) - 1].split('.'))
					except:
						return "File data invalid!"
					__ += 1
				else:
					text += line
	except:
		return "Encrypted file absent"

	def get_data(): 		# get tour sequences 
		try:
			with open(join(dirname(__file__),"tours.txt"),'r') as f:
				tours = []
				for line in iter(f):
					x = map(int,line.split())
					tours.append(x)
		except:
			return "KnightEncrypter corrupted. Reinstall the software"
		return tours

	tours = get_data()
	if isinstance(tours,basestring):	# If tour data is missing...
		return tours

	def get_decrypted_data(data,keys):
		l = len(data)
		i = x = 0
		decrypted_bits = []														# decrypt segment by segment
		while i < l:
			b = data[i:min(i+k,l)]
			lb = len(b)
			key = keys[x]
			order = [None for _  in range(lb)]
			t = 0
			for j in range(len(tours[key])):
				if tours[key][j] < lb:
					order[tours[key][j]] = b[t]
					t += 1
			decrypted_bits.append(''.join(order))
			i += k
			x += 1
		return ''.join(decrypted_bits)
	password = get_decrypted_data(password,pkeys)
	auth_decrypt(password)
	decrypted_data = get_decrypted_data(text,keys)
	try:
		with open(join(dirname(__file__),ofile),'w') as f:
			f.write(decrypted_data)						# write to output
	except:
		return "Output file couldn't be created. Check directory write permissions"

	return "Data successfully decrypted"
