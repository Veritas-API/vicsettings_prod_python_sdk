# swagger_client
APIs

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: Resource Specific
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.VeritasInformationClassifierVICApi()

try:
    # Get settings
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VeritasInformationClassifierVICApi->get_settings: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://veritas-prod-prod.apigee.net/vic/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*VeritasInformationClassifierVICApi* | [**get_settings**](docs/VeritasInformationClassifierVICApi.md#get_settings) | **GET** /settings | Get settings


## Documentation For Models

 - [ErrorResponse](docs/ErrorResponse.md)
 - [Settings](docs/Settings.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



