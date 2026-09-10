# Avoid Jira expression errors

When a Jira expression throws an error, Jira considers the result as `false` and hence the workflow condition/validator fails. The best way to avoid errors in your Jira expressions is to test your Jira expressions against an issue using the "Jira expression tester" before saving the condition/validator. Here are typical problems you need to look out for:

- `null` values: If your Jira expression returns `null`it is considered a non-boolean value and hence Jira returns an error. For example, to check that the issue is assigned, if you provide the Jira expression as:

  ```text
  issue.assignee
  ```

  when tested against an issue that is unassigned the expression returns `null`. In such cases, the easiest is to use two logical not operators (!!) to return `true` if the issue is assigned ( !issue.assignee returns `false` hence !! issue.assignee will return `true` when the issue is assigned).

  ```text
  !! issue.assignee
  ```

  You can also write a Jira expression to check that the result is not `null` like this:

  ```text
  issue.assignee != null
  ```
- If your Jira expression accesses properties of an object that is `null`, then your Jira expression and thereby your workflow condition/validator fail with an error. For example, to check that the issue's parent is a Story if you provide the Jira expression:

  ```text
  issue.parent.issuetype.name == "Story"
  ```

  when tested against an issue without a parent, the Jira expression will return an error "Type null does not have any properties". To handle this you should include an expression to test that the issue has a parent.

  ```text
  !! issue.parent && issue.parent.issuetype.name == "Story"
  ```

## Related articles

[unmapped inline: placeholder]

|  |  |
| --- | --- |
| Related issues |  |