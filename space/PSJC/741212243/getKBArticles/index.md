# getKBArticles

## Description

This function returns an array of JSMKBArticle structures for the provided search query.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getKBArticles(searchQuery) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| searchQuery | String | Yes | The string used to filter the articles. |

## Return Type

[**JSMKBArticle[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JSMKBArticle for the provided query.

## Example

The following script will return an array of JSMKBArticle structures for the provided query 'template'.

```javascript
JSMKBArticle[] articles = getKBArticles("template");
 return articles;
```

## See also