import subprocess
import MySQLdb
import certifi
import requests
from requests.auth import HTTPDigestAuth
import json

path_to_ca_cert = certifi.where()

def addUserInfo(username, pwd):
    # setup connection each time api is called
    connection = MySQLdb.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4Ro6YCY7Vu8bQRe.root",
    password="xwlcRDBN6WfMLmrk",
    database="TiDB_hackathon_2023",
    autocommit=True, # otherwise cannot save changes
    ssl={
    "ca": path_to_ca_cert
    }
    )

    with connection:
        with connection.cursor() as cursor:
            # Execute SQL statement
            try:
                cursor.execute("USE TiDB_hackathon_2023; INSERT INTO user_info (username, password, status, favorite_models) VALUES ('"+username+"', '"+pwd+"', 'active', '');")
            except:
                return False

    return True

def checkUserInfo(username):
    # Not Implemented Yet
    pass

def getUserFavModels(username):
    # setup connection each time api is called
    connection = MySQLdb.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4Ro6YCY7Vu8bQRe.root",
    password="xwlcRDBN6WfMLmrk",
    database="TiDB_hackathon_2023",
    ssl={
    "ca": path_to_ca_cert
    }
    )

    favorite_models = []

    with connection:
        with connection.cursor() as cursor:
            # Execute SQL statement
            cursor.execute("SELECT favorite_models FROM TiDB_hackathon_2023.user_info WHERE username = '" + username + "'")
            result = cursor.fetchone()

            if result:
                favorite_models = result[0].split('; ')

    return favorite_models

def modifyUserFavModels(username, model):
    # setup connection each time api is called
    connection = MySQLdb.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4Ro6YCY7Vu8bQRe.root",
    password="xwlcRDBN6WfMLmrk",
    database="TiDB_hackathon_2023",
    autocommit=True, # otherwise cannot save changes
    ssl={
    "ca": path_to_ca_cert
    }
    )

    favorite_models = []
    add_delete = 0 # 0 for error, 1 for add, -1 for remove

    with connection:
        with connection.cursor() as cursor:
            # Execute SQL statement
            cursor.execute("SELECT favorite_models FROM TiDB_hackathon_2023.user_info WHERE username = '" + username + "'")
            result = cursor.fetchone()

            if result:
                favorite_models = result[0]

                # check and handle if empty
                if favorite_models:
                    favorite_list = favorite_models.split('; ')
                else:
                    favorite_list = []

                # Check if the provided model is already in favorites
                if model in favorite_list:
                    favorite_list.remove(model)
                    add_delete = -1
                else:
                    favorite_list.append(model)
                    add_delete = 1

                # Update the favorite models in the database
                updated_favorite_models = '; '.join(favorite_list)
                cursor.execute("UPDATE TiDB_hackathon_2023.user_info SET favorite_models = %s WHERE username = %s", (updated_favorite_models, username))

    return add_delete

    