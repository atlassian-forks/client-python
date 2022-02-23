# grafeas.GrafeasV1Beta1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grafeas_v1_beta1_batch_create_notes**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_batch_create_notes) | **POST** /v1beta1/{parent}/notes:batchCreate | Creates new notes in batch.
[**grafeas_v1_beta1_batch_create_occurrences**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_batch_create_occurrences) | **POST** /v1beta1/{parent}/occurrences:batchCreate | Creates new occurrences in batch.
[**grafeas_v1_beta1_create_note**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_create_note) | **POST** /v1beta1/{parent}/notes | Creates a new note.
[**grafeas_v1_beta1_create_occurrence**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_create_occurrence) | **POST** /v1beta1/{parent}/occurrences | Creates a new occurrence.
[**grafeas_v1_beta1_delete_note**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_delete_note) | **DELETE** /v1beta1/{name_1} | Deletes the specified note.
[**grafeas_v1_beta1_delete_occurrence**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_delete_occurrence) | **DELETE** /v1beta1/{name} | Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.
[**grafeas_v1_beta1_get_note**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_get_note) | **GET** /v1beta1/{name_1} | Gets the specified note.
[**grafeas_v1_beta1_get_occurrence**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_get_occurrence) | **GET** /v1beta1/{name} | Gets the specified occurrence.
[**grafeas_v1_beta1_get_occurrence_note**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_get_occurrence_note) | **GET** /v1beta1/{name}/notes | Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.
[**grafeas_v1_beta1_get_vulnerability_occurrences_summary**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_get_vulnerability_occurrences_summary) | **GET** /v1beta1/{parent}/occurrences:vulnerabilitySummary | Gets a summary of the number and severity of occurrences.
[**grafeas_v1_beta1_list_note_occurrences**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_list_note_occurrences) | **GET** /v1beta1/{name}/occurrences | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.
[**grafeas_v1_beta1_list_notes**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_list_notes) | **GET** /v1beta1/{parent}/notes | Lists notes for the specified project.
[**grafeas_v1_beta1_list_occurrences**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_list_occurrences) | **GET** /v1beta1/{parent}/occurrences | Lists occurrences for the specified project.
[**grafeas_v1_beta1_update_note**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_update_note) | **PATCH** /v1beta1/{name_1} | Updates the specified note.
[**grafeas_v1_beta1_update_occurrence**](GrafeasV1Beta1Api.md#grafeas_v1_beta1_update_occurrence) | **PATCH** /v1beta1/{name} | Updates the specified occurrence.


# **grafeas_v1_beta1_batch_create_notes**
> V1beta1BatchCreateNotesResponse grafeas_v1_beta1_batch_create_notes(parent, body)

Creates new notes in batch.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the notes are to be created.
body = grafeas.Body() # Body | 

try:
    # Creates new notes in batch.
    api_response = api_instance.grafeas_v1_beta1_batch_create_notes(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_batch_create_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the notes are to be created. | 
 **body** | [**Body**](Body.md)|  | 

### Return type

[**V1beta1BatchCreateNotesResponse**](V1beta1BatchCreateNotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_batch_create_occurrences**
> V1beta1BatchCreateOccurrencesResponse grafeas_v1_beta1_batch_create_occurrences(parent, body)

Creates new occurrences in batch.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrences are to be created.
body = grafeas.Body1() # Body1 | 

try:
    # Creates new occurrences in batch.
    api_response = api_instance.grafeas_v1_beta1_batch_create_occurrences(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_batch_create_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the occurrences are to be created. | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**V1beta1BatchCreateOccurrencesResponse**](V1beta1BatchCreateOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_create_note**
> V1beta1Note grafeas_v1_beta1_create_note(parent, body, note_id)

Creates a new note.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the note is to be created.
body = grafeas.V1beta1Note() # V1beta1Note | The note to create.
note_id = 'note_id_example' # str | The ID to use for this note.

try:
    # Creates a new note.
    api_response = api_instance.grafeas_v1_beta1_create_note(parent, body, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the note is to be created. | 
 **body** | [**V1beta1Note**](V1beta1Note.md)| The note to create. | 
 **note_id** | **str**| The ID to use for this note. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_create_occurrence**
> V1beta1Occurrence grafeas_v1_beta1_create_occurrence(parent, body)

Creates a new occurrence.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrence is to be created.
body = grafeas.V1beta1Occurrence() # V1beta1Occurrence | The occurrence to create.

try:
    # Creates a new occurrence.
    api_response = api_instance.grafeas_v1_beta1_create_occurrence(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_create_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the occurrence is to be created. | 
 **body** | [**V1beta1Occurrence**](V1beta1Occurrence.md)| The occurrence to create. | 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_delete_note**
> object grafeas_v1_beta1_delete_note(name_1)

Deletes the specified note.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name_1 = 'name_1_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.

try:
    # Deletes the specified note.
    api_response = api_instance.grafeas_v1_beta1_delete_note(name_1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_1** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_delete_occurrence**
> object grafeas_v1_beta1_delete_occurrence(name)

Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.
    api_response = api_instance.grafeas_v1_beta1_delete_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_delete_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_get_note**
> V1beta1Note grafeas_v1_beta1_get_note(name_1)

Gets the specified note.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name_1 = 'name_1_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.

try:
    # Gets the specified note.
    api_response = api_instance.grafeas_v1_beta1_get_note(name_1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_1** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_get_occurrence**
> V1beta1Occurrence grafeas_v1_beta1_get_occurrence(name)

Gets the specified occurrence.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Gets the specified occurrence.
    api_response = api_instance.grafeas_v1_beta1_get_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_get_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_get_occurrence_note**
> V1beta1Note grafeas_v1_beta1_get_occurrence_note(name)

Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.
    api_response = api_instance.grafeas_v1_beta1_get_occurrence_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_get_occurrence_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_get_vulnerability_occurrences_summary**
> V1beta1VulnerabilityOccurrencesSummary grafeas_v1_beta1_get_vulnerability_occurrences_summary(parent, filter=filter)

Gets a summary of the number and severity of occurrences.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to get a vulnerability summary for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)

try:
    # Gets a summary of the number and severity of occurrences.
    api_response = api_instance.grafeas_v1_beta1_get_vulnerability_occurrences_summary(parent, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_get_vulnerability_occurrences_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to get a vulnerability summary for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 

### Return type

[**V1beta1VulnerabilityOccurrencesSummary**](V1beta1VulnerabilityOccurrencesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_list_note_occurrences**
> V1beta1ListNoteOccurrencesResponse grafeas_v1_beta1_list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)

Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the note to list occurrences for in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of occurrences to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.
    api_response = api_instance.grafeas_v1_beta1_list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_list_note_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note to list occurrences for in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of occurrences to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListNoteOccurrencesResponse**](V1beta1ListNoteOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_list_notes**
> V1beta1ListNotesResponse grafeas_v1_beta1_list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists notes for the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to list notes for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of notes to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists notes for the specified project.
    api_response = api_instance.grafeas_v1_beta1_list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_list_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to list notes for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of notes to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListNotesResponse**](V1beta1ListNotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_list_occurrences**
> V1beta1ListOccurrencesResponse grafeas_v1_beta1_list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists occurrences for the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists occurrences for the specified project.
    api_response = api_instance.grafeas_v1_beta1_list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_list_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to list occurrences for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListOccurrencesResponse**](V1beta1ListOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_update_note**
> V1beta1Note grafeas_v1_beta1_update_note(name_1, body, update_mask=update_mask)

Updates the specified note.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name_1 = 'name_1_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
body = grafeas.V1beta1Note() # V1beta1Note | The updated note.
update_mask = 'update_mask_example' # str | The fields to update. (optional)

try:
    # Updates the specified note.
    api_response = api_instance.grafeas_v1_beta1_update_note(name_1, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_1** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 
 **body** | [**V1beta1Note**](V1beta1Note.md)| The updated note. | 
 **update_mask** | **str**| The fields to update. | [optional] 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_v1_beta1_update_occurrence**
> V1beta1Occurrence grafeas_v1_beta1_update_occurrence(name, body, update_mask=update_mask)

Updates the specified occurrence.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
body = grafeas.V1beta1Occurrence() # V1beta1Occurrence | The updated occurrence.
update_mask = 'update_mask_example' # str | The fields to update. (optional)

try:
    # Updates the specified occurrence.
    api_response = api_instance.grafeas_v1_beta1_update_occurrence(name, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->grafeas_v1_beta1_update_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 
 **body** | [**V1beta1Occurrence**](V1beta1Occurrence.md)| The updated occurrence. | 
 **update_mask** | **str**| The fields to update. | [optional] 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

