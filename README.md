# Notes
This is version 2.0.0, version 0.0.0 was never released publically
pyTGM stands for Python Terminal Game Maker

pyTGM includes things like b64 encoding and decoding, random, encryption, and a lot more.

I do **NOT** condone morally questionable use, or illegal activities with this tool.
By using this; whatever you make is your own responsibility, **NOT MINE**

This was created because I didn't like how complex pygame was.
I also liked the idea of uing ascii characters to make a world, rather than images.
It has become organized chaos, as in it is so organized, its complicated.
I, the creator am still practicing. I started practicing it when I released 1.0; Practice! You can evntually learn it!

For public code updates Go [here](https://github.com/TokynBlast/pyTGM/tree/main) and go to the newest version.
pyTGM is liscenced under Bspace, which was made by the author, Tokyn Blast.

All versions before 2.0.0 were never tested. When testing 2.0.0, Tokyn Blast came across atleast 10 errors...

If anybody has any suggestions on how to remove the need for the time library, while still getting a random number, using something that all OSs will have (or atleast most)

# How it works
Here is a sample code snippet to shuffle then remove random parts of a list of players:

## Random
### Note: This is random, so the ouput may be different


Seq refers to sequence, which deals with lists
Example of random sequences:
```
players = [1, 2, 3, 4 ,5]
rnd = pytgm.random.seq.modify

rnd.shuffle(players)
rnd.remove(players, 3)

print(players)
```
Output :
[2, 5]


For a binary number:
```
print(random.num.binary())
```
Output:
0

For a random number in a range:
```
random.num.integer(1, 5)
```
Output:
3


## File Reading

'name' refers to the path to the file, including the file name
```
file.read.document(name)
file.read.line(name, line=0)
file.read.char(name, character_num)
```
It is file.read.document, instead of file.document,
because I have to make the code for file manipulation.


## Graphics
To clear the screen:
```
graphics.cls()
```

## Text Markdown:

### Color:
1. Printing Color
```
graphics.color.RGB(r,g,b)
```
3. Color Reset
```
graphics.color.res
```

Like most games, you want to play sound... Well, when 2.1.0 was released, you could!

Let's assume this file structure:
```
project/
     code/
          playSound.py
     sounds/
          mysound.mp3
```
To play sound this would be what you do:
```
sound('../sounds/mysound.mp3')
```
Sound works in macOS, Windows, and Linux!
