# Create a sub-task automatically based on custom field selection

```text
string issue_project = project;
string issue_parent_key = key;
string issue_type = "Sub-Task";
string issue_summary = "New subtask for " + key;
string issue_priority = "Minor";
string issue_description = "";
string[] issue_components;
date issue_dueDate = currentDate() + "30d";
interval issue_estimate = "1h 30m";
string issue_security_level;
string[] issue_fields_mapping;

string subTaskKey = createIssue(project, issue_parent_key, 
issue_type, issue_summary, issue_priority, issue_description, 
issue_components, issue_dueDate, issue_estimate, issue_security_level, 
issue_fields_mapping);

linkIssue(subTaskKey, issue_parent_key, "Relates");
```