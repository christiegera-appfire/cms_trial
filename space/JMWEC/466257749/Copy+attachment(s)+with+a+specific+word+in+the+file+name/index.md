# Copy attachment(s) with a specific word in the file name

This article provides the code snippet to copy attachment(s) that have a specific word in the file name from the current issue to other issue(s) using [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function.
5. Select the issues, for which the attachments should be copied, under “Target Issue(s)”.
6. Select the “Attachment” field and add the below Nunjucks template:

   ```java
   {% set finalAttachments = [] %}
   {% for att in issue.fields.attachment %}
   {% if (att | field("filename")).includes("test") %}
   {% set ignored = finalAttachments.push(att) %}
   {% endif %}
   {% endfor %}
   {{ finalAttachments | dump(2) }}
   ```

   Replace the word `test` in line #3 with the desired word.
7. Select the “Treat value as JSON” option (select/unselect other options as per your use case)

With this, the attachment(s) that contain the word `test` (modify it) in the filename are copied from the current issue to the configured target issue(s)

![JMWE for Jira Cloud attachment copying configuration with filename filtering options](/cms_trial/assets/aaaaddbb-7898-4578-99b8-2a55c9ce452a.png)

If this post-function is added on the create transition, select the checkbox *“Delay the execution of this post-function”* under *“Delayed execution”* and select a delay of 3 seconds.

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/)
- [field filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#field)
- [dump filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)

## \uD83D\uDCCB Related articles