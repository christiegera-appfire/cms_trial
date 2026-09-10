# getServiceDeskKBArticles

## Description

This function returns an array of JSMKBArticle structures for the provided serviceDeskId and search query.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getServiceDeskKBArticles(serviceDeskId, searchQuery) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id for which to search for articles. |
| searchQuery | String | Yes | The string used to filter the articles. |

## Return Type

[**JSMKBArticle[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JSMKBArticle for the provided parameters.

## Example

The following script will return an array of JSMKBArticle structures for the serviceDesk with id '1' and the provided query 'How'.

```javascript
JSMKBArticle[] articles = getServiceDeskKBArticles(1, "How");
 return articles;
```

## See also