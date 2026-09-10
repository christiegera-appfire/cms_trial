# Delete attachment(s) with a specific word in the file name

This article provides the code snippet to delete attachment(s) that have a specific word in the file name using <https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Build-your-own%20%28scripted%29%20Post-function&linkCreation=true&fromPageId=465504378>

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the <https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Build-your-own%20%28scripted%29%20Post-function&linkCreation=true&fromPageId=465504378>
5. Add the below Nunjucks script:

   ```java
   {% for att in issue.fields.attachment %}
   {% if (att | field("filename")).includes("test") %}
   {{ "/rest/api/2/attachment/:id" | callJira(verb="DELETE",params={"id":att | field("id")}) }}
   {% endif %}
   {% endfor %}
   ```

The above template deletes the attachment(s) that contain the word `test` in the filename (modify `test` in line #2 with your desired text)

![JMWE for Jira Cloud attachment deletion configuration with filename filtering](/cms_trial/assets/3308e2de-8a3e-4fae-8657-aeef65ce9126.png)

If this post-function is added on the create transition, select the checkbox *“Delay the execution of this post-function”* under *“Delayed execution”* and select a delay of 3 seconds.

### References

- [callJira filter](/cms_trial/space/JMWEC/465243039/callJira/)
- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/)

## \uD83D\uDCCB Related articles

[unmapped inline: placeholder]