# Critical version upgrade required

**Current latest version:** Salesforce Jira Cloud (SFJC)7.2.0

---

## What's changing

The Connector for Salesforce & Jira Cloud is transitioning from Connect to the Forge architecture. This migration improves performance and reliability but requires all customers to be on the latest marketplace version to ensure continued functionality. If your app version is below 7.0.0, follow the steps to upgrade it.

### Upgrade

1. Navigate to **Administration**>**Connected apps** in your Jira instance.
2. Find the **Connector for Salesforce & Jira Cloud** in your installed apps and click **View app details**.
3. Click the **Update** button at the top right.
4. Follow the prompts to complete the upgrade

From version 7.0.0, the app requires new permission scopes. Please review and approve these permissions during the upgrade process.

**If you remain on an older version, you can experience:**

- App malfunction or unexpected behavior
- Complete service disruption
- Inability to receive frontend updates once the Forge transition is complete
- Potential breakage when new backend versions are released

**Once we fully transition to Forge:**

- Frontend updates will only be delivered to customers on the latest version
- Automatic upgrades are not possible due to the new permission scope requirements
- Backend updates can inadvertently break compatibility with older frontend versions

---

**Support and resources**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=overview&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622094034771.1622098833267.313&__hssc=72543820.44.1622098833267&__hsfp=950301092).
- If you encounter any issues, raise a ticket with our [support team](https://appf.re/support)[.](https://appf.re/support)
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=reviews&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622094034771.1622098833267.313&__hssc=72543820.44.1622098833267&__hsfp=950301092).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Connector for Salesforce and Jira!