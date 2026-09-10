# Why does date-based data differ between Dashboard Hub and Jira?

![Dashboard Hub date filter comparison showing timezone differences between Jira and gadget results](/cms_trial/assets/292b4b86-df83-4f8b-86b7-86d63f882a18.png)

Sometimes, when we try to filter data based on a date range, we receive different results when we apply a filter or JQL query directly in Jira or when we apply the same filter or JQL query in a Dashboard Hub gadget.

This is related to your profile's timezone configuration, which can ultimately be affected by two different configuration parameters: timezone configuration and timezone visibility.

## Timezone configuration and timezone visibility in Jira

Navigate to your Atlassian account configuration using this [link](https://id.atlassian.com/manage-profile/profile-and-visibility) and click on the “Account preferences” option at the top of the page. Check your timezone settings. If you haven’t configured it, it’s probably set to the system’s timezone of your instance.

![Dashboard Hub Atlassian account preferences page with timezone settings](/cms_trial/assets/275b8333-29d9-48db-8714-66cf689e96c6.png)

The other parameter that you should take into account is your timezone visibility. To check that configuration option, click on the “Profile and visibility” option also at the top of the same page and scroll down until you find the “Local time” option.

![Dashboard Hub Profile and visibility page with Local time settings](/cms_trial/assets/4bd9432f-e3f6-4bb4-8e5b-3d1b311c0530.png)

You have different options to set the visibility for this value.

## Why can timezone configuration affect the data in my dashboards?

In every information system, date and time data are stored using a reference time zone, usually the UTC time zone. When we need to show a date to a user, we convert it to the user’s time zone.

For example, if you are located in Arizona, USA, your timezone will be 7 hours behind UTC time.

If you modify a Jira issue to set a date value to the 31st of December 2023 at 19:00 hours using your Arizona timezone, the value stored will be the 1st of January 2024 at 2:00 a.m.

If you filter your data taking into account date ranges, you’ll see that range limits differ between different time zones. In the previous example, the same issue could appear in different years depending on the time zone applied.

![Dashboard Hub video showing how timezone changes affect filter results](/cms_trial/assets/78d6b611-ea23-41d7-89ed-d925ea9bec4e.mp4)

## Ways to retrieve data from Dashboard Hub

![Dashboard Hub video showing how local time visibility affects data](/cms_trial/assets/739c451f-ff79-4972-b8b2-bb8a98d348fa.mp4)

In Dashboard Hub, we have different means to access the data from different instances. This time zone discrepancy can affect some of these means in different ways.

Our connector-based data sources rely on a Jira instance’s default timezone when the user’s setup includes visibility restrictions for its local time visibility.

In the previous image, we show the result of the exact same filter. The API token-based data source applies the user’s timezone preferences, while the connector-based data source can only access the data based on the source instance’s time zone configuration.

Depending on the data format that you are interested in, you can switch between different types of data sources or review your timezone settings.