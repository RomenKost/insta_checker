from yaml import safe_load as yaml

from resources_manager.directory import path


class MessageKeys:
    start = 'start'

    turn_status_receive_True_True = 'turn_status_receive_True_True '
    turn_status_receive_True_False = 'turn_status_receive_True_False '
    turn_status_receive_False_True = 'turn_status_receive_False_True '
    turn_status_receive_False_False = 'turn_status_receive_False_False '


class Languages:
    ru = 'ru'


def get_messages(key: str, language='ru', _path='config.yaml') -> str:
    """
    This function get config data from yaml-file (that is by path) by key.
    """
    with open(path(_path), 'r', encoding='UTF-8') as file:
        if hasattr(MessageKeys, key) and hasattr(Languages, language):
            return yaml(file)[language][key]
