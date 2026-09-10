# How to validate the reporter based on a group using JMWE app

This article explains how to validate the reporter of an issue based on a group while creating the issue using [Build-your-own (scripted) Validator](/cms_trial/space/JMWEC/466226183/Build-your-own+(scripted)+Validator/) validator. The group to use can be identified either by it’s name (e.g. “All Active Users”) or by group ID.

The most efficient method of finding a group’s id number is to open the group in Jira Administration and copy the id number from the end of the URL. To find the group id, follow these steps:

1. Log in to your Jira Cloud instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **User management**.
3. In the left-hand panel, click **Groups**.
4. Click the name of the group for which you need the ID number.
5. From the page URL, copy the value immediately after ‘**/groups/’**. This is the group ID number.

## Instructions

1. Navigate to the desired workflow *Create Issue* transition and add the Build-your-own (scripted) Validator.
2. Fill in the **Jira expression** as detailed below.

   1. If using **group name**, enter that name based on your instance details. For example:

      ```text
      !!issue.reporter && new User(issue.reporter.accountId).groups.includes("All Active Users")
      ```
   2. If using **group ID**, enter the unique ID of the group based on your instance details. For example:

      ```text
      !!issue.reporter && new User(issue.reporter.accountId).groupIds.includes("418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx")
      ```
3. Publish the workflow.
4. Create the issue. The above code will validate if the user who creates the issue belongs to the specific group name “All Active Users”. If not, it throws the following error message.

   ![JMWE for Jira Cloud groupbased validation configuration for reporter validation](/cms_trial/assets/56125bc2-97b1-41a2-829c-17d3b39f8f95.png)