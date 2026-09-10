# databaseAvailable

## Description

Checks if the database is available. Optionally, it can check also the availability of the results for the SQL passed in as the second parameter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | databaseAvailable(dbstring [, sqlstring]) | **Package** | sql |
| **Alias** |  | **Pkg Usage** | available(dbstring [, sqlstring]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| dbstring | String | Yes | Datasource JNDI name or the datasource name. For Jira database, this is set to "jdbc/JiraDS" by default, if exported. |
| sqlstring | String | No | SQL string. |

## Return Type

**Boolean (true/false)**

## Examples

### Example 1

Let's suppose in our examples `TextField` is a custom field text already configured for the current Jira server instance and `TestDB` represents the database resource name configured in the server context. For more details see [SQL data sources](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SQL%20data%20sources&linkCreation=true&fromPageId=434440086).

```javascript
TextField=databaseAvailable("TestDB"); //will set 'TextField' value to 'true'
```

### Example 2

```javascript
TextField=databaseAvailable("TestDB", "select pname from project"); //will set 'TextField' value to 'true' if the SQL passed in can be executed
```

### Example 3

```javascript
TextField=databaseAvailable("TestDB", "select pname from inexistentTableName");//will set 'TextField' value to 'false', because the SQL passed in cannot be executed
```

### Example 4

```javascript
TextField=databaseAvailable("InexistentTestDB", "select pname from project");//will set 'TextField' value to 'false', because the database resource does not exist
```

To configure the data source check the [SQL data sources](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SQL%20data%20sources&linkCreation=true&fromPageId=434440086) configuration chapter.

## See also