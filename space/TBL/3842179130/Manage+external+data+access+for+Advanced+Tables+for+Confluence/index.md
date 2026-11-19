# Manage external data access for Advanced Tables for Confluence

## External data access

Advanced Tables lets Confluence Site or Organization administrators control which external HTTPS domains the app can access to fetch CSV, JSON, Excel, and profile data.

This feature helps administrators manage external data access according to their organization's security policies while aligning with Atlassian's enhanced security requirements.

- You can approve up to 10 domains.
- Advanced Tables macros can fetch external data only from approved HTTPS domains, unless an administrator allows access to all external HTTPS domains.
- Users can use only HTTPS URLs for approved domains. For any other URL used, the macros show an error message.

You need Confluence Site or Organization administrator permissions to manage domains.

This page explains how to add, approve, and manage domains for external data access.

## Open the External data access page

To configure external domains, navigate to the **External data access** page:

1. Log in as a Confluence Site or Organization administrator and select **Settings** (▢).
2. In the left navigation, under **Apps**, click **Advanced Tables Configuration**.
3. The **Advanced Tables** **Configuration** page opens. Click **External data access**.
4. This page shows the list of approved domains and the domain entry field.

   ![AT_External data access config.png](/cms_trial/assets/a8cff7d4-962d-458f-91c9-5e2f3bf6e0d6.png)

If no domains are approved and configured, the page displays a message.

![External data access_No approved domains.png](/cms_trial/assets/5fd0ada0-cfe4-4e69-8dab-1b1515daacd2.png)

**Limitations**

You can approve up to 10 specific domains. To add more domains when you've reached the limit, remove an existing domain first.

## View approved domains

The **Approved domains** table shows how many domains you've approved out of the maximum, for example, **3 of 10**. The table displays these columns:

- **Domain**: The approved domain, for example, `confluence.atlassian.com`.
- **Added by**: The name of the administrator who added the domain.
- **Date added**: The date the domain was added.
- **Actions**: Controls for managing the domain. Click the **Delete** (▢) icon to remove a domain.

![AT_External data access.png](/cms_trial/assets/be33c754-9225-4622-a5a2-94a6d8ea4d88.png)

## Manage domains

You can add domains for external data access or allow all domains.

### Add a domain

To add a domain, on the *External data access* tab, provide the domain details.

- **Enter a domain**: Enter a domain name without specifying https:// or a path, for example, [*gitlab.com*](http://gitlab.com)
- The **Add domain** button is disabled until you enter a domain value. To add the domain, click **Add domain**.

  ![External data sources_Add domain.png](/cms_trial/assets/70f7c974-b471-4246-b234-6bf0a3914c44.png)
- The *Domain* *Approval* dialog opens. Review the details and, click **Approve**.

  ![Domain approval dialog.png](/cms_trial/assets/8b172112-b4c2-4f01-8ab1-ad186b2541dd.png)
- The domain is approved and added to the approved domains.

  ![External data access_Domain approved.png](/cms_trial/assets/e9ec58fa-818a-4308-8759-7e0b030e3131.png)

If you enter a domain that starts with http:// or includes a path, Advanced Tables displays an error message: “*Enter a secure HTTPS domain without a path”*.

![AT_External data access_domain error.png](/cms_trial/assets/7c5a56a9-a625-4c91-b86f-347005b0896e.png)

### Allow all external HTTPS domains

- To let Advanced Tables macros fetch data from any external HTTPS domain, enter `*` in **Enter a domain** and click **Add domain**.

  ![AT_allow all domains.png](/cms_trial/assets/51d84c4f-bc5e-44b3-9a94-165ffe37946d.png)
- The *Domain* *Approval* dialog opens to review the change. To continue, click **Approve**.

  ![Approval dialog 2.png](/cms_trial/assets/10caa339-ee23-4ec4-b536-f9f8178c5cc0.png)
- The `*` entry appears in the **Approved domains** table, indicating that Advanced Tables can access all external HTTPS domains.

Allowing all external HTTPS domains removes domain restrictions. Use this option only if your organization's security policy permits. Otherwise, approve specific domains.

- After you add `*`:

The page displays a warning message, **Approved domains (all external domains)**, and a **Saved domains** section.

- - **Approved domains (all external domains)**: The table under **Approved domains (all external domains)** shows one row with domain entry : `*`, labeled **All external HTTPS domains**.
  - **Saved domains**: When you allow all external HTTPS domains, Advanced Tables moves previously approved domains to the **Saved domains** section. These domains remain saved but aren't used to control access.

    - To restore access restrictions to specific domains, remove `*`. In the **Approved domains** table, click the Delete icon in the `*` row.
    - The domains under **Saved domains** will move back to **Approved domains**.

      ![AT_Approved and saved domains.png](/cms_trial/assets/2a4331c1-9f56-4825-9177-7f1671ed22c4.png)

### Add a domain while all external domains are allowed

If you have approved all external domains, then any new domain you add appears under **Saved domains** section.

- For example, enter [google.com](http://google.com) and click **Add domain**.

  ![AT_add domain to saved domains with all external added.png](/cms_trial/assets/14d0da71-07e0-46f0-b603-84d06a010322.png)
- The domain [google.com](http://google.com) is saved under **Saved domains** section.

  ![AT_domain added to saved domain.png](/cms_trial/assets/0460741d-3faf-4db2-a46d-81cf0a76b2a2.png)

### Remove a domain

You can remove a single domain or remove all at once.

1. In the **Approved domains** or **Saved domains** table, find the domain you want to remove. For example, [google.com](http://google.com).
2. In the **Actions** column, click **Delete** (▢).

   ![AT_click remove to delete a domain.png](/cms_trial/assets/093b9dca-3f1b-4e43-9dd0-390c95661a0d.png)
3. The domain is removed from the **Saved domains** list. You will see a removal message.

   ![AT_domain removal message.png](/cms_trial/assets/d2f703b2-f879-4c32-b880-d02fc5252932.png)

After you remove a domain, Advanced Tables can no longer fetch data from it. Tables that use that domain stop loading data, and users will see an error message.

### Remove all approved domains

- To remove all domains, including saved domains section, click **Remove all**.

  ![AT_remove all domains.png](/cms_trial/assets/4506ab59-c1b5-473e-9a89-0cfcb847e6ce.png)
- This removes all domain entries, whether it is under **Approved domains** or **Saved domains**.

  ![AT_All domains removed_message.png](/cms_trial/assets/27a6d9b4-dbe5-4524-881f-7b6e02878ea1.png)
- Advanced Tables macros that import data from these domains can't load data until you approve the required domains again. The Confluence users will see an error message until the domains are approved.

## Troubleshooting

If a table doesn't load external data, check the following:

- If the domain is approved, verify that the source URL starts with `https://`.

  ![AT_HTTP error.png](/cms_trial/assets/396fd0d8-d782-4ba5-b9b4-17a6b3a3477c.png)
- Verify that the domain appears in the **Approved domains** section.

  - If you have not added any domain for external data access, then Confluence users will see a message.

    ![AT_No approved domains message in macros.png](/cms_trial/assets/8a814eef-7439-4327-ac2b-fd75c573310e.png)
  - If Confluence users use a domain URL that is not approved, they will see an error message.

    ![AT_Error when domain is not approved.png](/cms_trial/assets/1b57bbc4-95b3-4950-8f97-6c2288a4f81e.png)
- Check whether the domain was removed after the macro was configured.

  - If you remove a domain that's used in a macro, the macro displays an error for the Confluence users.

    ![AT_Table not available message on page_users view.png](/cms_trial/assets/196e539e-961d-46f1-a182-66afa0bb952d.png)
  - If you remove a domain that's used in a macro, as an administrator, you will see this error on the Confluence page.

    ![AT_Table not available_admin message.png](/cms_trial/assets/a8ac4234-b11b-4dac-bc36-242b0c8b942d.png)
- Check whether the 10-domain limit has been reached. To add more domains, remove a domain you no longer need, then add the new one.

  ![AT_ten domains error.png](/cms_trial/assets/265763bc-128d-4a64-9288-34d350d8573b.png)
- If you encounter a permission issue and cannot approve the domain, check whether you have the required Confluence Site or Organization administrator permissions.