# Task synchronization with sub-boxes (timeboxes)

Keep in mind that if you want the task period to be adjusted to match the Box period, you have to adjust task scheduling settings (**Box configuration** > **Tasks** > **Scheduling** > **Set alignment on lower levels**). To learn more, go to [Task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/).

You can ensure that tasks are automatically planned for (assigned to) timeboxes (sub-boxes that don't have their own scope). Usually, those will be Iterations and Program Increments—they are used to organize tasks within a parent box.

The scope of sub-boxes will be automatically updated by synchronizing with a specified field.

The synchronization is bidirectional:

- planning a task for a specific box will update the synchronized field
- correspondingly, changing a field value will automatically assign a task to a timebox

### Step-by-Step Example

Let's look at a simplified example. We have a Box with multiple Iteration sub-boxes.

![contentId-1918405510](/cms_trial/assets/ff9704f1-443f-44a6-9bf5-cdbad56f6316.png)

In the Box configuration of the "Box scheduling" Box, we have to go to **Box configuration** > **Tasks** > **Scope definition** (the tab "Scheduling" is dedicated to Tasks, not sub-boxes). Below the scope settings, we can find our sub-box scheduling settings.

Let's select "Sprint" as the field we want to use for synchronization. Then, we should select the Jira board that contains our sprints.

![contentId-1918405510](/cms_trial/assets/f9b0e2e6-4f9c-458e-9549-dfcfc633b1c4.png)

Since no teams have been added to this box, the only item listed is "Unassigned." On the right, we select Sprint 1 to match our first Iteration.

![contentId-1918405510](/cms_trial/assets/95f6d2df-b4ce-409f-a8af-bd965827d12b.png)

When we zoom out, more Iterations become visible on the timeline. Once we are done, all we need to do is hit the "Save" button at the top right to confirm our changes.

![contentId-1918405510](/cms_trial/assets/1631c974-58fd-4fab-9a15-28469a7a2aae.png)

When we go to the **Board module**, we see that tasks have been successfully assigned to Iterations based on synchronization with a Jira Sprint field.

![contentId-1918405510](/cms_trial/assets/67d4e736-7379-4da5-afb4-1f8b82542500.png)

If we add a new Jira task using, for example, the **Gantt module** and set the value of the Sprint field to "Test Sprint 1" during the creation process, the task will automatically get planned for the Iteration.

![contentId-1918405510](/cms_trial/assets/a0647a7e-6a3c-41ad-99ac-7b72ce45f22b.png)![contentId-1918405510](/cms_trial/assets/d56e7956-d458-4022-b1d9-01f5db1ff05b.png)![contentId-1918405510](/cms_trial/assets/207e1d1e-8810-4936-b078-5f7113df5e8b.png)