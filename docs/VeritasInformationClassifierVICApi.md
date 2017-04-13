# swagger_client.VeritasInformationClassifierVICApi

All URIs are relative to *http://veritas-prod-prod.apigee.net/vic/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](VeritasInformationClassifierVICApi.md#get_settings) | **GET** /settings | Get settings


# **get_settings**
> Settings get_settings()

Get settings



### Example 
```python
from __future__ import print_statement
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

### Parameters
This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

