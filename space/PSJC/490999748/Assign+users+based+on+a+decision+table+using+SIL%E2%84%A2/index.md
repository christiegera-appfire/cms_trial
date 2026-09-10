# Assign users based on a decision table using SIL™

## Problem

You want to assign an issue to a predefined user and/or set certain custom fields, depending on specific criteria.

For example, given a custom field **Department** with the possible values **Production**, **Sales**, and **HR**, you want to assign an issue to the Department manager at a certain time.

## Solution

## Create the decision table

Create a table containing the names of department managers. You can name the table **dept\_managers**.

| Department | Manager |
| --- | --- |
| Production | john |
| Sales | mark |
| HR | marie |

It is recommended to enter the managers' usernames instead of full names so it’s simpler to assign them.

## Write the code

To assign the manager and add them to an appropriate step, enter the following SIL™ code (action).

#### **AssignManager.sil**

```text
string sqlSelect;
string[] sqlResult;
string user;

sqlSelect = "select manager from dept_managers where department = '" + Department + "'";
sqlResult = sql("myDB", sqlSelect);

user = getElement(sqlResult, 0);

if(isNotNull(user))
  assignee= user;
```

This code performs the following actions:

- creates a dynamic SQL named **sqlSelect**,
- runs the SQL and saves the result in the **sqlResult** variable (defined as a string array),
- retrieves the user from the first position of the result (index 0),
- if the user is found, it assigns the issue to them.

In the example above, if the **Department** custom field is set, for example, to **HR**, the assignee is set to the user with the username **marie**.