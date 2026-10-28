# Import from file

## Import from file (old navigation)

Click to expand the guide

You can easily import your task templates from tools like MS Project, MS Excel, CSV, or OpenDocument files. The option is available in Gantt and Scope modules.

Box admins and Jira admins can import tasks from a file. When the [Permissions for everyone](/cms_trial/space/SPM/1918535770/App-level+permissions/) option is enabled, every logged-in user can import tasks from a file.

To import tasks from a file:

1. Expand the **Add task +** drop-down menu.
2. Select **Import tasks from file**.

![Screenshot of the Import from file feature in the Scope module.](/cms_trial/assets/e02c0cf7-7de8-40f3-9906-86c455ed364c.png)

## Upload a file

The maximum file upload size is 300MB. The following file types are supported:

- .mpp
- .mpx
- .xls
- .xlsx
- .ods
- .csv

## Import data from MS Project

Once you import a file from MS Project, all columns with data will be automatically detected.

Check a list of supported fields in the *Supported fields* section below.

To import tasks:

1. Expand the **Add task +** drop-down menu.
2. Select **Import tasks from file**.
3. Upload a file.
4. Select how the tasks should be converted:

   1. Jira work items (parents will be converted to default issue types)
   2. Jira work items (parents will be converted to epics)
   3. BigPicture basic tasks
5. Select the Jira space where the tasks will be created. For more info, see the *Select Jira space* section below.
6. Add Jira labels to identify imported tasks.
7. Enable **Add labels as an additional filter for the box scope** if you want the entered labels to be added as filters on the [Work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page.
8. Decide whether the [ASAP mode](/cms_trial/space/SPM/1918865340/Strong+dependencies+(App+configuration)/) for dependencies should be on or off.
9. When ready, click **Import**.

![Screenshot of importing a Microsoft Project file with tasks in the Gantt module.](/cms_trial/assets/c9550cea-93ad-4f7b-8a43-d3f281eb8e0e.png)

Note that sub-tasks will be imported as default work item types.

To see a real example, watch the video below.

## Import data from MS Excel / OpenOffice

When importing MS Excel or OpenOffice files, you need to define the columns corresponding to the imported data. To simplify this step, BigPicture tries to recognize the column names and completes the fields accordingly.

Check a list of supported fields in the *Supported fields* section below.

To import tasks:

1. Expand the **Add task +** drop-down menu.
2. Select **Import tasks from file**.
3. Upload a file.
4. Select how the tasks should be converted:

   1. Jira work items (parents will be converted to default issue types)
   2. Jira work items (parents will be converted to epics)
   3. BigPicture basic tasks
5. Select the Jira space where the tasks will be created. For more info, see the *Select Jira space* section below.
6. Add Jira labels to identify imported tasks.
7. Enable **Add labels as an additional filter for the box scope** if you want the entered labels to be added as filters on the [Work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page.
8. Match the columns from the selected file to the corresponding task fields. You can set the relationships between tasks (**Parent row** and **Link** columns).
9. When ready, click **Import**.

![Screenshot of importing an Excel file with tasks in the Gantt module.](/cms_trial/assets/50d48657-aa91-4cfe-9d38-e526b4b90428.png)

## Import tasks without dates

The import mechanism allows to support tasks with a single date or undated tasks in the file. These tasks will be imported with one date or without dates.

## Supported fields

The table below presents the supported fields for particular files.

| **Supported field** | **Files - .xls, .xlsx, .csv, .ods (column name)** | **Files - .mpp, .mpx (column name)** |
| --- | --- | --- |
| Summary | ("Summary") | ("Task Name") |
| Start Date | ("Start Date") | ("Start") |
| End Date | ("End Date") | ("Finish") |
| Issue type | ("Issue Type") | - |
| Assignee | ("Assignee") | ("Resource Name") |
| Original Estimate | ("Original Estimate") | ("Work") |
| Milestone | - | ("Milestone") |
| Baseline Start Date | - | ("Baseline Start") |
| Baseline End Date | - | ("Baseline Finish") |
| Progress | - | ("% Complete") |

## Select Jira space

To carry out the import successfully, you need to define a Jira space where the imported issues should be created. Tasks are visualized in BigPicture and must exist somewhere in Jira itself.

You can:

- Use one of your current spaces. New issues will be added to the existing ones.
- You can also set up a new, empty Jira space in advance. It is possible to create a new Jira space using the **Create with shared configuration** option. This will result in copying the Jira space setup (permission, notification, issue security, workflow, work item types, issue type screen, and field configuration). For more information, refer to the screenshots below.

[Unmapped block: nestedExpand]

## XLSX data format

If the .xlsx file has been created by exporting BigPicture data, it can be easily imported.

Otherwise, ensure that data is formatted in the following way:

![Screenshot of an XLSX file.](/cms_trial/assets/a0ad4750-89b6-4524-8401-0c02269e7954.png)

**Start date, End date** - can be read in the following formats:

- yyyy-MM-dd (e.g. 2021-12-31)
- dd-MM-yyyy (e.g. 31-12-2021)
- MMM/dd/yyyy (e.g. Dec/31/2021).

**Parent Row** - the Excel row in which the parent of the task is

![Screenshot of a parent row in an imported file.](/cms_trial/assets/9e475dbc-3beb-4f95-acc5-dbd5ff308a76.png)![Screenshot of the parent task on the task tree.](/cms_trial/assets/ce6163d9-2a49-4cdd-ac0e-3669a13b66e8.png)

**Link** - a cell with dependencies/links, for example, 16FS-1 or 21SS+1, where:  
16, 21 - pointer to Excel's row with the linked task;  
FS, SS - link type:

- FS - finish to start;
- SS - start to start;
- FF - finish to finish;
- SF - start to finish.
- -1/+1 - link lag in days.

![Screenshot with an example of a link cell.](/cms_trial/assets/3214fde7-f55f-425e-8ed3-819eb56bd6cd.png)

In this case:

- The target of a link is in row 33
- Start to finish link
- 0 lag days

![Screenshot with an example of an imported file.](/cms_trial/assets/3f987dc5-d251-4115-810d-9841561379b4.png)![Screenshot with an example of the task tree before exporting.](/cms_trial/assets/65e614bf-4297-4b87-9a57-eedd78c430fb.png)

## Possible problems and solutions

### The Import from file option is greyed out.

The scope type dictates whether the option is available. If a box was created using a box type with **own scope**, the option is available.

For boxes with **sub** and **none** scopes, the **Import from file** optionis **unavailable.**

### Required fields

Make sure that all fields have been set to **optional** in the Jira field configuration before importing a file.

The process of making this adjustment is demonstrated below.

[Unmapped block: nestedExpand]

### Mapping task assignee

By importing from .mpp files, the system maps information about task assignees, so imported values are correct. To make sure the **Assignee** value is imported correctly, double-check if the value in the **Resource name** field in the .mpp file is the same as the value in the user's **full name** field in Jira (the case of characters will be ignored).

If there is no user match, the **Assignee** field will be set to **Unassigned**.

### Circular link dependencies

Once the file is imported, the application will not create strong dependencies if the circular dependency is identified (circular dependencies also include parent dependencies).

### Link ID

- Link with missing ID
- Missing Parent Task ID

### Period check failure

The start date is later than the end date.

## Import from file (new navigation)

Click to expand the guide

You can easily import your task templates from tools like MS Project, MS Excel, CSV, or OpenDocument files. The option is available in the Gantt and Scope modules.

Box admins and Jira admins can import tasks from a file. When the [Permissions for everyone](/cms_trial/space/SPM/1918535770/App-level+permissions/) option is enabled, every logged-in user can import tasks from a file.

To import tasks from a file:

1. Expand the **Tasks** menu.
2. Select **Import from file**.

![Screenshot of the Import from file option in the Gantt module.](/cms_trial/assets/f7dd1dcc-62f8-4f0f-b05d-7a8995a6d316.png)

## Upload a file

The maximum file upload size is 300MB. The following file types are supported:

- .mpp
- .mpx
- .xls
- .xlsx
- .ods
- .csv

## Import data from MS Project

Once you import a file from MS Project, all columns with data will be automatically detected.

Check a list of supported fields in the *Supported fields* section below.

To import tasks:

1. Expand the **Tasks** menu.
2. Select **Import from file**.
3. Upload a file.
4. Select how the tasks should be converted:

   1. Jira work items (parents will be converted to default work item types)
   2. Jira work items (parents will be converted to epics)
   3. BigPicture tasks
5. Select the Jira space where the work items will be created. For more info, see the *Select Jira space* section below.
6. Add Jira labels to identify imported tasks.
7. Enable **Add labels as an additional filter for the box scope** if you want the entered labels to be added as filters on the [Work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page.
8. Decide whether the [ASAP mode](/cms_trial/space/SPM/1918865340/Strong+dependencies+(App+configuration)/) for dependencies should be on or off.
9. When ready, click **Import**.

![Screenshot of importing a Microsoft Project file with tasks in the Gantt module.](/cms_trial/assets/c9550cea-93ad-4f7b-8a43-d3f281eb8e0e.png)

Note that sub-tasks will be imported as default work item types.

To see a real example, watch the video below.

## Import data from MS Excel / OpenOffice

When importing MS Excel or OpenOffice files, you need to define the columns corresponding to the imported data. To simplify this step, BigPicture tries to recognize the column names and completes the fields accordingly.

Check a list of supported fields in the *Supported fields* section below.

To import tasks:

1. Expand the **Tasks** menu.
2. Select **Import from file**.
3. Upload a file.
4. Select how the tasks should be converted:

   1. Jira work items (parents will be converted to default work item types)
   2. Jira work items (parents will be converted to epics)
   3. BigPicture tasks
5. Select the Jira space where the work items will be created. For more info, see the *Select Jira space* section below.
6. Add Jira labels to identify imported tasks.
7. Enable **Add labels as an additional filter for the box scope** if you want the entered labels to be added as filters on the [Work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page.
8. Match the columns from the selected file to the corresponding task fields. You can set the relationships between tasks (**Parent row** and **Link** columns).
9. When ready, click **Import**.

![Screenshot of importing an Excel file with tasks in the Gantt module.](/cms_trial/assets/50d48657-aa91-4cfe-9d38-e526b4b90428.png)

## Import tasks without dates

The import mechanism supports both single-date and undated tasks in the file. These tasks will be imported with one date or without dates.

## Supported fields

The table below presents the supported fields for particular files.

| **Supported field** | **Files - .xls, .xlsx, .csv, .ods (column name)** | **Files - .mpp, .mpx (column name)** |
| --- | --- | --- |
| Summary | ("Summary") | ("Task Name") |
| Start Date | ("Start Date") | ("Start") |
| End Date | ("End Date") | ("Finish") |
| Work item type | ("Work item Type") | - |
| Assignee | ("Assignee") | ("Resource Name") |
| Original Estimate | ("Original Estimate") | ("Work") |
| Milestone | - | ("Milestone") |
| Baseline Start Date | - | ("Baseline Start") |
| Baseline End Date | - | ("Baseline Finish") |
| Progress | - | ("% Complete") |

## Select Jira space

To carry out the import successfully, you need to define a Jira space where the imported work items should be created. Tasks are visualized in BigPicture and must exist somewhere in Jira itself.

You can:

- Use one of your current spaces. New items will be added to the existing ones.
- You can also set up a new, empty Jira space in advance. It is possible to create a new Jira space using the **Create with shared configuration** option. This will result in copying the Jira space setup (permission, notification, work item security, workflow, work item types, work item type screen, and field configuration). For more information, refer to the screenshots below.

[Unmapped block: nestedExpand]

## XLSX data format

If the .xlsx file has been created by exporting BigPicture data, it can be easily imported.

Otherwise, ensure that data is formatted in the following way:

![Screenshot of an XLSX file.](/cms_trial/assets/a0ad4750-89b6-4524-8401-0c02269e7954.png)

**Start date, End date** - can be read in the following formats:

- yyyy-MM-dd (e.g. 2021-12-31)
- dd-MM-yyyy (e.g. 31-12-2021)
- MMM/dd/yyyy (e.g. Dec/31/2021).

**Parent Row** - the Excel row in which the parent of the task is

![Screenshot of a parent row in an imported file.](/cms_trial/assets/9e475dbc-3beb-4f95-acc5-dbd5ff308a76.png)![Screenshot of the parent task on the task tree.](/cms_trial/assets/ce6163d9-2a49-4cdd-ac0e-3669a13b66e8.png)

**Link** - a cell with dependencies/links, for example, 16FS-1 or 21SS+1, where:  
16, 21 - pointer to Excel's row with the linked task;  
FS, SS - link type:

- FS - finish to start;
- SS - start to start;
- FF - finish to finish;
- SF - start to finish.
- -1/+1 - link lag in days.

![Screenshot with an example of a link cell.](/cms_trial/assets/3214fde7-f55f-425e-8ed3-819eb56bd6cd.png)

In this case:

- The target of a link is in row 33
- Start to finish link
- 0 lag days

![Screenshot with an example of an imported file.](/cms_trial/assets/3f987dc5-d251-4115-810d-9841561379b4.png)![Screenshot with an example of the task tree before exporting.](/cms_trial/assets/65e614bf-4297-4b87-9a57-eedd78c430fb.png)

## Possible problems and solutions

### The Import from file option is greyed out.

The scope type dictates whether the option is available. If a box was created using a box type with **own scope**, the option is available.

For boxes with **sub** and **none** scopes, the **Import from file** optionis **unavailable.**

### Required fields

Make sure that all fields have been set to **optional** in the Jira field configuration before importing a file.

The process of making this adjustment is demonstrated below.

[Unmapped block: nestedExpand]

### Mapping task assignee

By importing from .mpp files, the system maps information about task assignees, so imported values are correct. To make sure the **Assignee** value is imported correctly, double-check if the value in the **Resource name** field in the .mpp file is the same as the value in the user's **full name** field in Jira (the case of characters will be ignored).

If there is no user match, the **Assignee** field will be set to **Unassigned**.

### Circular link dependencies

Once the file is imported, the application will not create strong dependencies if the circular dependency is identified (circular dependencies also include parent dependencies).

### Link ID

- Link with missing ID
- Missing Parent Task ID

### Period check failure

The start date is later than the end date.