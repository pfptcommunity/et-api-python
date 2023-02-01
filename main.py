from json import dumps

from et_api import *

if __name__ == '__main__':
    api_key_file = open("et.api_key", "r")
    api_key = api_key_file.read()
    client = Client(Version.V1, api_key)

    categories = client.repcategories()
    for c in categories.get_response():
        print(c)

    # print(dumps(client.domains('yahoo.com'), indent=4))
