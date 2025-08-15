# Escratsou Fancy ![Logo](https://github.com/artelephantb/escratsou-fancy/blob/main/snake.png)
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

Another demo using a source file:
```python
Tools.compile_source('../my-source.json', '../my-output-directory/')
```
