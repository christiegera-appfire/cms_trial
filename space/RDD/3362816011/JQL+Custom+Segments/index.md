# JQL Custom Segments

## Overview

Dashboard Hub's **JQL Custom Segments** gadget lets you compare named subsets of Jira data on a single chart. Start with a base JQL query or saved filter that defines your set of work items, then add up to 10 color-coded segments that narrow it down. Each segment is defined by a JQL query or a saved Jira filter. The gadget renders all segments as separate series on one chart, so you can compare them at a glance.

![Example of the JQL Custom Segments gadget rendered as a pie chart in Dashboard Hub.](/cms_trial/assets/cd4c8713-4fa8-4a10-983c-f51f173bb28e.png)

The gadget offers similar functionality and view types to the Jira Custom Charts gadget, with the added flexibility of using JQL for variables instead of selecting a Jira field. With the JQL Custom Segments gadget, you define each group with its own JQL query. If you’ve ever needed multiple gadgets to compare different views of the same data, JQL Custom Segments lets you do it in one.

## Example use cases

Use this gadget to answer questions that require comparing subsets of the same data, such as:

- **Team comparison**: Compare bug counts by priority across teams. Base JQL: `type = Bug`. Segments: `team = "Alpha"`, `team = "Beta"`, `team = "Gamma"`.
- **Component breakdown**: Visualize work-in-progress across components. Base JQL: `status = "In Progress"`. Segments: one per component.
- **Squad trends over time**: Track resolution trends by squad using a multi-line chart. Base JQL defines the project and time window; segments narrow it by squad.
- **Benchmark your work**: See how your work compares to the rest of the team. Create a segment for `assignee = currentUser()` and let the [*Other*](/cms_trial/space/RDD/3362816011/JQL+Custom+Segments/) [segment](/cms_trial/space/RDD/3362816011/JQL+Custom+Segments/) provide the contrast.
- **SLA tiers**: Compare issue volumes across SLA tiers using a stacked bar chart. Base JQL: `project = SUPPORT`. Segments: one per SLA tier filter.
- **Total vs. subset**: Show a Total baseline alongside specific segments. One segment with an empty JQL field represents the entire base query.

## Overview video

Watch our overview video to learn more, or get started following the steps below.

Click to view transcript

Meet JQL custom segments. A gadget in dashboard hub for comparing subsets of Jira data. Reporting on your data for different stakeholders can often mean setting up several gadgets. But when you want to compare different portions of the same data, custom segments puts them all in one chart. You create data subsets using JQL variables instead of selecting a Jira field. Start with a base query. This is the data your segments will narrow down. Then add your segments. Give each one a name and its own JQL, or you can use a saved filter. You can add up to ten segments, and the preview updates as you go.

Next, select how to show the data. There are eight chart types to choose from. Just like our most popular gadget, Jira custom charts. Use a bar chart to compare segments side by side. A line chart to track them over time, or a pie chart for proportions. Whichever you pick, your segments stay the same.

Customization options let customization options let you change the order and Customization options let you change the order and color of the segments, show statistics in the gadget, such as total work items, or even hide segments in the rendered dashboard.

By default, each segment shows a count of work items. But you can switch the aggregation to sum, average, or mean. And point it to any numeric field. So in instead of how many work items are in each segment, you could compare the average story points or total time logged. This uses the same segments but answers a different question.

Segments don't just split things. They can also give you context. Add a segment called all and leave the JQL blank. This represents your entire base query. Now every other segment has something to measure against. Is security work ten percent of everything in flight or forty percent? You'll see it right away. You can also use the all segment for personal benchmarking. Add an All segment alongside a Me segment using assignee equals current user. Compare your story points to the team average, or if you're running a service desk, chart by priority, and see your ticket load against the rest of the team.

You'll also notice a label called other in your charts. It automatically groups every work item that your segments missed. This is your built in coverage check. You can see whether your categories cover everything, or if there's a gap. When your segments cover everything, it disappears. JQL custom segments turns the questions you already asked in Jira into one clear comparison.

Check out our documentation and examples to learn more about simplifying your reporting with Dashboard Hub.

## How to configure the gadget

### Add the gadget

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add Gadgets* page to find the required gadget.

   ![The JQL Custom Segments gadget shown in the Add Gadgets page.](/cms_trial/assets/ba6972bc-d0ae-4cea-b75d-699e0e01cc4c.png)
3. Click **Add** on the **JQL Custom Segments** gadget. The configuration page displays.
4. **Name** (*optional*): Edit the gadget name to make it meaningful to your team.
5. **Datasource**: Select a Jira datasource.
6. **JQL query or saved filter**: Enter a JQL query or select a saved filter to define the base set of work items.

### Add segments

Below the base query settings, the segments section lets you define up to 10 named subsets of your data. The default segment is All. You can keep this segment with an empty query field to show the base set of issues in your report. Click **Add segment** to add a new row.

Each segment requires:

- **Label**: Provide a name for the segment, for example, `Unresolved bugs`. This appears in the chart legend. Labels must be unique across segments.
- **JQL query or saved filter**: Enter a query, for example, `type=bug AND resolution=Unresolved`, or click **Filter** to select a saved filter from a list of available filters for your datasource. The query serves as an `AND` clause for the base query.

  ![Define custom segments options in Dashboard Hub.](/cms_trial/assets/e2ac5a8d-10e3-43b7-8ad4-e4a88166dd32.png)

See [Customizations](/cms_trial/space/RDD/3362816011/JQL+Custom+Segments/) to learn how to reorder or change the color of a segment.

### **The Other segment**

The gadget automatically creates an **Other** segment for any work items in the base query that are not matched by any named segment, so you can spot what you aren’t tracking. This ensures 100% of the data is represented in the chart. The Other segment appears only when there are unclaimed work items. It is hidden when all work items are covered by named segments; therefore, if you use the default All segment, the Other segment isn’t available.

### Select a view type

The gadget offers eight view types to visualize your data. See [Jira Custom Charts](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) for examples. This gadget is designed for visual comparison, where each segment becomes a series on a chart. For listing or cross-tabulating work items as tables or pivot tables, use the **Jira Custom Charts** gadget.

| **View type** | **Best for** |
| --- | --- |
| Bar chart | Comparing segment totals side by side |
| Grouped bar chart | Comparing segments across a second dimension for example, priority |
| Stacked bar chart | Showing segment contributions to a total |
| Line chart | Visualizing trends over time or categories |
| Multi-line chart | Comparing trends across segments over time |
| Area chart | Emphasising the magnitude of values over time |
| Stacked area chart | Showing cumulative trends with segment breakdown |
| Pie chart | Showing segment proportions of a total |

## Customizations

Extra settings let you customize the order and colors of the chart segments. To modify the chart’s appearance, click **Charts extra settings** in the gadget configuration page.

![The Charts extra settings options in Dashboard Hub gadgets.](/cms_trial/assets/607da26b-49e8-467a-b5dc-d3d8a09bee60.png)

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or diverts attention. Click the **Show**/**Hide** icon to switch the corresponding segment to hidden (or shown) in the chart.

### Reorder segments

Rearranging the positions of existing segments or values reinforces how we convey information in our charts. Drag any segment or value using the handle on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

### Custom colors

Within our organizations and teams, it’s common to associate concepts with specific colors, making it easier and quicker to communicate ideas and information.

Click a color icon to open the color picker. You can define a color by hexadecimal code, RGB, or select from the predefined 24-color palette. These were selected for optimal contrast and tone.

## Tips for getting the best results

- **Start broad**: Write a base query that captures the full data set you care about, then use segments to narrow it down. Segments narrow the base query; they can't return work items outside it.
- **Use a baseline**: Use the default **All** segment with an empty JQL field to show the full base set alongside your narrower segments. This helps contextualize each segment's size relative to the whole.
- **Choose the right chart type**: Use bar or grouped bar for comparisons, multi-line or stacked area for trends over time, pie for proportional breakdowns. Stacked bar works well when you want to see both individual segments and the total.

## Integrations

- Jira Software (Cloud)
- Jira Service Management (Cloud)

## Dashboards

This gadget isn't included in any dashboard templates.