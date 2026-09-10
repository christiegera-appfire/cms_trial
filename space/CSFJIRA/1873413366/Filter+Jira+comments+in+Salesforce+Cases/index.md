# Filter Jira comments in Salesforce Cases

This guide explains how admins can set up hashtag filters so only relevant comments appear in Salesforce, and how to view those filtered comments once configured.

Comments can be filtered using hashtags (e.g. `#jira`, `#support`, `#customer_desk`), so users only see the comments that matter to them instead of the full comment history. Filters are configured separately for each platform:

- The **Jira comments** tags control which Jira comments are shown in Salesforce in the **Jira Comment** component.
- The **Salesforce comments** tags control which Salesforce comments are shown in Salesforce in the J**ira Comment** component.

You can also [filter Salesforce comments within Jira](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/).

## Before you start

Make sure you have:

- Set the **Visibility** option under *Comment privacy* properly*.* Only comments that meet the configured visibility setting are displayed in Salesforce. For details, see [Comment configuration](/cms_trial/space/CSFJIRA/1873445530/Configure+settings+in+the+Salesforce+package/).
- Configure your record page in Salesforce to display the Jira Comments component. For details, see [Configure Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/).

Comments restricted to a Jira project role are excluded entirely, ensuring that role-restricted content is not disclosed to unauthorized users.

## Filter comments by tag

1. In Salesforce, click **Settings** > **Setup**.
2. Search for *Package* and go to **Installed Packages**.
3. Look for *Jira Cloud for Salesforce* and click **Configure**.
4. On the*Configuration* screen, scroll to the*Comment configuration* section.

   ![ Comment configuration section](/cms_trial/assets/a78a195e-9688-4d64-bc3e-eca6c52bc183.png)
5. For **Comment Privacy** settings, select which Jira comments are visible in Salesforce based on their privacy:

   - Show All
   - Show only unrestricted comments

The privacy setting is applied first and takes precedence over any hashtag filters below. A comment excluded based on privacy will never appear in Salesforce, regardless of its tags.

1. To filter which Jira comments appear in Salesforce under the Jira Comments component, click the **Edit**  (▢ ) icon next to the **Jira comment tag filter** and enter the hashtags you want to filter by, and click **Save**.

![image-20260831-084250.png](/cms_trial/assets/aa66fb6a-bb9d-4484-bae1-c9ea845cfca8.png)

1. To filter which Salesforce comments appear in Salesforce under the Jira Comments component, click the **Edit**  (▢ ) icon next to the **Salesforce comment tag filter** and enter the hashtags you want to filter by, and click **Save**.

Tags must be preceded by `#` and separated by a space. Hashtags in Salesforce are case-sensitive.

## View filtered comments in Salesforce

Filtered comments appear in the **Jira Comments** component based on what hashtags were configured by the administrator (see above).

![JCFS-jiracommentfiltered-logo.png](/cms_trial/assets/3c55e4a1-7149-4bdd-b3e3-eb328a1d313e.png)

You can also filter the comments visibility in Jira in the Salesforce Comments tab. For details, see [Filter Salesforce comments in Jira work items](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/).

## Related information

- [Filter Salesforce comments in Jira work items](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/)
- [View Jira comments in Salesforce](/cms_trial/space/CSFJIRA/1962607212/View+Jira+comments+in+Salesforce/)
- [Configure Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/)
- [Comment configuration](/cms_trial/space/CSFJIRA/1873445530/Configure+settings+in+the+Salesforce+package/)