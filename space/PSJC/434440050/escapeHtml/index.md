# escapeHtml

## Description

Escapes the given html removing traces of offending characters that could be wrongfully interpreted as markup
The following characters are reserved in HTML and must be replaced with their corresponding HTML entities:

- **"** is replaced with **&quot;**
- **&** is replaced with **&amp;**
- **<** is replaced with **&lt;**
- **>** is replaced with **&gt;**

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | escapeHtml(html) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| html | String | Yes | HTML to escape. |

## Return Type

**String**

Returns the html input escaped.

## Example

```javascript
return escapeHtml("<html><script><img src=1 onerror=alert(1)></script></html>");
```

Returns :Returns "&lt;html&gt;&lt;script&gt;&lt;img src=1 onerror=alert(1)&gt;&lt;/script&gt;&lt;/html&gt;"

## See also