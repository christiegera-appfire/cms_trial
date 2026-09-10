# Example 1 - Choose your assignee

Let's say you want to implement a workflow which should let the user select an agent they need help from based on the agents' location and other details like company department. Supposing that each employee has a user property with the country that they are based at; and that all employees are also grouped by their role in the team, this can be implemented very easily. After the end user selects the agent they want help from, an issue can be assigned to such employee.

To do this, add and configure a wizard.

![Power Scripts for Jira Cloud forms and wizards configuration interface](/cms_trial/assets/9386c726-d99c-4994-a062-f1ef05802f6d.png)

In this case, all screens should be visible, and thus – all condition scripts should return `ENABLED`.

The form can be a primary screen where you can select the country. The Screen script for the first wizard screen lets you select the available countries.

```text
use "poweraction";

setActionTitle("Country");

string[] countries = {"USA", "Canada", "The Netherlands"};
createSelectList("Country", countries, "", false, true, "Select the country where you are based");

setExecuteButtonText("Next");
```

By declaring the package (line 1) the script can now use the shortened version of the function names. So instead of using `BA_setActionTitle("Country")` we can simply write `setActionTitle("Country")`.

In the Action script of the first screen we need to get the value from the screen and save it into an auxiliary value:

```text
use "poweraction";

string country = getSingleValue(argv, "Country");
setAttribute("country", country);
```

![Power Scripts for Jira Cloud assignee selection form example](/cms_trial/assets/745d03ff-fe0e-470b-8744-ce84e91937e8.png)

After a user selects a country, they should be selecting a further filtering parameter – department. In this case, the Screen script should look like this:

```text
use "poweraction";

setActionTitle("Department");

string[] departments = {"HR", "Sales", "IT"};
createSelectList("Department", departments , "" ,false, true, "Select the department that best applies for your request");

setExecuteButtonText("Next");
```

In the Action script of the first step, we need to get the value from the screen and save it into an auxiliary value:

```text
use "poweraction";

string department = getSingleValue(argv, "Department");
setAttribute("department", department);
```

The last screen provides a list of users that are in the selected country and work in the selected department.   
Thus, the Select script will consider the values set in the previous screens.

```text
use "poweraction";

setActionTitle("User");

string country = getAttribute("country");
string department = getAttribute("department");

string[] users;
string[] usersInDepartment = usersInGroups(department);

for (string user in usersInDepartment) {
    if (getUserProperty(user, "country") == country) {
        users = addElement(users, user);
    }
}

createSelectList("User", users, "", false, true, "Select the person to help you");
```

In the Action script, we only set the selected value as the assignee:

```text
use "poweraction";

string user = getSingleValue(argv, "User");
assignee = user;
```

For this example, in the issue view, you will get a succession of the following screens:

|  |
| --- |
| Power Scripts for Jira Cloud form field selection interface |
| Power Scripts for Jira Cloud form configuration dialog |
| Power Scripts for Jira Cloud form validation settings |

After the last screen executes, the assignee of the current issue will be set to the value selected in the **User** field - "Josh" in this case.