boards = []

def new(title, component=None, value=None):
    """
    Makes a board, with a component and a value
    """
    for board in boards:
        if title in board:
            if component:
                board[title][component] = value
            return
    boards.append({title: {component: value}} if component else {title: {}})

def remove(title, component=None):
    """
    Removes a board or component of a board
    """
    for board in boards[:]:  # Create a shallow copy of the list for iteration
        if title in board:
            if component:
                if component in board[title]:
                    del board[title][component]
                    if not board[title]:
                        boards.remove(board)
            else:
                boards.remove(board)

def modify(title, component, function):
    """
    Modify a board's components

    In the future, this will become a class, where you can:
    
    """
    for board in boards[:]:  # Iterate over a shallow copy of the list
        if title in board and component in board[title]:
            board[title][component] = eval(f"{board[title][component]} {function}")

