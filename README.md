# Proofpoint Emerging Threats API Package

Library implements all of the functions of the ET API via Python.

### Requirements:

* Python 3.9+
* requests
 
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
        print("Nameserver: ", ns)

    whois = client.domains("yahoo.com").whois()
    for key, value in whois.items():
        print("{} = {}".format(key, value))

    for geo in client.domains("yahoo.com").geo_location():
        print("Geoloc: ", geo)
```

### Querying IP Information
```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    for reputation in client.ips("98.137.11.164").reputation():
        print(reputation)

    for url in client.ips("98.137.11.164").urls():
        print("URL: ", url)

    for sample in client.ips("98.137.11.164").samples():
        print("Sample: ", sample)

    for domain in client.ips("98.137.11.164").domains():
        print("Domain: ", domain)

    for event in client.ips("98.137.11.164").events():
        print("Event: ", event)

    for geo in client.ips("98.137.11.164").geo_location():
        print("Geo: ", geo)
```

### Querying Malware Samples
```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")


```

### Limitations
There are currently no known limitations. 

For more information please see: https://apidocs.emergingthreats.net/#introduction
