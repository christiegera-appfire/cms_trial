# Link parent of current sub-task to the new ticket in Create issue(s) (JMWE app) post-function.

This article explains how to link the parent of the current sub-task to the new issue in [Create issue(s) (JMWE app)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function.

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the “Create issue(s) (JMWE app)” post-function.
5. Fill in the required details.
6. Select the “Linked Issues” field under “Set specific fields of new issue(s)”. Select *“Set field value to:”* and add the below template :

   ```java
   {% set target = []%}
   {% set parentKey = issue | parentIssue("key") | field("key") %}
   {% if parentKey %}
   {% set val = {"type": {"name":"Blocks"}, "inwardIssue": {"key": parentKey} } %}
   {% set unused = target.push(val) %}
   {% endif %}
   {{target | dump(2)}}
   ```

   Modify the link type name(`Blocks` in line #4). Use either `inwardIssue` or `outwardIssue` in line #4 as per your use case]
7. Click **Add** and publish your workflow.

Now, when the transition is executed on the sub-task, a new issue is created with your configured details and then linked to the current subtask's parent.

![JMWE for Jira Cloud create issues post function with parent subtask linking](/cms_trial/assets/51ca7110-c97c-4527-8b21-bba34aa2a079.png)

## \uD83D\uDCCB Related articles

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [parentIssue filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#parentIssue)
- [field filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#field)
- [dump filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)