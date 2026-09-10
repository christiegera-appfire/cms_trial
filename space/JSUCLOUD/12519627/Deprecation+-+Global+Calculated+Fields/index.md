# Deprecation - Global Calculated Fields

We first launched Calculated Fields in August 2020 as part of the global configuration (***“global Calculated Fields”***) and the core functionality of JSU (***“Calculated Field post-function”***).

We value your feedback and strive to deliver a high-quality core product. Based on your feedback and an in-depth assessment, we decided to deprecate JSU's ***global Calculated Fields*****.**We apologize for any inconvenience this change might cause.

### What you need to know

The *Calculated Field post-function will* remain as part of the core JSU functionality and is not affected by this announcement. The ***global Calculated Fields*** will be deprecated and no longer available after **November 12, 2021**.

### How to migrate

You can transform your ***global Calculated Field*** into a *Calculated Field* post function within JSU or use an alternative Marketplace app. Read more about the different options below.

## Use cases and alternatives

The *Calculated Field* post function is a workflow function that performs automated calculations after a work item transitions to a new status. Its main difference from *global* *Calculated Fields*is that the calculations are performed as part of a workflow transition and are not recurring on any other work item field change. Read more about it on the dedicated [documentation page](/cms_trial/space/JSUCLOUD/12520029/Calculated+Field+post+function/).

Here is an example of the steps you can take to replace an existing ***global Calculated Fields***configuration with *Calculated Field post-function*.

|  |  |
| --- | --- |
| ***Use Case*** | Roll up the total story points of work items to your Epic. |
| **Step 1**  Prepare to configure the *Calculated Fields post-function* | ***Option A***  When creating a ***global*** ***Calculated Field***, a custom field is automatically created under Jira custom fields. contentId-12519627 If you want to utilize this already existing custom field to configure a *Calculated Field post-function*, you can delete the global calculated field **without** trashing the custom field by not checking the checkbox as shown. contentId-12519627 Then, select this custom field as your result field in the configuration of the *Calculated Field post-function* following Step 2.  ***Option B***  Otherwise, create a new Jira custom (number) field and give it a name. Assign your field to the project screens where you want it to appear. This will be your result field for the calculation. Then, follow the instructions in Step 2  for the *Calculated Field post-function*. contentId-12519627 |
| **Step 2**  Configure the *Calculated Fields post-function* | Go to your project's settings and select the "Workflows" tab from the left-side navigation. contentId-12519627 Click on the edit button on the right, and select the transition you want your calculation to perform. For example, if you select the *Start Progress* transition, your field will be calculated once your work item is in the **In Progress** status. contentId-12519627 Switch to the post-functions tab and click the button "Add post-function". contentId-12519627 Select the *Calculated Field post-function* from the list of post-functions and click "Add" contentId-12519627 Configure your calculation to perform within the same work item and input the formula using the functions and fields drop-downs to calculate the total Story Points of the work items under your Epic. contentId-12519627 Add your post-function and publish your workflow to save your changes.  Go to your Epic, input Story Points to the work items under your Epic, transition your Epic to **In Progress**, and your field is calculated.  The calculation will be performed every time your Epic transitions to the **In Progress** status.  Precondition (optional) Configure the ***Value Field precondition*** in your *Calculated Field post-function* to restrict it to a specific project and/or work item type. contentId-12519627 |

## Other Appfire alternatives

Not happy with the *Calculated Field* post function? No worries! Here are other Appfire solutions available for Jira Cloud that may better apply to your specific use cases:

| **Product name** | **Functionality** |
| --- | --- |
| [Power Custom Fields](https://marketplace.atlassian.com/apps/1210749/power-custom-fields-for-jira?hosting=cloud&tab=overview) | Power Custom Fields for Jira offers a suite of useful and configurable custom fields to help you extend the data inside Jira using predefined calculations.  Available Custom Fields:   - Number Fields    - Sum Of Story Points   - Un-sized Issues   - Number of Stories   - Completed Story Points   - Completed Issues By Percentage - User Picker Fields    - Previous Assignee   - Modified By - Text-Fields    - Parent Field Value   - Parent Status   - Time in Previous Status |
| [Reports & Timesheets for Jira](https://marketplace.atlassian.com/apps/1212942/reports-and-timesheets-for-jira?hosting=cloud&tab=overview) | Being a powerful reporting tool with an intuitive interface, Reports & Timesheets for Jira helps you create custom **reports and dashboards** for daily use. It also provides calculated fields functionalities to help you get more meaningful data **in your reports**.  Supported functions:   - Numeric functions - String functions - Date functions - Logical functions |

## Get help

Do you have any questions or need support?

Feel free to contact our team through our [support portal](https://appfire.atlassian.net/servicedesk/customer/portals). We are always happy to help!