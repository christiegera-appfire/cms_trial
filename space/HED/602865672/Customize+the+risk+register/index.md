# Customize the risk register

The Risk Register *General settings* page lets you customize each risk register by editing its name and owner and choosing which projects and issue types it includes.

![Risk register settings](/cms_trial/assets/11eef2e7-5567-4bb9-bf35-a4f8d1b51ddb.png)

## Access general settings from the Risk Register list

1. In the Jira global menu, click ***Apps*** > ***Risk Management*** to see the list of Risk Registers.
2. Click the [ellipsis icon] menu on the right side of the Risk Register that you want to customize.
3. Click **Register settings**.
4. Click the **General settings** tab.

## Access the general settings from a Risk Register table

1. From a Risk Register, click **Settings**in the top right corner.
2. Click the **General settings** tab.

## Customize your risk register

![General settings tab](/cms_trial/assets/c142487c-cc39-41fe-ab32-5f4eae1141b8.png)

1. In the **General settings** tab, click the Risk Register attribute or field that you want to update and make your desired changes.

   - You can update Name, Owner, Projects, and Issue Types attributes.
2. Click **Save Changes**.

Select issue types that are available in your selected projects in Jira. If you select an issue type that is not added to your Jira project, you will not be able to create a risk in this project for this issue type.

## Map risk metrics to Jira fields

The **Risk register frameworks** tab of Register settings includes a **Metrics** section, where each metric (for example, *Likelihood* and *Consequence*) lists its value names, colors, and numeric values. Starting in version 8.0.0, you can also map a metric to a Jira field, so its value shows up alongside your everyday Jira views instead of staying inside Hedge only.

For each metric, you can either let Hedge create the matching Jira field automatically, or choose an existing Jira field to map it to.