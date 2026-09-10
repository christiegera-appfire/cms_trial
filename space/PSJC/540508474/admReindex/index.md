# admReindex

## Description

Triggers a re-index for the issues returned by the jqlQuery, it will re-index the issues in the background.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admReindex(jqlQuery) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | reindex(jqlQuery) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| jqlQuery | string | Yes | The results of the query will be used to reindex. |

## Return Type

**boolean**

Returns true if the reindex was started and false otherwise.

## See also