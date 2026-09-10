# sql

## Description

Executes the SQL phrase over the defined datasource. For selects returning multiple rows, it concatenates the values (for instance you select 2 values and the select returns 4 rows, you will have 2\*4 = 8 values). For updates, it returns the update count.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sql(datasourceName, sqlstring, [...]) | **Package** | sql |
| **Alias** |  | **Pkg Usage** | sql(datasourceName, sqlstring, [...]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| datasourceName | String | Yes | Datasource name or JNDI name. For Jira database, this is set to "jdbc/JiraDS" by default. |
| sqlstring | String | Yes | SQL string. |

## Return Type

**String []**

## Error Handling

Throws **SqlException**

## Examples

### Example 1

```javascript
string [] results = sql("datasourceName", "select project_id from project_lookaside where project_code='" + project + "'");
//Note: this example is open to SQL injection if 'project' is not the standard issue project (derived) but a variable supplied by user. Take care.
```

### Example 2

```javascript
string [] results = sql("datasourceName", "select project_id from project_lookaside where project_code=?", project);
//this is better. No sql injection possible.
```

### Example 3

It is tedious to iterate over a result in its flat form. The better way is to do it like this:

```javascript
struct Person {
  string fName;
  string lName;
  number age;
}
Person [] results = sql ("datasourceName", "SELECT fName, lName, age FROM person WHERE group_member = 'Y'");
//checks to see if there are results there are skipped for brevity, but
//now you can iterate over and use the dot notation, and 'age' is really a number.
string firstResult = results[0].fName + " " + results[0].lName + " " + results[0].age;
```

To configure the data source, check the [SQL data sources](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SQL%20data%20sources&linkCreation=true&fromPageId=434864654) configuration chapter.

## See also