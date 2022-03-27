
from pymongo import MongoClient
CONNECTIONS = dict()

def connect(uri, connection_key="default"):
    client = MongoClient(uri,
                         connect=True,
                         maxPoolSize=50,
                         maxIdleTimeMS=10000,
                         socketTimeoutMS=10000,
                         connectTimeoutMS=100000)
    CONNECTIONS[connection_key] = client    
    return client


def check_connection(conn_key="default", client=None):
    try:
        if client is not None:
            client.server_info()
        else:
            client = CONNECTIONS[conn_key]
            client.server_info()
    except Exception as e:
        raise e
