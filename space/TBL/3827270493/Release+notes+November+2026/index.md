# Release notes November 2026

**Release date**: November 19, 2026

This page outlines the updates included in the latest release of Advanced Tables for Confluence.

Version: 9.0.0

---

## New features

## Bulk migration for legacy table macros

Confluence administrators can now bulk-migrate legacy Advanced Tables macros – CSV, JSON Table, and Table Plus to new macros in a Confluence space.

| **Legacy macro** | **New macro** |
| --- | --- |
| CSV | Advanced Table Viewer |
| JSON Table | Advanced Table Viewer |
| Table Plus | Native Table Enhancer |

You cannot roll back a bulk migration. To reverse the migration changes on an individual page, restore an earlier version of that page from its Confluence version history.

Administrators can scan a space for legacy macros, review the expected migration impact, and migrate selected macros in bulk to the new macros.

- To get started, navigate to **Advanced Tables Configuration** from Confluence administration and select **Migration**.

- Select a space and provide a label (optional) to set up the migration scope and scan the space for legacy macros.

  ![Select a space and provide a label (optional) to set up the migration scope and scan the space for legacy macros](/cms_trial/assets/0dfdf1af-a7a7-4791-bbd4-85253bfc7a55.png)

- Review the list of legacy macros and their migration impact, then run the bulk migration. For more information, refer to [Migrate legacy table macros to new Advanced Tables macros](/cms_trial/space/TBL/3815178296/Migrate+legacy+table+macros+to+new+Advanced+Tables+macros/).

  ![Review the list of legacy macros and their migration impact, then run the bulk migration](/cms_trial/assets/c99acd75-dd97-4af6-bb85-20fc6521fe76.png)

Macros that cannot be migrated are automatically excluded from bulk migration.

## External data access controls

Advanced Tables for Confluence now lets Confluence Site and Organization administrators control which external HTTPS domains the app can access to import CSV, JSON, Excel, and profile data.

This feature helps administrators manage external data access according to their organization's security policies while aligning with Atlassian's enhanced security requirements.

You need Confluence Site or Organization administrator permissions to manage domains.

**Action required**: The Advanced Tables macros already using external URLs to import CSV, JSON, Excel, and profile data will stop loading data until a Site or Organization administrator approves the domain. Users see an error instead of the table data.

![AT_Table not available message on page_users view.png](/cms_trial/assets/cad8de8d-9354-4c49-84ab-1863aa21d90b.png)

**Administrators can:**

- Approve up to 10 specific HTTPS domains for external data access.
- Allow access to all external HTTPS domains by entering \*, if the organization's security policy permits.
- Add or remove approved domains and manage domains.

To add and approve domains, go to **Advanced Tables Configuration** > ***External data access***, and add the specific HTTPS domains. For more details, refer to [Manage external data access for Advanced Tables for Confluence](/cms_trial/space/TBL/3842179130/Manage+external+data+access+for+Advanced+Tables+for+Confluence/).

![To add and approve domains, go to Advanced Tables Configuration then External data access and add the specific HTTPS domains](/cms_trial/assets/dbbcbc80-2254-42f4-bae9-6ddf63f32d52.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Advanced Tables for Confluence!