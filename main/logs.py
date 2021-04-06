from datetime import datetime


"""
This module includes classes and methods to printing messages about script status. 
"""


class Console:
    """
    This class has methods printing messages to the console. All messages are printed by class method '__print'.
    """
    def __init__(self, name):
        """

        :param name: name of program,
        """
        self.__name = name

    def __print(self, message: str, user: str, show=True):
        """
        This method prints into the console a message in the format
        '[name of program, time in the format 'YYYY.MM.DD HH:MM:SS'] {message} by {user}'

        :param message: message, that
        :param user:
        :param show:
        """
        if show:
            print(f'[{self.__name}, {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}] {message} by {user}')

    def start(self):
        self.__print('the script was started', 'admin')

    def new_insta_loop(self, user: str):
        self.__print(f'the process of finding new story of "{user}" was started', 'insta-bot')

    def story_was_saved(self, user):
        self.__print(f'The story of "{user}" was saved', 'insta-bot')
