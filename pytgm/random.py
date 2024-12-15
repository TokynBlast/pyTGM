"""
Module for random number and sequence operations.

Provides functionality for generating random numbers, choosing and modifying lists.
"""

import time
import random


class Num:
    """
    A class for random number operations.
    """

    @staticmethod
    def integer(min_value, max_value, seed=None):
        """
        Generate a random integer within a specified range.

        Args:
            min_value (int): The minimum value.
            max_value (int): The maximum value.
            seed (int, optional): The seed for random number generation. Defaults to None.

        Returns:
            int: A random integer within the range.
        """
        if seed is None:
            seed = int(time.time() * 1000)
        random.seed(seed)
        return random.randint(min_value, max_value)

    @staticmethod
    def binary():
        """
        Generate a random binary value (0 or 1).

        Returns:
            int: 0 or 1.
        """
        return random.randint(0, 1)


class Seq:
    """
    A class for random sequence operations.
    """

    @staticmethod
    def choose(lst, amnt=1):
        """
        Choose a specified number of random elements from a list.

        Args:
            lst (list): The list to choose from.
            amnt (int): The number of elements to choose.

        Returns:
            list: A list of randomly chosen elements.
        """
        return random.sample(lst, amnt)

    class Modify:
        """
        A nested class for modifying sequences.
        """

        @staticmethod
        def shuffle(lst, times=1):
            """
            Shuffle a list a specified number of times.

            Args:
                lst (list): The list to shuffle.
                times (int): The number of times to shuffle.

            Returns:
                list: The shuffled list.
            """
            shuffled_list = lst[:]
            for _ in range(times):
                random.shuffle(shuffled_list)
            return shuffled_list

        @staticmethod
        def duplicate(lst, times=1):
            """
            Duplicate and shuffle a list a specified number of times.

            Args:
                lst (list): The list to duplicate and shuffle.
                times (int): The number of times to duplicate and shuffle.

            Returns:
                list: The duplicated and shuffled list.
            """
            duplicated_list = lst * times
            random.shuffle(duplicated_list)
            return duplicated_list

        @staticmethod
        def remove(lst, amnt):
            """
            Remove a specified number of random elements from a list.

            Args:
                lst (list): The list to remove elements from.
                amnt (int): The number of elements to remove.

            Returns:
                list: The modified list after removing elements.
            """
            modified_list = lst[:]
            for _ in range(amnt):
                if modified_list:
                    modified_list.remove(random.choice(modified_list))
            return modified_list
