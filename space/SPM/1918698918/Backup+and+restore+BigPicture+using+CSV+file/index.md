# Backup and restore BigPicture using CSV file

BigPicture visualizes data from connected tools, such as Jira.

Jira lets you export data in CVS format. You can export data regarding selected issues (for example, a single project). The backup file can include all existing Jira fields, including custom fields.

Data can be selectively restored from a file. You can specify the field for which you want to make changes. Other fields can be left in their present state.

This process can't be used to restore the WBS structure. It is strictly used to change the values of Jira fields.

## Export

To prepare for export, go to Issue Search. Use JQL filters to display the issues you want to create a backup for.

For example, the "Allocation Details" box has only one Jira project in its scope.

![contentId-1918698918](/cms_trial/assets/6e90f938-088e-43c5-846c-88d5bbc15205.png)

This makes creating a backup file for this box easy. However, a more complex set of JQL filters could be used to include multiple Jira projects or just a limited number of tasks from a project or projects.

![contentId-1918698918](/cms_trial/assets/41221f40-f602-448c-b401-c309a603631d.png)![contentId-1918698918](/cms_trial/assets/aa442bb9-2d85-4462-9f54-419a84a32ec9.png)

Next, export the data into the CSV file.

![contentId-1918698918](/cms_trial/assets/d03c5a13-b10c-4070-bcdd-9d908ee4fe40.png)

## Prepare the app for import

Before the import, you may want to change the period mode in which Gantt tasks operate to manual in some cases. This will prevent any automatic calculations from being performed in BigPicture.

![contentId-1918698918](/cms_trial/assets/95f59c1a-aea5-4663-89a4-f84a1bcf62df.png)

Without this change, the restore process of timeline-related data (start date, end date) has a chance of failure if the existing automatic rules don't allow for making a given change.

To perform this change, select the Data → Task mode → Manual on the Gantt, which will be restored.

## Import data into Jira

Importing an external project lets you selectively overwrite data instead of creating new issues and projects.

To initiate the import, select the *Import External Project* option from the Jira Project dropdown. For official documentation, visit Atlassian documentation for [Running the CSV file import wizard](https://confluence.atlassian.com/adminjiraserver071/importing-data-from-csv-802592885.html#ImportingdatafromCSV-howRunningtheCSVfileimportwizard).

Do not use the Issue dropdown, which has a position called *Import issues from CSV.* Thisoption will not allow you to overwrite the data and will force you to create new items.

For official Atlassian documentation on importing Jira Project from external sources while updating existing Jira issues, please visit [this documentation article.](https://confluence.atlassian.com/adminjiraserver071/importing-data-from-csv-802592885.html#ImportingdatafromCSV-Updatingexistingissues)

![contentId-1918698918](/cms_trial/assets/e244c866-15a5-4ef1-af6b-90cfd0f6f2c1.png)![contentId-1918698918](/cms_trial/assets/bbf2bd29-62c9-4154-ae94-770b6fb2dd25.png)

Especially if Jira issues come from different Jira projects, use data included in the CVS file to overwrite existing issues within those projects.

![contentId-1918698918](/cms_trial/assets/aeae1196-5ffa-4a86-892a-e82650d51662.png)

### Field mapping

Always include the following fields:

- issue key → This will ensure that Jira issues will get updated instead of creating new ones
- Summary → Summary
- Project name → Project name
- Project key → Project key
- Project type → Project type

Additionally, select which fields you want to be overwritten. In the example below "Start Date" and "End Date" fields are selected.

![contentId-1918698918](/cms_trial/assets/312f8e43-192e-4ba9-bcd2-e288fda95928.png)![contentId-1918698918](/cms_trial/assets/5edae5b7-61c2-40ac-ad37-63d00cb8a4da.png)