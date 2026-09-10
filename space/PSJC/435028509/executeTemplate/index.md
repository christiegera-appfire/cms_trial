# executeTemplate

## Description

Executes a template. All variables already defined in the script are passed to that template. All variables already defined in the script are passed to that template. This function obeys the context it is called. If you call it in an issue context, you can access issue fields in the template, if not you cannot.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | executeTemplate(template\_path[, charset] ) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| template\_path | String | Yes | The template path, either absolute or relative. Note that if relative, this path is based on **KEPLER\_HOME directory**, and not to the mail templates directory. |
| charset | String | No | Specifies the charset used to read that template. |

## Return Type

**String**

## Examples

The template is represented below:

```javascript
$! if(isNotNull(baseVar)) { $
Well done, <strong>aseVar$ !
$! } else { $
Nobody to congratulate ?!? Whoaaaa !!!
$! } $
```

The script is represented below:

```javascript
string baseVar = "Monster";
return executeTemplate("templates/some.tpl"); //note that we refer this relative to Kepler Home directory !
```

The output produced is following:

```javascript
Well done, Monster!
```

## See also