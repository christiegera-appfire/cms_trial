# Configure time series

## About time series

Time series are collections of data points based on your issues’ date fields – for example, the number of issues due for each week of the current quarter or the monthly SLA %Met ratio of the last year. The data points can be based on issue counts or values computed from issue fields. JQL filters can optionally be used to limit series to subsets of issues.

The time series can be displayed as line charts with the [Rich Filter Time Series Chart](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) or tables with the [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) gadget. Several time series can and are generally displayed simultaneously in the same gadget, allowing users to compare and identify trends and correlations between series.

![time series_dashboard.png](/cms_trial/assets/719c2cec-5b19-43a4-a8d9-31d719d705f1.png)![time series dashboard.png](/cms_trial/assets/2ce69d54-822d-471c-bf2b-b8050cef13e4.png)

## Time series key attributes

You can add new and see existing time series and their configuration in the*Time series*section of your rich filter.

![time series.png](/cms_trial/assets/2d06a280-65d5-4c11-abef-87b59f3da7d4.png)

The **key attributes** of a time series are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each time series has a **name** that must be unique among the time series within the rich filter. |
| **Color** | The selected color will be used to display the series in some of the rich filter gadgets. |
| **Series** | Each time series is based on a date field, which is used to identify the issues contributing to each data point.  SLA Time Series The user can also select any SLA field as the base for the time series. Each SLA option behaves like a date field representing the completion date of the SLA (only issues with completed SLAs are taken into account; the completion date of the last SLA cycle is used). |
| **Base value** | The value on which the data points are based. This can be Issue Count, numeric and time-tracking fields, SLA values (see below), [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), or [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/).  SLA Time Series If the series are based on SLA fields, then the following SLA values become available:   - *SLA Completed* – returns the issues for which the SLA is completed - *SLA Met* – returns the issues for which the SLA is completed and met - *SLA Breached* – return the issues for which the SLA is completed and breached - *SLA %Met* – return the percentage of issues for which the SLA is met out of the issue for which the SLA is completed - *SLA %Breached* – returns the percentage of issues for which the SLA is breached out of the issues for which the SLA is completed - *SLA Average* – displays the average completion time for the issues that have their SLA completed   In all the cases, only the issues with the SLA completed are considered, and only the last cycle is included in any computation. |
| **Value type**  Displayed in the time series table | The *value type* is automatically computed based on the *base value*. The possible *value types* are:   - Issue Count – for series based on the number of issues, directly (Issue Count) or through [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) - Numeric – for series based on numeric fields, directly or through [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) - Time Tracking – for series based on time tracking fields, directly or through [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) - SLA Average – for series based on SLA averages - Ratio – for series based on SLA ratios or on [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/)   The *value type* is pertinent in the [Rich Filter Time Series Chart](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) gadget, where the time series plotted together on the same chart must have the same *value type*. |
| **JQL** | You can optionally define a JQL query to filter the issues contributing to the time series. Only the issues satisfying this query will be taken into account when calculating the data points. |

## Add and edit time series

The **Time Series** section of your rich filter lets you perform the following operations:

### 1. **Add a new time series**

1. Click the **Create time series** button at the top-right of the page.

   ![contentId-783942356](/cms_trial/assets/f992ff2a-6f8d-4f4d-86ce-d2f03e0f8463.png)
2. Type a **Name**, select a color, **Series**, and a **Base value**, and optionally type a **JQL** query, then click **Create**.

   ![contentId-783942356](/cms_trial/assets/42db7dbd-5c09-4eda-9f8b-c822fb19caff.png)

You can add up to 100 time series in each rich filter.

### 2. **View or edit a time series**

Click the **Edit** (▢) icon next to a time series to view or edit its configuration.

![contentId-783942356](/cms_trial/assets/5549ac0f-9898-4ff9-ac9a-db021eb47d64.png)

### 3. **Reorder the time series**

Hold the pointer over the queue's **Grid** (▢) icon, then drag up or down to the new position.

![contentId-783942356](/cms_trial/assets/8ecc1cab-47bc-41a0-9ce2-782023299b4e.png)

### 4. **Delete a time series**

Click the **Delete** (▢) icon next to the time series name.

![contentId-783942356](/cms_trial/assets/fddbce50-89e7-45bb-9307-9b5555457d26.png)

## Computed time series

Users can define *unresolved* *time series, a* special type of time series, falling under the *Computed* category. Unlike the other time series based on a date field, *unresolved time series* are computed as the difference between *Created* and *Resolved* time series. *Unresolved time series* allows users to monitor the size of the backlog easily.

To create an unresolved time series, start by creating one as described in [Adding & Editing Time Series](/wiki/pages/resumedraft.action?draftId=783942356#ConfiguringTimeSeries-section3) and then select the *Unresolved* option in the *Series* drop-down menu. The option is available under the *Computed* category:

![contentId-783942356](/cms_trial/assets/0d03bd89-ed08-4ce4-b45f-68266cb119d8.png)

The newly created unresolved time series can then be displayed in rich filter gadgets like any other time series. In the example below, the Unresolved time series is used in a rich filter time series *gadget*. The gadget enables users to track the trend of unresolved issues within a specific time range by monitoring the unresolved issues of each aggregation period.

![time series_chart.png](/cms_trial/assets/dfe69913-997a-466d-a359-82b636399fc1.png)

## **Use time series in Rich Filter gadgets**

Below, we provide the list of rich filter gadgets that can display time series:

- **Rich Filter Time Series Chart** gadget – it displays the time series as line charts

  ![time to resolution series.png](/cms_trial/assets/9eadaf61-48fa-4ea0-ba79-800b0c99e823.png)

Check the [Rich Filter Time Series Chart Gadget](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) documentation page to see how to configure the gadget.

- **Rich Filter Flexi Chart** gadget

![flexi chart by time.png](/cms_trial/assets/27f763dc-f3bb-42aa-aedc-c5b50fdb543c.png)

Check the [Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) documentation page to see how to configure the gadget.

- **Rich Filter Statistics** gadget – it displays the time series in table format.

  ![statistics by time.png](/cms_trial/assets/70214120-69be-48bf-8230-81cdf003155f.png)

Check the [Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) documentation page to see how to configure the gadget.

- **Rich Filter Two-Dimensional Statistics** gadget

![two cimentional by asignee.png](/cms_trial/assets/cd841b8e-4243-4877-b6dd-71419df46192.png)

Check the [Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) documentation page to see how to configure the gadget.