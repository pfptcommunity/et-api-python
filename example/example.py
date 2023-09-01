from et_api.v1 import *

if __name__ == '__main__':
    api_key_file = open("et.api_key", "r")
    api_key = api_key_file.read()
    client = Client(api_key)

    categories = client.repcategories()
    for category in categories:
        print(category)

    sid_info = client.sids("2000005")()
    print(sid_info)

    for domains in client.sids("2000005").domains():
        print(domains)

    sample_info = client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff")()
    print(sample_info)

    data = client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff").connections()

    for connection in client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff").connections():
        print(connection)

    for dns in client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff").dns():
        print(dns)

    for event in client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff").events():
        print(event)

    for http in client.samples("fa86e86e9dfb7a4571b3c3091fbf4bff").http():
        print(http)

    wi = client.domains("yahoo.com").whois()
    print("Domain: ", wi.domain)
    print("Registrar Name: ", wi.registrar_name)
    print("Registrar Country: ", wi.registrar_country)
    print("Registrar Website: ", wi.registrar_website)
    print("Registrant Name: ", wi.registrant_name)
    print("Registrant Email: ", wi.registrant_email)
    print("Registrant Created: ", wi.registrant_created)
    print("Registrant Updated: ", wi.registrant_updated)
    print("Registrant Expires: ", wi.registrant_expires)

    #
    # for event in client.domains("yahoo.com").events():
    #     print("Event: ", event)
    #
    # for geo in client.domains("yahoo.com").geoloc():
    #     print("Geoloc: ", geo)
    #
    # for ips in client.domains("yahoo.com").ips():
    #     print("IPs: ", ips)
    #
    # for ns in client.domains("yahoo.com").nameservers():
    #     print("Name Server: ", ns)
    #
    # for rep in client.domains("yahoo.com").reputation():
    #     print("Reputation: ", rep)
    #
    # for sample in client.domains("yahoo.com").samples():
    #     print("Sample: ", sample)
    #
    # for url in client.domains("yahoo.com").urls():
    #     print("URL: ", url)
