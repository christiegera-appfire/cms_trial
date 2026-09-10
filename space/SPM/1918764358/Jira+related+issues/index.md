# Jira related issues

## Jira corrupted index

If you see any symptoms that your Jira index is corrupted (for example, your JQL queries return wrong data), disable BigPicture, perform Jira reindex, and enable BigPicture back.

Work breakdown structure data is stored in the BigPicture table called:

```text
T_DEP_STATE_VERSION
T_DEP_TREE_EVENT
T_DEP_LINK_EVENT
T_DEP_NODE_SIBLING
```

If you have a backup that contains such a table, your WBS can be restored.

Maintaining a Jira index is critical - when the index is corrupted, synchronizing tasks can result in data loss (the existing task hierarchy is changed). When the index is corrupted, JQL does not work, and the plugins treat all the issues as new upon the synchronization. This means that the task structure based on artificial tasks changes during a sync. The old structure is lost.

More about Jira index corruption can be found in the Atlassian documentation:

- [Understand the indexing process in the Jira server](https://confluence.atlassian.com/jirakb/jira-indexing-faq-776654790.html)
- [Troubleshoot Lucene index corruption in the Jira server](https://confluence.atlassian.com/jirakb/lucene-index-corruption-931237172.html)

## Impact on synchronization

Full synchronization is not run when BigPicture gets information about the corrupted index from the Jira API. A user can perform a Jira reindex. This should solve the corrupted index problem. Users can also continue without reindexing, which can cause irreversible and unintended changes in Box scope.

## Insufficient Jira permissions

If you see a message about insufficient Jira permissions while trying to access the app for Jira Cloud, follow the steps described in this article.

**Steps:**

1. Go to **Settings** > **System** > **Global permissions**.
2. Scroll down to the **Grant permission** section.
3. Select the **'atlassian-addons-admin'** group.

   ![Screenshot of the Grant permission section in Jira global permissions.](/cms_trial/assets/36555d93-46de-44be-bfaf-2c8c17a3b43f.png)
4. Steps:

   1. From the **Grant** drop-down, select **Browse users and groups.**
   2. From the **Group** drop-down, select **atlassian-addons-admin.**
   3. Click the **Add** button.

   Repeat the steps for **Share dashboards and filters**.

   ![Screenshot of granting permissions to a group in Jira global permissions.](/cms_trial/assets/312a8d71-0fe2-4858-9af2-cc85c7e5ecc1.png)

   You can see that the permissions above have been updated.

   ![Screenshot of Jira global permissions section.](/cms_trial/assets/653de630-17f3-4606-84be-baf8ba455605.png)
5. If the message still appears, reinstall the plugin (**Apps drop-down at the top** > **Manage your apps).**

   ![Screenshot of the Manage apps section in Jira.](/cms_trial/assets/25cdc2f4-b6fb-47a4-9450-ba5e6f5d4366.png)

If you need help, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) team.

## The connection between Jira and BigPicture has been lost

After the base URL change, the link to BigPicture has been lost.

Try reinstalling the plugin (NOT turn on/off). Plugin reinstallation will not cause data loss. If you have further questions, please contact our support team via our [Service Desk](https://appfire.atlassian.net/servicedesk/customer/portal/11).