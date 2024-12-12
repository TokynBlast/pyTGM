boards = []

def new(title, component=None, value=None):
    for board in boards:
        if title in board:
            if component:
                board[title][component] = value
            return
    boards.append({title: {component: value}} if component else {title: {}})

def remove(title, component=None):
    for board in boards:
        if title in board:
            if component:
                if component in board[title]:
                    del board[title][component]
                    if not board[title]:
                        boards.remove(board)
                return
            else:
                boards.remove(board)
                return

def modify(title, component, function):
    for board in boards:
        if title in board and component in board[title]:
            board[title][component] = eval(f"{board[title][component]} {function}")
