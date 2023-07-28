import MySQLdb
import certifi
import requests
from requests.auth import HTTPDigestAuth

HOST = "https://api.tidbcloud.com"

path_to_ca_cert = certifi.where()

def trial_connection():
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

    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            system_databases = ('INFORMATION_SCHEMA', 'mysql', 'PERFORMANCE_SCHEMA', 'test')
            user_defined_databases = [db[0] for db in databases if db[0] not in system_databases]
            for database in user_defined_databases:
                print(database)

def get_all_projects(public_key: str, private_key: str) -> dict:
    """
    Get all projects
    :param public_key: Your public key
    :param private_key: Your private key
    :return: Projects detail
    """
    url = f"{HOST}/api/v1beta/projects"
    resp = requests.get(url=url, auth=HTTPDigestAuth(public_key, private_key))
    if resp.status_code != 200:
        print(f"request invalid, code : {resp.status_code}, message : {resp.text}")
        raise Exception(f"request invalid, code : {resp.status_code}, message : {resp.text}")
    return resp.json()

def get_cluster_by_id(public_key: str, private_key: str, project_id: str, cluster_id: str) -> dict:
    """
    Get the cluster detail.
    You will get `connection_strings` from the response after the cluster's status is`AVAILABLE`.
    Then, you can connect to TiDB using the default user, host, and port in `connection_strings`
    :param public_key: Your public key
    :param private_key: Your private key
    :param project_id: The project id
    :param cluster_id: The cluster id
    :return: The cluster detail
    """
    url = f"{HOST}/api/v1beta/projects/{project_id}/clusters/{cluster_id}"
    resp = requests.get(url=url,
                        auth=HTTPDigestAuth(public_key, private_key))
    if resp.status_code != 200:
        print(f"request invalid, code : {resp.status_code}, message : {resp.text}")
        raise Exception(f"request invalid, code : {resp.status_code}, message : {resp.text}")
    return resp.json()


if __name__ == "__main__":
    project = get_all_projects("1A5RPEbh", "3884202b-a9eb-406f-af4c-c26fc3a724b5")
    print(project)
    cluster = get_cluster_by_id("1A5RPEbh", "3884202b-a9eb-406f-af4c-c26fc3a724b5", "1372813089444651289", "1379661944646225457")
    print(cluster)