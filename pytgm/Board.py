boards = []

def new(title, player=None, value=None):
    for board in Board.boards:
        if title in board:
            if player:
                board[title][player] = value
            return
    Board.boards.append({title: {player: value}} if player else {title: {}})

def remove(title, player=None):
    for board in Board.boards:
        if title in board:
            if player:
                if player in board[title]:
                    del board[title][player]
                    if not board[title]:
                        Board.boards.remove(board)
                return
            else:
                Board.boards.remove(board)
                return

def modify(title, player, f_value):
    for board in Board.boards:
        if title in board and player in board[title]:
            board[title][player] = eval(f"{board[title][player]} {f_value}")
