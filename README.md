# Proofpoint Emerging Threats API Package

Library implements all of the functions of the ET API via Python.

### Requirements:

* Python 3.9+
* requests
* pysocks

### Installing the Package

You can install the API library using the following command directly from Github.

```
pip install git+https://github.com/pfptcommunity/et-api-python.git
```

or can install the API library using pip.

```
pip install et-api
```

### ET API Versions

Selecting the version of the ET API is done at time of import

```python
# Version 1
from et_api.v1 import *
```

### Creating an API client object

```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")
```

### Querying Reputation Categories

```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    # Get all the reputation categories
    categories = client.reputation_categories()
    for category in categories:
        print(category)
```

### Querying Domain Information

```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    for reputation in client.domains("yahoo.com").reputation():
        print(reputation)

    for url in client.domains("yahoo.com").urls():
        print("URL: ", url)

    for sample in client.domains("yahoo.com").samples():
        print("Sample: ", sample)

    for ips in client.domains("yahoo.com").ips():
        print("IPs: ", ips)

    for event in client.domains("yahoo.com").events():
        print("Event: ", event)

    for ns in client.domains("yahoo.com").nameservers():
        print("Nameserver: ", ns)

    for key, value in client.domains("yahoo.com").whois().items():
        print("{} = {}".format(key, value))
```

### Querying IP Information

```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    # Get IP Information
    ip = "98.137.11.164"

    for reputation in client.ips(ip).reputation():
        print("Reputation:", reputation)

    for url in client.ips(ip).urls():
        print("URL: ", url)

    for sample in client.ips(ip).samples():
        print("Sample: ", sample)

    for domain in client.ips(ip).domains():
        print("Domain: ", domain)

    for event in client.ips(ip).events():
        print("Event: ", event)

    for geo in client.ips(ip).geo_location():
        print("Geo: ", geo)
```

### Querying Malware Samples

```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    # Get Malware Samples
    md5 = "cd88c95ca03b86d9ca32f322d69a7ee9"

    details = client.samples(md5)()
    print("details:", details)

    for connection in client.samples(md5).connections():
        print("Connection:", connection)

    for event in client.samples(md5).ids_events():
        print("Event:", event)

    for dns in client.samples(md5).dns():
        print("DNS:", dns)

    for http in client.samples(md5).http():
        print("HTTP:", http)
```

### Querying Malware Samples

```python
from et_api.v1 import *
from et_api.common import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    sid = "2012199"

    info = client.sids(sid)()
    print("SigInfo:", info.sid, '-->', info.name)

    f = IPFilter()

    # SortBy and SortOrder are located in et_api.common
    f.sort_by = SortBy.LAST_SEEN
    f.sort_direction = SortOrder.ASCENDING

    for ip in client.sids(sid).ips(f):
        print("IP:", ip)

    for domain in client.sids(sid).domains():
        print("Domain:", domain)

    for sample in client.sids(sid).samples():
        print("Sample:", sample)

    for key, value in client.sids(sid).signature().items():
        print("{} = {}".format(key, value))

    for key, value in client.sids(sid).documentation().items():
        print("{} = {}".format(key, value))

    for ref in client.sids(sid).references():
        print("Type:", ref.type)
        print("Description:", ref.description)
        print("Urls:", ref.urls)
```

### Proxy Support
Socks5 Proxy Example:
```python
from et_api.v1 import *
if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('socks5', credentials, '<your_proxy>', '8128')}
```
HTTP Proxy Example (Squid):
```python
from et_api.v1 import *
if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")
    credentials = "{}:{}@".format("proxyuser", "proxypass")
    client.session.proxies = {'https': "{}://{}{}:{}".format('http', credentials, '<your_proxy>', '3128')}

```

### HTTP Timeout Settings
```python
from et_api.v1 import *
if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")
    # Timeout in seconds, connect timeout
    client.timeout = 600
    # Timout advanced, connect / read timeout
    client.timeout = (3.05, 27)
```

### Type Hinting and Auto Completion Helpers

All dictionaries and lists have helper properties to prevent needing to identify the key values associated.

### Limitations

There are currently no known limitations.

For more information please see: https://apidocs.emergingthreats.net/#introduction
