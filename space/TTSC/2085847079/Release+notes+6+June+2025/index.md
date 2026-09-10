# Release notes 6 June 2025

**Release date**: June 3, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## New features

### New SLA pause logic after a breach

We’ve refined how Time to SLA handles pause conditions that occur after an SLA has breached, ensuring more consistent and transparent SLA tracking.

Previously, SLA target dates could be recalculated even after the SLA had breached, if the issue entered a paused state (such as Waiting for customer ). With this update:

#### What’s new?

- If an issue enters a paused state after the breach has occurred, the SLA target date will no longer change.
- The SLA remains marked as breached, and the pause is logged for reporting and auditing purposes.
- Only pauses that occur *before* the breach continue to affect the countdown and adjust the target date.

This refinement makes it easier to interpret SLA timelines and understand exactly when a breach occurred, even if the issue enters a paused state afterward.

#### Example

Let’s say your SLA duration is 8 business hours, starting on **May 12 at 9:00 AM**:

- If the issue is paused from **11:00 AM to 12:00 PM**, the countdown is paused, and the SLA deadline is extended accordingly.
- If the issue continues and breaches the SLA at **May 12, 5:00 PM**, any *later* pause (for example, at 6:00 PM or the next day) **does not extend the target date or undo the breach**.

#### What stays the same?

- Pauses applied *before* a breach still extend the target date based on your configuration.
- All pause events are logged, including those that happen after a breach, for visibility and audit purposes.
- SLA start times are always preserved.

#### Why this matters

This update helps ensure your SLA metrics are both consistent and easy to audit. It also removes any ambiguity around how pauses work after a breach — once an SLA is breached, it stays that way.

Have questions? Feel free to contact our [support team](https://appf.re/support).

---

## Enhancements

### Terminology improvements

We updated the *API Token* page to use **Generate** instead of the ambiguous **Save** button label. This small change improves clarity and reflects the actual action being performed.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where the SLA panel was not visible after the third activation cycle. The panel now displays correctly.
- Resolved an issue where gadgets failed to show issues if an SLA used a dynamic calendar. Gadgets now work as expected with dynamic calendars.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---