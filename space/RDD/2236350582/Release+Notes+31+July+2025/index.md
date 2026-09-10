# Release Notes 31 July 2025

**Release date**: July 31, 2025

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira, Confluence, Bitbucket and monday.com.

[unmapped inline: placeholder]

---

## Enhancements

## Miscellaneous improvements

- Better error logging.
- Hybrid users (those who are both Jira users and JSM customers) are now **automatically redirected** to Dashboard Hub in Jira, improving the experience for agents working across JSM and Jira projects.
- Dark mode in Data Center is now based on host theme configuration.
- Better messages for invalid tokens.
- The default private datasources *This Jira instance* and *This Confluence instance* now display the original owner’s name, so it’s easier to understand when configuring a gadget with different datasources, for example, *This Jira instance* - `https://jira.atlassian.net (as Maria McFlurry):`

  ![Dashboard Hub datasource shown in a gadget configuration dialog](/cms_trial/assets/105f897c-606e-43e8-8c3e-9eadd4fc594b.png)

---

## Bug fixes

The following bugs are fixed in this release:

- Images in the **Description** field were not displayed when dashboards were shared publicly.
- The **Parent** field mapping was incorrect.
- Confluence macros unexpectedly resized when using Firefox.
- **Jira Custom Charts gadget**:

  - Did not correctly display sprint names.
  - Displayed user IDs instead of names in multi-user fields.
  - Displayed an error when using a Pie Chart with a Single List (Cascading) field.
- Romanian translation did not appear correctly on some screens.
- **Projectrak:**

  - Gadgets continued showing a loading spinner even after data had fully loaded.
  - Users were unable to add Projectrak datasources.
  - The Project Timeline gadget returned an error due to JQL query issues.
- Incorrect trend lines appeared under certain edge-case conditions.
- The selected maximum number of segments was lost when switching between view types.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in the Dashboard Hub family of apps!

---