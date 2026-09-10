# Calculate the due date based on custom field values

Call the following script from a workflow transition action. The script sets the due date based on the value of custom field **10703**.

```text
if(isNotNull(customfield_10703)) {
    interval i = (string)customfield_10703 + "d";
    dueDate = currentDate() + i;
};
```