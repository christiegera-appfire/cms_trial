# Start/end date fields

## Start/End date fields

### Overwrite Jira task data with data from the App

If you want to use a different field, it is possible to overwrite Jira task data with data from BigPicture. When you select a field other than currently used, you can switch on the **"Overwrite Jira task data with data from the App"** option below.

**This action is irreversible.**

![contentId-1918507050](/cms_trial/assets/ec47c6e3-b349-4206-a519-1c62f34aba2a.png)

In general, there are three main strategies for task synchronization:

- Not synchronized - use this option if you do not want to update Jira issues while still being able to plan using the Gantt module. Changes to date estimates will not sync to Jira, meaning task start and end dates might differ from those in Jira issues.
- Two 'Date picker' (or 'Date time picker') fields - recommended when assignees work on multiple tasks simultaneously.
- One 'Date picker' (or 'Date time picker') field and a time estimate field (Original estimate or Time spent + Remaining estimate) - recommended for working on one task at a time.

The App will not update fields mapped above as a start and end date if they are not defined in the Jira Project Screen scheme (excluding Time Spent + Remaining Estimate). In other words, for synchronization to work, you must ensure that the fields exist in Jira for a particular project.

If you need more details, take a look at the example:

See the example

A separate custom configuration has been specified for the "OMEGA" Jira project. This ensures that other projects are not affected.

![contentId-1918507050](/cms_trial/assets/02d28d81-d6f8-429f-90ad-5af6bc075f0a.png)

Create a Jira Screen that has those fields. You can copy an existing screen and modify it to make things easier. In the example, a copy was made and named "OMEGA."

![contentId-1918507050](/cms_trial/assets/f9d73f1e-0ede-484b-9d70-07b09d5afcdd.png)

Add a Screen scheme. The system will ask you what screen you want to associate it with.

![contentId-1918507050](/cms_trial/assets/f59335ad-1384-462d-b3aa-98b00498e789.png)![contentId-1918507050](/cms_trial/assets/af1cda35-dc1d-47d9-8043-5b87185f5dc7.png)

Add an Issue type screen scheme.

![contentId-1918507050](/cms_trial/assets/e6c14054-9359-4043-b8d0-ca90aad0cac4.png)![contentId-1918507050](/cms_trial/assets/dd12deb3-0730-4018-bc0f-888c75bc210c.png)

You'll be taken to the following screen (click the name of the Screen Scheme).

![contentId-1918507050](/cms_trial/assets/a6d7278e-bad1-491c-96a4-1be4615bc2e9.png)

Click the name of the screen.

![contentId-1918507050](/cms_trial/assets/6a7a6179-26d9-4818-b81e-8c93832b89da.png)

Ensure the fields you set in the Technical configuration are listed. In this case, the "Start Date" field already exists, and the "Due date" needs to be added.

![contentId-1918507050](/cms_trial/assets/adc19dac-b856-4b69-ae41-5ebcf5f0d796.png)

Go to the Jira Project settings and implement the new screen scheme.

![contentId-1918507050](/cms_trial/assets/1192f655-9ea9-4240-acb9-ccf685c16596.png)![contentId-1918507050](/cms_trial/assets/236aa498-22b0-4f18-9031-4cc67797787a.png)![contentId-1918507050](/cms_trial/assets/9c78d00f-6f2b-4a6b-bdc5-b67cc2935ae8.png)![contentId-1918507050](/cms_trial/assets/eac30f06-fc4d-47ad-90e8-44d521d17ecf.png)

Now, the App can synchronize with Jira - making changes within the App will update respective fields.

## Scheduling impact

### Start/end dates mapped to estimate fields

- Start date

  - can be mapped to the **Original Estimate**
- End date

  - can be mapped to **Original Estimate**or
  - **Time Spent +** **Remaining Estimate**

**Note**: Only one of the fields (either start or end date) can be mapped to an estimate. The other field must remain as a date field, such as the start/end date.

#### **Expected behavior (dates exist)**

You can update the following values:

- star/end date
- task duration
- the estimate field

Updates can be done by:

- change of a field value, for example, by editing a value in a column in BigPicture
- adjustment of a task position and length on a Gantt chart

**New start/end value (inline editing or update of a field on Jira issue page)**

Behavior is the same regardless of mapping:

- Change of the **start date** results in a task being moved.
- Change of the **end date** results in a task being resized. The estimate field and task duration field reflect the change. The start date is unaffected.

![Estimate mapping - start_end update.mov](/cms_trial/assets/e4ff19c2-fa33-4737-acc6-8494a4cb684f.mov)

| **Change** | **Result** | **value** | **Affected** | **Mapping** |
| --- | --- | --- | --- | --- |
| start date updated | Task moved | start date | ✅ | - start date = Original Estimate - end date = Original Estimate - end date = Time Spent + Remaining Estimate |
| end date | ✅ |
| task duration | ❌ |
| Estimate | ❌ |
| end date updated | Task resized | start date | ❌ |
| end date | ✅ |
| task duration | ✅ |
| Estimate | ✅ |

**New task duration OR estimate field value**

Behavior depends on the mapping:

- the date mapped to the estimate is adjusted

![Estmate mapping - task duration.mov](/cms_trial/assets/90500fc4-5253-4a6f-8799-cab2776321ce.mov)![Estimate mapping - estimate update.mov](/cms_trial/assets/ef9eaec5-d764-4341-94a3-eec895a9a798.mov)

| **Change** | **Result** | **value** | **Affected** | **Mapping** |
| --- | --- | --- | --- | --- |
| task duration updated  OR  estimate value updated | Task resized | start date | ✅ | - start date = Original Estimate |
| end date | ❌ |
| task duration | ✅ |
| estimate | ✅ |
| start date | ❌ | - end date = Original Estimate - end date = Time Spent + Remaining Estimate |
| end date | ✅ |
| task duration | ✅ |
| estimate | ✅ |

**Task position adjusted on the timeline**

All fields are updated to reflect the task position on the timeline. 

The position of the “Overwrite Jira task data with data from the App” slider is ignored. BigPicture operates based on the built-in field values.

## Affected by

The **Respect Jira screen scheme** toggle switch applies to **start/end date field mapping**.