"""
Module for managing boards, their components, and values.

Provides functions to create, modify, and remove boards and their components.
"""

from operator import add, sub mul, truediv, mod

boards = []

OPERATIONS = {
    '+':add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '%': mod
}

def new(title, component=None, value=None):
    """
    Creates a new board with an optional component and value.
    
    Args:
        title (str): The title of the board.
        component (str, optional): The name of the component.
        value (any, optional): The value of the component.
    """
    for board in boards:
        if title in board:
            if component:
                board[title][component] = value
            return
    boards.append({title: {component: value}} if component else {title: {}})

def remove(title, component=None):
    """
    Removes a board or a component of a board.
    
    Args:
        title (str): The title of the board.
        component (str, optional): The component to remove.
    """
    for board in boards[:]:  # Iterate over a shallow copy of the list
        if title in board:
            if component:
                if component in board[title]:
                    del board[title][component]
                    if not board[title]:  # Remove the board if empty
                        boards.remove(board)
            else:
                boards.remove(board)

def modify(title, component, operation, operand):
    """
    Modifies a board's component value using the specified operation and operand.
    
    Args:
        title (str): The title of the board.
        component (str): The component to modify.
        operation (str): The operation ('+', '-', '*', '/', '%').
        operand (int or float): The value to apply the operation with.
    """
    for board in boards[:]:  # Iterate over a shallow copy of the list
        if title in board and component in board[title]:
            current_value = board[title][component]
            if operation in OPERATIONS:
                board[title][component] = OPERATIONS[operation](current_value, operand)
