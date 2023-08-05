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
    ssl={
    "ca": path_to_ca_cert
    }
    )

    with connection:
        with connection.cursor() as cursor:
            # Execute SQL statement
            try:
                cursor.execute("INSERT INTO user_info (username, password, status) VALUES ('"+username+"', '"+pwd+"', 'active');")
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