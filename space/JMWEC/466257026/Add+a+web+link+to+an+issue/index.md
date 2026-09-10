# Add a web link to an issue

This article provides the code snippet to add a web link to an issue, using [Build-your-own (scripted) Post-function (JMWE app)](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Build-your-own%20%28scripted%29%20Post-function&linkCreation=true&fromPageId=466257026) post-function and [callJira](/cms_trial/space/JMWEC/465243039/callJira/) filter.

## Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the “Build-your-own (scripted) Post-function (JMWE app)” post-function.
5. Add the below Nunjucks template:

   ```java
   {{"/rest/api/2/issue/:issue/remotelink" | callJira(verb=("post"),params={"issue":issue.key},body={"object":{
     url:"https://appfire.atlassian.net/wiki/spaces/JMWEC/",
     title:"JMWE for Jira Cloud"
   } }) }}
   ```

With this, the URL "[https://appfire.atlassian.net/wiki/spaces/JMWEC/](https://appfire.atlassian.net/wiki/spaces/JMWEC)" will be linked to the current issue, with the title "JMWE for Jira Cloud" - modify them as per your use case.

![JMWE for Jira Cloud interface for adding web links to issues with input fields and options](/cms_trial/assets/443429c8-5875-44a0-9ab4-270c2ebb4297.png)

If this post-function is added on the create transition, select the checkbox *“Delay the execution of this post-function”* under *“Delayed execution”* and select a delay of 3 seconds.

### References

- [callJira filter](/cms_trial/space/JMWEC/465243039/callJira/)
- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)