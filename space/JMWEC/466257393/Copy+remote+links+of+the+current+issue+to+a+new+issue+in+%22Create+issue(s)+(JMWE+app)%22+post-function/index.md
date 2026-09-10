# Copy remote links of the current issue to a new issue in "Create issue(s) (JMWE app)" post-function

This article provides the code snippet to copy remote links ofthe current issue to the new issue in [Create issue(s) (JMWE app)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function, using [callJira](/cms_trial/space/JMWEC/465243039/callJira/) filter.

## Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Select *Create issue(s) (JMWE app)* and click `Add`.
5. Enter the required details:  
   Select the checkbox **Add a comment to the current issue**and enter the following template in **Comment** to copy the remote links on the current issue to the newly created issue:

   ```java
   {% for link in issue | remoteLinks %}
   {% set dummy = "/rest/api/2/issue/:issue/remotelink" | callJira(verb="post",params={"issue":newIssueKey},body=link) %}
   {% endfor %}
   ```

No comment will be added to the current issue since the template returns nothing.

![JMWE for Jira Cloud create issues post function with remote link copying settings](/cms_trial/assets/379f2c52-ca0e-4aa5-b915-df5845ee5c0e.png)

Publish the workflow to see the changes reflected on the new issue.

### References

- [remoteLinks filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#remoteLinks)
- [callJira filter](/cms_trial/space/JMWEC/465243039/callJira/)
- [newIssueKey variable](https://appfire.atlassian.net/wiki/spaces/JMWEC/pages/78482179/Variables+in+Nunjucks+Templates#newIssueKey)
- [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/)