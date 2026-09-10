# Add rich filter statistics gadgets to your dashboard

By the end of this tutorial, you will be able to configure and use Rich Filter Statistics gadgets and control the displayed data with a Rich Filter Controller gadget.

![statistics dashboard.png](/cms_trial/assets/de4eaea8-48c4-49d5-978f-80de8227adf8.png)

For this tutorial, you need to have already created:

- a rich filter with at least one smart filter
- a dashboard with one Rich Filter Controller gadget and at least one Rich Filter Filter Results gadget based on your rich filter.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941961/Add+smart+filters+and+smart+columns+to+your+dashboard/).

## Add Rich Filter Statistics gadgets

1. Open the dashboard based on your rich filter, or [build a new one](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/). Add two **Rich Filter Statistics** gadgets to the dashboard.   
   We have used the **Right sidebar** layout and added gadgets directly to the empty column on the right by clicking the **add a new gadget** link in the middle of the column.

   ![Change layout sidebar.png](/cms_trial/assets/3a61bb7b-048e-4ec2-ae04-74239460d04e.png)

In the *Add a Gadget* dialog, simply type “rich” in the **Search** field to easily find the gadgets provided by the Rich Filters for Jira Dashboards app.

1. Click the **Add** button twice to add two Rich Filter Statistics gadgets.

   ![Add Statistics gadget.png](/cms_trial/assets/ef112d0a-44c1-4c19-be53-1baeae61236e.png)
2. Select your rich filter in the configuration form of the first Rich Filter Statistics gadget.

   ![contentId-783941968](/cms_trial/assets/07539ddd-4605-4cf8-b110-3766757f13a0.png)
3. Let's suppose we need to exclude canceled issues from the statistics. The gadget should work only with non-canceled issues, which in our case means issues with no resolution or a Fixed or Done resolution. To achieve this, type the JQL `resolution in (EMPTY, Fixed, Done)` in the **Working Query** field.

   ![contentId-783941968](/cms_trial/assets/5d7d38ad-1462-4ea9-b6e9-f10b0431ccd8.png)
4. Select **Assignee** as **Statistic type**, and click **Submit**.

   ![contentId-783941968](/cms_trial/assets/b3de3122-4559-41a8-9b0b-9812a3e48792.png)
5. Rename the gadget as *Not Cancelled - Statistics by Assignee*. The gadget displays the Issue Count and the sum of the Story Points for each assignee, excluding the canceled issues.

   ![2026-02-19_09-10-03.png](/cms_trial/assets/007bb9d4-0222-4385-8d67-c588457d39b9.png)
6. You can click the header of any column to sort the rows by the values in that column (clicking the same header again reverses the sort order).

   ![2026-02-19_09-10-37.png](/cms_trial/assets/f9972d2e-50ad-4bf4-880e-c5e9ded3a3c0.png)
7. Select your rich filter in the configuration form of the second Rich Filter Statistics gadget. In the **Statistic type** options, you'll notice that the smart filters configured in the selected rich filter are available. Select the **Warnings** smart filter as *Statistic type*.

   ![contentId-783941968](/cms_trial/assets/d76fc427-dcd4-4496-9048-0f4a877a714f.png)
8. Add **Issue Count** to the list of **Values**, then click **Submit**.   
   The gadget displays the Issue Count for each clause of the smart filter.

   ![2026-02-19_10-05-38.png](/cms_trial/assets/39faa3b9-128b-44c9-8fdd-6320c9b8ca09.png)

By combining Rich Filter Statistics gadgets with smart filters you can cover a very wide range of complex and specific statistics use cases.

1. If you activate quick filters in the Rich Filter Controller gadget (any combination of static, dynamic, and smart filters), the other gadgets on the dashboard that use the same rich filter update to show only issues that satisfy the active quick filters. If a gadget has a JQL filtering condition defined in the Working Query, this condition is also applied to that gadget.

   ![2026-02-19_10-07-37.png](/cms_trial/assets/423dcccf-64a4-4cba-96a1-98235f3c26bb.png)

## Use quick charts in Rich Filter Statistics gadgets

In addition to the default table view, the Rich Filter Statistics gadget provides a **quick** **chart view**. We call these charts quick charts because they are directly available on gadgets without requiring any specific configuration. Let's see how they work in your dashboard's first Rich Filter Statistics gadget.

Click the **Chart** (▢) icon at the bottom right of the gadget.

![2026-02-19_10-08-35.png](/cms_trial/assets/ed5455a4-7a06-4a52-9932-248ee014288f.png)

1. A donut chart of Issue Count by Assignee is displayed. The chart type selector at the bottom of the gadget lets you switch to any of the available chart types. Let's switch to the **Bar chart**.

   ![2026-02-19_10-09-56.png](/cms_trial/assets/d3470fbc-735e-4b31-9f55-ec0dbbbbed2a.png)
2. A second selector at the bottom of the gadget lets you switch between its values (columns). Let's switch to **Story Points**.

   ![2026-02-19_10-10-44.png](/cms_trial/assets/b0c1e52a-7912-4a70-bc69-b517ade32eaa.png)
3. You can hold the pointer over the bars to see a tooltip with details.

   ![2026-02-19_10-29-44.png](/cms_trial/assets/ddf31b5c-bda8-4038-bef5-edce985b22a4.png)
4. Enable **Show values** in the **Three-dot menu** (▢) to display numeric values directly on the chart when space allows.

   ![2026-02-19_10-37-35.png](/cms_trial/assets/42392312-c701-4d8e-aa87-e66207c43bf6.png)
5. You can switch back to the table view at any moment by clicking the **Table** (▢) icon at the bottom right of the gadget.

   ![2026-02-19_10-39-43.png](/cms_trial/assets/b4c51d85-26ea-4a31-9f70-a309cc9ab566.png)

   The slices or bars are displayed in the same order as the table. To change the order, switch to the table view, change the sort order by clicking on the column header, and then switch back to the chart view.

### See also

[Configuring Smart Filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/)

[Rich Filter Statistics gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/)

[Add Rich Filter Two-Dimensional Statistics gadgets to your dashboard](/cms_trial/space/RFCDOC/783941975/Add+rich+filter+two+dimensional+statistics+gadgets+to+your+dashboard/).