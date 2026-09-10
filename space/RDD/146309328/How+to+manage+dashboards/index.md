# How to manage dashboards

## Overview

From the main dashboards page, you can switch to Dark mode, Share your dashboards internally or externally, change the Access restriction, Edit your dashboard layout, or perform several other actions using the More Actions menu.

If you have shared your dashboards with your internal Jira or Confluence users, a new URL format has been introduced due to changes to Atlassian’s Cloud platform. As of November 26, 2025, when a user tries to access a dashboard using an **internal link** with the old format, they will be redirected to our link migration tool to update the link. See our [release note](/cms_trial/space/RDD/2571436035/Release+notes+26+November+2025/) to learn more.

To access the management options:

- **Option 1** - Go to the dashboard selector in the top left section of the navigation bar, then select **Manage Dashboards**.

![Dashboard Hub How to manage dashboards dashboard preview](/cms_trial/assets/e8e44fed-5cb5-48ec-b041-f97bb4fe2d4f.png)

- **Option 2** - From a dashboard page, select **More actions** (**…**) in the top right of the navigation bar. All the available options for the current dashboard (settings, delete, clone or export), create a new dashboard, handle datasources (add or manage existing datasources) or get help (Global help, Get Started, product news, support or book a demo).

![Dashboard Hub dashboard action menu](/cms_trial/assets/7b0e2a6b-015b-4830-b92b-c0593f76cf26.png)

## Manage dashboards

The *Manage Dashboards* page is a convenient way to find and organize all your dashboards, star your favorites, filter your dashboard list, and view key information at a glance.

For each dashboard that you have access to, you’ll see the name of the creator/owner, the dashboard restrictions, the public sharing status, and the creation and last update date.

See [Dashboard permissions](/cms_trial/space/RDD/146309693/Dashboard+permissions/) for more on permissions.

![Dashboard Hub How to manage dashboards dashboard preview](/cms_trial/assets/cef29d87-b28f-451b-a247-00e684e9f7b8.png)

The *Actions* column contains the **More actions** menu for each dashboard with the following options:

- **Dashboard settings:** Edit your dashboard’s details.
- **View dashboard:** Open the corresponding dashboard.
- **Clone dashboard:**  Create a new dashboard with the same settings.
- **Delete** **dashboard:** Delete the dashboard.

## Dashboard settings

### Settings

Here you can edit the details of your dashboard: Name and description.

### Slideshow

![Dashboard Hub How to manage dashboards Dashboard settings dialog](/cms_trial/assets/ac82a3c5-ad88-4500-adb9-b121ae1a9c60.png)

In the slideshow settings, you can:

- Set the default time for the slides to advance to the next one.
- Add more slides to the slideshow.
- Reorder the slides.
- Set the individual time for each slide to advance to the next one.

Tables in the JQL Custom Charts gadget **auto scroll** when the slideshow is playing, so viewers can see the content without interaction!

For that, enable “Enable automatic table scrolling when the slideshow is in play mode”

See [How to set up a slideshow](/cms_trial/space/RDD/146309888/How+to+set+up+a+slideshow/) for further information.

### High Priority

High priority gadgets are intended for those use cases where the default refresh rate of 3 minutes (15 minutes in case of Opsgenie) is not enough, like strict SLAs in premium support for example.

![Dashboard Hub How to manage dashboards Dashboard settings with high priority gadget](/cms_trial/assets/e40f5c92-7901-42cd-b8cb-7d78cecdd40d.png)

Dashboard creators can select up to two gadgets to increase the refresh rate to one minute. For those gadgets, the information will be updated every minute.

A frequent refresh rate can degrade performance. We recommend reading each service provider’s rate limit policy

Opsgenie applies a [rate limit](https://docs.opsgenie.com/docs/api-rate-limiting) to the API and integration requests.

The selected gadgets display a high-priority icon to indicate that their refresh rates are more frequent than the others.

![Dashboard Hub high priority gadget preview](/cms_trial/assets/32fef309-bbe7-4f77-bbdf-0e9bfb7a5f69.png)

## Related pages

- [How to set up a slideshow](/cms_trial/space/RDD/146309888/How+to+set+up+a+slideshow/)
- [How to set up a wallboard](/cms_trial/space/RDD/146310022/How+to+set+up+a+wallboard/)
- [Add and configure gadgets](/cms_trial/space/RDD/146310019/Add+and+configure+gadgets/)
- [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/)
- [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)