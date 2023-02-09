# Proofpoint Emerging Threats API Package

Library implements all of the functions of the ET API via Python.

### Requirements:

* Python 3.9+
* requests
 
### Installing the Package
You can install the API library using the following command. 
```
pip install git+https://github.com/pfptcommunity/et-api-python.git
```

### Getting Started
```python
from et_api import *

if __name__ == '__main__':
    client = client = Client(Version.V1, "<enter_your_api_key_here>")
    
    # Get all the reputation categories
    categories = client.repcategories()
    for category in categories:
      print(category)
```

### Limitations
There are currently no known limitations. 

For more information please see: https://apidocs.emergingthreats.net/#introduction
