# Copy linked issues(of a specific link type) from current issue to new issue in Create / Clone issue(s) (JMWE app)

This article explains how to link the *issues linked to the current issue* (through a specific link type) to the new issue in [Create issue(s) (JMWE app)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function.

## Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the “Create issue(s) (JMWE app)” post-function.
5. Fill in the required details.
6. Select the “Linked Issues” field under “Set specific fields of new issue(s)”. Select *“Set field value to:”* and add the below template :

   ```java
   {% set isBlockedByKeys = issue | linkedIssues("is blocked by") | field("key")%}
   {% set target = []%}
   {% for key in isBlockedByKeys %}
   {% set val = {"type": {"name":"Blocks"}, "inwardIssue": {"key":key} } %}
   {% set unused = target.push(val) %}
   {% endfor %}
   {{target | dump(2)}}
   ```

The above code :

- Retrieves the issues linked to the current ticket through `is blocked by` link type (line #1)
- Loops through the retrieved issues and adds them to the array in the expected format(lines #3 to #6) [modify the link type name. Use either `inwardIssue` or `outwardIssue` in line #4 as per your use case]
- Returns the result in the expected format

With this, the issues linked to the current ticket through `is blocked by` link type will be linked to the new ticket through `is blocked by` link type. Modify the link type names as per your use case.

![JMWE for Jira Cloud create issues post function with linked issue copying configuration](/cms_trial/assets/d4277896-d3e9-42ef-98a9-44d471a8e846.png)

### References

- [How to insert information using Nunjucks annotations](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [linkedIssues filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#linkedIssues)
- [field filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#field)
- [dump filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)