# Story points field

## Story points field (old navigation)

Click to expand the guide

The Story Points field can be mapped to various other numerical value fields. Mapping can be configured per the Jira Project. By default, the field is mapped to the native Story Points field in Jira.

In the drop-down menu, the App offers you a variety of existing fields with a numerical value - that doesn't mean each possible mapping will suit your needs. Make sure that the mapping meets your business needs.

For example:

If you mapped "Story Points" to "Time Tracking Progress (Original)," a built-in Story Points field value for a new task would be 0, and for a finished task, it would be 100 story points.

When the Original Estimate is 2d and the time logged is 1d, the value of the built-in Story Points field will be 50.

- The Story Points field in a column/card view can display values stored within multiple fields (e.g., from various team-managed projects).
- The Story Points totals in the Board module (capacity allocation, work progress) can be calculated based on selected fields.

The Story Points built-in field, aggregating data from mapped fields, can be added to the column/ card view.

![contentId-1918507163](/cms_trial/assets/a58620f2-4f73-47d7-b018-cef94b5c0f35.png)

### Not Synchronized

When selecting the "Not Synchronized" option, the App will use the default Jira "Story Points" field for all operations. The built-in "Story Points" field will display the same value as the Jira "Story Points" field in:

- Column/Card views
- The **Resources** module (Workload Contouring, Story Point mode)

The system will display no value if the Jira "Story Points" field hasn't been added to the screen scheme. Operations such as workload contouring won't be available, and the system will show you a warning, letting you know Story Points haven't been configured and can't be used.

### Mapped

The App uses the built-in field value for all operations (workload contouring, resource planning in story point mode, etc.)

After the mapping,  even if the Jira "Story Points" field has been added to the Jira screen and has a value, the App will use the mapped field value for all operations (for example, in the Resources module in Story Points mode and for workload contouring).

For columns/card views, you can select if you want the system to display a Jira "Story Points" field value or the built-in "Story Points" field value.

![contentId-1918507163](/cms_trial/assets/d50a04b4-b332-4e2e-8634-5e8e7d952b4f.png)

### Custom Field

You can create a custom numerical field in your Jira and add it to the screen scheme. The field will be available in the Technical configuration drop-down menu and can be used for mapping.

To add a custom field, go to Jira configuration (cog at the top right) > Issues > Custom Fields (on the left) > Add custom field (button at the top right).

The field has to have a numerical value.

![contentId-1918507163](/cms_trial/assets/98587f13-471f-4d8c-b329-37ae754d44c4.png)![contentId-1918507163](/cms_trial/assets/d64195d8-627c-4bbd-8bf8-5fec536953bf.png)

Remember to add the field to the screen scheme(s) used by projects where you want the field to be available.

![contentId-1918507163](/cms_trial/assets/941b78e6-4a24-4f70-bd2b-c7a9db149b98.png)

On the **App Configuration > General > Fields** page, you can use the custom field for mapping - either for the entire application or various projects.

![contentId-1918507163](/cms_trial/assets/a87bc2eb-d0e2-4b94-bbf0-83d7c4e6fe7e.png)

## Story points field (new navigation)

Click to expand the guide

The **Story points** field can be mapped to various other numerical value fields. Mapping can be configured per the Jira space. By default, the field is mapped to the native Story Points field in Jira.

In the drop-down menu, the App offers you a variety of existing fields with a numerical value - that doesn't mean each possible mapping will suit your needs. Make sure that the mapping meets your business needs.

For example:

If you mapped "Story Points" to "Time Tracking Progress (Original)," a new task's built-in Story Points field would be 0, and a finished task’s would be 100.

When the Original Estimate is 2d and the time logged is 1d, the value of the built-in Story Points field will be 50.

- The Story Points field in a column/card view can display values from multiple fields (e.g., across various team-managed projects).
- The Story Points aggregation in the Board module (capacity allocation, work progress) can be calculated based on selected fields.

The Story Points built-in field, which aggregates data from mapped fields, can be added to the column/card view.

![contentId-1918507163](/cms_trial/assets/a58620f2-4f73-47d7-b018-cef94b5c0f35.png)

### Not Synchronized

When selecting the "Not Synchronized" option, the App will use the default Jira "Story Points" field for all operations. The built-in "Story Points" field will display the same value as the Jira "Story Points" field in:

- Column/Card views
- The **Resources** module (Workload Contouring, Story Point mode)

The system will display no value if the Jira "Story Points" field hasn't been added to the screen scheme. Operations such as workload contouring won't be available, and the system will show you a warning, letting you know Story Points haven't been configured and can't be used.

### Mapped

The App uses the built-in field value for all operations (workload contouring, resource planning in story point mode, etc.)

After the mapping,  even if the Jira "Story Points" field has been added to the Jira screen and has a value, the App will use the mapped field value for all operations (for example, in the Resources module in Story Points mode and for workload contouring).

For columns/card views, you can select if you want the system to display a Jira "Story Points" field value or the built-in "Story Points" field value.

![Screenshot of adding the Story Points column to the Gantt module view.](/cms_trial/assets/74061681-e19a-40e6-a78f-c4d16a17b727.png)

### Custom Field

You can create a custom numerical field in your Jira and add it to the screen scheme. The field will be available in the Technical configuration drop-down menu and can be used for mapping.

1. To add a custom field, go to Jira **Settings** > **Work items** > **Fields** (on the left) > **Create new field**.

   ![Screenshot of the Jira Fields tab in the Jira settings. ](/cms_trial/assets/ba2adbdb-8c0e-4591-a6f5-4559d62d8edd.png)
2. The field has to have a numerical value.

   ![Screenshot of creating a new number field in Jira settings.](/cms_trial/assets/caa9b8ec-f0b5-4491-8a1e-64b4d1c0d963.png)
3. Remember to add the field to the screen scheme(s) used by projects where you want the field to be available.
4. On the **App Configuration > General > Fields** page, you can use the custom field for mapping - either for the entire application or various projects.

   ![contentId-1918507163](/cms_trial/assets/a87bc2eb-d0e2-4b94-bbf0-83d7c4e6fe7e.png)