# Automatic assignment

## Based on task assignee

The task is automatically assigned to the team based on the task assignee.

#### Trigger

Change of the task assignee.

#### Conditions

- The "Tasks assigned to an individual are auto-assigned to their team" functionality is enabled.
- The task is in the scope of the box.
- The assignee is in only one team in a box.
- The assignee must be available in the team (has an active [membership](/cms_trial/space/SPM/1918537450/Manage+team+membership/) in a given task period).
- Recalculation of the team takes place only when the task assignee is changed in BigPicture or Jira.

#### Limitations

The automation is not run:

- If the assignee is in more than one team in a box.
- The task is in the sub-scope (sub-box such as Iteration) and the scope definition is different for each team (avoiding the endless loop of team assignment).

Recalculation is **NOT** triggered when:

- The team membership changes:

  - The assignee is moved to another team in the box.
  - The assignee is added to another team in the box.
  - The assignee is removed from another team in the box.
  - The assignee is removed from a team (to which the task is currently assigned).
- The task period changes (the assignee's membership is no longer in the task period).

#### Deleted team

When a team is deleted from a box, the task is placed in the 'unknown' team swimlane.