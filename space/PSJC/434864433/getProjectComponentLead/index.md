# getProjectComponentLead

## Description

Returns the **leader** of the specified component from the specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectComponentLead(pkey, compname) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Key of the selected project. |
| compname | String | Yes | Name of the component. |

## Return Type

**String**

Returns the **lead** of the specified component from the specified project.

## Example

```javascript
//lead of the component comp1 from the project with key TSTPRJ is TL1
string leader = getProjectComponentLead("TSTPRJ", "comp1");
```

Result: TL1

## See also