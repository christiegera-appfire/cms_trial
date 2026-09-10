# Release notes 25 June 2026

**Release date**: June 25, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## New features

## JQL Custom Segments

The new JQL Custom Segments gadget lets you compare custom subsets of Jira data on a single chart. Define a base JQL query, then add up to 10 named segments, each with its own JQL or saved filter, then view them side by side as bars, lines, areas, or pie slices. It works like the Jira Custom Charts gadget, but instead of grouping by a single Jira field, each segment has its own query, so you can compare across criteria that don’t map to any one field. This replaces the need to set up multiple separate gadgets to compare different views of the same data. You can also add an *All* segment to compare your subsets against the full base query, while the automatic *Other* segment groups any work items not covered by your named segments.

![JQL Custom Segment gadget rendered as a bar chart in Dashboard Hub.](/cms_trial/assets/45808cc3-bf78-4348-a929-d53794eca097.png)

Use a single gadget to explore subsets of the same data, such as:

- **Team comparison**: Compare bug counts by priority across teams. Base JQL: `type = Bug`. Segments: `team = "Alpha", team = "Beta", team = "Gamma"`.
- **Component breakdown**: Visualize work in progress across components. Base JQL: `status = "In Progress"`. Segments: one per component.
- **Benchmark your work**: See how your work compares to the rest of the team. Create a segment for `assignee = currentUser()` and let the [*Other*](https://support.appfire.com/space/RDD/3362816011/JQL+Custom+Segments#The-Other-segment) [segment](https://support.appfire.com/space/RDD/3362816011/JQL+Custom+Segments#The-Other-segment) provide the contrast.
- **Total versus subset**: Show a Total baseline alongside specific segments. One segment with an empty JQL field represents the entire base query.

See [JQL Custom Segments](https://apps.appf.re/dh/doc/jira-segments) to learn more.

---

## Bug fixes

The following bugs are fixed in this release:

- **Dashboard macro in Confluence**: Resolved an issue where text was unreadable when using dark mode.
- **Dashboard creation**: Resolved an issue where a new dashboard was created every time a user navigated to Dashboard Hub within a Jira project, resulting in duplicate dashboards.
- **Jira Custom Charts gadget**: Resolved an issue where users were unable to scroll down in the 2D Pivot Table view when results exceeded the initial visible rows.
- **Progress Tracker gadget**: Resolved an issue where the app attempted to load filters that weren’t available, but not required for data visualization.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!