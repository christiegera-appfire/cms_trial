# Configure views

## **About views**

Views allow users to define the columns the Rich Filter Results gadgets display. Each view contains a list of columns based on issue fields, [special columns](/wiki/pages/resumedraft.action?draftId=783941729#ConfiguringViews-section4), [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), or tags based on [static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/) or [smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/). Additionally, a view can also contain a [Gantt chart](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/). The *Rich Filter Results* gadgets can display multiple views of the issue collection returned by the rich filter.

Views enable the *Rich Filter Results* gadgets to display large amounts of information in a clean manner:

- Each view can contain columns that are relevant for a particular purpose – users in different roles might need to see different columns;
- The Rich Filter Results gadgets can display multiple views at once, allowing users to easily switch between them by clicking on tabs located at the top of the gadget;
- For any column, users can customize the column header to be displayed in Rich Filter Results gadgets;
- The computed columns based on *static* and *smart filters* allow users to display computed tags (labels) and to add color coding;
- Users can customize the display format of the columns based on numeric fields (number of decimals, thousand separators) and on time-tracking fields (Jira's time display format, days, hours, minutes, or seconds);
- Views can optionally show column totals based on numeric and time-tracking fields or custom values. The formula used for aggregation can be selected for each column among four options: sum, average, minimum, or maximum value;
- Views can optionally display a [Gantt chart](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/).

![results views.png](/cms_trial/assets/c67ac8a9-ec82-4339-bd79-ee9b6ce93bb5.png)

## **Views key attributes**

You can add new views and see their configuration in the **Views** section of your rich filter.

![views options](/cms_trial/assets/6f112880-2494-45d5-a7cf-de32e02db724.png)

The key attributes of a view are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each view has a **name** used to identify and display it. The name is mandatory and must be unique among the views within the rich filter. |
| **Show Gantt chart** | If enabled, the view will have a Gantt chart as its last column, in addition to the columns selected in the *Columns* list. |
| **Show totals row** | If enabled, the view will have an extra row at the bottom, showing totals for columns based on numeric and time-tracking fields or custom values.  For numeric and time-tracking fields, the total formula (sum, average, min, or max) can be configured for each column individually. For custom values, the total formula is the one selected for the [custom value configuration](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/). |
| **One-line rows by default** | The view will be displayed with one line per row by default (compact layout) if enabled. Users can still [switch between the two layouts](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) in the Rich Filter Results gadgets.  Views with the Gantt chart enabled can only be displayed with one line per row. |
| **Columns** | Each view contains a list of columns that are displayed when the view is used in *Rich Filter Results* gadgets. The columns can be:   - Issue fields - [Special columns](/wiki/pages/resumedraft.action?draftId=783941729#ConfiguringViews-section4) - [Custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) - Tags based on [static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/) or [smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) |

## Add and edit views **and columns**

The **Views** section of your rich filter lets you perform the following operations:

### **1. Add a new view**

1. Click **Create view** at the top-right of the page.

![create view option](/cms_trial/assets/2fd771f7-90b5-4545-8b4a-ee2d4f1ac7ae.png)

1. Type a name, check the checkboxes you need for the view, and click the **Create**button.

![Create a view](/cms_trial/assets/abbe59a3-33cb-4811-b1fd-906572f60040.png)

You can add up to 100 views in each rich filter.

### **2. Browse the views list**

Depending on your rights, you can click any view name to view or edit its properties.

![contentId-783941729](/cms_trial/assets/f9c4f8ad-0e9e-46ba-b0ed-2869c439be6e.png)

### **3. Reorder the views**

In the views list, hold the pointer over the view's **Grid** (▢) icon, then drag up or down to the new position.

![Reorder the views](/cms_trial/assets/306dd427-d896-46ef-b495-780b189e47a4.png)

### **4. Duplicate a view**

1. Click **Duplicate** under the **Menu** (▢) next to your view name.

![duplicate view.png](/cms_trial/assets/fbe19aa1-ce9b-4c52-9f86-4191a5d3e131.png)

1. Type the name of the new view and click **Duplicate**. A new view with the same columns is created.

![duplicate summary](/cms_trial/assets/3c22afda-e7f5-44a8-9b4a-205bb2efadb4.png)

### 5. **Delete a view**

Click the **Delete** option under the **Menu** (▢) next to the view’s name.

![delete view.png](/cms_trial/assets/1840b8e0-f5cb-406e-93d2-bb9704cc5668.png)

## Set up a view

When you create a new view or click an existing one, a new screen focused on the selected view is displayed. This screen lets you perform the following operations on the selected view:

### **1. Edit a view name**

Click the **Edit** icon located next to the view’s name.

![change view name.png](/cms_trial/assets/788ceeb0-0fdc-42cd-a7f6-bfa0cd3ae3cf.png)![edit view name.png](/cms_trial/assets/9a7a5f29-2c05-4258-a275-8c842ef268e8.png)

### 2. **Enable totals and one-line rows by default**

Toggle the corresponding switch by clicking it.

![contentId-783941729](/cms_trial/assets/07074d89-0de1-4855-b142-6376eeef81d8.png)

### 3. **Enable Gantt chart**

Toggle the **Show Gantt chart** switch to turn the Gantt chart on or off.

![image-20250729-053005.png](/cms_trial/assets/dc898687-363e-4c11-b276-38a9c8b8ff8c.png)

A configuration dialog is displayed when the Gantt chart is first enabled in a view. To configure the Gantt chart, follow these steps:

- Select the issue fields to be used as start and end dates. In the example below, the chart is based on the issue fields *Start date* and *Target end*. This means that the bars start on the issues' *Start date* and finish on their *Target end*.
- Optionally, configure the *dependencies* to be shown in the chart. The dependencies represent the order in which issues need to be done. They are based on the [issue link types](https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-linking/) configured in your Jira instance. To add a new dependency, select an issue link type from the *Add a link type* dropdown – the dependency will be added to the list. In the example below, we have configured a dependency based on the issue link type *Blocks*, so the dependency will use the [blocks / is blocked by links](https://support.atlassian.com/jira-service-management-cloud/docs/link-subtasks-issues-and-pages-from-the-new-issue-view/#Link-issues) between the issues. You can reverse the precedence order by clicking on the *swap* link at the right of the dependency line. When issue A *precedes* issue B (i.e., issue A must be done before issue B), in the chart, a link to issue A will be displayed to the left of the bar of issue B, and a link to issue B will be displayed to the right of the bar of issue A. The dependencies in the Gantt chart configuration are optional and purely informative – they do not affect any calculation.
- Specify how the bars should be colored. You can select either *Status Category* (the default option – for predefined bar colors)or one of the [smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) defined in the rich filter (for custom bar colors)*.* With the *Status Category* option, the bars will have the color of the issue's status, as defined in Jira. If you select a smart filter, the bars will have the color of the first clause of the selected smart filter that matches the issue (first match logic); if none of the clauses matches the issue, a default gray color will be used for that issue. This means that, by using a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/), you can specify the colors of the bars depending on the priority of the issues or any other filtering criteria that can be expressed in JQL.

![contentId-783941729](/cms_trial/assets/2efead83-2a7b-41f8-85bf-42585f46b2b3.png)

For details about using Gantt charts in the *Rich Filter Results* gadget, look at [Use Gantt charts](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/).

### 4. **Edit the Gantt chart**

If the Gantt chart is already enabled, click the **Edit** (▢) icon to view or edit the configuration of the Gantt chart – the configuration dialog described above will be displayed.

![contentId-783941729](/cms_trial/assets/464018bf-4ddd-4ef6-ba60-6eefde4dfdb5.png)

### 5. **Add columns to a view**

Click the **Add a column...**field to display all the available options: issue fields, special columns, static filters, smart filters, and custom values. Scroll through the list, use the section scroll buttons to quickly jump between sections, or use the search box to quickly find the columns you're looking for.

![contentId-783941729](/cms_trial/assets/093382de-cf7e-48d7-a3c3-3844f01bfb6c.png)

The views with no columns are not displayed by *Rich Filter Results* gadgets. You can add up to 30 columns in each view.

### 6. **Edit columns**

1. Click the **Edit** (▢) icon next to the column.

![2025-08-01_12-35-49.png](/cms_trial/assets/5f527a74-e238-4af9-a5a1-e3f608a9ee20.png)

1. Depending on the type of column, the following options are available:

- **Column heading** – for any column, you can customize the column header to be displayed in Rich Filter Results gadgets:

  ![contentId-783941729](/cms_trial/assets/52019f72-f4f7-4455-a33c-1fea40071107.png)
- **Display as** – You can also customize the way the tags are displayed for smart columns. (This also depends on the configuration of the smart filter. For example, a smart filter with only the color tag type cannot display labels.)  
  If the smart filter tags are shown as labels, you can also use the **Equal size lozenges** checkbox, which forces all tags to have the same width. This can make a smart column look nicer.

  ![contentId-783941729](/cms_trial/assets/ac27ebc1-6c25-442b-9be1-13ac3d321fb2.png)
- **Total formula** – for numeric and time-tracking fields, if the view is configured to show the totals row, you can select the formula to be used for computing totals. The possible options are sum, average, minimum, maximum, and none if you want to hide the total for the field.

  ![contentId-783941729](/cms_trial/assets/ed6a7c76-946e-461b-b7b3-215572ed98f2.png)
- **Value formatting** – for columns based on numeric and time-tracking fields, you can choose the format of the values (including the total if enabled) among the following options:

  - For numeric fields:

    - Thousand separators on/off
    - Number of decimals: none or maximum 3, 2 or 1 or exactly 3, 2 or 1
  - For time-tracking fields, you can select the **Time display format**:

    - **Jira's time display format** – uses the time format as configured in Jira by the administrator of the instance:
    - Days, hours, minutes, or seconds

**What's the difference between maximum 2 and exactly 2 decimals?**

If you select the *exactly 2* option, the value will always be displayed with 2 decimals. This is achieved by rounding to 2 decimals if more than 2 are available (e.g., 23.4567 → 23.46) or padding with zeros up to a total of 2 decimals if fewer than 2 are available (e.g., 23.4 → 23.40).

Selecting the maximum 2 option will display the value with 0, 1, or 2 decimals. This is achieved by rounding to 2 decimals if more than 2 are available (e.g., 23.4567 → 23.46) and leaving the value as it is if 2 or fewer decimals are available (e.g., 23.4 → 23.4).

### 7. **Reorder columns**

Hold the pointer over the **Grid** (▢) icon, then drag it up or down to the new position. *Rich Filter Results* gadgets will display the columns in this order.

![2025-08-01_12-37-32.png](/cms_trial/assets/e2b36b8a-d5c7-4239-9c56-0359e0d5e02d.png)

### **8. Delete columns**

Click the **Delete** (▢) icon next to the column.

![Delete the column](/cms_trial/assets/a744fd27-e147-41d2-8527-f4261e92108b.png)

### **9. Freeze columns**

Click the **Freeze** (▢)icon to freeze or unfreeze the corresponding column. Frozen columns remain visible during horizontal scrolling in the *Rich Filter Results* gadget.

![Frozen column](/cms_trial/assets/227ffbad-0b63-4c71-9c3e-116809d037d1.png)

Look at the [Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) documentation page to learn how to display views in dashboards.

## **Work with special columns**

*Special columns* display issue-related information that is not available in issue fields. The available special columns are:

- Last comment – displays the most recent comment added to an issue
- Jira Service Management special columns – the following special columns are available only for issues in Service Management projects:

  - Last external comment – the most recent external comment added either by a Service Management agent or by a customer
  - Last internal comment – the most recent comment added internally
  - Last reply from customer – the most recent comment added by the customer
  - Last reply to customer – the most recent external comment added by a Service Management agent

To add a special column, click the **Add a column...** drop-down menu and scroll to the

section (Hint: you can click the quick scroll button available in the drop-down menu):

![contentId-783941729](/cms_trial/assets/ca0a8fa5-fcbc-440c-b82a-60ef58f571c3.png)