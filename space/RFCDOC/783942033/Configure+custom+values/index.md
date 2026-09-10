# Configure custom values

## About custom values

Custom values are user-defined outputs that can be used in rich filter gadgets. They are available as columns in views and as values in gadgets alongside the Jira fields. They provide support for custom aggregation formulas (sum, average, minimum, and maximum, with optional JQL filtering of contributing issues) and custom results display (label, color, and format). Custom values can be based on Issue Count or numeric and time-tracking fields.

Below is an example of a Rich Filter Statistics gadget that displays, by assignee, the following custom values: the sum of the story points of the resolved issues, the sum of the time spent for support issues, the average time spent (displayed in hours) and the maximum remaining estimate for the unresolved issues.

![statistics with custom val.png](/cms_trial/assets/72a1a107-5470-4c4b-b7d3-66b81f5152c6.png)

## Custom values key attributes

The **Custom values**section of your rich filter lets you add new custom values and view their configuration.

![custom_values.png](/cms_trial/assets/43b5418a-5c04-4460-9c6d-0dba2c48b81f.png)

The **key attributes** of a custom value are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each custom value has a **name** used to identify and display it. The name is mandatory and must be unique among the custom values within the rich filter. |
| **Color** | The selected color will be used to display the value in some of the rich filter gadgets. |
| **Base value** | The value on which your custom value is based is selected among Issue Count or numeric and time-tracking fields. contentId-783942033 |
| **Total formula** | The formula used for aggregation. The possible options are sum, average, minimum, and maximum. contentId-783942033 |
| **Display** | The display format of the custom value. The available options are   - For numeric fields:    - Thousand separators on/off   - Number of decimals: none or maximum 3, 2 or 1 or exactly 3, 2 or 1  contentId-783942033 **What's the difference between maximum 2 and exactly 2 decimals?**  If you select *exactly 2* options, the value will always be displayed in 2 decimals. This is achieved by rounding to 2 decimals if more than 2 are available (e.g., 23.4567 → 23.46) or padding with zeros up to a total of 2 decimals if fewer than 2 are available (e.g., 23.4 → 23.40).  Selecting the maximum 2 option will display the value *with 0, 1,* or 2 decimals. This is achieved by rounding to 2 decimals if more than 2 are available (e.g., 23.4567 → 23.46) and leaving the value as it is if 2 or fewer decimals are available (e.g., 23.4 → 23.4).   - For time-tracking fields, you can select the **Time display format**:    - **Jira's time display format** – uses the time format as configured in Jira by the administrator of the instance:   - Years, weeks, days, hours, minutes, or seconds |
| **JQL** | You can optionally define a JQL query to filter the issues contributing to the custom value. Only the issues satisfying this query will be taken into account when calculating the custom value. |

## Add and edit custom values

The *Custom values* section of your rich filter lets you perform the following operations:

### 1. **Add a new custom value**

1. Click **Create custom value** at the top-right of the page.

   ![create_custom_val.png](/cms_trial/assets/d16ed742-db06-43cc-b0ae-eb5d76ade44c.png)
2. Type a **Name**, select a color, **Base value,** **Total formula**, and a display format,
3. (Optional) Type a JQL query.
4. Click **Create**.

   ![contentId-783942033](/cms_trial/assets/c59e09d4-8068-4ac0-90af-7fd27f1ef765.png)

You can add up to 100 custom values in each rich filter.

### 2. **View or edit a custom value**

Click the **Edit** (▢)icon next to a custom value to view or edit its configuration. Depending on your rights, you can edit or only view the custom value.

![contentId-783942033](/cms_trial/assets/12be2e4f-08a2-44d4-8e9c-98ea401fc481.png)

### 3. **Reorder the custom values**

Hold the pointer over the queue's **Grid** (▢) icon, then drag the custom value up or down to the new position.

![contentId-783942033](/cms_trial/assets/9003e6fd-7391-4719-98eb-0e7061bb08fe.png)

### 4. **Delete a custom value**

Click the **Delete** (▢) icon next to the custom value name.

![contentId-783942033](/cms_trial/assets/6106344b-6109-47ab-b4e3-b93c0c863462.png)

## Computed custom values

*Computed custom values* are a special case of custom values having a computed base value. Like any other custom value, computed custom values can be used in views and rich filter gadgets.

The *Rich Filter app* provides two computed duration custom values:

- *Issue age / resolution time* - predefined duration value calculated as the time elapsed between the *resolution time (*or *now* for unresolved issues*)* and the *created date*
- *Custom duration* - duration value calculated as the time elapsed between any two date/date time fields or between a date/date time field and now

 These options are further detailed in the sections below.

### Issue age/resolution time

Issue age / resolution time is a predefined computed duration value based on the issue created and resolved dates. The issue age / resolution time is calculated as:

- for unresolved issues – the time elapsed between now and the created date (issue age)
- for resolved issues – the time elapsed between the resolution date and the created date (resolution time)

To create a custom value based on the issue age / resolution time, select the **Issue age / resolution time** option in the**Base value** drop-down menu. The option is available under the **Duration (computed)** category:

![contentId-783942033](/cms_trial/assets/4c88c855-432c-4831-b486-889c2d012861.png)

The **Total formula** and **JQL**fields are the same as any other custom value described in [Custom Values' Key Attributes](/wiki/pages/resumedraft.action?draftId=783942033#ConfiguringCustomValues-section2).

The **Duration display format** field is duration-specific and lets you choose between **Days** and **Hours**.

![contentId-783942033](/cms_trial/assets/979b7543-23d3-47a7-9e16-f5116b8a3f8f.png)

### Custom duration

*Custom duration* is a computed duration value, calculated as the time elapsed between any two date/date-time fields or between a date/date-time field and now.

1. Select the**Custom duration**option in the **Base value** drop-down menu to create a custom value based on a custom duration.   
   The option is available under the **Duration (computed)**category:

![contentId-783942033](/cms_trial/assets/3f50eae4-4d0b-40cb-991b-feb11677dcf2.png)

1. Select the **Start** and **End**, which can be a date/date-time field or the **Current time***.*   
   If the selected date/date-time field can be empty, an extra checkbox becomes available in the selection window, allowing the current day to be used instead of an empty value:

![contentId-783942033](/cms_trial/assets/c21f96e9-d9c8-4581-bcaa-df24e2b247fd.png)

The **Total formula** and **JQL** fields are the same as any other custom value described in [Custom Values' Key Attributes](/wiki/pages/resumedraft.action?draftId=783942033#ConfiguringCustomValues-section2).

The **Duration display format** field is duration-specific and allows you to choose between **Days** and **Hours**.

![contentId-783942033](/cms_trial/assets/979b7543-23d3-47a7-9e16-f5116b8a3f8f.png)

If one of the selected values for the start or end date is of type date, the display format is automatically set to **Days**. In this case, the computed value is a non-fractional number of days.

![contentId-783942033](/cms_trial/assets/437e8404-7b53-49a3-8c7b-ac9c8b09bb44.png)

### Lead time

*Lead Time* is an important concept, defined as the average resolution time for the resolved issues. To compute the lead time, create a custom value based on issue age / resolution time and choose the *average* formula. Use the JQL to eliminate all those issues that are not yet resolved:

![contentId-783942033](/cms_trial/assets/68750df7-a2ed-48fd-991a-d0f4a7bae71c.png)

## Use custom values in rich filter gadgets

Custom values can be added to views displayed as columns in Rich Filter Results gadgets or as values in the Rich Filter gadgets displaying aggregated issue data.

Below are some examples of rich filter gadgets configured to display custom values:

- **Rich Filter Results** gadget displaying a view that contains a custom value based on Time Spent and formatted in hours:

![result with custom_val.png](/cms_trial/assets/13684c4c-9f19-4729-99ac-1eeef7477d1e.png)

Look at the Rich Filter Results Gadget documentation page to find out how to configure the gadget.

The display format settings can be very handy if you wish to display some numeric or time-tracking fields in a particular format, e.g., hours for a time-tracking field.

- **Rich Filter Simple Counters** gadget displaying four custom values:

![counters with custom val.png](/cms_trial/assets/1761166b-eaf0-409a-a56e-c52d8a8acde0.png)

Look at the Rich Filter Simple Counter Gadget documentation page to find out how to configure the gadget.

- **Rich Filter Statistics** gadget displaying four custom values aggregated by assignee:

![statistics with custom val.png](/cms_trial/assets/72a1a107-5470-4c4b-b7d3-66b81f5152c6.png)

Look at the [Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) documentation page to learn how to configure the gadget.

- **Rich Filter Two Dimensional Statistics** gadget displaying a custom value named Support Time Spent aggregated by the issue field Priority and a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) named Team:

![two dimentional stat.png](/cms_trial/assets/d8a2698c-f47f-4c4d-a300-8fae03ba3c7f.png)

Check the [Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) documentation page to see how to configure the gadget.

- **Rich Filter Flexi Charts** gadget displaying a bar chart of a custom value named Resolved Story Points by assignee:

![flexi charst with custom val.png](/cms_trial/assets/93ffedaf-d2e3-431f-9981-7394c6a6b492.png)

Check the [Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) documentation page to see how to configure the gadget.