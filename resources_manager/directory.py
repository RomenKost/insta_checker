from os import getcwd


def __cur_dir() -> str:
    main_directory = getcwd()
    last_slash = main_directory[::-1].find('\\')
    return main_directory[:-last_slash]


def path(_path: str) -> str:
    return f'{__cur_dir()}resources\\{_path}'
