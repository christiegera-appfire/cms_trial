# Week numbering

## What are the week numbers?

There are at least six different week numbering systems in use around the world.

The most widely used system for week numbering is the International Standard ISO 8601. In this system, Monday is considered the first day of the week, followed by Tuesday, Wednesday, Thursday, Friday, and Saturday, with Sunday as the seventh and final day. According to this standard, the first week of the year is the week containing the first Thursday.

In the Gregorian calendar, most years consist of 52 weeks, but if a year begins on a Thursday or is a leap year starting on a Wednesday, it will have 53 numbered weeks. These week numbers are commonly used in many European and Asian countries.

On the other hand, in countries such as the United States, Canada, Australia, and New Zealand, calendars typically begin the week on Sunday rather than Monday.

In BigPicture, the **Region** > **Week numbering** tab allows you to customize the week numbering settings to match the week numbering system used in your organization.

## Security and access

Only Jira/App Admins can manage the app on the global (app) configuration level.

To access the global settings for the week numbering:

1. Click the **wrench icon** in the top right corner.
2. Select **Region** from the dropdown.

This will take you directly to the **Week numbering** page.

![App configuration page.](/cms_trial/assets/f517c1fd-32db-4947-b833-523c12bdb130.png)

## Adjust week numbering

On the **Week numbering** page, you can set the first week to begin on Monday or Sunday, including January 1 or January 4.

![Week numbering settings.](/cms_trial/assets/1891ee89-ca9a-469a-9096-d9995e9a9419.png)

## Week numbers on timelines

You can observe the impact of your settings in modules that visualize a project against a timeline (scale). Currently, the week numbering is supported in the Gantt and Resources modules.

**Week numbering** settings do not affect weekends. Regardless of your custom settings, all the timelines in the Gantt and Resources modules will display weekends as gray columns on Saturdays and Sundays.

### Gantt module

In the Gantt module, only the Gantt timeline visualizes week numbers.

To see the **week numbers**, check the box under the timeline settings (**triple dots**). The week numbers will appear above the daily scale.

For example, W50 means Week 50.

![Gantt timeline settings.](/cms_trial/assets/dd2a0afa-e907-4c2c-98ff-f536594743d5.png)

If the timeline is zoomed out too much, the **Week numbers** option is grayed out. Zoom in the scale until this option becomes available.

![Week numbering checkbox is grayed out.](/cms_trial/assets/71d6e1ca-9dfe-4951-97bf-7d70425ed378.png)

Below, you can see the effect of a week numbering beginning on Sunday and including January 1 on the Gantt timeline. The first week of 2025 begins on Sunday, December 29, 2024.

![First week of 2025 visualized on the Gantt timeline.](/cms_trial/assets/ea96c10c-ecc5-4034-b1ea-dcc721efa77c.png)

### Resources module

In the Resource module, the week numbering is enabled by default and available in a combination of any **Time period** and **Aggregation**.

![Rresources grid timeline showing half-year time period aggregated by months.](/cms_trial/assets/cb1d495f-923e-40e2-a2bd-ce78af2ce131.png)

If you change the time period and aggregation to more granular levels, you will notice that the first week of 2025 also begins on Sunday, December 29, 2024.

![First week of 2025 visualized on the resources grid timeline.](/cms_trial/assets/be1e6a79-6199-4887-b49f-0d2acaa1e73a.png)