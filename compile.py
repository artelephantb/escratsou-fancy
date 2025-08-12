import os
from shutil import rmtree

class CompileData:
	'''Compile source into datapacks'''
	def __init__(self, source: dict, out_folder: str, name: str, namespace: str, author: str, description: str, version: str):
		self.source = source
		self.out_folder = out_folder

		self.name = name
		self.namespace = namespace
		self.author = author
		self.description = description
		self.version = version

		self.loads = ''
		self.ticks = ''
	
	def get_target(self, target, selector=None):
		'''Converts readable entity targets into datapack targets'''
		target_type = target # For direct player names
		if target == 'self':
			target_type = '@s'
		elif target == 'all-players':
			target_type = '@a'
		elif target == 'nearest-players':
			target_type = '@p'
		elif target == 'random-players':
			target_type = '@r'
		elif target == 'all-entities':
			target_type = '@e'
		elif target == 'nearest-entities':
			target_type = '@n'
		if selector:
			target_type += '['
			for select in selector:
				target_type += select['type'] + '=' + select['value'] + ','
			target_type += ']'
		return target_type

	def lookup(self, function: dict):
		'''Different possible functions for datapacks'''
		# Check for error
		if not 'function' in function:
				print('Key Error: \'function\' not in block')
				exit(1)
		# Show message in chat
		if function['function'] == 'chat':
			selector = None
			if 'selector' in function['input']:
				selector = function['input']['selector']
			target = self.get_target(function['input']['target'], selector=selector)
			return 'tellraw ' + target + ' \'' + function['input']['message'] + '\''
		# Give player tags
		elif function['function'] == 'tag':
			selector = None
			if 'selector' in function['input']:
				selector = function['input']['selector']
			target = self.get_target(function['input']['target'], selector=selector)
			if function['input']['operation'] == 'list':
				return 'tag ' + target + ' list'
			elif function['input']['operation'] == 'add':
				return 'tag ' + target + ' add ' + function['input']['name']
			elif function['input']['operation'] == 'remove':
				return 'tag ' + target + ' remove ' + function['input']['name']

	def export(self, overide=False):
		'''Exports into datapack'''
		# Remove and create files
		if overide and os.path.isdir(os.path.join(self.out_folder, self.name)):
			rmtree(os.path.join(self.out_folder, self.name))
		os.makedirs(os.path.join(self.out_folder, self.name + '/data/minecraft/tags/function'))
		os.makedirs(os.path.join(self.out_folder, self.name + '/data/' + self.namespace + '/function'))

		# Create pack configeration
		with open(os.path.join(self.out_folder, self.name + '/pack.mcmeta'), 'x') as document:
			document.write('{"pack":{"description":"' + self.description + '","pack_format":' + self.version + '}}')

		# Create loads
		if self.source['load']:
			with open(os.path.join(self.out_folder, self.name + '/data/minecraft/tags/function/load.json'), 'x') as document:
				document.write('{"replace":false,"values":["' + self.namespace + ':load"]}')
			for block in self.source['load']:
				self.loads += self.lookup(block)  + '\n'

			# Output files
			with open(os.path.join(self.out_folder, f'{self.name}/data/{self.namespace}/function/load.mcfunction'), 'x') as document:
				document.write(self.loads)

		# Create ticks
		if self.source['tick']:
			with open(os.path.join(self.out_folder, self.name + '/data/minecraft/tags/function/tick.json'), 'x') as document:
				document.write('{"replace":false,"values":["' + self.namespace + ':tick"]}')
			for block in self.source['tick']:
				self.ticks += self.lookup(block)  + '\n'

			# Output files
			with open(os.path.join(self.out_folder, f'{self.name}/data/{self.namespace}/function/tick.mcfunction'), 'x') as document:
				document.write(self.ticks)

		# Create user controlled files
		if self.source['paper']:
			for block in self.source['paper']:
				with open(os.path.join(self.out_folder, block['file']), 'a') as document:
					document.write(block['document'])