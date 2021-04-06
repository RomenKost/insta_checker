from sqlite3 import connect

from resources_manager.directory import path


def __sql(query: str, _path='data.db'):
    """
    This function works with SQL-database (DB), does any queries (from SELECT to INSERT).

    :param query: SQL-query
    :param path: path to the DB
    :return result, that DB return on query 'query'
    """
    _path = path(_path)

    database = connect(_path)
    cursor = database.cursor()

    cursor.execute(query)
    result = cursor.fetchall()
    database.commit()

    database.close()
    return result


def is_story_saved(story_id: int) -> bool:
    result = __sql(f"SELECT * "
                   f"FROM stories "
                   f"WHERE id = {story_id}")
    return bool(result)


def write_story(story_id: int, user: str):
    __sql(f"INSERT INTO stories(id, user) "
          f"VALUES({story_id}, '{user}')")
