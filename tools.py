import json
import os

def create_text(location: str, file: str, content: str):
	with open(os.path.join(location, file), 'x') as output:
		output.write(content)

def create_json(location: str, file: str, content: dict):
	with open(os.path.join(location, file), 'x') as output:
		json.dump(content, output, indent='\t')

def finish(catagory, *message):
	print('\033[96m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[92m' + catagory + '\033[0m: \033[92m' + ' '.join(message) + '\033[0m')
	print('\033[96m*', '~' * 64, '*\033[0m')
	exit(0)

def warning(catagory, *message):
	print('\033[93m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[95m' + catagory + '\033[0m: \033[95m' + ' '.join(message) + '\033[0m')
	print('\033[93m*', '~' * 64, '*\033[0m')

def error(catagory, *message):
	print('\033[95m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[91m' + catagory + '\033[0m: \033[91m' + ' '.join(message) + '\033[0m')
	print('\033[95m*', '~' * 64, '*\033[0m')
	exit(1)