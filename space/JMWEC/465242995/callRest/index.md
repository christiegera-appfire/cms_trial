# callRest

**callRest** is a JMWE-specific custom Nunjucks filter that makes an HTTPS call to an external REST API. This enables you to access data external to your Jira system during a transition, either to sync that external data to a work item, or to use external systems in the calculation of a variable within a Nunjucks script; this includes accessing a Jira instance outside of the instance where the transition including the callRest filter was triggered. It operates on a string representing the REST API endpoint to call, and it returns the response as JSON (unless customized using the noJSON parameter, see below).

To make a call to any Jira Cloud REST API on the **current** Jira instance use [callJira()](/cms_trial/space/JMWEC/465243039/callJira/) filter

## Applies to

A string representing the REST API endpoint to call. For example `"https://reqres.in/api/users"`. Note it can also be another Jira instance like `https://example.atlassian.net/`

## Parameters

Note the use of named parameters instead of positional parameters because of the number of parameters and their optional nature.

| **Named parameter** | **Description** | **Examples** |
| --- | --- | --- |
| `verb` | Indicates the HTTP verb such as GET (to get information), PUT (to update existing information), POST (to post or create a new item), DELETE (to delete an item).  The default is `GET`.  The verb is not case-sensitive. | - `{{ "https://reqres.in/api/users" | callRest() | dump(2)}}`  dumps all the users in a pretty JSON format - ```text   {{ "https://reqres.in/api/users/1" | callRest( verb="PUT",   body= {   	"data": [{   		"first_name": "David"   	}]   }) | dump(2)}}   ```   updates the first name of the user whose id is `1`   - ```text   {{ "https://reqres.in/api/users" | callRest( verb="post",   body={       "name": "morpheus",       "job": "leader"   }) }}   ```   creates a new user in the rest API   - `{{ "https://reqres.in/api/users/12" | callRest(verb="delete") | dump(2)}}` deletes the user with id 12 |
| `params` | Indicates the parameters to be passed to replace placeholders in the rest-url. It is a hash of key and values. Any instance of ":key" in the `rest-url` is replaced with its value found in the hash under "key". The value will be Uri-Encoded.  The default is no param | `{{ "https://reqres.in/api/users/:id" | callRest(params={"id":"11"}) | dump(2)}}` dumps the information of the user with id 11. |
| `query` | Indicates the query parameters to be added to the http call. It is a hash of key and values. The values must be scalar and will be encoded appropriately. This is used to return a subset of fields.  The default is no query param. | `{{ "https://reqres.in/api/users" | callRest(verb= "GET",query={"id":"2"}) | dump(2)}}` will call `https://reqres.in/api/users?id=2` and dump the information of the user with the id `2`. |
| `body` | Indicates the body to pass to `PUT` and `POST` calls. It is an object that will be automatically converted to JSON.  The default is no body. | ```text {{ "https://reqres.in/api/users" | callRest( verb="post", body={     "name": "morpheus",     "job": "leader" }) }} ```  creates a new user in the API with the information provided in the body |
| `options` | Indicates the options passed to the "request" call. Often this is used to pass authentication information (see the example at right) but many other options are supported (see [this section](https://www.npmjs.com/package/request#requestoptions-callback) for the entire list).  The default is no options.  Timeout duration can be set here. Value is set in milliseconds, with a default value of 20s and a maximum timeout of 3 minutes.  Use the format:  `options = { timeout: 120000; }`  Where ‘120000’ is 2 minutes.  When using the [Nunjucks Template Tester](/cms_trial/space/JMWEC/465373737/Nunjucks+Template+Tester/), the **maximum** timeout value is 20 seconds! | The following code dumps the data for the issue with key TEST-1, operating with the provided authentication information set in `auth` within `options`.  ```javascript {{ "https://example.atlassian.net/rest/api/2/issue/TEST-1" | callRest( options = { "auth":    {"username" : "abc@example.com",     "password": "sdfuhsdlsle9t739875983"    } }) | dump(2)}} ```  To send parameters as `application/x-www-form-urlencoded` use the following options:  ```text {{ "https://reqres.in/get_token_oauth" | callRest( verb="post", options = {    headers: {     "Accept": "*/*",      "Content-type": "application/x-www-form-urlencoded"   }  },  body={"grant_type": "client_credentials" } ) }} ```  Body can either be in a form such as `param1=value1&param2=value2` or as JSON object.  To send multiple parameters using `multipart/form-data`, use the `form` option. This is particularly useful when there are too many parameters to include as query parameters.  ```text {{ "https://xxxxxx.example.app/job/test_job/buildWithParameters" | callRest( verb = "post",  options = {    "auth": {      "username": "username",      "password": "xxxxx"   }, "form": {     "param1": "veryLongParameterValueWouldGoHere",      "param2": "anEvenLongerParameterValueCouldGoHere",      "param3": "theseParametersAreSoLongItWouldMaybeTriggerA414Error"}   } ) | dump(2) }} ``` |
| `noJSON` | Controls the response format. If `true`, the response body will be returned *as is* instead of being parsed as JSON. Also, the *request* body will not be automatically converted to JSON.  The default is `false` | ```javascript {{ "https://currency-exchange.p.rapidapi.com/listquotes" |  callRest( options = {     headers: {       "x-rapidapi-host": "currency-exchange.p.rapidapi.com",       "x-rapidapi-key": "89397d9ee7msh152cdc367c4c66fp16691ejsn9bb6a580e905"     }   },noJSON=true) | dump }} ```  dumps the response as plain text. |
| `dontFail` | If `true`, when the REST call returns an error, instead of throwing an exception, the error will be returned as an object containing an `_error` and/or a `_statusCode` field. | - `{{ "https://httpstat.us/404" | callRest(dontFail=true) | dump(2)}}` returns:  ```text   {     "_error": {       "code": 404,       "description": "Not Found"     },     "_statusCode": 404   }   ``` |
| `fixedIP` | **Warning**: This parameter has been deprecated. Existing IP addresses will be ignored and AWS IP addresses (listed below) will be used instead. Functions using **callRest** that include a value for this parameter will log a warning to the [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/).  If `true`, the REST call is made from a fixed static IP address, which users can then whitelist for security purposes.  The following IP addresses are used:   - 18.211.22.6 - 34.193.8.92   The default is `false` | ```text {{ "https://currency-exchange.p.rapidapi.com/listquotes" |  callRest( options = {     headers: {       "x-rapidapi-host": "currency-exchange.p.rapidapi.com",       "x-rapidapi-key": "89397d9ee7msh152cdc367c4c66fp16691ejsn9bb6a580e905"     }   },fixedIP=true) | dump }} ``` |

## Examples

Here are a few examples using the `callRest` filter

### Get the information from an API

```text
{{ "https://reqres.in/api/users" | callRest(query={"id":"2"}) | dump(2)}}
```

Getsthe information of a user with id `2` and outputs the information in a pretty JSON format with 2 spaces indentation.

### Get issue information from another Jira instance

Using this filter you can make calls to another Jira instance. You will need to authenticate using the username (one used to log in to the instance) and password (the [API token](https://confluence.atlassian.com/cloud/api-tokens-938839638.html) created for the destination instance).

```text
{{ "https://example.atlassian.net/rest/api/2/issue/TEST-1" | callRest(
options = { "auth": 
  {"username" : "abc@example.com",
    "password": "sdfuhsdlsle9t739875983" 
  }
})
| dump(2)}}
```

dumps the details of the issue with key TEST-1 using the provided authentication information.

### Convert the amount in a custom field to a specific currency

```text
{{ "https://currency-exchange.p.rapidapi.com/exchange" | 
 callRest( query={ "q": "1.0", "from": "USD", "to": "INR"},
  options = ( { headers: { 
   "x-rapidapi-host": "currency-exchange.p.rapidapi.com",
   "x-rapidapi-key": "89397d9ee7msh152cdc367c4c66fp16691ejsn9bb6a580e905" 
   } 
  } )
 ) * issue.fields.customfield_11507 }}
```

returns the amount in the custom field in INR currency.

### Use a callRest response in a template

In scenarios where the response from a REST API needs to be used in a template, use the `{% set %}` tag. For example:

```text
{% set response = "https://reqres.in/api/users" | callRest(query={"id":"2"}) | dump(2) 
%}
{{ response }}
{# remainder of template #}
```