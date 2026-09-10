# Release Notes 12 June 2026

**Release date**: June 12, 2026

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

---

## Forge transition

We are transitioning the underlying architecture of **7pace for Jira from Atlassian Connect to Atlassian Forge**. This migration aligns with Atlassian’s modern Cloud standards, moving our app's logic and execution directly into Atlassian’s secure, cloud-native infrastructure.

While the core functionality of your time-tracking tools remains the same, this infrastructure upgrade changes how data is processed, secured, and rendered.

### Key Advantages

- **Enterprise-Grade Security and Compliance:** Because Forge apps execute within Atlassian’s multi-tenant cloud environment, your data remains within the established Jira security perimeter. This ensures strict compliance with enterprise data residency and privacy regulations.
- **Optimized Performance:** Operating as a native component rather than through external iframes reduces latency, providing faster load times for timelines, calendar views, and timesheets.
- **Platform Future-Proofing:** Moving to Forge ensures full compatibility with Atlassian Cloud updates, deep Jira Automation capabilities, and upcoming features like Atlassian Rovo AI agents.

### What to Expect & Required Actions

Because Forge changes how apps interact with Jira, please note the following operational adjustments:

- **Updated URL Structure:** Forge uses a different routing mechanism. Existing browser bookmarks, pinned tabs, or hardcoded report URLs will need to be updated to match the new URL pattern.
- **One-Time Re-Authorization:** Upon the first login post-migration, some users may see an authentication prompt requesting permission to connect their accounts to the new Forge-based system:

  ![forge-banner.png](/cms_trial/assets/44ccf47d-047a-4d47-a4ea-9a8cd062aac2.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to improve our apps continually. We appreciate your trust in 7pace Timetracker for Jira!