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
    categories = client.repcategories()
    for category in categories:
        print(category)
```


### Querying Domain Information
```python
from et_api.v1 import *

if __name__ == '__main__':
    client = Client("<enter_your_api_key_here>")

    # Get all the reputation categories
    categories = client.domains("domain.com")
    for category in categories:
        print(category)
```

### Limitations
There are currently no known limitations. 

For more information please see: https://apidocs.emergingthreats.net/#introduction
