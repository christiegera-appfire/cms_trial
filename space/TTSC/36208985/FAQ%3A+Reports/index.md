# FAQ: Reports

Below are some answers to questions we're commonly asked about creating SLA reports. For help with something we haven't addressed, [please contact us](https://appfire.atlassian.net/servicedesk/customer/portals).

#### ***Are JQL functions available?***

Answer:

SLA Search functionalities are not available on Cloud due to the limitations of the Atlassian Cloud API. This means you won’t be able to use SLA Search functionalities on the work item navigator.

As SLA Search functionalities are not available, we recommend that you use the **+** **More** button to set the SLA scope.

***I’m getting a request timeout error while trying to generate my report. How can I fix that?***

Answer:

It could be that you simply have way too many work items, SLAs, and other information. Try to use as many Filter Types as you can, and if possible, split the information in your report into numerous other reports. Then, you can also try to generate your report as a background report. If the problem persists, please contact us.

#### ***Is there a limit to the work items I can use in my reports?***

Answer:

We can't offer you an exact work item limit as this depends on how your SLA is configured, the number of SLAs utilized, the configurations, how many goals are in each SLA, and many other parameters.

We strongly recommend you generate your reports with low work item numbers in the UI and create background reports for those with high numbers.

As a rule of thumb, always use as many filters as you can! Creating as many different reports as possible is also a good option.

To ensure that the report generation process runs smoothly, always try to fill out either Project, JQL, or Filter Type, since these will have a significant impact on the generation performance of your report.

#### ***I selected my filters and generated my report. However, some of my selected SLAs are missing from the report’s column section. Why?***

Answer:

If there is no relevant information about the SLA you selected, it will not appear in your report. In the near future, those SLAs will appear as a blank column in your report.

#### ***My report has incorrect and/or missing information. How can I fix this?***

Answer:

First, recalculate the report’s scope. After that, if there are still inaccuracies in your SLAs, you can run another report to compare the two reports.

#### ***Is there a way to delete old reports automatically?***

Answer:

Yes! Go to **Settings** > **Advanced** > **Clean Old Reports**. Here you can select how often reports will be automatically deleted.

#### ***My SLA Summary Reports and SLA Detail Reports are showing different values. Why?***

Answer:

The SLA Summary Report is useful for developing work item-based reports, whereas the SLA Detail Report is better for creating SLA-based reports. Once you’ve created a summary report, if you have an SLA that didn’t reach the target date, it shows the remaining duration of this SLA. If you have an SLA that has already been breached, it shows the overdue duration of the SLA.

Once you’ve created a Detail report, it shows the elapsed duration in the working duration column, the remaining duration in the remaining duration column, and the overdue duration in the breach duration column.

| **REPORT TYPE** | **SLA INDICATOR** | **RESULT ON REPORT** |
| --- | --- | --- |
| SUMMARY | EXCEEDED | OVERDUE DURATION |
| SUMMARY | MET/PROGRESS | REMAINING DURATION |
| DETAIL | EXCEEDED | ELAPSED, REMAINING, BREACHED in different columns |
| DETAIL | MET/PROGRESS | ELAPSED, REMAINING, BREACHED in different columns |

Please note that you shouldn’t compare the Summary report with the Detail report to avoid this misunderstanding.