from contextlib import contextmanager
import os

import tools
import compile

class CreateFunctions:
	def __init__(self, display_name: str, description: str, author: str, version: int, credit_overide=''):
		self.display_name = display_name
		self.description = description
		self.author = author
		self.version = version
		self.credit = credit_overide

		self.statements = []
		self.catagories = []
		self.current = []

		self.data = []

	@contextmanager
	def Namespace(self, name: str):
		try:
			yield
		finally:
			self.data.append({'namespace':name,'content':self.catagories})
			self.catagories = []

	@contextmanager
	def Catagory(self, name: str, catagory: str):
		try:
			yield
		finally:
			self.catagories.append({'catagory':catagory,'file':name,'content':self.statements})
			self.statements = []
	
	def Chat(self, message: str, target='ap', selector=[]):
		structure = {'function':'chat','input':{'message':message,'target':target,'selector':selector}}
		self.statements.append(structure)

	def export_source(self, location: str, file: str, overide=False):
		if os.path.isfile(os.path.join(location, file + '.json')):
			if overide:
				os.remove(os.path.join(location, file + '.json'))
			else:
				tools.error('Source Datapack Duplicate', 'Source datapack already existant at', os.path.join(location, file))
		tools.create_json(location, file + '.json', {'overide':overide,'display_name':self.display_name,'description':self.description,'author':self.author,'version':self.version,'data':self.data})

	def export(self, location: str, overide=False):
		compile.CompileData(self.display_name, self.description, self.author, self.version, self.data, credit_overide=self.credit).export(location, overide=overide)