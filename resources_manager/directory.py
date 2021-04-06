from os import getcwd
from urllib.request import urlopen


def __cur_dir() -> str:
    main_directory = getcwd()
    last_slash = main_directory[::-1].find('\\')
    return main_directory[:-last_slash]


def path(_path: str) -> str:
    return f'{__cur_dir()}resources\\{_path}'


def save_file(url: str, name: str, story_type: str):
    with open(path(f'stories\\{name}.{story_type}'), 'wb') as file:
        send = urlopen(url).read()
        file.write(send)
