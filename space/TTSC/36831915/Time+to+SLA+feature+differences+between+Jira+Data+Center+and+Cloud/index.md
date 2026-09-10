# Time to SLA feature differences between Jira Data Center and Cloud

Last updated: July 8, 2026

This page provides a high-level overview of Data Center and Cloud feature differences. If you’d like a more detailed breakdown, refer to the in-depth [feature comparison page](/cms_trial/space/TTSC/2760802311/Detailed+feature+comparison/).

## Advantages of Time to SLA for Jira Cloud

The Cloud version of Time to SLA is designed to minimize administrative work, support complex business processes, and provide a guided, ready-to-use setup for teams of any size.

Click to learn more about the benefits:

Each improvement in the cloud contributes to one of three main areas: a smarter administrator experience, advanced process control, and global collaboration. Here’s what you and your teams will gain:

### **A smarter, faster administrator experience**

We've redesigned the administrator experience to significantly reduce the learning curve and the time spent on configuration.

- **Get started in minutes:** A new **Onboarding Helper** provides a getting-started guide and ready-made solutions for common goals (like tracking compliance or improving response times).
- **Build SLAs with confidence:** Create new SLAs in four easy, well-defined steps, or use templates to get started even faster.
- **Eliminate JQL guesswork:** Our goal definition tool features built-in filters for work item type, request type, and assignee, making it user-friendly for novice administrators and reducing the need for complex JQL.
- **Automated best practices:** We automatically create built-in notifiers (like 50% elapsed time reminders) for every new SLA, saving you setup time and ensuring your teams are always proactive.

### **Powerful, real-world process control**

Cloud enables sophisticated, enterprise-grade logic that mirrors your true business processes, no matter how complex.

- **Chain SLAs together:** You can now trigger SLAs based on other SLAs. This lets you build true "chain of command" workflows (for example, when the *UX SLA* completes, the *Dev SLA* automatically starts, which then triggers the *QA SLA*).
- **Handle any contractual need:** Easily create grouped (All/Any) conditions to build sophisticated rules that match your most complex enterprise contracts.
- **Flexible, real-world adjustments:** Admins can grant work item-level contract extensions for one-off customer-approved delays, ensuring reports are accurate and teams aren't penalized for exceptions.
- **Manage event "race conditions":** A new setting lets you override the default event order (start/pause/stop), giving you precise control when two events happen at the exact same moment.

### **Unmatched multi-team and global operations**

The cloud version is built for how modern, distributed teams work. It breaks down silos between departments and time zones.

- **Dynamic calendars:** You can now use dynamic calendar selection based on a work item field. This is a massive win for global teams, empowering users in different time zones to customize SLAs on the fly without forcing admins to create dozens of separate goals.
- **Create shared accountability (The "push"):** You can "push" a primary SLA's panel onto linked work items. This makes a customer-facing SLA visible to internal teams (like DevOps), ensuring everyone understands the urgency.
- **Build a "mission control" (The "pull"):** You can "pull" all SLA panels from linked work items and display them on a parent ticket. This is perfect for managing complex processes (like employee onboarding) from a single "mission control" view.

For details on how the Data Center and Cloud versions compare, refer to the table below.

| **Feature/Parameter** |  | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- | --- |
| Main features |  | ✅ | ✅ |  |
| Onboarding helper (Getting Started Guide) | ❌ | ✅ |  |
| List / Filter SLAs | ✅ | ✅ |  |
| Import JSM SLAs | ✅ | ❌ |  |
| Add new SLA definition from template | ❌ | ✅ |  |
| Create new SLA definition from scratch | ✅ | ✅ |  |
| Define SLA Scope | ✅ | ✅ |  |
| Condition Definitions (Start/Stop/Pause/Reset) | ✅ | ✅ |  |
| Condition Based on other SLAs | ❌ | ✅ |  |
| Conditions with pre-filled common settings | ❌ | ✅ | Such as a start condition, such as `Issue is Created`, or a stop condition, such as `Issue Resolved`. |
| Grouped conditions | ❌ | ✅ |  |
| Goal definition | ✅ | ✅ |  |
| Goals definition with built-in issue type, request type, assignee and issue filter. | ❌ | ✅ |  |
| Calculation Method | ✅ | ✅ |  |
| Critical Zone | ✅ | ✅ |  |
| Event Order | ❌ | ✅ |  |
| Linked Issue SLA | ❌ | ✅ |  |
| Notifiers definition | ✅ | ✅ |  |
| Built-in notifiers automatically created after SLA creation | ❌ | ✅ |  |
| Calendar definition | ✅ | ✅ | Unlike the 24-hour shifts in DC, a maximum shift in the cloud runs from 00:00 to 23:59. |
| Dynamic calendar selection via issue | ❌ | ✅ |  |
| SLA fields | ✅ | ✅\* | \*Cloud currently supports the **SLA Date**, **SLA Indicator**, **SLA Duration**, and **Dynamic Calendar** fields.  Since the functionality differs, please refer to the [documentation](/cms_trial/space/TTSC/2875654192/Custom+fields/) for full details. |
| SLA Panels | ✅ | ✅ |  |
| Permissions | ✅ | ✅ |  |
| SLA Reports | ✅ | ✅\* | \*Cloud also supports [Executive reports](/cms_trial/space/TTSC/3404431363/Executive+reports/). |
| SLA Recalculation | ✅ | ✅ |  |
| Integrity Checker | ✅ | ❌ |  |
| Settings | ✅ | ✅ |  |
| Import/Export | ✅ | ✅ |  |
| License Management | ✅ | ❌ |  |
| Time to SLA preferences | ✅ | ✅ |  |
| Features in Project Settings | Customer Portal SLAs | ✅ | ✅ |  |
| Features in Workflow | Post function (Reset SLA) | ✅ | ✅ |  |
| Features in Dashboards | Gadgets | ✅ | ⚠️ | Currently, only `TTS - Periodic Met vs Exceeded SLA` is available in the cloud. However, a new gadget called `TTS - SLA/Assignee Performance Gadget` is now on the cloud. |
| Features in Issue Search | JQL Functions | ✅ | ❌ |  |
| Features in Issue View | Issue Actions | ✅ | ✅ | In the cloud, you can [trigger Jira automation rules via notifiers](https://appfire.atlassian.net/wiki/x/kgVEVw). |
| SLA History | ✅ | ✅ |  |
| SLA Overview | ✅ | ❌ |  |
| SLA Panel - SLA info | ✅ | ✅ |  |
| SLA Panel - Contract Extension | ❌ | ✅ |  |
| Features in Non-GUI Access | REST API | ✅ | ✅ |  |
| Integrations | eazyBI | ✅ | ✅ |  |
| Automation for Jira | ✅ | ✅ |  |
| Better Excel Exporter | ✅ | ❌ |  |
| Configuration Manager for Jira | ✅ | ❌ |  |
| Theme Extension for JSM | ✅ | ❌ |  |
| PowerBI Connector for Jira | ✅ | ❌ |  |
| Dashboard Hub Pro (Charts, Reports, Time in Status for Jira) | ❌ | ✅ |  |