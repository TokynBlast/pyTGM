# Notes
This is version 2.0.0, version 0.0.0 was never released publically
pyTGM stands for Python Terminal Game Maker

pyTGM includes things like b64 encoding and decoding, random, encryption, and a lot more.

I do **NOT** condone morally questionable use, or illegal activities with this tool, however,
by using this; whatever you make is your own responsibility, **NOT MINE**

This was created because I didn't like how complex pygame was.
I also liked the idea of uing ascii characters to make a world, rather than images.
It has become organized chaos, as in it is so organized, its complicated.
I, the creator am still practicing. I started practicing it when I released 1.0; Practice! You can evntually learn it!

For public code updates Go [here](https://github.com/TokynBlast/pyTGM/tree/main) and go to the newest version.
pyTGM is liscenced under Bspace, which was made by the author, Tokyn Blast.

# How it works
Here is a sample code snippet to shuffle then remove random parts of a list of players:

## Random
### Note: This is random, so the ouput may be different


Seq refers to sequence, which deals with lists
Example of random sequences:
```
players = [1, 2, 3, 4 ,5]
rnd = pytgm.players.random.seq.modify

rnd.shuffle(players)
rnd.remove(players, 3)

print(players)
```
The output could be:
[4, 2, 5]


For a binary number:
```
print(random.num.binary())
```
Output:
0

For a range of a random number:
```
random.num.integer(1, 5)
```
Output:
3


## File Reading

'name' refers to the file name, including the file type
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
graphics.clear()
```

To color the text:
```
graphics.color(r,g,b)
```
