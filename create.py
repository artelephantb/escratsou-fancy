from contextlib import contextmanager
import compile

class CreateFunctions:
	def __init__(self, display_name: str, description: str, author: str, format: int, credit_overide=''):
		self.display_name = display_name
		self.description = description
		self.author = author
		self.format = format
		self.credit = credit_overide

		self.statements = []
		self.catagories = []
		self.current = []

		self.data = []

	@contextmanager
	def Namespace(self, name):
		try:
			yield
		finally:
			self.data.append({'namespace':name,'content':self.catagories})
			self.catagories = []

	@contextmanager
	def Catagory(self, name, format):
		try:
			yield
		finally:
			self.catagories.append({'format':format,'file':name,'content':self.statements})
			self.statements = []
	
	def Chat(self, message: str, target='ap', selector=[]):
		'''Add tag to entity'''
		structure = {'function':'chat','input':{'message':message,'target':target,'selector':selector}}
		self.statements.append(structure)

	def export(self, location: str, overide=False):
		compile.CompileData(self.display_name, self.description, self.author, self.format, self.data, credit_overide=self.credit).export(location, overide=overide)

generate = CreateFunctions('My datapack', 'Example', 'Me', 81)

with generate.Namespace('my-namespace'):
	with generate.Catagory('my-function', 'function'):
		generate.Chat('Hello!')

generate.export('output', overide=True)