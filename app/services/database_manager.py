from typing import Optional
import pymongo


class DatabaseException(Exception):
    pass


def get_database(
    db_host: str, db_port: int, db_name: str
) -> Optional[pymongo.MongoClient]:
    """
    This function return a database connection
    """
    try:
        client = pymongo.MongoClient(host=db_host, port=db_port)
        db = client[db_name]
        return db
    except DatabaseException as e:
        raise e
