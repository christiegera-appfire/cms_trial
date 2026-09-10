# Send email to members of groups selected in multi-group picker field

This article provides the code snippet to send email to users in the group(s) selected in a multi-group picker field in [Email issue(s) (JMWE app)](/cms_trial/space/JMWEC/466322658/Email+issue/).

## Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the *Email issue(s) (JMWE app)* post-function.
5. Add:   
   **Email content**: Enter **Subject**, **Text** **Body** as needed.  
   **Recipients**: Enter the following in **Users from template**:

   ```java
   {% set allUsers = [] %}
   {% for grp in (issue.fields.customfield_10082 | field("name"))%}
   {% for user in (grp | groupMembers) %}
   {% if (allUsers | filter(user | field("accountId")) | length == 0) %}
   {% set ignored = allUsers.push(user | field("accountId")) %} 
   {% endif %}
   {% endfor %}
   {% endfor %}
   {{ allUsers }}
   ```

Replace `10082` with the id of the multi-group picker custom field.

![JMWE for Jira Cloud email configuration for multigroup picker field notifications](/cms_trial/assets/9ededff8-5c78-4d9f-bbd8-7d8b6dbd7432.png)

Publish the workflow for the changes to be applied as configured.

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [field filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#field)
- [filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#filter)
- [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/)

\uD83D\uDCCB Related articles