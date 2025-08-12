# Escratsou Fancy
Escratsou, but fancy.

## About
*Escratsou Fancy* is a Minecraft datapack generator, created to be used in **Python**.

## Demonstration
```python
import create

generate = create.CreateFunctions('...my-output', 'My Datapack', 'my-datapack', 'Me', 'This is a example datapack created using Escratsou Fancy!', '71')

with generate.load():
	generate.tag('my-tag')
	generate.chat('Hello World!', 'all-players', [{'type':'tag', 'value':'my-tag'}])

generate.export()
```