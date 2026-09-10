# sqlCallStoredProcedureWithOutParams

## Description

Executes the stored procedure over the defined datasource.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sqlCallStoredProcedureWithOutParams(datasourceName, procedureName, [params]) | **Package** | sql |
| **Alias** |  | **Pkg Usage** | callSPWithOutParams(datasourceName, procedureName, [params]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| datasourceName | String | Yes | Datasource name or JNDI name. For Jira database, this is set to "jdbc/JiraDS" by default. |
| procedureName | String | Yes | Stored procedure name. |

## Return Type

**String []**

## Examples

Where showMessage() is a stored procedure existing in myDB database.

```javascript
string [] results = sqlCallStoredProcedureWithOutParams("myDB", "showMessage");
```

Where INSERTTEST is a stored procedure existing in myDB database, you can see it below:

```javascript
string [] results = sqlCallStoredProcedureWithOutParams("myDB", "INSERTTEST", {"p_userid", "FLOAT", "IN", "1.22"}, {"p_username", "VARCHAR2", "IN", "username"}, {"p_createdby", "VARCHAR2", "IN", "admin"}, {"p_date", "TIMESTAMP", "IN", "28-APR-2015"});
```

To configure the data source, check the [SQL data sources](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SQL%20data%20sources&linkCreation=true&fromPageId=434799404) configuration chapter.

## See also