# Time period and aggregation

## Time period and aggregation (old navigation)

Click to expand the guide

## Adjust the timeline view

You can adjust your timeline view by different time periods and aggregations. If the time period exceeds your screen resolution, the horizontal scroll bar will let you scroll your resource data (capacity, workload, etc.) along the timeline.

![Available time periods and aggergations in the new Resources module.](/cms_trial/assets/09c2f1a8-5234-4bd4-b8d8-f2688b5b08cc.png)

### Select the time period

Use the [letter] button above the timeline to select the respective time period:

- Week [W]
- Month [M]
- Quarter [Q]
- Half year [H]
- Year [Y]

### Aggregate the time period

Aggregate the selected time period by clicking one of the available options from the dropdown menu.

- Daily
- Weekly
- Monthly
- Quarterly
- Yearly
- By timeboxes (for example, by Sprints) - Before you set aggregation by timeboxes, select the **Timeboxes** in theView menu.

Tasks with short durations (like 1 day) cannot be stretched on a timeline set to a Year or Half Year time period view (but they can be moved).

### Set the timeline’s beginning date

To set the timeline's beginning date, click the start date and select a date from the date picker. You can also click the **Today** button on the date picker to set today’s date as the beginning of the timeline.

![Setting the beginning date of the timeline.](/cms_trial/assets/8d0e93f8-7222-4cbe-8734-027090e8de6d.png)

## Navigate the timeline view

### Navigation buttons

When you set the time period to one year, half a year, a quarter, and so on, the navigation arrows will help you quickly move along the timeline throughout the selected period. The actions apply to time periods and are affected by the selected aggregation.

The **Today** button always adjusts the timeline to show the current date, and the **Previous** and **Next** buttons (**<<** and **>>**) always adjust the timeline by the time period selected. Both actions are independent of the aggregation options.

|  |  |  |
| --- | --- | --- |
| **Time period** | **Aggregation** | **Action** |
|  | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 |
| Year | Yearly | Previous year | Previous quarter | Today | Next quarter | Next year |
| Quarterly | Previous year | Previous quarter | Today | Next quarter | Next year |
| Monthly | Previous year | Previous month | Today | Next month | Next year |
| Weekly | Previous year | Previous month | Today | Next month | Next year |
| by timeboxes | Previous year | Previous timebox | Today | Next timebox | Next year |
| Half year | Quarterly | Previous half year | Previous month | Today | Next month | Next half year |
| Monthly | Previous half year | Previous month | Today | Next month | Next half year |
| Weekly | Previous half year | Previous week | Today | Previous week | Next half year |
| by timeboxes | Previous half year | Previous timebox | Today | Next timebox | Next half year |
| Quarter | Quarterly | Previous quarter | Previous month | Today | Next month | Next quarter |
| Monthly | Previous quarter | Previous month | Today | Next month | Next quarter |
| Weekly | Previous quarter | Previous week | Today | Next week | Next quarter |
| Daily | Previous quarter | Previous week | Today | Next week | Next quarter |
| by timeboxes | Previous quarter | Previous timebox | Today | Next timebox | Next quarter |
| Month | Monthly | Previous month | Previous week | Today | Next week | Next month |
| Weekly | Previous month | Previous week | Today | Next week | Next month |
| Daily | Previous month | Previous day | Today | Next day | Next month |
| by timeboxes | Previous month | Previous timebox | Today | Next timebox | Next month |
| Week | Weekly | Previous week | Previous day | Today | Next day | Next week |
| Daily | Previous week | Previous day | Today | Next day | Next week |
| by timeboxes | Previous week | Previous day | Today | Next day | Next week |

### Move to the closest timebox

Right-click the **No timeboxes in this period** tab to see the **Move to closest timebox** button.

![Move to the closest timebox button in the Resources module.](/cms_trial/assets/383da350-5836-45ed-a5c1-3e91c59ddad7.png)

### Today’s date marker

Additionally, when you click the **Today** button, a marker on your timeline will appear to mark the current day. The marker can activate only if the today’s date is within the time period and aggregation you selected.

![A marker marking the current day on the timeline in the new resources module.](/cms_trial/assets/5d2a4010-7717-47fc-84e3-053b1c7990b9.png)

## About the yearly timeline view

The new timeline view lets you set a one-year period starting from a specific date and aggregate data by quarters and the entire year.

With this extended timeframe displayed on the resources grid, you can analyze annual data for a clear overview of upcoming team tasks, capacity, and workload. You can also leverage it to generate a resource heat map for planned hours in your fiscal year and provide upper management with long-term insights into resource needs.

When you set your timeline to a year, you can perform the same actions as with shorter periods, including:

- use the [Scenario mode](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/297601099),
- switch between the Individuals, Teams, projects, and Skills [swimlanes](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) and group them,
- [export](https://appfire.atlassian.net/wiki/spaces/BTc/pages/3536093283) your yearly view to PDF,
- send a link to your yearly view using the [share view](/cms_trial/space/SPM/1918504353/Share+view/) option.

The **Year** time period is available for all [box scope types](/cms_trial/space/SPM/1918766536/Scope+types/): none-scope, own-scope, and sub-scope boxes.

### Yearly timeline aggregation limitations

You can have your timeline display time period aggregations as granular as individual days or set the time period to show the entire year, for example, a fiscal year.

However, not every aggregation can be selected for every time period. Aggregation options that are not available for the selected time period are grayed out on the dropdown menu.

In the table below, you can see which aggregations you can apply to specific time periods on your timeline.

|  |  |
| --- | --- |
| **Time period** | **Time period aggregation** |
| Daily | Weekly | Monthly | Quarterly | Yearly | Timeboxes |
| Year | No | Yes | Yes | Yes | Yes | Yes |
| Half year | No | Yes | Yes | Yes | No | Yes |
| Quarter | Yes | Yes | Yes | Yes | No | Yes |
| Month | Yes | Yes | Yes | No | No | Yes |
| Week | Yes | Yes | No | No | No | Yes |

## Aggregation limitations

- If box periods overlap, aggregation by timeboxes is not available.
- If there are no timeboxes for a given time period, the "No timeboxes in this period" message appears.

- For the time between defined timeboxes, data is aggregated based on the length of that period; e.g., if the time slot between periods is nine days, data from nine days will be aggregated.
- Aggregation before and after defined time periods are based on the corner time periods, for example, if in the project lasts two years, there were two weeks sprints at the beginning of the project and 1-week sprint at the end of the project, the aggregation will be visualized:

  - as 2 week periods before the project starts
  - as 1 week period after the project ends

## Time period and aggregation (new navigation)

Click to expand the guide

## Adjust the timeline view

You can adjust your timeline view by different time periods and aggregations. If the time period exceeds your screen resolution, the horizontal scroll bar will let you scroll your resource data (capacity, workload, etc.) along the timeline.

![resources-time-aggregation.png](/cms_trial/assets/86ec40b7-8e33-4a25-ad43-4ad4073882f2.png)

### Select the time period

Use the [letter] button above the timeline to select the respective time period:

- Week [W]
- Month [M]
- Quarter [Q]
- Half year [H]
- Year [Y]

### Aggregate the time period

Aggregate the selected time period by clicking one of the available options from the dropdown menu.

- Daily
- Weekly
- Monthly
- Quarterly
- Yearly
- By timeboxes (for example, by Sprints)

Tasks with short durations (like 1 day) cannot be stretched on a timeline set to a Year or Half Year time period view (but they can be moved).

### Set the timeline’s beginning date

To set the timeline's beginning date, click the start date and select a date from the date picker. You can also click the **Today** button on the date picker to set today’s date as the beginning of the timeline.

![resources-start-date.png](/cms_trial/assets/442b4856-f5d2-4fd2-8bc8-e4ee30968e02.png)

## Navigate the timeline view

### Navigation buttons

When you set the time period to one year, half a year, a quarter, and so on, the navigation arrows will help you quickly move along the timeline throughout the selected period. The actions apply to time periods and are affected by the selected aggregation.

The **Today** button always adjusts the timeline to show the current date, and the **Previous** and **Next** buttons (**<<** and **>>**) always adjust the timeline by the time period selected. Both actions are independent of the aggregation options.

|  |  |  |
| --- | --- | --- |
| **Time period** | **Aggregation** | **Action** |
|  | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 | contentId-1918702075 |
| Year | Yearly | Previous year | Previous quarter | Today | Next quarter | Next year |
| Quarterly | Previous year | Previous quarter | Today | Next quarter | Next year |
| Monthly | Previous year | Previous month | Today | Next month | Next year |
| Weekly | Previous year | Previous month | Today | Next month | Next year |
| by timeboxes | Previous year | Previous timebox | Today | Next timebox | Next year |
| Half year | Quarterly | Previous half year | Previous month | Today | Next month | Next half year |
| Monthly | Previous half year | Previous month | Today | Next month | Next half year |
| Weekly | Previous half year | Previous week | Today | Previous week | Next half year |
| by timeboxes | Previous half year | Previous timebox | Today | Next timebox | Next half year |
| Quarter | Quarterly | Previous quarter | Previous month | Today | Next month | Next quarter |
| Monthly | Previous quarter | Previous month | Today | Next month | Next quarter |
| Weekly | Previous quarter | Previous week | Today | Next week | Next quarter |
| Daily | Previous quarter | Previous week | Today | Next week | Next quarter |
| by timeboxes | Previous quarter | Previous timebox | Today | Next timebox | Next quarter |
| Month | Monthly | Previous month | Previous week | Today | Next week | Next month |
| Weekly | Previous month | Previous week | Today | Next week | Next month |
| Daily | Previous month | Previous day | Today | Next day | Next month |
| by timeboxes | Previous month | Previous timebox | Today | Next timebox | Next month |
| Week | Weekly | Previous week | Previous day | Today | Next day | Next week |
| Daily | Previous week | Previous day | Today | Next day | Next week |
| by timeboxes | Previous week | Previous day | Today | Next day | Next week |

### Move to the closest timebox

Right-click the **No timeboxes in this period** tab to see the **Move to closest timebox** button.

![Move to the closest timebox button in the Resources module.](/cms_trial/assets/383da350-5836-45ed-a5c1-3e91c59ddad7.png)

### Today’s date marker

Additionally, when you click the **Today** button, a marker on your timeline will appear to mark the current day. The marker can activate only if the today’s date is within the time period and aggregation you selected.

![resources-today-marker.png](/cms_trial/assets/63758465-28fc-48d6-b6e4-e7dd04af9422.png)

## Yearly timeline view

The new timeline view lets you set a one-year period starting from a specific date and aggregate data by quarters and the entire year.

With this extended timeframe displayed on the resources grid, you can analyze annual data for a clear overview of upcoming team tasks, capacity, and workload. You can also leverage it to generate a resource heat map for planned hours in your fiscal year and provide upper management with long-term insights into resource needs.

When you set your timeline to a year, you can perform the same actions as with shorter periods, including:

- use the [Scenario mode](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/297601099),
- switch between the Individuals, Teams, projects, and Skills [swimlanes](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) and group them,
- [export](https://appfire.atlassian.net/wiki/spaces/BTc/pages/3536093283) your yearly view to PDF,
- send a link to your yearly view using the [share view](/cms_trial/space/SPM/1918504353/Share+view/) option.

The **Year** time period is available for all [box scope types](/cms_trial/space/SPM/1918766536/Scope+types/): none-scope, own-scope, and sub-scope boxes.

### Yearly timeline aggregation limitations

You can have your timeline display time period aggregations as granular as individual days or set the time period to show the entire year, for example, a fiscal year.

However, not every aggregation can be selected for every time period. Aggregation options that are not available for the selected time period are grayed out on the dropdown menu.

In the table below, you can see which aggregations you can apply to specific time periods on your timeline.

|  |  |
| --- | --- |
| **Time period** | **Time period aggregation** |
| Daily | Weekly | Monthly | Quarterly | Yearly | Timeboxes |
| Year | No | Yes | Yes | Yes | Yes | Yes |
| Half year | No | Yes | Yes | Yes | No | Yes |
| Quarter | Yes | Yes | Yes | Yes | No | Yes |
| Month | Yes | Yes | Yes | No | No | Yes |
| Week | Yes | Yes | No | No | No | Yes |

## Aggregation limitations

- If box periods overlap, aggregation by timeboxes is not available.
- If there are no timeboxes for a given time period, the "No timeboxes in this period" message appears.

- For the time between defined timeboxes, data is aggregated based on the length of that period; e.g., if the time slot between periods is nine days, data from nine days will be aggregated.
- Aggregation before and after defined time periods are based on the corner time periods, for example, if in the project lasts two years, there were two weeks sprints at the beginning of the project and 1-week sprint at the end of the project, the aggregation will be visualized:

  - as 2 week periods before the project starts
  - as 1 week period after the project ends