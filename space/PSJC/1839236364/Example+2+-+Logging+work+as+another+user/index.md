# Example 2 - Logging work as another user

Using Forms and Wizards and the power of SIL, you can do a lot of things with your Jira. For example, you can log work on behalf of another user.

For this, you can configure a form with one step:

![Power Scripts for Jira Cloud forms and wizards configuration interface](/cms_trial/assets/1e141ccc-17a8-4d3a-9328-b1da8214c414.png)

The form will be always enabled and it's essentially a script asking for a confirmation that we want to log work for another user. If the answer to the confirmation question on the first screen is "yes", then the action will be enabled, otherwise the action will be disabled.

The form contains a confirmation question and on its Action screen we save the selected value:

- Screen script:

  ```text
  use "poweraction";
  setActionTitle("Are you sure?");
  createRadioGroup("Sure?", {"yes", "no"}, "yes", false, true, "You are about to log work on behalf of another user. This may have certain consequences. Are you sure you want to do this?");
  setExecuteButtonText("Submit");
  ```
- Action script:

  ```text
  use "poweraction";
  string option = getSingleValue(argv, "Sure?");
  setAttribute("option", option);
  ```

The Condition script for the step would look like this:

```text
use "poweraction";
number ENABLED = 1;
number DISABLED = 2;
number HIDDEN = 3;

string option = getAttribute("option");
return option == "yes" ? ENABLED : HIDDEN;
```

In the Screen script we configure the fields that we need to log the work:

```text
use "poweraction";
setActionTitle("Log work as user");

createUserPicker("User", currentUser(), false, true, "");
createInput("Time Spent", "", false, true, "(eg 3w 4d 12h)");
createDateTimePicker("Date Started", currentDate(), false, false, "");
createRadioGroup("Remaining Estimate", {"Adjust automatically", "Use existing estimate"},"Adjust automatically", false);
createTextArea("Work Description", "", false);

setExecuteButtonText("Done");
```

In the Action script we retrieve the values from the screen and add the worklog:

```text
use "poweraction";
string user = getSingleValue(argv, "User");
interval timeSpent = getSingleValue(argv, "Time Spent");
date startDate = getDateValue(argv, "Date Started");
string estimate = getSingleValue(argv, "Remaining Estimate");
string comment = getSingleValue(argv, "Work Description");

if (estimate == "Adjust automatically") {
    addWorklogAdjustEstimate(key, user, timeSpent, startDate, comment);
} else {
    addWorklogExistingEstimate(key, user, timeSpent, startDate, comment);
}
```

![Power Scripts for Jira Cloud worklog form configuration](/cms_trial/assets/bcec7f62-f28d-4e9f-aa99-27ee3d6aa85e.png)

That's it!

That's how the implementation looks like in the ticket:

|  |
| --- |
| Power Scripts for Jira Cloud user worklog input form |
| Power Scripts for Jira Cloud worklog submission confirmation |