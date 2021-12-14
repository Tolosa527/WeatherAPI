import pymongo
import settings
import secrets

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.exceptions import HTTPException
from fastapi import Depends
from starlette import status


def get_current_username(
        credentials: HTTPBasicCredentials = Depends(HTTPBasic())) -> str:
    '''
        This is a basic authentication funtion that recieved some
        credenctials, verify them and return a user authenticated
    '''

    # I have to inclued this ones in the config file
    client  = pymongo.MongoClient(settings.DB_URI)
    db      = client["weather"]
    col     = db["users_authorized"]
    user    = ''

    # find the user in the databases
    query = {"password":credentials.password}
    projection = {"password":1, "username":1}
    
    try:
        user = col.find_one(query, projection)
    except Exception as e:
        print(e)

    if user:
        username = user.get("username", None)
        password = user.get("password", None)
        correct_username = secrets.compare_digest(credentials.username, username)
        correct_password = secrets.compare_digest(credentials.password, password)

        if not correct_username or not correct_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
                headers={"WWW-Authenticate": "Basic"},
            )
