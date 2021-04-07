from yaml import safe_load as yaml

from resources_manager.directory import path


class Keys:
    TelegramBotToken = 'TelegramBotToken'
    InstagramUsername = 'InstagramUsername'
    InstagramPassword = 'InstagramPassword'


def get_config(key: str, _path='config.yaml') -> str:
    """
    This function get config data from yaml-file (that is by path) by key.
    """
    with open(path(_path), 'r', encoding='UTF-8') as file:
        if hasattr(Keys, key):
            return yaml(file)[key]
