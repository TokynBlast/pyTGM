# pyTGM (Python Terminal Game Maker)

>[!NOTE]
> There was an accidental deletion of the original pyTGM library. This is an updated version of the newest version I had on hand.
>
>This note will be deleted in the next version.

>[!NOTE]
> Versions dedicated to just Windows, Linux, macOS, and some others are still being developed.<br>
> For now, this works with most OSes.
>
>This note will be deleted when the versions for others are developed.

>[!NOTE]
>This will be on PyPi soon. Once PyPi tech support replies, and I change the email associated with my account (It wasn't the correct one), it will be uploaded.
>
>This note will be deleted once uploaded to pypi.

pyTGM is a simplified alternative to Pygame, focusing on ASCII and ANSI based game development, with utilities for encryption, randomization, and more.

## Features

### Random Operations
```python
# Shuffle and remove items from a list
players = [1, 2, 3, 4, 5]
rnd = pytgm.random.seq.modify
rnd.shuffle(players)
rnd.remove(players, 3)
print(players)  # Example output: [2, 5]

# Generate random numbers
random.num.binary()        # Returns 0 or 1
random.num.integer(1, 5)   # Returns number between 1 and 5
```

### File Operations
```python
file.read.document(name)           # Read entire file
file.read.line(name, line=0)       # Read specific line
```

### Graphics and Text Styling
```python
# Clear screen
graphics.cls()

# Color text (RGB)
graphics.color(0, 255, 0)  # Green text
graphics.res               # Reset color
```

### Sound Support
Works across Windows, macOS, and Linux:
```python
# Play audio file
sound('../sounds/mysound.mp3')
```

### Scoreboard System
```python
# Add a scoreboard (board, component, amount)
Board.add("Penguins", "Amount", 400)

# Modify score (board, component, function and value)
Board.modify("Penguins", "Amount", "+100")

# Remove board (board, component)
Board.remove("Penguins", "Amount")
```

### Local Server Support
```python
# Starting a server and client (PORT, message)
LocalServer(1080, {'MarkTheMight':((243,332), 57)})
```
An example of a returned value would be:
```python
{'LordMinion777':((0,0), 100)), 'Muyskerm':((245,334), 43)}
```

### Get Key
```python
getch(times)
```

## Links
>[!NOTE]
>As of Tuesday, December 10, 2024, 2:23 PST, these links are valid and do work.
- [Homepage](https://pytgm.tokynblast.space/home)
- [Documentation](https://pytgm.tokynblast.space/documentation/use)
- [Source Code](https://github.com/TokynBlast/pyTGM/tree/main)
- [Bug Tracker](https://github.com/TokynBlast/pyTGM/issues)
- [Changelog](https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt)

## License
pyTGM is licensed under Bspace, created by Tokyn Blast.
