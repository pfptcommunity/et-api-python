from et_api.v1 import *

if __name__ == '__main__':
    api_key_file = open("et.api_key", "r")
    api_key = api_key_file.read()
    client = Client(api_key)

    categories = client.reputation_categories()
    for category in categories:
        print(category)

    for reputation in client.domains("yahoo").reputation():
        print(reputation)

    for url in client.domains("yahoo.com").urls():
        print("URL: ", url)

    for sample in client.domains("yahoo.com").samples():
        print("URL: ", sample)

    for ips in client.domains("yahoo.com").ips():
        print("IPs: ", ips)

    for event in client.domains("yahoo.com").events():
        print("Event: ", event)

    for ns in client.domains("yahoo.com").nameservers():
        print("Namserver: ", ns)

    whois = client.domains("yahoo.com").whois()
    for key, value in whois.items():
        print("{} = {}".format(key,value))

    for geo in client.domains("yahoo.com").geoloc():
        print("Geoloc: ", geo)
