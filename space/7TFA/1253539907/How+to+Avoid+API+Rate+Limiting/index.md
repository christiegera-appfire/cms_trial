# How to Avoid API Rate Limiting

Every system has its limits. At 7pace, there are limits on the number of API requests that you and your team are allowed to ensure quality of service for all users. Please see [API Request Limits](/cms_trial/space/7TFA/1253539983/7pace+Timetracker+API+Important+Information/) and [Lifetime Policies](/cms_trial/space/7TFA/1253539983/7pace+Timetracker+API+Important+Information/) for more information. This article contains techniques that may help you to achieve less frequent and more effective interaction with 7pace's API.

## Incremental refresh

Incremental refresh is a great way to decrease the load on the API. Instead of repeatedly polling the entire history of data, *the data created, changed, or deleted during a specified period is requested (refreshed) from the API*. Whereas, the data created, changed, or deleted *before*this specified period stays stored in the dataset and is no longer requested from the API. Data older than a specified archived period is removed from the dataset altogether. The archived period is usually set to years, while the refreshed period is set to days or single months (more on this later).

![Incremental_Refresh.png](/cms_trial/assets/046446ff-966a-40be-920d-d2857c8666c0.png)

How to set this up with 7pace Reporting API? Use the **EditedTimestamp** attribute of worklogs and only query data where **EditedTimestamp** was changed within a specified period. The **EditedTimestamp** attribute is updated whenever a worklog is created, updated, or deleted. Make sure you use API of version 3.3 or higher and utilize endpoints ending with `WithDeleted` so that you get deleted worklogs in responses.

![Edited_Timestamp.png](/cms_trial/assets/2b6fc261-624c-4b67-90ee-6aaa72e402d0.png)

Incremental refresh can be implemented manually, e.g., via using two reports (one for historical data, one for fresh data). The easiest way, though, is to use native Power BI functionality. We recommend reading the [official Microsoft documentation](https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview) first.

## Incremental refresh via PowerBI

In this section, the process to connect Power BI to our data source and set up incremental refresh is described.

### Prerequisites and recommendations

- You need Power BI Desktop together with a Power BI Pro license or higher. Data model and incremental refresh is set up on Power BI Desktop, but incremental refresh only works if a model is published as a service. See [Power BI documentation](https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview) for up to date information.
- **OData feed** data source is more suitable for incremental refresh because it supports automatic pagination (via `@odata.nextlink` attribute in metadata). Therefore, we recommend using the [7pace reporting API](https://appfire.atlassian.net/wiki/x/qoG3Sg).

  - For optimal process, use version 3.3 or higher because it can also provide information about deletedworklogs. Why does it help? If you process information about deleted worklogs, you can select shorter refresh periods because you need not be dependent on locking past weeks for editing; you can simply get all changes no matter how old the edited or removed worklogs were.
- If you decide to connect a data source as regular JSON content into Power BI (**New Source** > **Web**), you must implement pagination logic. This most likely prevent query folding that is required for incremental refresh to work (more on this later).

### Process

For incremental refresh to work, you need to:

- [Set up a data source](#Set-up-data-source) that will obtain data from the 7pace API for a certain date/time interval.
- [Set up incremental refresh parameters](#Set-up-incremental-refresh) for this data source.
- [Publish the data source](#Publish-to-a-service-and-schedule-regular-refresh) to a Power BI service and schedule its regular refresh interval.

#### Set up data source

First, connect Power BI to the 7pace OData data source (see [our 7pace documentation](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for our step-by-step guide). For optimal performance, it is strongly recommended to use API v3.3 or higher and utilize endpoints providing deleted worklogs as well (they end with `WithDeleted` suffix).

Once the data source is connected, you must set the **RangeStart** and **RangeEnd** parameters, and update the Power Query accordingly. This tells Power BI how to filter records from a specified refresh period.

1. Edit the query, e.g. via the context menu:

   ![Edit_Query.png](/cms_trial/assets/5a9659af-8607-412e-a2c5-885b0b45c22a.png)
2. Add **RangeStart** and **RangeEnd** parameters using the [official Microsoft configuration guide](https://docs.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-configure). The parameters must be in the Date/Time format, otherwise, the incremental refresh will not work. For the initial values, we set **RangeStart** in the past (i.e. years) and **RangeEnd** to the current date.
3. Next, choose a field with **RangeStart**and **RangeEnd** as ranges when obtaining data from the API. The field must contain a date and time. It is recommended to use the **EditedTimestamp**of a work log; even if a user creates a work log in the future or changes an old record, **EditedTimestamp** will contain the system date of the time when the change took place.  
   OData source, however, stores timestamps in DateTimeZone format, so you must create a function that transforms **DateTimeZone** to **DateTime**. Therefore, create a blank query, call it `DateKey`, and paste the following code to the body:  
   `= (x as datetime) => DateTimeZone.From(x)`  
   The result looks like this:

   ![DateKey.png](/cms_trial/assets/92481513-9b08-4f38-aa09-f9001f267466.png)
4. As the final step, apply the filtering by **RangeStart**and **RangeEnd** to the field of our choice from the previous step with the `DateKey` conversion function applied to it. An easy way to do this is to first filter the field with some random value:

   ![Range_Start_End.gif](/cms_trial/assets/db3835b9-008e-4a59-9a94-01892b3c9f27.gif)

   Next, update the transformation step so it works with the **RangeStart** and **RangeEnd**parameters with the `DateKey`function applied.

   ![Filtered_Rows.png](/cms_trial/assets/5eaf6260-df9f-46c2-83bc-45a5f0b1b925.png)![Date_Timezone.gif](/cms_trial/assets/08dc2e2a-85dc-4c3c-a4b2-a53d3a30cbd6.gif)

Make sure the interval is closed on one side (that is, `>=`) and open on the other side (that is, `<`), otherwise, the data in the report can get duplicated.

The final Power Query must look like this:

```text
let
  Source = OData.Feed("https://{replaceByYourURL}.timehub.7pace.com/api/odata/v3.3-beta", null, [Implementation="2.0"]),
  workLogsWorkItems_table = Source{[Name="workLogsWorkItemsWithDeleted",Signature="table"]}[Data],
  #"Filtered Rows" = Table.SelectRows(workLogsWorkItems_table, each [EditedTimestamp] >= DateKey(RangeStart) and [EditedTimestamp] < DateKey(RangeEnd))
in
  #"Filtered Rows"
```

1. Further transformations, if needed, can be done after the previously-mentioned steps, but only transformations that allow the query to be [folded](https://docs.microsoft.com/en-us/power-query/power-query-folding) must be applied*.*

Now that the filtering is set, check if Power BI translates the Power Query to the API request properly. In other words, the filters must be applied in the API calls directly, instead of Power BI downloading all data first and then applying the filters after post.

- Incorrect: `GET https://{sampleURL}.timehub.7pace.com/api/odata/v3.3-beta/workLogsWorkItemsWithDeleted`
- Correct: `GET https://{sampleURL}.timehub.7pace.com/api/odata/v3.3-beta/workLogsWorkItemsWithDeleted?$filter=EditedTimestamp ge 2022-06-01T00:00:00%2B02:00 and EditedTimestamp lt 2022-06-09T00:00:00%2B02:00`

One option to verify this is to use a tool for capturing and debugging network traffic (WireShark, Fiddler); or, use the Power BI built-in diagnostic tools as demonstrated below:

1. In the Power Query editor, choose **Tools** > **Start Diagnostics**.

   ![Start_Diagnostics.png](/cms_trial/assets/8777c8ea-8f1d-4d1b-a007-d75a02686b15.png)
2. Refresh the query.

   ![Refresh_Preview.png](/cms_trial/assets/76c2d938-8642-4135-9251-e558dd28fefc.png)
3. In **Tools**, select **Stop Diagnostics** and check the **Detailed results** of the **Query** section.

   ![Diagnostics_Detailed_Result.png](/cms_trial/assets/2b0ddf68-d25c-47a9-9086-089cd973221b.png)
4. Filter only those rows that have the **Data Source Query**column filled in and check the requests. In the example below, the query folding works correctly and **EditedTimestamp** filter is used in the API call directly.

   ![Data_Source_Query.png](/cms_trial/assets/08a5427f-5996-46cf-a690-0649af26b154.png)

**Troubleshooting - start with a base URL**

What if you still cannot see filters applied in the URL? The issue may lie in how you set up the data source in the first place - for PowerBI query folding to work, you muststart with the base URL (e.g. `https://{sampleURL}.timehub.7pace.com/api/odata/v3.3-beta`), and then,choose the endpoint you wish to use as a subsequent step in PowerBI.

- Incorrect URL when setting up data source: `https://{sampleURL}.timehub.7pace.com/api/odata/v3.3-beta/workLogsWorkItemsWithDeleted`
- Correct URL when setting up data source: `https://{sampleURL}.timehub.7pace.com/api/odata/v3.3-beta`

The selection of a specific endpoint is represented by the second row of the Power Query example (the one starting with `workLogsWorkItems_table`).

```text
let
  Source = OData.Feed("https://{replaceByYourURL}.timehub.7pace.com/api/odata/v3.3-beta", null, [Implementation="2.0"]),
  workLogsWorkItems_table = Source{[Name="workLogsWorkItemsWithDeleted",Signature="table"]}[Data],
  #"Filtered Rows" = Table.SelectRows(workLogsWorkItems_table, each [EditedTimestamp] >= DateKey(RangeStart) and [EditedTimestamp] < DateKey(RangeEnd))
in
  #"Filtered Rows" 
```

### Set up incremental refresh

After making sure that Power BI is calling the correct API queries, go ahead and set up incremental refresh of the data source.

![Incremental_Refresh_Setup.png](/cms_trial/assets/e6b79674-f27c-48fd-a033-57eed644efd9.png)

 The setting of incremental refresh attributes can vary per organization, depending on how much past data is needed for your reports (months or years), if you process deleted worklogs or not, and, the frequency of your reporting.

An example of the setting can be:

- The archive period is set to two years, which means that data up to two years old is a part of the dataset. Older data will no longer be kept in the dataset in Power BI (which means it will not be in your reports, but will still remain in 7pace database).
- Refresh period*:*

  - **Recommended:** set to one weekif you fetch all changes including deletedworklogs (i.e. you are using an endpoint ending with `withDeleted`). This way, PowerBI only fetches worklog changes (creation, modification, deletion) done during the past 7 days, while the rest of the data stays untouched.
  - Set to one monthif you do not process deleted worklogs so that you have more space to catch changes. One month refresh period means that data creation/deletion/update within the past month is reflected in your report. This also includes the update of records that are much older than one month, because **EditedTimestamp**is replaced with the current date in this case. Only deletion of records older than the refresh period are not reflected.

If the refresh period is kept short, the response becomes faster; though the API returns less data.

![Incremental_Refresh_Real_Time_Data.png](/cms_trial/assets/a720c04c-3662-46c1-aa76-a9cdcf174e80.png)

The warning about query folding does not necessarily mean that the query folding will not actually work. It just means that Power BI was not able to verify the query. If Power BI called the URLs with the correct filters, as described in the previous section, and if a refresh can be scheduled after the dataset is published as a Power BI service (see below), the warning sign can be ignored.

**Will this create duplicate records?**

Yes, if somebody updates a worklog older than your refresh period, you will get a new record via a refresh along with the original record created or updated before the refresh period. It is, therefore, recommended to set up a follow-up Power Query that shows records only with the latest **EditedTimestamp** according to its **id**. Removing duplication is not in scope of this tutorial, but watch [this video](https://www.youtube.com/watch?v=QaodJFeX49k) as a guideline.

### Publish to a service and schedule regular refresh

With the incremental refresh set, the dataset to a Power BI service must be published. If any changes occurs in the Power BI Desktop afterwards, the data model must be published again for the changes to take place in the service. Click **Publish**.

![Publish.png](/cms_trial/assets/4d3f2141-1442-46fa-b449-aa41a5982488.png)

In Power BI cloud, navigate to our dataset and refresh the data manually for the first time. You may need to enter credentials (this is described at the bottom of the article).

![Refresh.png](/cms_trial/assets/823a6137-75f4-45b1-abc5-bb764bd91b19.png)

After the first refresh is done, you can schedule a regular refresh of the dataset.

![Schedule_Refresh.png](/cms_trial/assets/28dd7676-e907-45e9-88da-70561e355922.png)![Gateway_Connection.png](/cms_trial/assets/50e1b319-174c-4e5f-b316-abb4c503cbd0.png)

#### Troubleshooting

When experimenting with the incremental refresh ourselves, there can be several potential issues. Use the following information to troubleshoot or avoid them altogether:

- The refresh fails/asks for credentials if Power BI does not know the given API yet. Try updating the credentials in the settings of the data source and try again.
- Datasets with dynamic data sources cannot be refreshed from the service (although they seem to work fine in Power BI Desktop). You have to rewrite your Power Query:

  - If using `OData.feed`in your PowerQuery, as is recommended for 7pace API, remember that you must obtain the feed via the base URL (e.g. `https://{sampleURL}.timehub.7pace.com/api/odata/v3.3/workLogsWorkItemsWithDeleted`) without parameters, and, subsequently, filter results using `Table.SelectRows` as described in [this post](https://community.powerbi.com/t5/Power-Query/OData-filter-pass-through/m-p/156845/highlight/true#M9455). You must go through the guide thoroughly to avoid this error.
  - If using `Web.Contents`in your Power Query, see this [blog post](https://blog.crossjoin.co.uk/2016/08/23/web-contents-m-functions-and-dataset-refresh-errors-in-power-bi/) for more details. However, you can encounter the *dynamic data source* issue when implementing pagination anyway.

#### Final thoughts

It is recommended to verify the refresh status of the PowerBI service once the process is completed.

![Dataset_Details.png](/cms_trial/assets/96f95d17-5744-49cf-af1e-b482def3e990.png)

#### Template

A Power BI template file - [7pace Incremental Load Example.pbit](https://appfire.atlassian.net/wiki/download/attachments/1253539907/7pace%20Incremental%20Load%20Example.pbit) - is available that contains a simple example of incremental refresh. Just input initial start and end dates, change URL in the datasource, and, enter your credentials.

## Incremental refresh in Excel

Currently, Excel does not support incremental refresh.

It is recommended to set up a service in Power BI (see above) and then using the result as a data source in Excel to save API calls.

![Incremental_Refresh_in_Excel.png](/cms_trial/assets/c2dd03ea-6576-405f-be63-d94b77b67be6.png)

## Incremental refresh in other tools

Incremental refresh can be achieved in the other tools as well, but you need to keep two separate reports: one with stable data and one with fresher 'delta' data.

If you are used to loading 7pace Timetracker data to your database and evaluating the changes there, you can miss deleted records (because they are currently deleted for good, without being indicated using a delete flag in the API responses). In this case, do add and/or upvote our [feature request for webhooks](https://support.7pace.com/hc/en-us/community/posts/360062515011-Feature-Request-for-webhooks-on-time-entry).