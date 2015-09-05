from random import *
from os.path import *
from auth import auth

def Encrypt(ifile,ofile,x = 3,y = 10):
	k = x*y 				# segment length
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

	def get_encrypted_data(a):
		l = len(a)
		encrypted_bits = []
		encrypt_key = []
		i = 0
		while i < l:						# Take segments and encrypt each
			b = a[i:min(l,i+k)]
			lb = len(b)
			x = randint(0,p)
			encrypt_key.append(str(x))
			if lb < k:
				order = []
				for j in tours[x]:
					if j < lb:
						order.append(j)
				c = ''
				for x in order:
					c += b[x]
				encrypted_bits.append(c)
			else:
				c = ''
				for j in tours[x]:
					c += b[j]
				encrypted_bits.append(c)
			i += k
		return encrypted_bits,encrypt_key

	tours = get_data()
	if isinstance(tours,basestring):	# If tour data is missing...
		return tours

	p = len(tours) - 1

	try:
		with open(join(dirname(__file__),ifile),'r') as f:		# Read file to encrypt
			a = f.readlines()
	except:
		return "Input file doesn't exist!"	

	a = ''.join(v for v in a)			# Merge the list of strings as one string
	encrypted_bits,encrypt_key = get_encrypted_data(a)
	password = auth()
	cryptic_pass,pkey = get_encrypted_data(password)
	try:
		with open(join(dirname(__file__),ofile),'w') as f:			# create/open an output file
			f.write('.'.join(encrypt_key) + '\n' + ''.join(encrypted_bits))
			f.write('\n-k-' + ''.join(cryptic_pass) + ' ' + '.'.join(pkey))
	except:
		return "Output file couldn't be created. Check directory write permissions"
	return "File data encrypted!"