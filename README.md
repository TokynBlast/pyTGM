# Notes
This is version 2.1.1, version 0.0.0 was never released publically
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

# How it works

## Random

### Note: This is random, so the ouput may be different
Here is a sample code snippet to shuffle then remove random parts of a list of players:

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

## Boards
Boards add a new and unique way to keep track of scores.<br>
It takes inspiration from Minecraft's board style like this: Title = {player:value}<br>
Obviously, positioning and other stuff it up to you
### Add
Let's add a board titles Penguin, with a value, Amount, and set it as 400
```
tgm.Board.add("Penguins", "Amount", 400)
```
The values are Title, Player, value

### Modify
Like most animals, penguines breed... So, lets add 100 penguins!
```
tgm.Board.modify("Penguins", "Amount", "+", 100)
```
The values are Title, Player, Function, Amount

### Remove
Something terrible happened, THEY WERE ALL EATEN!!
So, lets remove their board 😊
```
tgm.Board.remove("Penguins")
```
Now there is NOTHING to suggest they ever lived!

> [!IMPORTANT]
> This version has been fully tested.<br>
> (Not all versions get tested, due to lack of memory skills sometimes)
