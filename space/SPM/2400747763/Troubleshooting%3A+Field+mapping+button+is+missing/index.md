# Troubleshooting: Field mapping button is missing

## Problem

- As a Box Admin, I cannot access the custom field mapping screen because the Field button is missing at the top of the **App settings** dropdown and at the bottom of the **Add or edit columns** panel.

| A snippet of the app settings dropdown. | Add or edit columns panel. |
| --- | --- |

## Solution #1

The custom **Field mapping** button for a particular box can be missing because there are no actual Jira work items in the scope of that box.

For example, if you [created a box using the](/cms_trial/space/SPM/2400616769/Use+case%3A+Create+a+box+with+sample+data/) [**Play with sample data**](/cms_trial/space/SPM/2400616769/Use+case%3A+Create+a+box+with+sample+data/) option, then the scope is composed of dummy Jira work items that do not exist in any Jira project.

In such a case, if you intend to use this box for a real project or tasks, you need to add them to the scope of the box.

Visit the [Populate a box with Jira work items](/cms_trial/space/SPM/2400714956/Populate+a+box+with+Jira+work+items/) page to learn how to do this.

Note that adding new tasks/projects to the scope will not remove the dummy tasks that already exist, and you will need to delete them manually. For that reason, using a sample box for real data may not be the most feasible approach. We suggest you [create a new box](/cms_trial/space/SPM/2400780468/Create+your+first+box/) for your real project.

## Solution #2

The custom **Field mapping** button for a particular box can be missing because there are no Jira work items in the scope of that box.

For example, you added several basic tasks to your box but no Jira tasks from actual Jira projects. Since basic tasks cannot be synchronized with Jira, the field mapping does not apply to them.

If you want to synchronize your basic tasks, you need to convert them to Jira work items.

Visit the [Convert basic task to Jira work item / Convert BigPicture task to Jira work item](/cms_trial/space/SPM/1918863006/Convert+basic+task+to+Jira+work+item+%2F+Convert+BigPicture+task+to+Jira+work+item/) page to learn how to convert basic tasks to Jira work items.

Note that you need an already-existing Jira project to add the converted basic tasks to.