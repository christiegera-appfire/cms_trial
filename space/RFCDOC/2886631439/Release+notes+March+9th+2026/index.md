# Release notes March 9th 2026

**Release date**: March 9, 2026

Our team is thrilled to announce the latest release of Rich Filters for Jira Dashboards.

---

## Enhancements

## Enhanced permission control

A new **Managing rich filters** setting has been added to the **App configuration** > **Permissions** page. This is a significant quality-of-life update for Jira admins who need to delegate authority.

**What’s changed**

You can now grant specific user groups administrative rights over *all* rich filter objects.

**The benefit**

These groups can edit or delete any rich filter across the instance, even if they aren't explicitly assigned to it.

Jira admins still retain management rights by default. Enhanced permission control just allows broader "super-user" delegation.

To learn more about permissions, see [App configuration](https://appfire.atlassian.net/wiki/spaces/RFCDOC/pages/edit-v2/783943002).

## Decimal precision in Gauge gadgets

You now have granular control over how percentages appear in both **Simple** and **Smart Gauges**. This solves the issue of inconsistent rounding on dashboards.

Setting name: **Decimals for percentage**

|  |  |  |
| --- | --- | --- |
| **Setting value** | **Result example** | **Best for** |
| **None** (default) | `2%`, `26%`, `100%` | Clean, high-level overviews |
| **Maximum 1** | `2.4%`, `25.6%`, `100%` | Precision tracking and nuanced KPIs |

- **Automatic update**: Existing gadgets will default to the **None** setting.
- To keep your dashboards looking sharp, values **above 100%** drop the decimals to save space.

To learn more about gauge gadgets, see [The Rich Filter Smart Gauges Gadget](https://appfire.atlassian.net/wiki/x/ZgK6Lg) and [The Rich Filter Simple Gauges Gadget](https://appfire.atlassian.net/wiki/pages/resumedraft.action?draftId=783942228).

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Rich Filters for Jira Dashboards!