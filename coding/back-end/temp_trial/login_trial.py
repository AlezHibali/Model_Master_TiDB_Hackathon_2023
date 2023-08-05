import subprocess
import MySQLdb
import certifi
import requests
from requests.auth import HTTPDigestAuth
import json

path_to_ca_cert = certifi.where()

# make data output with newlines 
def format_data(data):
    formatted_data = "\n".join(str(item) for item in data)
    return formatted_data

def pre_processing(input):
    suffix = ", ignore ones that are zero or null, include model name if possible"
    return input + suffix

# PROCESSING FROM:
# {"type":"chat2data_endpoint","data":{"columns":[{"col":"name","data_type":"VARCHAR","nullable":true},
# {"col":"average_age","data_type":"DOUBLE","nullable":true}],"rows":[{"average_age":"21","name":"Orduspor"},
# {"average_age":"21","name":"Akhisarspor"},{"average_age":"21.4","name":"Bursaspor"},{"average_age":"21.6","name":"FC Nordsjaelland"},
# {"average_age":"22","name":"Balikesirspor"}],
# "result":{"code":200,"message":"Query OK!","start_ms":1689643589903,"end_ms":1689643595333,"latency":"5.430048563s",
# "row_count":5,"row_affect":0,"limit":50,
# "sql":"SELECT `name`, `average_age` FROM `Football_Club` WHERE `average_age` \u003e 0 AND `average_age` IS NOT NULL ORDER BY `average_age` ASC LIMIT 5;",
# "ai_latency":"5.400326162s","databases":["Football_Club"]}}}
# TO OUTPUT:
# status code, data
def post_processing(output):
    # Parse the JSON data into a Python dictionary
    data_dict = json.loads(output)

    # Extract the "data" and "code" fields
    code = data_dict.get('data', {}).get('result', {}).get('code')

    if code == 200:
        data_row = data_dict.get('data', {}).get('rows', {})
        # Convert 'model size' values to include units
        for row in data_row:
            if 'model_size' in row:
                pass
        return data_row, 200
    elif code == 405:
        return "Error: no available request tokens, try tomorrow!", 405
    else:
        return "Error", code
    
def connect_and_process(username):
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

# output0 is formatted data, output1 is status code
def main_process(input):
    # prompt = pre_processing(input)
    # out = connect_and_process(prompt)
    # output = post_processing(out)
    # return format_data(output[0]), output[1]
    return connect_and_process(input)

if __name__ == "__main__":
    input = "admin"
    out = main_process(input)
    print(out)
    # print("status code: " + str(out[1]) + "\n" + out[0])
    

# sample output
