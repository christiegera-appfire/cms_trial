# sqlCallStoredProcedure

## Description

Executes the stored procedure over the defined datasource name / JNDI datasource.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sqlCallStoredProcedure(datasourceName, procedureName, [...]) | **Package** | sql |
| **Alias** |  | **Pkg Usage** | callSP(datasourceName, procedureName, [...]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| datasourceName | String | Yes | Datasource name / JNDI name. For Jira database, this is set to "jdbc/JiraDS" by default. |
| procedureName | String | Yes | Stored procedure name. |

## Return Type

**String []**

## Examples

### Example 1

Where showMessage() is a stored procedure existing in myDB database.

```javascript
string [] results = sqlCallStoredProcedure("myDB", "showMessage");
```

### Example 2

Where addComponent(String id, String name) is a stored procedure existing in myDB database.

```javascript
string [] results = sqlCallStoredProcedure("myDB", "addComponent", "componentId", "componentName");
```

To configure the data source, check the [SQL data sources](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SQL%20data%20sources&linkCreation=true&fromPageId=434733692) configuration chapter.

## See also