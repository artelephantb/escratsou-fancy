import create

generate = create.CreateData('My datapack', 'Example', 'Me', 81)

with generate.Namespace('my-namespace'):
	with generate.Catagory('my-function', 'function'):
		generate.Chat('Hello')
		generate.Chat('World!')

generate.export('output', 'hello', overide=True)