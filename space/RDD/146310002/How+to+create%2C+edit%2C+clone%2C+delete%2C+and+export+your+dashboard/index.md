# How to create, edit, clone, delete, and export your dashboard

## Overview

Learn how to create and organize the right metrics to transmit quick feedback to your team.

new **Project** dashboards are automatically generated for every space (project), giving teams instant visibility into space-specific reports. These dashboards are populated with gadgets tailored to the space type, including dedicated dashboards for Software and Service Management. This feature is available in Dashboard Hub Cloud apps.

The first time a user opens Dashboard Hub from a space, the app automatically creates and loads the dashboard in the **Dashboard Hub** tab. The space owner is assigned as the default dashboard owner. To access Dashboard Hub from your project, go to **More > Dashboard Hub**.

## How to create a dashboard

1. Go to Dashboard Hub, then click the **More actions** icon (**…**).
2. Select **Create Dashboard** to create a blank dashboard or use one of the provided templates.
3. In the next screen, select whether you want to start with a blank template or select one of the provided templates.
4. Click **Create**.

   ![Dashboard Hub Create a dashboard template preview](/cms_trial/assets/ff349542-dd13-4e8c-893e-c1a40cd2f055.jpg)

   For a complete list of templates, see [Dashboard templates](/cms_trial/space/RDD/146310013/Dashboard+templates/).

## Use a template

If you chose one of the available templates (see [Dashboard templates](/cms_trial/space/RDD/146310013/Dashboard+templates/)) you’ll have several gadgets in your dashboard panel. These gadgets are selected based on the type of team the dashboard is intended for. See [Add and configure gadgets](/cms_trial/space/RDD/146310019/Add+and+configure+gadgets/) to learn more.

![Dashboard Hub template selection page](/cms_trial/assets/922373cf-9822-4395-b3ca-a2c9773d9fc4.png)

## Add gadgets

To complete your dashboard panel setup with KPIs and metrics, while in edit mode, remember, to click the **Edit** button in the top right navigation bar; you’ll see new controls in the middle of the top navigation bar:

1. Click the **Add gadget** (**+**) button to open the gadgets catalog menu.

See Dashboard Hub gadgets for the full list.

1. Browse the gadgets available for each of the provided integrations and select the one you want to add to the current dashboard.
2. Complete the configuration settings for the gadget.
3. Click **Add**.

![Dashboard Hub Add gadget screen](/cms_trial/assets/88876e43-ed6d-4226-a4ec-3a617dbd7139.jpg)

## How to configure a gadget

The main components of a dashboard are the gadgets that display the information you need, in the format you want. Gadgets have to be configured with a datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/) and [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/)) that connects the tool or source of the data that you to display.

![Dashboard Hub Create dashboard dialog](/cms_trial/assets/ac5efa71-8052-4caa-bf89-dc90ba2370ff.png)

1. Click the **Settings** cog to open the configuration menu, or click **Config**.
2. Enter a name for your gadget.
3. Select a datasource. Use **Current** for the default datasource of the current instance, or select a different datasource.
4. Choose whether you want to use the current gadget configuration for all other compatible gadgets.
5. Click **Save**.

See [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/) and [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/) for more information.Create a dashboard

You can create your own instance dashboard to display the information you and your team need to stay on track:

1. Go to Dashboard Hub, then select the **More actions** icon (**…**) in the top right of the page.
2. Select **Create Dashboard** to create a blank dashboard or use one of the provided templates.
3. Fill out the **Name, Description,** and set the **Access** restriction for your dashboard.
4. In the next screen, select whether you want to start with **a blank template** or select **one of the provided templates**.
5. Click **Create**.

## Edit your dashboard

Click Edit at the top right of the navigation bar to access edit mode. New controls for adding slides or gadgets are in the middle of the top navigation bar.

Gadgets display a **Config** button and a More actions menu (**…**) to open the gadget configuration menu: *Configure*.

![Dashboard Hub How to create, edit, clone, delete, and export your dashboard dashboard preview](/cms_trial/assets/05ef5152-f2a4-43fa-9629-2946625dddcf.png)

## Clone your dashboard

Whenever you need to create a similar dashboard, you don’t need to start from scratch, you can clone an existing dashboard. From the top right **…** menu (or from the **Manage dashboards** screen) click on **Clone dashboard**. You only need to provide a new name, a description and set the new **Access** restriction. We’ll take care of the rest for you, slides, gadgets or public links are copied from the original dashboard.

## Delete your dashboard

Use this option to permanently delete a dashboard. From the top right **…** action menu (or from the **Manage dashboards** screen) click **Delete dashboard** then confirm.

## Bulk delete dashboards

new In the *Manage Dashboards* page, you can sort your dashboards by creation date, last updated date, or by owner. You can then select one or more dashboards and delete them in a single action. This helps you quickly manage multiple dashboards and keep your data up to date.

![Dashboard Hub Manage Dashboards page showing Bulk Delete](/cms_trial/assets/cb4423f2-fd1d-4182-8395-832056447c56.png)

## Export your dashboard

There are several use cases that require a fixed snapshot of a dashboard, either because you need to create a report in a given date and live information should be frozen in time, or because you need an image to use it in a different product or service, or embed it in a Notion page (remember that we have a Confluence version too).

No matter the reason, to export the whole dashboard to a PNG file, select the **Export dashboard option** in the top right **…** action menu, and voila! Your dashboard is now a snapshot in the form of an image.

Remember that you can also export individual gadgets to images, see [Export gadget data to CSV, XLSX and PNG](/cms_trial/space/RDD/146310658/Export+gadget+data+to+CSV%2C+XLSX+and+PNG/).

## Slideshow mode

See [How to manage dashboards](/cms_trial/space/RDD/146309328/How+to+manage+dashboards/) and [How to set up a slideshow](/cms_trial/space/RDD/146309888/How+to+set+up+a+slideshow/).

## Dark mode

To switch to **Dark mode**, turn on the toggle in the top navigation bar. By default, the wallboard mode has it enabled. This is to facilitate and increase attention in offices, hallways, or big rooms.

Dark mode in shared links:

- If the user has the browser in dark mode, the dark mode is activated automatically.
- Force dark mode by adding the following parameter to the shared link `darkMode=true`.

For example, `https://NICE_URL/dashboard?boardToken=VTJ…&darkMode=true`.

Thanks to the use of a **darker color pallette**, it reduces the emmitted screen luminance, what **reduces the impact on the eyesight**. It also is **soothing to the eyes**, and **improves the visual ergonomics** due to the better contrast ratios.

## Share your dashboard

Did you know that you can share your dashboards with external customers, even without having access to your Jira instance? And in a secure way, thanks to our public link sharing mechanism.

The wallboard mode is the default mode when you share publicly a dashboard. To create a public link:

1. Click the **Share** button.
2. Enable the **Public Link** toggle and copy the URL.
3. Use this link to display your information radiator. Remember that anyone with that link can see the dashboard content.

## Wallboard mode

This is the mode that users see when accessing a dashboard using a public link. See [Learn about Access Restrictions](/cms_trial/space/RDD/146310576/Share+a+dashboard+with+a+public+link/) to learn how to publicly share a dashboard with users outside your organization.

The main differences with the normal dashboard view are:

- Dark mode is switched on by default, although you can switch it off.
- There’s no top Jira menu bar, more space for your dashboard.
- There are no options to edit the dashboard or the slide, but you can still control the slideshow to pause/play or move to the next/previous slide.
- You can view the dashboard in full screen.

See [How to set up a wallboard](/cms_trial/space/RDD/146310022/How+to+set+up+a+wallboard/).