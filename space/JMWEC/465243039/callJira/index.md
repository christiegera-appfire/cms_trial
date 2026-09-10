# callJira

`callJira`

This is a *custom* Nunjucks filter that operates on a string representing the partial URL, starting with either:

- **/rest**
- **/gateway**

Both of which are part of the Jira API. Any Jira API endpoint beginning with these is callable and returns the response in JSON.

To make a call to any Jira Cloud REST API of another instance of Jira or any external REST API, user [callRest](/cms_trial/space/JMWEC/465242995/callRest/) filter

For information about the Jira REST API, see:

- Core API: <https://developer.atlassian.com/cloud/jira/platform/rest/v2/>
- Jira Software-specific API: <https://developer.atlassian.com/cloud/jira/software/rest/>
- Jira Service Desk-specific API: <https://developer.atlassian.com/cloud/jira/service-desk/rest/>

## Applies to

A string representing the partial URL, starting with /rest. For example: `"/rest/api/2/issue/TEST-1"`

## Parameters

Note the use of named parameters instead of positional parameters because of the number of parameters and their optional nature.

| **Named parameter** | **Description** | **Examples** |
| --- | --- | --- |
| `verb` | Indicates the HTTP verb such as GET (to get information), PUT (to update existing information), POST (to post or create a new item), DELETE (to delete an item).  The default is `GET`.  The verb is not case-sensitive. | - `{{ "/rest/api/2/issue/TEST-1" | callJira() | dump(2)}}` dumps the information of the issue with key TEST-1 - `{{ "/rest/api/2/issue/:issue" | callJira(verb = "GET", params={"issue":issue.key}) | dump(2)}}` dumps the information of the current issue. - `{{ "/rest/api/2/issue/TEST-1" | callJira(verb=("PUT"), params={"issue":"TEST-1"}, body={"fields": {"summary": "New summary"} }) }}` updates the summary of the issue with key TEST-1 to “New summary” - See the [examples section](/wiki/spaces/MWECS/pages/78481843/callJira#Examples) for an example on the POST verb - `{{ "/rest/api/2/issue/TEST-1" | callJira( verb=("DELETE"), params={"issue":"TEST-1"} ) }}` deletes the issue with key TEST-1 |
| `params` | Indicates the parameters to be passed to replace placeholders in the rest-url. It is a hash of key and values. Any instance of ":key" in the `rest-url` is replaced with its value found in the hash under "key". The value will be Uri-Encoded.  The default is no param | - `{{"rest/api/2/customFieldOption/:id" | callJira(verb = "GET", params={"id":"10000"}) | dump(2)}}` replaces `:id` with `10000` and dumps the custom field option - `{{"/rest/api/2/priority/:id" | callJira(verb = "GET", params={"id":linkedIssue.fields.priority.id}) | dump(2)}}` replaces `:id` with the id of the linked issues' priority and dumps the priority object in a pretty JSON format |
| `query` | Indicates the query string to be appended to the url. It is a hash of key and values. The values must be scalar and will be encoded appropriately. This is used to return a subset of fields.  The default is no query param. | - `{{ "/rest/api/2/issue/TEST-1" | callJira(query={"fields":"reporter"}) | dump(2) }}` will call `/rest/api/2/issue/TEST-1?fields=reporter` and dump the issue whose key is TEST-1 with its Reporter information. - `{{ "/rest/api/2/issue/:issue" | callJira(params={"issue":linkedIssue.key}, query={"fields":"subtasks"}) | dump(2) }}`  dumps the linked issue with its subtasks in a pretty JSON format. |
| `body` | Indicates the body to pass to `PUT` and `POST` calls. It is an object that will be automatically converted to JSON.  The default is no body. | - `{{ "/rest/api/2/issue/:issue" | callJira(verb=("put"), params={"issue":linkedIssue.key}, body={"fields": {"summary": "Updated Summary"} }) }}` updates the Summary of the current issue to `Updated Summary` - `{{ "/rest/api/2/issue/:issue" | callJira(verb=("put"), params={"issue":parentIssue.key}, body={"fields": {"versions": issue.fields.versions | first | field("name"} }) }}` updates the Affects Version/s of the parent issue to the first Affects Version/s of the current issue. - For examples using POST call and PUT verb see [here](/wiki/spaces/MWECS/pages/78481843/callJira#Examples). |
| `impersonate` | Indicates the impersonation to be applied to the call. It is either `true` to impersonate the current user, or an accountId to impersonate that user.  The default is no impersonation and acts as the add-on user. | - `{{ "/rest/api/2/issue/:issue" | callJira(verb=("put"), params={"issue":parentIssue.key}, body={"fields": {"summary": "Hello" } }, impersonate="accountId:5d94aa5a4af8460dd557a40a" ) }}` updates the Summary of the parent issue to “Hello” as the user with the specified accountID. |
| `dontFail` | If `true`, when the REST call to Jira returns an error, instead of throwing an exception, the error will be returned as an object containing an `_error` and/or a `_statusCode` field. | - `{{ "/rest/api/2/issue/:issue" | callJira(verb=("put"), params={issue:issue.key}, body={fields:{components: [{name:"Server"}]} }, dontFail=true) | dump(2)}}` updates the Component/s of the issue to “Server”, and if the “Server” component doesn’t exist, returns:  ```text   {     "_error": {       "code": 400,       "detail": {         "errorMessages": [],         "errors": {           "components": "Component name 'Server' is not valid"         }       }     }   }   ``` |

## Examples

Here are a few examples using the `callJira` filter

### Get the issue information

```text
{{ "/rest/api/2/issue/:issue" | callJira(params={"issue":issue.key}) | dump(2)}}
```

Getsthe current issue information and outputs the current issue as JSON in a pretty format with 2 spaces indentation.

### Get the issue information with just the Reporter

```text
{{ "/rest/api/2/issue/:issue" | callJira(params={"issue":issue.key}, query={"fields":"reporter"}) | dump(2) }}
```

Getsthe current issue information and outputs the current issue with the Reporter as JSON

### Update the Summary of the current issue

```text
{{ "/rest/api/2/issue/:issue" | callJira(verb=("PUT"), params={"issue":issue.key}, body={"fields": {"summary": "Updated Summary"} }) }}
```

Updatesthe summary of the current issue and outputs nothing

### Create a new issue

```text
{{ "/rest/api/2/issue" | callJira(verb=("post"), 
body={
  "fields": {
    "issuetype": {
      "self": "https://JMWEtest.atlassian.net/rest/api/2/issuetype/10001",
      "id": "10001",
      "description": "A user story. Created by JIRA Software - do not edit or delete.",
      "iconUrl": "https://JMWEtest.atlassian.net/images/icons/issuetypes/story.svg",
      "name": "Story",
      "subtask": false
    },
    "project": {
      "self": "https://JMWEtest.atlassian.net/rest/api/2/project/13410",
      "id": "13410",
      "key": "PC",
      "name": "Project Cloud",
      "projectTypeKey": "software",
      "simplified": false,
      "avatarUrls": {
        "48x48": "https://JMWEtest.atlassian.net/secure/projectavatar?pid=13410&avatarId=10761",
        "24x24": "https://JMWEtest.atlassian.net/secure/projectavatar?size=small&s=small&pid=13410&avatarId=10761",
        "16x16": "https://JMWEtest.atlassian.net/secure/projectavatar?size=xsmall&s=xsmall&pid=13410&avatarId=10761",
        "32x32": "https://JMWEtest.atlassian.net/secure/projectavatar?size=medium&s=medium&pid=13410&avatarId=10761"
      }
    },
   "summary": "New Task"
  }
}) | dump(2) }}
```

Createsa new current issue

```text
{
  "id": "50078",
  "key": "PC-267",
  "self": "https://JMWEtest.atlassian.net/rest/api/2/issue/50078"
}
```

### Use dynamic data when creating an issue

To use the current issue’s data when creating a new issue, insert it into the body section. In the example below, the current issue’s project is used to create a new issue in the same project.

```text
{{ "/rest/api/2/issue" | callJira(verb=("post"), 
body={
  "fields": {
    "project": {
      "key":issue.fields.project.key
    },
    "summary": "Summary of Issue",
    "issuetype": {
      "name": "Story"
    ...
    }
  }
) | dump(2) }}
```

### Delete the current issue

```text
{{ "/rest/api/2/issue/:issue" | callJira( verb=("DELETE"), params={"issue":issue.key} ) }}
```

### Update Fix Version/s of the current issue

```text
{{ "/rest/api/2/issue/:issue" | callJira(verb=("put"), params={"issue":issue.key}, 
body={
  "fields": {
    "fixVersions": [
      {
        "self": "https://JMWEtest.atlassian.net/rest/api/2/version/12721",
        "id": "12721",
        "description": "",
        "name": "1.0",
        "archived": false,
        "released": false
      }
     ]
	}
}, impersonate=("accountId:63d6aa5a4af8460dd557a40a")) | dump(2) 
}}
```

Updates the Fix Version/s of the current issue to 1.0 impersonating as the user with the specified `accountId`.