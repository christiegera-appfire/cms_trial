# Dark theme

Sometimes you need to work with your dashboards in the evenings, and a white glowing dashboard is hard to look at after many hours in front of the screen. Rich Filters for Jira Dashboards lets you switch to Jira's dark theme, so every gadget, filter, and chart stays legible in the dark as in the light.

![image-20260922-064317.png](/cms_trial/assets/b035599f-0a27-40b7-a1ea-3d2cd0b07535.png)

## Prerequisites

- Access to a Jira instance with the [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) app installed.
- A dashboard already configured with one or more rich filter gadgets (see [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) if you don't have one yet).

## Let rich filters follow your Jira dark theme

Rich filter gadgets don't have their own theme toggle; they simply follow the appearance setting you've already chosen in Jira. That means switching to dark mode shows the same dashboard, filters, and data, just rendered with a dark palette.

1. In Jira, click your profile avatar in the top-right corner.

   ![image-20260720-072342.png](/cms_trial/assets/63c06a22-580d-4c8c-8b3b-1c4f0f97afa9.png)
2. Click **Theme** and select **the Dark** option (or **Match browser** if you want it to follow your OS).
3. Open any dashboard containing rich filter gadgets. They all pick up the new theme immediately.  
   If you present dashboards on a shared screen or projector, try switching back and forth between light and dark to see which is easier to read for your room's lighting.

## Rich filter gadgets follow your Jira theme automatically

Below are examples of rich filter gadgets rendered in the dark theme.

- **Rich Filter Controller gadget**: You can see filters (for example, *Assigned to me*, Status: *In Progress*, Priority: *High*) keep their assigned colors adjusted to the dark theme.

  ![Rich Filter Controller gadget in a dark mode](/cms_trial/assets/7a4780d1-cd1a-46d5-bab1-39c2a5921beb.png)

- **Rich Filter Results gadget**: displays an issue list with issue-type icons, priority header colors, status tags, and row highlighting, all of which have been adapted to the dark theme.

  ![Rich Filter Results gadget in a dark theme](/cms_trial/assets/280d7e98-65e7-4ebf-86d7-7f6c4612daab.png)

- **Rich Filter Issue Activity Stream gadget**: displays a chronological feed of recent activity (comments, status changes, etc.), with readable timestamps and activity icons in the dark theme.

  ![Rich Filter Issue Activity Stream gadget](/cms_trial/assets/be87be94-c5c9-4f5f-8ef6-2d1b794480d3.png)
- **Rich Filter Smart Counter gadget** - displays issues resolved by teams, with each team labeled in a selected color.

  ![image-20260723-061453.png](/cms_trial/assets/8970d575-29cd-4e2a-9437-df80f41ff080.png)

- **Rich Filter Simple Gauges gadget** - displays gauges representing custom ratios as percentage-based visual indicators, each gauge labeled in a selected color.

  ![image-20260722-113023.png](/cms_trial/assets/5617adee-a8bf-4e06-8776-c237001ba585.png)

- **Rich Filter Two Dimensional Statistics gadget**: clustered bar chart of Story Points by Assignee, displaying color-labeled Priorities.

  ![image-20260722-121952.png](/cms_trial/assets/d8e2a12b-51bd-43f7-826b-cd6144b32d5d.png)

- **Rich Filter Flexi Charts gadget**: *Donut chart* of Story Points by Priority displays different priority levels that are easily distinguishable with color adjusted to the dark theme.

  ![Rich filter Flexi Charts gadget in a dark theme](/cms_trial/assets/484fe9d6-485e-4cdd-8181-dcadf5b73bf9.png)

- **Rich Filter Time Series Chart gadget**: *Time series* presenting cumulative trend of average resolution time. The trend lines and thresholds stay readable and match the same dark theme.

  ![image-20260722-080040.png](/cms_trial/assets/5d830cb7-cbfd-481d-8951-06151341ede8.png)

## Rich filters configuration

When you need to configure your rich filter, the dark theme is

![Rich filters configuration](/cms_trial/assets/4ec83b06-0f86-4209-94a6-31471f05f459.png)

## Rich filter features referenced in this article

- [Rich Filter Controller gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) for quick filters that keep their color-coding in dark mode.
- [Rich Filter Results gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) for issue lists with status colors and the **Open issue** dialog.
- Rich Filter Charts & Stats gadgets for burndown charts, gauges, and single-value stats with dark-mode-aware color contrast.
- [Rich Filter Text Panel gadget](/cms_trial/space/RFCDOC/783942398/The+Rich+Filter+Text+Panel+Gadget/) for checklists, links, and expandable notes.