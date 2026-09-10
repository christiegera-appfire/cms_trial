# Messages - troubleshooting

## Dependencies

Soft dependencies don’t have a scheduling impact.

A strong dependency ensures that the starting point of a dependency is before the target point of a dependency.

![contentId-1918536577](/cms_trial/assets/e6cbf5ec-8d5c-4bc4-a81c-fd296fd0ec70.png)

Strong dependencies (solid line on a Gantt chart) connect tasks in the following ways:

- end to start
- end to end
- start to end
- start to start

There are two types of strong dependencies:

- ASAP - one task immediately follows the other
- non-ASAP - one task follows the other, but doesn’t have to follow immediately

Lag time:

- a mandatory gap between tasks

### Unable to change dates

The dates of this task are determined by the dependency linking it to another task.

The dates of this task are determined by the dependencies linking it to other tasks.

A strong dependency makes it impossible to change the task dates in a way that would break the rules:

- Task can’t be moved on the Gantt module timeline
- Task can’t be moved in the Resources module
- Task dates can’t be manually changed (editing a date of a Jira issue, Gantt module column, task details pop-up)

![contentId-1918536577](/cms_trial/assets/e6cbf5ec-8d5c-4bc4-a81c-fd296fd0ec70.png)

To see the dependencies, go to the Gantt module.

- You can use the search function to locate the task.
- When you click on a task row, the row is highlighted in blue (the task is selected). When you clear the search, the task is still highlighted in blue.
- When dependencies are collapsed, you can click on a dependency dot to see the details.
- When dependencies are expanded, you can see dependencies visualized as arrows connecting tasks.

![contentId-1918536577](/cms_trial/assets/659a6f23-acc4-4963-9afb-26b52bccc714.mov)

Solutions:

- move the source task before moving the target task.
- change the task scheduling mode to manual (automatic rules no longer apply - you can manually change the dependency dates). The dependency arrow is orange to indicate the rules are broken, but you are allowed to place the task wherever you want.
- change the dependency type to ‘soft’ - soft dependencies don’t have a scheduling impact. They can be used to indicate a connection between tasks.
- remove the dependency.

![contentId-1918536577](/cms_trial/assets/f46b2c93-6035-45ac-bc09-5f47c0cc3d68.mov)

### Dates adjusted by a dependency

Dependency rules have repositioned a task.

In the example below:

- strong ASAP dependency connects tasks - an ASAP dependency positions source and target points right after the other. Lag time is added (when specified).
- Scheduling mode of the target task was manual (dependency didn’t apply).
- Scheduling mode of a task changed to auto bottom-up - dependency is applied. The task is moved.

![contentId-1918536577](/cms_trial/assets/438aa0c2-eb05-475d-b5e4-be312f2f7d59.mov)

The dates of this task are determined by the dependency linking it to another task.

When a target task doesn’t have start/end date, it is not on the timeline. Once a task is positioned on the timeline, dependency rules apply.

![contentId-1918536577](/cms_trial/assets/6160bbf5-8714-4766-bdbb-fa190708ff89.mov)

## Scheduling mode

### Unable to change dates

#### **Auto top-down task**

The dates of this task depend on the dates of its parent, which is set to auto top-down scheduling mode.

When a task is in the ‘auto top-down’ scheduling mode, it adjusts its period to fit under the parent task.

![contentId-1918536577](/cms_trial/assets/18b0a200-1309-4915-8336-f59155a769a4.png)

Parent-child relationships can be viewed in the Gantt module - task tree shows how tasks are nested.

![contentId-1918536577](/cms_trial/assets/6583a454-489b-4f1c-91a2-c7f323ca7c09.mov)

Solutions:

- Change the position of the parent
- Change the scheduling mode

  - of the child to ‘manual’ - automatic rules don’t apply. You can position tasks as you want.
  - of the child to ‘auto bottom-up’ - parent task period is modified by children
  - of a child to ‘auto basic’ - a task responds only to dependencies and non-working days. Period and position of the parent are ignored.
- change how tasks are nested in the tree

![contentId-1918536577](/cms_trial/assets/47247546-f050-427d-8d9d-84da37601231.mov)

#### **Locked parent**

The dates of this task depend on the dates of its parent, which is set to Locked scheduling mode.

When a task is in a ‘locked’ scheduling mode, its period cannot be changed (can’t be repositioned on a timeline, dates can’t be manually changed). A child in an ‘auto top-down' scheduling mode adjusts its period to fit under a parent.

![contentId-1918536577](/cms_trial/assets/3b7905f7-1870-4290-b3e1-ea5373fc038d.mov)

Solutions:

- Change the scheduling mode of the child task
- Change the period of the parent task (if parent is ‘locked', the parent scheduling mode must be changed to allow for changes of its period).
- change how tasks are nested in the tree.

#### **Locked task**

This task is set to Locked scheduling move, so its dates can’t be changed.

A task has a start/end date - start/end cannot be modified (the task can’t be moved on a timeline and dates can’t be manually changed).

A task doesn’t have a start/end date - start/end date can’t be entered.

![contentId-1918536577](/cms_trial/assets/fe7186fb-d15f-40bd-baaf-4759eb34847c.png)

Solution:

- change the task scheduling mode.

#### **Auto bottom-up task**

This task is set to auto bottom-up scheduling mode, so its dates depend on the dates of its subtasks.

The period of an auto bottom-up task is based on the periods of its children.

When children don’t have a start/end date, the parent task doesn’t have dates.

![contentId-1918536577](/cms_trial/assets/6ed2f7a1-b9e3-41e7-a0d3-c53bdd519c4e.mov)

Solution:

- change the parent scheduling mode
- change the dates of the child tasks.

### Dates adjusted by parent task

**Auto top-down**

The dates of this task depend on the dates of its parent, which is set to Auto top-down scheduling mode.

Parent task dates are changed. The child task adjusts its period to fit the parent.

![contentId-1918536577](/cms_trial/assets/03cb3f96-2368-414a-9004-ba30df645b5d.mov)

The child didn’t have dates. Once the child is placed on a timeline, it adjusts to fit the parent.

![contentId-1918536577](/cms_trial/assets/25801d30-cff9-40e3-a335-ee5a9fe03caf.mov)

**Locked parent**

The dates of this task depend on the dates of its parent, which is set to Locked scheduling mode.

![contentId-1918536577](/cms_trial/assets/280ea886-5000-4f21-89a2-2c0771a1fd6b.mov)

### Dates adjusted by subtasks

**Auto bottom-up task**

This task is set to the auto bottom-up scheduling mode, so its dates depend on the dates of its subtasks.

![image-20241008-073017.png](/cms_trial/assets/cb893551-8db4-4cb0-87f2-316c22db9e35.png)

See the video:

![2024-10-08_09-21-47.mp4](/cms_trial/assets/1a0113ce-960a-4b2b-b0c1-bc8c7488c1c9.mp4)

## Field mapping

### Date adjusted by time logged on task

Example:

The task duration is 4 days. The **End Date** field is mapped to the **Remaining Estimate + Time Spent** field. An assigned person logged 3 days on this task. The remaining estimate is 1 day now. A user changed the task duration to 2 days (either by resizing the task on the Gantt chart, changing the End Date field, or editing the Duration Working Days field).

BigPicture adjusts the task duration to the value of the time logged for the task.

The following message is displayed:

*Due to the mapping of the End Date field, the duration of this task cannot be shorter than the time logged on this task.*

## App access

### App level

BigPicture requires administrative rights to function properly. To start using the BigPicture Trello Power-Up, please ensure the Team’s Administrator has already launched it.

Solution:

- An admin of the organization must start the App (and use it - click something while the App is running).
- If the administrator who initially started the App lost their Admin rights, another admin must start the App again.
- This must be done by the admin of the **Trello team** (not the admin of the board!).

### Jira project level - access denied (missing App permissions)

This splash screen appears when a user tries to enter the App from a Jira Project context, but lacks permission to access it.

Make sure users have access to the App and Boxes as needed. Verify the [security settings](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297765911) of the App and Boxes.

#### No App access

Users must be added to BigPicture ([Administration > Security](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298287400)) if not granted access to the app.

![contentId-1918536577](/cms_trial/assets/251555ae-fae5-464a-8f25-52b99674ca51.png)

#### No Box access

Even if a matching Box exists, if a user doesn't have access to it (they haven't been added as Box users) they can't access it through a Jira project.

The app will try to suggest to a user to create a "perfect match" Box:

- the user either sees an option to create a new Box
- or a message informing them that they don't have permissions sufficient to create a Box

### No permissions to create a Matching Box

![contentId-1918536577](/cms_trial/assets/cff921ff-90cd-48d3-9c81-98ba34acdc66.png)

You can't create a Box, because of App security settings.

In order to create a Box you need to:

- have [access to the App](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298287400)
- at the [Root Box (home Box) level](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297669047), you must be a **sub-Box creator** or an **Admin.**

## License invalid

![image (10).png](/cms_trial/assets/b6e8a4e0-af2c-4616-bf47-88882430b2d4.png)

**Standard Atlassian licensing guidelines apply (**[**read more**](https://www.atlassian.com/licensing/purchase-licensing#licensing)**).**

We don't sell licenses directly. All purchases must be made through the Atlassian marketplace.

### BigPicture Enterprise

BigPicture Enterprise is **NOT** a stand-alone product (BigPicture required).

## BigPicture loading crashed

If you see the following screen, it means that the plugin failed to load:

![contentId-1918536577](/cms_trial/assets/425d9cdb-c5c6-4703-b973-d02d1b77cd80.png)

It might occur in the following few situations.

### No locks available

#### Cause

No file locks are available on the NFS file system. This problem will occur if your Jira runs on an NFS file system - this applies mainly to Jira Data Center.

The situation may occur:

- after performing a "Create Snapshot" operation,
- after starting the "Restore" process,
- after updating the application to a newer version.

#### **Diagnosis**

Verify if the following entry appears in the logs:

```text
============================================================================================================
NO LOCKS AVAILABLE, this error is usually caused by the NFS daemons not running or malfunctioning.
Try to restart and verify functionality of all NFS related daemons on your system, most importantly lockd.
```

You can also ensure this is the case by manually creating a lock on a file in a directory used by the plugin, e.g. */shared-data/sharedhome/export/softwareplant/bigpicture*. As a result of such action, the same error should appear as in our application logs i.e., "No locks available".

#### **Solution**

Restart and verify the functionality of all NFS-related daemons on your system, most importantly `lockd`. See the following page for further reference: <http://osr507doc.sco.com/en/NetAdminG/nfsC.daemons.html>

### Directory Access Denied

#### Cause

You will see this screen when directory access has been denied for Jira - this applies to Jira Server/Data Center.

The situation may occur:

- after performing a "Create Snapshot" operation,
- after starting the "Restore" process,
- after updating the application to a newer version.

#### **Diagnosis**

Verify if the following entry appears in the logs:

```text
============================================================================================================ 
ACCESS DENIED FOR DIRECTORY UNDER PATH: <directoryPath>.
The problem occurs because the directory might not be owned by user that Jira is run on the behalf of.
Check whether that particular user has 'write' access to <directoryPath>.
```

#### **Solution**

The given directory is not accessible to Jira. You should grant the Jira user access to this directory.  
If this is not enough, then try to grant access to these two directories in addition:

- */media/atl/<directory-path>/export*
- */media/atl/<directory-path>*

For Unix/Unix-like systems, use the command: '***chown <user that jira is run on the behalf of> <directoryPath>***'  
e.g. '***chown jira jira-data***'

If you are experiencing more complicated issues or having problems following the instructions, please contact our helpful support using the customer [portal](https://softwareplant.com/jira/servicedesk/customer/user/login?destination=portals)[.](mailto:support@bigpicture.on) Our team will be more than happy to assist.