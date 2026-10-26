# admCreateAccount

## Description

Adds an account on the system. You need to specify an array of Jira products.
NOTE: Requires admin token to be set!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateAccount(email, atlproducts) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use "adm"; createAccount(email, atlproducts);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| email | string | Yes | The email of the user to be added |
| atlproducts | string [] | Yes | Array of products, may be jira-core/jira-software/jira-servicedesk |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

An invitation is sent for that user.

## Example

```javascript
admCreateAccount("thecool@company.com", {"jira-core","jira-software","jira-servicedesk"});
```

Returns the created user

## See also