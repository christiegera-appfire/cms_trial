# Skill widget on Jira work item page

The Skill widget lets you assign skills (project roles) to the task directly on the Jira issue page.

![A screenshot of the Jira issue page featuring Skill widget.](/cms_trial/assets/75f47422-2270-47ff-97a8-09db8c8dd0bc.png)

## Add and remove skills

To add or remove a skill from a task, click the **Required Skills** box. A drop-down list with all the defined skills will appear. Select the skill from the list to add it. To remove a skill, click the cross next to the skill in the Required Skills box.

![skill-widget-add-remove-skills.png](/cms_trial/assets/a7ae3d8b-a213-4afd-a0ba-ba37d1b3264c.png)

To define new skills, go to the **Administration** > **Resources** > **Individuals** page (requires the App Administrator security role).

## Find the Perfect Match

You can use the Skill widget to find the best matching assignee for your task.

1. Add the required skill (or skills) to the task.
2. Click the **Find the Perfect Match** option.
3. Select the assignee from the list.

![A screenshot featuring the Skill widget. Below the Required Skills box, the Find the Perfect Match option appears.](/cms_trial/assets/898cbd52-a599-4912-8539-ca5f83ddea83.png)

The widget can suggest up to five potential assignees and rank them by relevance: the first is the best match, the second is the second best, and so on.

With this feature, you can assign tasks to both individuals and teams. Once you select the assignee, you can always reassign a task to another individual or team.

The Find the Perfect Match feature uses linear regression (a statistical modeling method) to determine the best matches. Our statistical algorithm takes into consideration the following criteria:

- Skills needed to complete the task.
- Skills assigned to the individuals or team members.
- The Remaining capacity of the individuals or teams, which is the result of the effort mode set in the Resources module (Original estimate, Remaining estimate, or Story Points mode).

Skills are the highest weighting factor (about 80%) in finding the best matches, followed by the Remaining capacity (20%).

If you don’t have skills added to your resources, the Remaining capacity will be the only factor considered.