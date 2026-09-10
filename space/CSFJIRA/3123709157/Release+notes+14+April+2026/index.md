# Release notes 14 April 2026

**Release date**: April 14, 2026

Our team is thrilled to announce the latest release of Connector for Salesforce & Jira Cloud.

---

## Enhancements

## Salesforce Security fixes

- Security vulnerability fixes have been added.

## Jira Cloud Visual improvement

- The layout of Jira Work Item Panel dialogs, including *Create Salesforce Record, Associate, Bulk Associate, Details*, and *Configure,* has been updated for improved visual consistency across all modals. Existing functionality is unchanged.

## Jira CloudImproved navigation

- A top navigation bar in the administrator UI, providing a tab-based experience with consistent branding, has been introduced. You can now switch quickly between your **Connections**, **Bindings**, **Settings**, and **Get started** tabs.

  ![image-20260331-114138.png](/cms_trial/assets/22114420-e53a-4244-9ccd-46baf1fc3fb9.png)

---

## Bug fixes

- Jira Cloud Salesforce **Restricted comments sent in notifications**

We have fixed an issue where **Simple Email Notifications** included the full content of role-restricted Jira comments. The Connector now checks comment visibility settings before dispatching notifications, and any comment restricted to a project role is excluded entirely from email content. This ensures that role-restricted comments remain confidential to their intended audience and are no longer disclosed through notification emails.

- Jira Cloud **Unable to delete Bindings**

We have resolved an issue where integration bindings could not be deleted. You can now successfully remove bindings again.

- Jira Cloud **Unable to access Connector for Salesforce & Jira**

We have resolved an issue where users were unable to access the Connector for Salesforce & Jira app due to a policy error. You can now access the Connector in Jira without interruption.

---

**Support and resources**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=overview&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622094034771.1622098833267.313&__hssc=72543820.44.1622098833267&__hsfp=950301092).
- If you encounter any issues, raise a ticket with our [support team.](https://appf.re/support)
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=reviews&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622094034771.1622098833267.313&__hssc=72543820.44.1622098833267&__hsfp=950301092).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Connector for Salesforce and Jira!