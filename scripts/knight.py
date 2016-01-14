from os.path import exists, dirname, join

class KnightEncrypter(object):
	'''
		This class contains the common attributes to the Encryption and Decryption
		modules. 
		Attributes:
			ifile - input file name
			ofile - output file name
			x = number of rows in the chessboard
			y = number of columns in the chessboard
			k - segment length = x*y
			error - error messages if any
			tours = list of knight tours
			Default: x=3 & y=10 & k=30
	'''
	def __init__(self,ifile,ofile):
		self.ifile = join(dirname(__file__),ifile)
		self.ofile = join(dirname(__file__),ofile)
		self.x = 3
		self.y = 10
		self.k = self.x*self.y
		self.error = None
		self.tours = self.load_data()


	def load_data(self): 		# store the list of tour sequences 
		tours = []
		tours_data_path = join(dirname(__file__),"tours.txt")
		if exists(tours_data_path):
			with open(tours_data_path,'r') as f:
				for line in iter(f):
					x = map(int,line.split())
					tours.append(x)
		else:
			self.error = 'KnightEncrypter corrupted. The tours file is missing!'
			return None
		return tours

