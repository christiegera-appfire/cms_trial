# Configure custom ratios

## About custom ratios

Custom ratios are computed user-defined outputs that can be used in rich filter gadgets. They are defined as ratios, with a numerator and a denominator**,** which can be based on issue count or numeric & time tracking fields. Optional JQL filtering conditions can filter the contributing issues for the numerator and/or the denominator. Custom ratios can thus be used to compute ratios of different values.

Below is an example of a *Rich Filter Simple Gauges* gadget that displays two gauges based on custom ratios: *Completion rate* and *Work ratio*.

![Rich Filter Simple Gauges gadget.png](/cms_trial/assets/0d887f2c-7497-4fb2-96ea-7a744901d132.png)

## Custom ratios key attributes

The **Custom ratios** section of your rich filter lets you add new custom ratios and view existing ones and their configurations.

![Custom ratio.png](/cms_trial/assets/31f79940-a246-45e2-8ef4-64b9368a4a57.png)

The **key attributes** of a custom ratio are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each custom ratio has a **Name** that must be unique among the custom ratios within the rich filter. |
| **Color** | The selected color will be used to display the ratio in some of the rich filter gadgets. |
| **Numerator**  **Base value** | The value on which the numerator of your custom ratio is based is selected among Issue Count or numeric and time-tracking fields. contentId-783942266 |
| **Numerator**  **JQL** | You can optionally define a JQL query to filter the issues contributing to the numerator of the custom ratio. Only the issues satisfying this query will be taken into account when calculating the numerator. |
| **Denominator**  **Base value** | The value on which the denominator of your custom ratio is based. The numerator and the denominator can be based on the same field or two different fields of the same type. The denominator can also be a constant (fixed value), which you enter when defining the custom ratio.  The available options for the denominator base value depend on the selected numerator base value:  [Unmapped macro: nested-table — no content to fall back on] contentId-783942266 |
| **Denominator**  **JQL** | You can optionally define a JQL query to filter the issues contributing to the custom ratio's denominator. Only the issues that satisfy this query will be considered when calculating the denominator. |
| **Display format** | Specifies the format used to display custom ratios in the rich filter gadgets. The available options are:   - Percentage – for example, if the value is 3/10, the gadget displays 30% - Ratio – for example, if the value is 3/10, the gadget displays 0.3   If the *Ratio* option is selected, you can further select how many decimals by selecting from 0 to 6 decimal places. contentId-783942266 Independent of this setting, custom ratios are always displayed as percentages in gauge gadgets. |

## Add and edit custom ratios

The *Custom ratios* section of your rich filter lets you perform the following operations:

### 1. **Add a new custom ratio**

1. Click the **Create custom ratio** button at the top-right of the page.

   ![2025-09-04_08-13-53.png](/cms_trial/assets/502ed025-cce9-4b15-ab9e-5257895421f6.png)
2. Type a **Name**, select a color, configure the **Numerator** and **Denominator**, choose the **Display format**, and click **Create**.

   ![contentId-783942266](/cms_trial/assets/ab9b91fb-6705-40b8-a466-2b4f1a4c27e0.png)

You can add up to 100 custom ratios in each rich filter.

### **2. View or edit a custom ratio**

Click the **Edit** (▢)icon next to a custom ratio. to view or edit its configuration. Depending on your rights, you can edit or only view the queue.

![contentId-783942266](/cms_trial/assets/eef229b7-4699-40c8-99a2-f83ac11d0c2b.png)

### 3. **Reorder the custom ratios**

Hold the pointer over the queue's **Grid** (▢) icon, then drag the custom ratio up or down to the new position.

![contentId-783942266](/cms_trial/assets/ad4382dc-f23b-41e9-921f-ac85e9ed2277.png)

### **4. Delete a custom ratio**

Click the **Delete** (▢) icon next to the custom ratio.

![contentId-783942266](/cms_trial/assets/12621231-cdbd-4a97-acaf-15ce3b1a2992.png)

## **Use custom ratios in Rich Filter gadgets**

Below, we provide the list of rich filter gadgets that can display custom ratios:

- The **Rich Filter Simple Gauges** gadget displays gauges based on three custom ratios: *Completion rate, Work ratio,* and *SLA %Met*:

![SLA.png](/cms_trial/assets/ae6b3e86-0f0c-4f50-b636-9f6954a4fcf4.png)

Check the [Rich Filter Simple Gauges Gadget](/cms_trial/space/RFCDOC/783942228/The+Rich+Filter+Simple+Gauges+Gadget/) documentation page to see how to configure the gadget.

- The **Rich Filter Smart Gauges** gadget displays for each team (defined in a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/)) a gauge representing a custom ratio named *Work ratio*:

Check the [Rich Filter Smart Gauges Gadget](/cms_trial/space/RFCDOC/783942246/The+Rich+Filter+Smart+Gauges+Gadget/) documentation page to see how to configure the gadget.

- The **Rich Filter Statistics** gadget displays two custom ratios, Completion rate, and Work ratio, aggregated by the issue field Priority:

![statistics custom.png](/cms_trial/assets/fb50daf3-a911-42c3-bf89-74bbed34dbbb.png)

Check the [Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) documentation page to see how to configure the gadget.

- The **Rich Filter Two**[-](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/)**Dimensional Statistics** gadget displays a custom ratio named *SLA %Met*, aggregated by the issue field Priority and a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) named Team:

![statistic custom ratio.png](/cms_trial/assets/02a4b463-4299-4aa0-8906-3778d1715cfa.png)

Check the [Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) documentation page to see how to configure the gadget.

- The **Rich Filter Flexi Chart** gadget display[s](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) the *Completion rate* custom ratio broken down by assignees.

![flexi chart with custom ratio.png](/cms_trial/assets/b5c912c4-6baa-4479-ae24-45b26b8babb1.png)

Check the  [Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) documentation page to see how to configure the gadget.

- The **Rich Filter Time Series Chart** gadget displays two time series: *Work ratio* and *Resolved issues.*

![time series chart.png](/cms_trial/assets/6adee2a6-3711-4920-9b94-7d468bd15574.png)

Check the [Rich Filter Time Series Chart Gadget](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) documentation page to see how to configure the gadget.