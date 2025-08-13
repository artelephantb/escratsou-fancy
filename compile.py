import json
import os
from shutil import rmtree

class Tools:
	def create_text(location: str, file: str, content: str):
		with open(os.path.join(location, file), 'x') as output:
			output.write(content)

	def create_json(location: str, file: str, content: dict):
		with open(os.path.join(location, file), 'x') as output:
			json.dump(content, output, indent='\t')
	
	def read_source(location: str):
		with open(location, 'r') as source:
			return json.load(source)

class CompileData:
	def __init__(self, display_name: str, description: str, format: int, author: str, content: list, credit_overide=''):
		'''Compile datapacks'''
		self.display_name = display_name
		self.description = description
		self.format = format
		self.author = author
		self.content = content

		# Check if credit exists
		self.credit = credit_overide
		if self.credit == '':
			self.credit = 'This datapack has been made by \'' + self.author + '\', made with Escratsou Fancy!'
	
	def get_target(self, target: str, selector: list):
		'''Get target in datapack form'''
		final_target = ''
		if target == 's': # Executer
			final_target = '@s'
		elif target == 'ae': # All entities
			final_target = '@e'
		elif target == 'ap': # All players
			final_target = '@a'
		elif target == 'ne': # Nearest entity
			final_target = '@n'
		elif target == 'np': # Nearest player
			final_target = '@p'
		elif target == 're': # Random entity
			final_target = '@e[limit=1,sort=random,'
		elif target == 'rp': # Random player
			final_target = '@r'
		
		if len(selector) > 0:
			if not '[' in final_target:
				final_target += '['
			for selection in selector:
				final_target += selection + ','
			final_target += ']'
		elif '[' in final_target:
			final_target += ']'
		
		return final_target

	def create_functions(self, functions: list):
		'''Create functions in datapack form'''
		final = ''
		for function in functions:
			if function['function'] == 'chat':
				target = ''
				if 'selector' in function['input']:
					target = self.get_target(function['input']['target'], function['input']['selector'])
				else:
					target = self.get_target(function['input']['target'], [])

				final += 'tellraw ' + target + ' \'Escratsou Test Message\'\n'
			elif function['function'] == 'default':
				target = ''
				final += function['input']['function'] + '\n'
		return final

	def export(self, location: str, overide=False):
		'''Export datapacks in file form'''
		# Check if datapack exists
		if os.path.isdir(os.path.join(location, self.display_name)):
			if overide:
				rmtree(os.path.join(location, self.display_name))
			else:
				raise FileExistsError('Datapack existant at', os.path.join(location, self.display_name))
		
		# Create base directories
		os.makedirs(os.path.join(location, self.display_name, 'data'))

		# Create credit file
		Tools.create_text(location, self.display_name + '/.credit', self.credit)

		# Create pack.mcmeta
		Tools.create_json(location, self.display_name + '/pack.mcmeta', {'pack':{'pack_format':self.format,'description':self.description}})

		# For each namspace
		for namespace in self.content:
			os.mkdir(os.path.join(location, self.display_name, 'data', namespace['namespace']))
			# Catagories like functions, advancements, tags, etc...
			for catagory in namespace['content']:
				directory = ''
				if 'directory' in catagory:
					directory = catagory['directory']

				if catagory['format'] == 'function':
					os.makedirs(os.path.join(location, self.display_name, 'data', namespace['namespace'], 'function', directory))
					Tools.create_text(os.path.join(location, self.display_name, 'data', namespace['namespace'], 'function', directory), catagory['file'] + '.mcfunction', str(self.create_functions(catagory['content'])))