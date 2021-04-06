from yaml import safe_load as yaml


def get_config(key: str, path='resources/config.yaml') -> str:
    """
    This function get config data from yaml-file (that is by path) by key.

    Config-YAML-file have following keys:
    'TelegramApiId', 'TelegramApiHash', 'TelegramPhoneNumber', 'InstagramUsername', 'InstagramPassword'
    """
    keys = ['TelegramApiId', 'TelegramApiHash', 'TelegramPhoneNumber', 'InstagramUsername', 'InstagramPassword']
    with open(path, 'r', encoding='UTF-8') as file:
        if key in keys:
            return yaml(file)[key]
