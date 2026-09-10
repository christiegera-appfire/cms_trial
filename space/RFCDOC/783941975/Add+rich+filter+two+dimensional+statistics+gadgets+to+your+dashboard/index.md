# Add rich filter two dimensional statistics gadgets to your dashboard

By the end of this tutorial, you will be able to configure and use Rich Filter Two-Dimensional Statistics gadgets and control the displayed data with a Rich Filter Controller gadget.

![Rich Filter Two-Dimensional Statistics gadgets.png](/cms_trial/assets/ab70c4ec-0979-4b9b-84c4-9d517eea65bb.png)

For this tutorial, you need to have already created:

1. a *rich filter*
2. a dashboard with one *Rich Filter Controller* gadget based on your *rich filter*.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941968/Add+rich+filter+statistics+gadgets+to+your+dashboard/).

## Add Rich Filter Two Dimensional Statistics gadgets

1. Open the dashboard based on your rich filter or [build a new one](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/). Add one *Rich Filter Two Dimensional Statistics*gadget to the dashboard by clicking the *Add gadget* button at the top right of the screen.

   ![contentId-783941975](/cms_trial/assets/6586e405-2024-4664-89a7-aabc9ad28bc9.png)
2. To add one *Rich Filter Two-Dimensional Statistics* gadget, click **Add**.

   ![Rich Filter Two-Dimensional Statistics.png](/cms_trial/assets/767d625a-2a89-4a73-bb51-4646d45a516e.png)

   The gadget will be added to the left column of the dashboard. If you want the same layout as in our example, you can move it to the top of the right column (sidebar) using drag and drop.
3. In the configuration form of the gadget, select your *rich filter*.

   ![contentId-783941975](/cms_trial/assets/788aef52-4b74-458b-9876-d7e006238ca9.png)
4. Select Status as the Statistic type for the Horizontal breakdown, Priority as the Statistic type for the Vertical breakdown, and Story Points as the Value, then click **Submit**.

   ![Select Status as the Statistic type.png](/cms_trial/assets/07af23d1-962e-4ec0-98ac-19a9e85a15f3.png)

   The gadget displays the sum of the *Story Points* broken down by *Status* and *Priority*.

   ![contentId-783941975](/cms_trial/assets/67356ad7-6fd8-4d5d-88ac-75930029887c.png)
5. You can sort the data by the values of any column or row (including the totals) by clicking on the icon at the right of the header (clicking again on the same icon will the sort order). You can return to the initial order by clicking on the sort icon (▢ ) at the right of the top left cell of the table (the *Priority* header in our case) and selecting **Reset sort order**.

   ![Sort by Open.png](/cms_trial/assets/92f0a77f-f763-4ae8-8872-9d5cc28535dc.png)
6. As always, if you activate *quick filters in the Rich Filter Controller gadget (any combination of static, dynamic, and smart filters), the other gadgets in the dashboard, which are based on the same rich filter, will be updated to use only the issues that satisfy the active quick filters*. In the example below, we have activated the clause *Top Priority* of the smart filter *Warnings* (this clause has the JQL condition `priority in (1, 2) AND status = Open`).

   ![top_priority.png](/cms_trial/assets/efb2cdac-9a3d-4b74-93f4-5d1e7f6c5151.png)

## Use quick charts in Rich Filter Two Dimensional Statistics gadgets

In addition to the default *table view*, the *Rich Filter Two-Dimensional Statistics* gadget provides a *chart view*. We call these charts *quick charts* because they are directly available on gadgets without requiring any specific configuration. Let's see how they work in our gadgets.

1. Click the **Chart** (▢) icon at the bottom right of the gadget.

   ![switch tocharts view.png](/cms_trial/assets/bf4d37d7-cf52-46dd-b945-5458b5124c2b.png)
2. A *clustered bar chart* of *Story Points* by *Status* and *Priority* is displayed. The chart type selector at the bottom of the gadget lets you switch to a *stacked bar chart*.

   ![clustered bar chart of Story Points.png](/cms_trial/assets/b2807ec3-669d-4ea4-bc90-94dc64a5446a.png)
3. You can click the **swap** icon (<>) to swap the two breakdowns.

   ![Click to swap.png](/cms_trial/assets/d8327957-1be4-4e4e-a70d-dacba5a8c608.png)
4. The *Story Points* are broken down first by *Priority* and then by *Status*. You can hover over the bars or slices to see a detailed tooltip.

   ![stacked bar chart.png](/cms_trial/assets/f5b4e8ef-4038-4f56-9ba3-769512506a27.png)
5. You can switch back to the table view at any moment by clicking on the table icon at the bottom right of the gadget.

In addition to statistics based on issue fields, the *Rich Filter Two-Dimensional Statistics* gadget can also display statistics based on *smart filters*. In the previous tutorial, we've seen an example of statistics based on a smart filter.

### See also

[Rich Filter Two-Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/)

[Add Rich Filter Flexi Charts gadgets to your dashboard](/cms_trial/space/RFCDOC/783941981/Add+rich+filter+flexi+charts+gadgets+to+your+dashboard/)