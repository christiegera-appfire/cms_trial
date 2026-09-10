# Release notes May 2026

**Release date**: May 7, 2026

This page outlines the updates included in the latest release of Advanced Tables for Confluence.

Version: 7.2.0

---

## New features

## Advanced Table Viewer macro

### Group calculation

Now you can perform column calculations at the group level and display summarized values at each level of the nested group. The summarized value for each group is calculated from the values in its nested groups, rolling up through each level.

- To apply group calculations, you must first group the required columns.
- To configure group calculation for any column, navigate to **Edit column** > **Edit group calculation**.

  ![Edit column with Edit group calculation selected.](/cms_trial/assets/4c5f0a3b-6a2e-4211-b4f5-108fe872e44a.jpg)
- Select the calculation type. You can apply only one calculation type for each ungrouped column.

  ![Edit group calculation dialog with None option selected.](/cms_trial/assets/1c3b7f93-8c9c-4728-8b13-61b087dea70e.png)
- The group calculation appears as follows:

  - For example, Average is applied to the **Unit Price** column, and Minimum is applied to the **Stock Qty** column.
  - The average unit price and the minimum stock quantity roll up from individual product rows to their Stock Status, Supplier group, and further to the top-level category.

    ![Advanced Table View macro showing Group calculation.](/cms_trial/assets/a78b91e8-814a-4f5c-aa1e-70d15299e535.jpg)
- For more information, refer to [Column group calculation with Advanced Table Viewer macro](/cms_trial/space/TBL/3219587079/Column+group+calculation+with+Advanced+Table+Viewer+macro/).

---

## Bug fixes

The following bugs are fixed in this release:

- The JSON macro was not rendering data from a Jira REST API URL using authenticated profiles.

  - This issue is resolved. The JSON macro correctly renders data from Jira REST API URLs using authenticated profiles.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Advanced Tables for Confluence!