# Copy data from the parent issue

Call the following script from a workflow transition action. The script sets the fields to the value of the corresponding field in the parent issue.

```text
if(isNotNull(parent)) { 
    summary = %parent%.summary;
    description = %parent%.description;
    dueDate = %parent%.dueDate;
}
```