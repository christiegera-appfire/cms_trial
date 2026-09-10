# Find the perfect match

## Find the perfect match (old navigation)

Working with numerous tasks and large teams can be challenging, but BigPicture can help you with assigning tasks and propose the best-suited assignee based on the following:

- Resource's (individual or team) skillset - skills weigh most in the algorithm, approx.—70%.
- Remaining capacity -  remaining capacity weighs the remaining 30%.

Finding the **perfect match** also works when a user is not assigned to any team. In such a case, the availability is assumed to be 100%.

For best results, define the required skills to complete a task on the Jira issue detail page.

See the video on how the feature works.

## Find the perfect match

To use the **Find the perfect match** feature:

1. Go to the Resources module.
2. Click the task that you want to assign.
3. A dialog with task details appears. When you enable the skill panel, the **Required skill** section appears in the dialog.

   ![find-perfect-match.png](/cms_trial/assets/6684fd1b-aed8-4ba4-998e-e0b75642a5b8.png)
4. Click the icon▢next to the Individual. BigPicture will propose the perfect match.

   ![find-perfect-match-2.png](/cms_trial/assets/906ee5f7-a1c1-4b9d-bac3-3e30fae27c0d.png)

Tasks assigned to both individuals and teams that the individual is not a part of are marked in yellow, and you can see a warning informing you about the steps to be performed.

![find-perfect-match-3.png](/cms_trial/assets/4656ef8d-b6f3-409e-a9aa-4c7084ab4ce9.png)

Inactive users **are NOT** visible in the find perfect match results. They are excluded by default.

You can also find the perfect match by using the [skill widget](/cms_trial/space/SPM/1918701583/Skill+widget/), which you can find on the issue details page just below the **People** section.

![Screenshot of the Jira issue page with the BigPicture - Skills section.](/cms_trial/assets/9be49866-0720-4078-b1c5-68b6f85c7655.png)

## How the mechanism works

BigPicture propose up to five matching assignees and sort them by relevance. The first on the list is the best match, the second is the second-best, and so on.

- Resources matching is cut off after the fifth-best one (linear regression, statistical modeling, is used to determine the list of five).
- You can assign both individuals and teams using this feature.
- The five best assignees are proposed based on:

  - skills required to complete a task
  - skills that an individual or team members have
  - The remaining capacity of resources – individuals or teams. The remaining capacity is calculated depending on the mode selected in the Resources module, namely **original estimate, remaining estimate, or story points.**
- Skills account for the most in the algorithm (approximately 70%), but the remaining capacity is important too (30%).
- If you don’t manage skills in Jira, the remaining capacity is the only contributing factor.
- The remaining capacity can be expressed as a time period or story points.
- You can always reassign a task to another individual or team.

## Find the perfect match (new navigation)

Working with numerous tasks and large teams can be challenging, but BigPicture can help you with assigning tasks and propose the best-suited assignee based on the following:

- Resource's (individual or team) skillset - skills weigh most in the algorithm, approx.—70%.
- Remaining capacity -  remaining capacity weighs the remaining 30%.

Finding the **perfect match** also works when a user is not assigned to any team. In such a case, the availability is assumed to be 100%.

For best results, define the required skills to complete a task on the Jira issue detail page.

See the video on how the feature works.

## Find the perfect match

To use the **Find the perfect match** feature:

1. Go to the Resources module.
2. Click the task that you want to assign.
3. A dialog with task details appears. When you enable the skill panel, the **Required skill** section appears in the dialog.

   ![find-perfect-match.png](/cms_trial/assets/6684fd1b-aed8-4ba4-998e-e0b75642a5b8.png)
4. Click the icon▢next to the Individual. BigPicture will propose the perfect match.

   ![find-perfect-match-2.png](/cms_trial/assets/906ee5f7-a1c1-4b9d-bac3-3e30fae27c0d.png)

Tasks assigned to both individuals and teams that the individual is not a part of are marked in yellow, and you can see a warning informing you about the steps to be performed.

![find-perfect-match-3.png](/cms_trial/assets/4656ef8d-b6f3-409e-a9aa-4c7084ab4ce9.png)

Inactive users **are NOT** visible in the find perfect match results. They are excluded by default.

You can also find the perfect match by using the [skill widget](/cms_trial/space/SPM/1918701583/Skill+widget/), which you can find on the issue details page just below the **People** section.

![Screenshot of the Jira issue page with the BigPicture - Skills section.](/cms_trial/assets/9be49866-0720-4078-b1c5-68b6f85c7655.png)

## How the mechanism works

BigPicture propose up to five matching assignees and sort them by relevance. The first on the list is the best match, the second is the second-best, and so on.

- Resources matching is cut off after the fifth-best one (linear regression, statistical modeling, is used to determine the list of five).
- You can assign both individuals and teams using this feature.
- The five best assignees are proposed based on:

  - skills required to complete a task
  - skills that an individual or team members have
  - The remaining capacity of resources – individuals or teams. The remaining capacity is calculated depending on the mode selected in the Resources module, namely **original estimate, remaining estimate, or story points.**
- Skills account for the most in the algorithm (approximately 70%), but the remaining capacity is important too (30%).
- If you don’t manage skills in Jira, the remaining capacity is the only contributing factor.
- The remaining capacity can be expressed as a time period or story points.
- You can always reassign a task to another individual or team.