from contextlib import contextmanager
import compile

class CreateFunctions:
	def __init__(self):
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

	def export(self, overide=False):
		print(self.data)

generate = CreateFunctions()

with generate.Namespace('my-namespace'):
	with generate.Catagory('my-function', 'function'):
		pass

generate.export()