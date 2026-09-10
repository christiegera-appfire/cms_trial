# Initial guide for administrators

This article outlines the most essential configuration steps required to start using the App and provides guidance and best practices on the most common use cases.

Make sure that the version of the App you want to install is compatible with your Jira instance. We recommend using Atlassian's plugin manager, which will always install the latest compatible version of our App.

Before installing the app on your production instance, make sure to test it using the staging environment. If it is not possible, create a separate project on your instance and test how the App works.

## Process identification

The first step should be to identify the business processes that will be affected by BigPicture and to develop, at least at a high level, for piloting purposes.

There are administrator-level settings in BigPicture - the Jira administrator on the company side should be included in the BP installation process.

## Documentation

We strongly recommend that you go through the documentation, especially the cross-module features and scheduling rules.

## Test it first

As with all new software installations, we recommend using a stage instance to test it first and to back up your data before installing it on a production instance.

## Configuration

The minimal resolution of the app is 1280x720. If you make the viewing tab narrower, the view cannot be further compressed, and part of it will be cut off.

Start with the App's configuration, which requires Jira administrator access. The most important are the following:

- [Security](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297994764) - if you are evaluating the App, you can grant permissions to everyone or restrict access by assigning security roles to users or user groups.
- [Task](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297767423) - specify which fields will be synchronized when using the App. Each task has a start and end date, and it can be mapped to different fields. If you are already using date fields in Jira (such as "Due date") simply map them and the App will use those dates during the synchronization to generate the tasks correctly.

**Note**

The start and end dates are required by the App to generate the task on the timeline. When tasks without date estimates are synchronized, the App will use the "Creation date" as both the start and end date mapped field values. If the task dependencies are defined this might result in unintentional updates of schedules.

Besides the task field mapping, we recommend disabling the comments and notifications. While they are very useful and improve communication, when you create your Boxes and synchronize existing data, users might receive numerous notification emails. Enable these features once your Boxes are synchronized.

- [Dependency configuration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298126901) - like with the task field mapping, you can synchronize up to five different dependency types to visualize the task relationships.
- [Team field configuration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297572703) - Teams are a very important element, especially when using the Board and Resources modules. Make sure to select the fields used for Team assignment.
- [Risks](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298158654) -  check if the Risk heat map matches your organization's needs - change the field mapping or update the select options if required.

## Administration

The administration section is another important area and it requires App administrator access:

- [Security Global roles in Administration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298287400) - grant access to the App. There are two global security roles - App users and App admins.
- [Box types](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297538577) - configure the default setting of your Boxes.

## Automation

BP has a so-called [Scheduling mode (previously period mode)](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297046573) functionality that can influence the length of parent ribbons and/or child ribbons. As a precaution, it is best to set the "Manual" period mode before the Box scope is defined. BP gives you the ability to set up an automatic record of actions performed on a given ribbon and send notifications to an email to Jira users. In case of unforeseen events, a large number of emails can be sent to the mailbox.

Golden rule: at the beginning of the road with the App, remember not to throw all of Jira's issues into the scope. It can be quite easy to make a mistake, e.g. if you have incorrectly written JQL when defining the scope of a Box.

There is no "UNDO" button in Jira, so make changes very consciously, especially when you define the scope of a Box and synchronize data. We do recommend testing the App in a safe test environment.

Depending on the configuration of the App, your tasks might get updated or recalculated during the synchronization, for example, once the scope is defined. By default, the App requires two points on the timeline (in other words two dates) to generate a taskbar and determine the start and endpoints. Those points in time are the task's "Start Date" and "End date" and are stored as "Start Date" and "End date" custom fields by default.

If a Task with no Start and/or End Dates is added to the scope of a Box, the App will pick the Original Estimate value to calculate the duration and set the task's Start date to the Creation date.

Following this logic, if no Original Estimate value is available the app will again use the creation date as the Start Date and when the End Date is empty, then it picks the resolution date (if the issue was Resolved) instead. This usually means that a Task will be set as a 1-day duration starting on the Creation date. With the Original Estimate mapped as the Start or End Dates, it will represent the duration of a Task.

As a consequence, in such a scenario, the period mode will be applied to tasks with empty date fields to avoid data corruption when the tasks are structured automatically using presets.

In the case of Sprint and Version tasks synchronization, the "Auto top-down" is used by default.

Read more about the scheduling and synchronization settings in the [Scheduling](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=DLPDRAFT&title=Scheduling&linkCreation=true&fromPageId=298156290) section.