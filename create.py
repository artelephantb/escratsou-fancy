from contextlib import contextmanager
import compile

# Handle errors
def error(error_type, message):
	'''Errors'''
	print()
	print('*' * 51)
	print(error_type + ':', message)
	print('*' * 51)
	print()
	exit(1)

class CreateFunctions:
	'''Uses python language'''
	def __init__(self, out_folder: str, name: str, namespace: str, author: str, description: str, version: str):
		self.out_folder = out_folder
		self.name = name
		self.namespace = namespace
		self.author = author
		self.description = description
		self.version = version

		self.statements = []
		self.current = []

		self.loads = []
		self.ticks = []
		self.papers = []

	@contextmanager
	def load(self):
		'''When datapack loads'''
		if self.loads:
			error('Duplicate Error', 'Only one load allowed')

		try:
			yield
		finally:
			self.loads = self.statements
			self.statements = []

	@contextmanager
	def tick(self):
		'''Every tick'''
		if self.ticks:
			error('Duplicate Error', 'Only one tick allowed')

		try:
			yield
		finally:
			self.ticks = self.statements
			self.statements = []

	def chat(self, message: str, target='all-players', selector=[]):
		'''Send message in chat'''
		structure = {'function':'chat','input':{'message':message,'target':target,'selector':selector}}
		if self.current:
			self.current[-1]['child'].append(structure)
		else:
			self.statements.append(structure)
	
	def tag(self, tag: str, operation='add', target='all-players', selector=[]):
		'''Add tag to entity'''
		structure = {'function':'tag','input':{'name':tag,'operation':operation,'target':target,'selector':selector}}
		if self.current:
			self.current[-1]['child'].append(structure)
		else:
			self.statements.append(structure)
	
	def export(self, overide=False):
		compile.CompileData({'load':self.loads,'tick':self.ticks, 'paper':[]}, self.out_folder, self.name, self.namespace, self.author, self.description, self.version).export(overide=overide)