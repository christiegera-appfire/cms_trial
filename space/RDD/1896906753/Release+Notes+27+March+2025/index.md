# Release Notes 27 March 2025

**Release date**: March 27, 2025

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira, Confluence, Bitbucket, and monday.com.

[unmapped inline: placeholder]

---

## New features

## Permissions in datasources

Now you can configure permissions in datasources, and indicate who can use and/or edit your datasources. You’ll find the following options to set up access restrictions:

- "Anyone can use and edit"
- "Anyone can use, some can edit"
- "Only specific people can use or edit"

Read everything you need to know here: [Manage permissions on datasources](/cms_trial/space/RDD/1899429890/Manage+permissions+on+datasources/)

## Custom Reports beta

Breaking changes! Thanks to your comments and increasing demand of more complex functionality, we are moving to more robust delimiters for interpolations. Now, instead of using single curly brackets, descriptors will require double curly brackets. Thus, if your JSON data is `{ hello: 'world', number: 4 }` then your interpolated text will be `Hello {{$.data.hello}} {{$.data.number}}` and the result will render as `Hello world 4` .

Thanks to all customers and partners for sending your feedback, please, keep contacting us.

## Transition Time from Status to Status

Gain deeper workflow insights with the new **Transition Time from Status to Status** gadget.  
Measure how long it takes for issues to move between statuses to identify delays, spot bottlenecks, and optimize team efficiency.  
Generate flexible reports by issue or over time (daily, weekly, monthly, etc.), and analyze transition trends to continuously improve your delivery process.

![Dashboard Hub transition time from status to status](/cms_trial/assets/8c739999-f39a-4898-af05-9643e393c32f.jpeg)

Read more details of this new gadget here: [Transition Time from Status to Status](/cms_trial/space/RDD/1898709009/Transition+Time+from+Status+to+Status/)

---

## Enhancements

## UX improvements

- Quickly rename dashboards and gadgets without opening their settings.
- Improved visibility for unsaved changes, unsaved changes message is now more prominent.
- Faster previews with default JQL applied to gadgets.

## Enhance Datasources Security

To improve control over data access and reduce the risk of unauthorized visibility, this release introduces a new global setting: **Restrict Owner View Mode**.

By default, datasources like “This Jira Instance” use **Owner View Mode** (see [datasource viewing modes](/cms_trial/space/RDD/146309943/Learn+about+datasources/)), meaning gadgets load data using the dashboard owner's permissions. This ensures a consistent view for all users.  
With this new restriction enabled, gadgets will instead use **Viewer Mode**, showing data based on each viewer’s own permissions. Users without access to certain fields or projects will not see restricted information.

This setting can be configured in **Global Settings > Datasource Restrictions** and does **not** apply to datasources using credentials (e.g., password or token). Read more [here](/cms_trial/space/RDD/1900118024/Manage+Datasource+Restrictions/).

## Misc

- Translations to Romanian, Russian, Arabic, and French for our international customers.
- New template for BigPicture PPM Insights, enjoy quicker access to your BigPicture metrics.
- The BigPicture Custom Charts gadget now accepts aggregations for Timetracking fields: SUM, MIN, MAX, MEAN

---

## Bug fixes

The following bugs are fixed in this release:

- Sprint Health gadget doesn’t display closed sprints data
- Menu option to access the app was visible with a dead link for restricted users (DC)
- Global access settings were restricting access to the Customer Portal
- Toggle to share the gadget configuration failed to save the setting
- Wrong order in some dates in 2D Pivot Tables

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in the Dashboard Hub family of apps!

---