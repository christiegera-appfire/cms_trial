# Release notes 25 November 2025

**Release date**: November 25, 2025

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira and Confluence.

---

## New features

## Space dashboards

Dashboards are now automatically generated for every space (project), giving teams instant visibility into space-specific reports. These dashboards are populated with gadgets tailored to the space type, including dedicated dashboards for Software and Service Management.

The first time a user opens Dashboard Hub from a space, the app automatically creates and loads the dashboard in the **Dashboard Hub** tab. The space owner is assigned as the default dashboard owner.

To access Dashboard Hub from your project, go to **More > Dashboard Hub**.

![Dashboard Hub Release notes 25 November 2025 dashboard preview](/cms_trial/assets/ade4b4a8-2662-4cff-9575-85e85319b729.png)

---

## Enhancements

### Improved alignment with Jira’s Scrum board velocity report

The Scrum Velocity gadget now uses *Actual Start Date* to calculate all related metrics.

---

## Bug fixes

- **Jira Custom Charts gadget**:

  - Resolved an issue with 1D and 2D pivot tables where the gadget rendered with excessive additional space at the bottom.
  - Resolved an issue with HTML tags in the *Last Comment* field. HTML tags no longer display in the report for the *Last Comment* field.
- **SLA report by field gadget:** Resolved an issue where the *Avg. Time* and *SLA Met* data did not load when the gadget was configured with a Jira custom field.
- **CSV and XLSX exports:** Resolved an issue with misalignment between column headings and data. Now, columns are aligned correctly if the gadget includes a multi-value field, for example, Label.

---

## Platform updates

Due to our ongoing architecture updates for Atlassian Cloud apps, the **External Page** gadget will no longer work in our Dashboard Hub Cloud apps.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! We appreciate your trust in the Dashboard Hub family of apps!

---