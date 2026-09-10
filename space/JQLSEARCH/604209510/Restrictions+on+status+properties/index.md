# Restrictions on status properties

Although the app has required permissions as described in [Global permissions](/cms_trial/space/JQLSEARCH/604209847/Global+permissions/) and [App permissions](/cms_trial/space/JQLSEARCH/604209961/App+permissions%C2%A0/), there could be status properties restricted to groups/roles/users. Ensure the app has all the permissions to view the issues for completing indexing.

## Restrictions for workflow properties

To check if there are restrictions applied to workflow properties:

1. Navigate to the project workflow.
2. Select a workflow and click **Edit**.
3. Click **View Properties** for the status. A list of properties displays.

   ![contentId-604209510](/cms_trial/assets/88428873-23e8-455b-9153-169237eba4b1.png)
4. If there are any properties as shown below, there are restrictions applied at the status (here, the edit and comment permissions are only granted to group Development), which means the app doesn't have complete permissions. When you perform indexing, this workflow’s issues will not proceed with indexing.

   ![JSE-permissions-dev.png](/cms_trial/assets/1c52230e-a106-41ab-9b9d-08c7ede608ee.png)
5. To resolve this permission issue, add the Edit permission for the **projectrole** for **atlassian-addon-project-access**.

   ![JSE-permissions-atlassian.png](/cms_trial/assets/10bb2c41-d937-42b5-937c-91ea61ed56d2.png)
6. Contact our [support team](https://appf.re/support) to perform the indexing.