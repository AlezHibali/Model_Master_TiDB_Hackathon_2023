import subprocess
import MySQLdb
import certifi
import requests
from requests.auth import HTTPDigestAuth

HOST = "https://api.tidbcloud.com"

path_to_ca_cert = certifi.where()

connection = MySQLdb.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="4Ro6YCY7Vu8bQRe.root",
    password="xwlcRDBN6WfMLmrk",
    database="test",
    ssl={
    "ca": path_to_ca_cert
    }
    )

def pre_processing(input):
    return 0

def post_processing(output):
    return 0

with connection:
    with connection.cursor() as cursor:
        # cursor.execute("SHOW DATABASES;")
        # databases = cursor.fetchall()
        # system_databases = ('INFORMATION_SCHEMA', 'mysql', 'PERFORMANCE_SCHEMA', 'test')
        # user_defined_databases = [db[0] for db in databases if db[0] not in system_databases]
        # for database in user_defined_databases:
        #     print(database)

        # Define the command you want to execute
        command = "curl --digest --user \"q472yi96:6bc870a3-43f7-4dbb-a7f8-b97eaf50a565\"\
        --request POST \"https://eu-central-1.data.tidbcloud.com/api/v1beta/app/chat2query-YdBxnPzY/endpoint/chat2data\"\
        --header \"content-type: application/json\"\
        --data-raw \"{\
        \\\"cluster_id\\\": \\\"1379661944646225457\\\",\
        \\\"database\\\": \\\"Football_Club\\\",\
        \\\"tables\\\": [\\\"Football_Club\\\"],\
        \\\"instruction\\\": \\\"top 5 club that has the smallest average age, ignore ones that are zero or null\\\"\
        }\"\
        "

        # Execute the command in CMD and capture the output
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            print("Command output:")
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")