import json

from et_api.v1 import *

if __name__ == '__main__':
    api_key_file = open("et.api_key", "r")
    api_key = api_key_file.read()
    client = Client(api_key, True)

    # # Get the categories
    # categories = client.reputation_categories()
    # for category in categories:
    #     print(category.name, "-->", category.description)

    # Get Domain information
    # for reputation in client.domains("yahoo.com").reputation():
    #     print(reputation)

    # for url in client.domains("yahoo.com").urls():
    #     print("URL: ", url)

    # for sample in client.domains("yahoo.com").samples():
    #     print("Sample: ", sample)

    # for ips in client.domains("yahoo.com").ips():
    #     print("IPs: ", ips)

    # for event in client.domains("yahoo.com").events():
    #     print("Event: ", event.count)

    # for ns in client.domains("yahoo.com").nameservers():
    #     print("Nameserver: ", ns)

    # whois = client.domains("yahoo.com").whois()
    # for key, value in whois.items():
    #     print("{} = {}".format(key, value))

    # for geo in client.domains("yahoo.com").geo_location():
    #     print("Geo: ", geo.city)

    # # Get IP Information
    # ip = "98.137.11.164"
    # for reputation in client.ips(ip).reputation():
    #     print(reputation)
    #
    # for url in client.ips(ip).urls():
    #     print("URL: ", url)
    #
    # for sample in client.ips(ip).samples():
    #     print("Sample: ", sample)
    #
    # for domain in client.ips(ip).domains():
    #     print("Domain: ", domain)
    #
    # for event in client.ips(ip).events():
    #     print("Event: ", event)
    #
    # for geo in client.ips(ip).geo_location():
    #     print("Geo: ", geo)

    # Get Malware Samples
    # md5 = "cd88c95ca03b86d9ca32f322d69a7ee9"

    # details = client.samples(md5)()
    # print("details:", details)


    # for connection in client.samples(md5).connections():
    #     print("Connection:", connection)
    #
    # for event in client.samples(md5).ids_events():
    #     print("Event:", event)
    #
    # for dns in client.samples(md5).dns():
    #     print("DNS:", dns)
    #
    # for http in client.samples(md5).http():
    #     print("HTTP:", http)

    sid = "2012199"

    info = client.sids(sid)()
    print("SidInfo:", info)

    for ip in client.sids(sid).ips():
        print("IP:", ip)
