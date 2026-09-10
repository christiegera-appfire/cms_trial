# admAddProjectComponent

## Description

Adds a component in the project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddProjectComponent(pkey, compname, compdesc, complead, defassignee) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addComponent(pkey, compname, compdesc, complead, defassignee) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |
| compname | String | Yes | Component name. |
| compdesc | String | Yes | Description. |
| complead | String | Yes | Component lead. |
| defassignee | number | Yes | Possible values and their respective effects: 0 - project default; 1 - component lead; 2 - project lead; any other value - unassigned. |

## Return Type

**boolean**

Returns true if the component was added and false otherwise.

## See also