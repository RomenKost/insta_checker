from sqlite3 import connect

from resources_manager.directory import path


def __sql(query: str, _path='data.db'):
    """
    This function works with SQL-database (DB), does any queries (from SELECT to INSERT).

    :param query: SQL-query
    :param _path: path to the DB
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


def write_story(story_id: int, user: str, current_datetime: str):
    __sql(f"INSERT INTO stories(id, user, datetime) "
          f"VALUES({story_id}, '{user}', '{current_datetime}')")


def last_story_id(user: str):
    return __sql(f"SELECT id "
                 f"FROM stories "
                 f"WHERE user = {user} "
                 f"ORDER BY datetime DESC"
                 f"LIMIT 1 ")


def user_exist(user_id: int):
    return bool(__sql(f"SELECT * "
                      f"FROM users "
                      f"WHERE id = {user_id}"))


def add_user(user_id: int):
    if not user_exist(user_id):
        __sql(f"INSERT INTO users(id) "
              f"VALUES({user_id}) ")


def get_status(user_id):
    if user_exist(user_id):
        return __sql(f"SELECT status")


def change_status(user_id: str, status: bool):
    __sql(f"UPDATE users "
          f"SET status = '{status}' "
          f"WHERE id = {user_id}")
