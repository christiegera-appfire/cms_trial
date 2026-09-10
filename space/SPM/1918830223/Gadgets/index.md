# Gadgets

**Depreciated** **by Atlassian**

[Atlassian ended support for gadgets in Confluence 7.0](https://confluence.atlassian.com/doc/gadgets-moved-to-a-marketplace-app-from-confluence-9-2-onwards-1431545691.html) and completed their removal in Confluence 9.0 to reduce technical debt.

In Confluence 9.0, pages that were using gadgets show a grey ‘Unknown macro’ placeholder where gadgets were embedded.

## Security

You need at least a **box viewer** security role to view the gadgets on Confluence pages and Jira Dashboards.

Jira Cloud **hasn’t supported** Confluence Gadgets since 2017.

More information on differences between cloud and server versions of the App can be found on the [Cloud vs. Data Center - Key Differences between Platforms](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298092263) page.

## Gadgets overview

**BigPicture** is an excellent source of information about your projects and portfolios. But if you want to find specific data quickly and in an easy-to-digest form without constantly switching between Jira and BigPicture, gadgets are the way to go.

With **BigPicture gadgets**, you can add dynamic content to a Confluence page or the Jira application dashboard to monitor the health of projects, departments, or specific processes. This means that you can have your favorite Gantt charts and Risks all in one place and up to date thanks to the auto-refresh. Gadgets mirror the BigPicture’s modules.

There are five gadgets available:

- [Gantt gadget](/cms_trial/space/SPM/1918863157/Gantt+gadget/)
- [Overview gadget](/cms_trial/space/SPM/1918537895/Overview+gadget/)
- [Calendar gadget](/cms_trial/space/SPM/1918504663/Calendar+gadget/)
- [Risks gadget](/cms_trial/space/SPM/1918669227/Risks+gadget/)
- [Objectives gadget](/cms_trial/space/SPM/1918863565/Objectives+gadget/)

![Screenshot of BigPicture gadgets on Jira dashboard.](/cms_trial/assets/1adc436e-a55f-44aa-832c-53216df420e7.png)

## Actions on gadgets using Jira dashboard

### Add gadgets

To add a gadget:

1. Click **Edit**.
2. Click the **Add a gadget** button when viewing a Jira dashboard.
3. Type **BigPicture** to see available gadgets.
4. Click **Add** to select the gadget you want to add to your dashboard.
5. When ready, click **Done**.

![Screenshot of adding BigPicture gadgets on Jira dashboard.](/cms_trial/assets/b67dbacb-3e03-4fc7-97ff-df66efd9b693.png)

### Edit gadgets

The edit options depend on the added gadget. For example, the Gantt gadget allows you to change the display and content options. In contrast, the Overview gadget does not offer any customization and shows the same view as the Hierarchy mode of the Overview modules.

To edit a gadget:

1. Click **Edit**.
2. Click on **More actions …** menu next to a gadget.
3. Select **Configure**.
4. When ready, click **Save**.
5. Click **Done** to apply changes.

![Screenshot of configuring a BigPicture gadget on the Jira dashboard.](/cms_trial/assets/c1d153e6-b55d-41e5-9381-2c930013ecee.png)

### Delete gadgets

To delete a gadget:

1. Click **Edit**.
2. Click on **More actions …** menu next to a gadget.
3. Select **Delete**.
4. Confirm by clicking **Delete**.

![Screenshot of deleting a BigPicture gadget on the Jira dashboard.](/cms_trial/assets/21200b53-7c42-4c7b-a339-b09b3b03f012.png)

## Add gadgets to Confluence pages

To add a gadget to a Confluence page:

1. Go to the Confluence Administration.
2. Click on the **Application links**.
3. Enter the **URL** associated with your Jira System.
4. Click on the **Authenticate to see status** and the **Allow** button.

For official Atlassian documentation on configuring application links, see [Linking Confluence to Another Application](https://confluence.atlassian.com/doc/linking-to-another-application-360677690.html).

Now, you need to add the URLs of XML files from a Jira instance:

1. Go to the Confluence Administration.
2. Go to **External Gadgets**.
3. Add the **Gadget Specification URL**, which you can find on your Jira Dashboard.

For official documentation, see [Finding the URL of an Atlassian Gadget](https://confluence.atlassian.com/display/GADGETS/_Finding+the+URL+of+an+Atlassian+Gadget).

![Screenshot of the External Gadgets section in Confluence Administration.](/cms_trial/assets/59e349cb-afee-480e-a3e5-caddee61fb0a.png)

1. Go to your Confluence page.
2. Click the **Edit** button.
3. Click the **+** button.
4. Select the gadget you want to add.
5. Click **Save** and **Insert** the gadget.
6. Click **Update** on your Confluence page.

![Screenshot of inserting a gadget on a Confluence page.](/cms_trial/assets/2a255266-b063-48ce-9454-040eb94ff09c.png)