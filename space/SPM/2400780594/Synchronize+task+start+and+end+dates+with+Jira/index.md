# Synchronize task start and end dates with Jira

## What will I learn on this page?

> 💡 On this page, we will show you how the project data synchronization between BigPicture and Jira works.

You will learn:

- What a field and field mapping are.
- How to map fields between BigPicture and Jira.

In this example, you will see how to synchronize task start and end dates, but the process for mapping other fields is similar.

## What is a field?

A field in BigPicture and Jira is a designated space or attribute used to capture specific information, such as "Summary," "Description," or "Assignee."

There are two types of fields in BigPicture:

- [Built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/) (BigPicture fields) - System-generated fields that come with the app. They provide essential information for tracking issues. Not all built-in fields can be mapped with Jira fields.
- Jira fields: Fields that display values pulled from Jira.

## What is field mapping?

The field mapping means assigning (mapping) fields in BigPicture to corresponding fields in Jira.

Such a setup ensures that the data pulled from Jira fields corresponds to what you want to see in BigPicture. This way, whenever you make a change in Jira, you can see the same changes in your project in BigPicture—and the other way around.

Depending on the field, you have different options for mapping, including leaving the field unsynchronized.

For example, you can map Story Points in BigPicture with Story Points in Jira. This way, when someone changes the task estimate in Jira or BigPicture, the same number of story points will be displayed in both apps.

![An example of the Story points field mapping.](/cms_trial/assets/91da9615-e358-43ba-b366-2e60542867a0.png)

Note that only fields in Jira work items can be synced between Jira and BigPicture. [Basic tasks](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2024282166) cannot be field-mapped and synchronized.

## Field map Start and End dates step-by-step

By default, all Jira projects use global synchronization settings created by Jira or App Admin. But it is also possible to configure a custom field mapping for selected Jira projects.

Let’s start with the global (general) configuration of the Start and End dates.

important Each Jira field can be mapped only once. So if you map a Due date in Jira with the End date in BigPicture, you cannot map it with another field in the same Jira project.

### Configure global field mapping (Jira/App Admin)

1. Click the **wrench icon** (**App settings**) and select **General** on the dropdown.
2. You are now on the **Fields > General mapping** page, where you can configure field sync for the following built-in fields for all Jira projects:

- Start date
- End date
- Baseline start date
- Baseline end date
- Team Code
- Milestone field
- Story Points
- Required Skills
- Actual cost
- Estimated cost
- Progress
- Scheduling mode

![General field mapping page in BigPicture.](/cms_trial/assets/9cd34f79-1ff5-40a3-a338-1480d2a238df.png)

1. Open a dropdown for the Start date Jira field and select one of the available options:

- Not synchronized
- Date field (for example, Start date)
- Time tracking estimates (for example, Original Estimate)

1. Open a dropdown for the End date Jira field and select a field (for example, Due date).
2. Click **Save**.

### Configure custom field mapping (Jira/App Admin)

1. Click the **wrench icon** (**App settings**) and select **General** on the dropdown.
2. You are now on the **Fields > General mapping** page. Switch to the **Custom mapping** tab.
3. Click the **Add project** button.
4. The **Add project** modal displays.

![Add project modal on the App Configuration page in BigPicture.](/cms_trial/assets/329f941b-dbe7-4fe8-8c27-61bd6c32772b.png)

1. Select a Jira project from the dropdown. Confirm with the **Add and configure** button.
2. A field mapping screen displays for the selected Jira project.
3. Map the Start and End date fields.
4. Click **Save**.

### Configure custom field mapping (Jira/App/Box Admin)

1. Open a box for which you want to configure the field mapping.
2. Click the **plus icon** (**Add or edit columns**) in the column view (or the **wrench icon** (**App settings**)) **>** **Field mapping** button.

| field-mapping-column-view.png | field-mapping-app-settings.png |
| --- | --- |

1. A **Field sync configuration modal** displays.

![Custom field mapping inside the box.](/cms_trial/assets/39350c28-7e35-494a-98d6-af48f45738f2.png)

1. Open a dropdown for the Start date Jira field, and select one of the available options (for example, Start date).
2. Open a dropdown for the End date Jira field (for example, End date or Due date).
3. Click **Save**.

- If you cannot see the **Field mapping** button, it means the box scope does not contain any Jira work items or Jira projects.

Visit the [Populate a box with Jira work items](/cms_trial/space/SPM/2400714956/Populate+a+box+with+Jira+work+items/) course to see how to define which tasks and/or Jira projects appear in the box.

- If the button is grayed out, it means your box consists of multiple Jira projects or tasks from multiple projects.

The field mapping for each project can be customized, but only by the Jira or App Admin on the **App Configuration > General > Fields > Custom field mapping** page (as shown in the [previous section](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/2396390500/Synchronize+task+start+and+end+dates+with+Jira#Configure-custom-field-mapping-(Jira-Admin))).

## Explore other use cases

- Field mapping Start and End dates based on time estimates (Original Estimate)

## Prerequisites

- Field mapping access and permissions:

  - Only Jira and App Admins can create global field mapping and custom field mapping in the **App Configuration**.
  - Box Admins can create a custom field mapping directly in a box.

    - Your box must contain tasks from a single Jira project.
  - Every other user permitted to edit or view the box can check the field mapping settings for that box, but cannot edit them.

## Learn more

- [Concept of a field](/cms_trial/space/SPM/1918633429/Concept+of+a+field/)
- [Fields](/cms_trial/space/SPM/1918635376/Fields/)
- [Built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/)
- [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/)
- [Mapping options for built-in fields](/cms_trial/space/SPM/1926234390/Mapping+options+for+built-in+fields/)