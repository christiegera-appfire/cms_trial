# Code snippet to get the date, time when the issue was moved to a specific status

**Requirement:**

Nunjucks code snippet to retrieve the date, time when the issue was moved to a specific status.

**Solution:**

If the issue was moved to the desired status *multiple times*:

**Case 1:** Code to get the date, time when the issue was *last* moved to the desired status:

```java
{{ issue | fieldHistory("status") | filter(["to_string","STATUS_NAME"]) | last | field("date") | date }}
```

**Case 2:** Code to get the date, time when the issue was *first* moved to the desired status:

```java
{{ issue | fieldHistory("status") | filter(["to_string","STATUS_NAME"]) | first | field("date") | date }}
```

Replace `STATUS_NAME` with the desired status name (as-is → case sensitive and no trailing/leading white spaces)

This Nunjucks code can be added in [workflow](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Post-functions&linkCreation=true&fromPageId=465474587) [*post-functions*](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Post-functions&linkCreation=true&fromPageId=465474587) (and Actions)

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [fieldHistory](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#fieldHistory)
- [filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#filter)
- [last](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)
- [first](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)
- [field](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#field)
- [date](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#date)