# Release notes 10 July 2025

**Release date**: July 10, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### **Excel export now respects 32,000-character cell limit**

We’ve implemented a safeguard for Excel exports to prevent any cell from exceeding the 32,000-character limit. This ensures compatibility with Excel’s constraints and avoids data truncation or file corruption.

### Refined handling of 'No target' goal type

SLAs configured with the No target goal type are now handled explicitly as a valid goal type instead of being treated as null. This improvement ensures better consistency across SLA calculations and reporting when no specific target time is required.

### Auto-match for SLA groups and calendars

To streamline SLA setup, we’ve added automatic matching for:

- **Groups** – SLA groups are now auto-selected based on issue context, minimizing manual configuration.
- **Calendars** – The system now automatically applies the most relevant calendar, ensuring accurate time tracking without user intervention.

---

## Bug fixes

The following bugs are fixed in this release:

- We fixed a validation issue that was preventing users from saving or editing certain report configurations. You can now set up and modify reports without running into unexpected errors.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---