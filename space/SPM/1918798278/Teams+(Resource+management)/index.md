# Teams (Resource management)

## Teams (Resources management) (old navigation)

## Global teams

You can group individual users into teams, which enables effort-based planning. The concept of teams is used mainly in the Resources, Gantt, and Board modules, but since the information about teams can be stored as a label or a custom field, it can also be displayed using the Gantt, Scope, or Risks module by adding it to the Column Views or Card View.

You can create global teams and assign them to multiple Boxes. Once created, you can easily convert them to Box teams that can not be reassigned.

![image-20240119-093348.png](/cms_trial/assets/68ef73b7-836b-45a6-9401-3e711854cb41.png)

### Team configuration

Your Teams are not created automatically unless you synchronize with Tempo or inherit the Team from upper-level Boxes. This means that you need to create Teams in the Root Box first:

The team configuration panel is located on the right.

![image-20240119-092805.png](/cms_trial/assets/579703f2-d391-4459-94e0-b7cac0a4c122.png)

#### Details tab

![contentId-1918798278](/cms_trial/assets/b24594af-8cdd-46d1-93f0-ad5bb5d90657.png)

#### Team name

The team name is used for identifying teams by the App's modules. It is displayed together with the Team code in the Resources, Board, and Roadmap modules to indicate the team's swimlane and in the Team picker's drop-down when configuring Box-level teams.

#### Team code and color

Team code is used for identifying teams by the App's modules and, when synchronized, also the Host and connected platforms. Depending on the [configuration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297962731), the Team code is stored as the following fields:

- Labels type
- Select list – single choice type
- --none-- (not synchronized)

You can use these fields in your JQL to create a Jira Board dedicated to a specific team or as Quick Filters.

#### Team board link

Link the team to its Jira Board to quickly switch between different views. Based on this link, the App can auto-configure the Sub-Box scope synchronization and create sprints on the selected Jira Agile Board.

#### Members tab

![contentId-1918798278](/cms_trial/assets/47f936a2-375d-4312-8694-d20645253569.png)

#### Add team members

Fill in the fields at the top and click the "+" button to add a team member.

![image-20240119-092839.png](/cms_trial/assets/585a6878-518a-482c-80ca-49466a903688.png)

#### Remove a team member

![contentId-1918798278](/cms_trial/assets/8c23fcea-b88c-4e23-8611-4f05eccd160d.png)

#### Membership period

Your resources can be shared across different teams in the same period of time or can be fully allocated to a single team. This can be set using memberships and the availability of the team members. The capacity of your resource will depend on the current membership.

#### Availability

Calculation of an individual resource's capacity takes into account the availability of the member across all Teams.

Availability impacts capacity based on Workload plans and the number of non-working days. Currently, there is no validation of the availability across different teams, which means that total availability across different teams may exceed 100% (a warning icon appears).

![image-20240119-092912.png](/cms_trial/assets/ee313fe5-eaa5-4846-8a48-b929342a6c2c.png)

An individual's capacity in the Resources module is calculated dynamically and will change depending on the applied Team filter.

#### Edit details of a team member

Click on a team member's name to select them:

![image-20240119-092926.png](/cms_trial/assets/e6f7dac3-8396-472c-a3e2-8737d3e8a999.png)

You see a list of entries:

![image-20240119-092939.png](/cms_trial/assets/a7b5b2ef-fb5e-467a-ae02-342e6c46147e.png)

Fill in the fields at the top and click the "+" button to add a new membership period.

Use the delete button to remove entries from the list.

#### Boxes involved tab

This tab contains a list of Boxes a team is assigned to:

![image-20240119-093006.png](/cms_trial/assets/fced9af8-5f32-4081-b041-f1bbaf4321d1.png)

### Synchronize with Tempo

For more information, visit the [Tempo integration](/cms_trial/space/SPM/1918504442/Tempo+integration/) page.

You can set automatic synchronization with Tempo and define items to synchronize:

- Individuals
- Workload plans
- Holiday plans
- Skills
- Teams

#### Remove teams synchronized with Tempo

The App allows you to remove teams that are synced with Tempo - you can remove teams from BigPicture that:

- No longer exist in Tempo
- When a synced team is no longer needed (If the item still exists in Tempo, it will be added again during the next sync.)

## Inherited team

Inherited teams are marked with an arrow next to the team name.

![Screenshot of the Teams module with an inherited team.](/cms_trial/assets/35a93cad-e639-4b43-950d-60fb9e47d6ba.png)

## **Global teams in timebox schedules**

The timebox schedule works only with global teams. Once connected, your current box teams will no longer work. Only global teams linked to the timebox schedule will be available. See more on the [Timebox schedule](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.

## Teams (Resources management) (new navigation)

## Global teams

You can group individual users into teams, which enables effort-based planning. The concept of teams is used mainly in the Resources, Gantt, and Board modules but since the information about teams can be stored as a label or a custom field, it can also be displayed using the Gantt, Scope, or Risks module by adding it to the Column Views or Card View.

You can create global teams and assign them to multiple Boxes. Once created, you can easily convert them to Box teams that can not be reassigned.

![teams-main.png](/cms_trial/assets/f51bff17-7e78-4d71-ae2a-d65565b2c9eb.png)

### Team configuration

Your Teams are not created automatically unless you synchronize with Tempo or inherit the Team from upper-level Boxes. This means that you need to create Teams in the Root Box first:

The team configuration panel is located on the right.

![teams-creation.png](/cms_trial/assets/6a5a37f7-b342-4b4a-acfb-fa5887c0fb31.png)

#### Details tab

![teams-details.png](/cms_trial/assets/7cd5e525-244e-415d-94d2-350b3e336fb0.png)

#### Team name

The team name is used for identifying teams by the App's modules. It is displayed together with the Team code in the Resources, Board, and Roadmap modules to indicate the team's swimlane and in the Team picker's drop-down when configuring Box-level teams.

#### Team code and color

Team code is used for identifying teams by the App's modules and, when synchronized, also the Host and connected platforms. Depending on the [configuration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297962731), the Team code is stored as the following fields:

- Labels type
- Select list – single choice type
- --none-- (not synchronized)

You can use these fields in your JQL to create a Jira Board dedicated to a specific team or as Quick Filters.

#### Team board link

Link the team to its Jira Board to quickly switch between different views. Based on this link, the App can auto-configure the Sub-Box scope synchronization and create sprints on the selected Jira Agile Board.

#### Members tab

![teams-members.png](/cms_trial/assets/cd93f128-1c28-4cb1-bf3f-e792b065194b.png)

#### Add team members

Fill in the fields at the top and click the "+" button to add a team member.

![team-members-adding.png](/cms_trial/assets/fc09b448-2da5-4cbb-8c65-9e77e1c93ef7.png)

#### Remove a team member

![delete-member.png](/cms_trial/assets/3ba2bfeb-fd97-4dfa-8b0d-2a79cddb18a7.png)

#### Membership period

Your resources can be shared across different teams in the same period of time or can be fully allocated to a single team. This can be set using memberships and the availability of the team members. The capacity of your resource will depend on the current membership.

#### Availability

Calculation of an individual resource's capacity takes into account the availability of the member across all Teams.

Availability impacts capacity based on Workload plans and the number of non-working days. Currently, there is no validation of the availability across different teams, which means that total availability across different teams may exceed 100% (a warning icon appears).

![member-warning.png](/cms_trial/assets/6ac94711-f671-42b4-9489-b0dc9b6c779b.png)

An individual's capacity in the Resources module is calculated dynamically and will change depending on the applied Team filter.

#### Edit details of a team member

Click on a team member's name to select them:

You see a list of entries:

![member-memberships.png](/cms_trial/assets/e15c2853-1135-4fc2-bb18-f45083e16031.png)

Fill in the fields at the top and click the "+" button to add a new membership period.

Use the delete button to remove entries from the list.

#### Boxes involved tab

This tab contains a list of Boxes a team is assigned to:

![boxes-involved.png](/cms_trial/assets/9556d065-d532-44cf-9834-f787a6f66ae6.png)

### Synchronize with Tempo

For more information, visit the [Tempo integration](/cms_trial/space/SPM/1918504442/Tempo+integration/) page.

You can set automatic synchronization with Tempo and define items to synchronize:

- Individuals
- Workload plans
- Holiday plans
- Skills
- Teams

#### Remove teams synchronized with Tempo

The App allows you to remove teams that are synced with Tempo - you can remove teams from BigPicture that:

- No longer exist in Tempo
- When a synced team is no longer needed (If the item still exists in Tempo, it will be added again during the next sync.)

## Inherited team

Inherited teams are marked with an arrow next to the team name.

![inherited-team.png](/cms_trial/assets/fef9ba45-4355-4b56-a318-b8c723f2f219.png)

## **Global teams in timebox schedules**

The timebox schedule works only with global teams. Once connected, your current box teams will no longer work. Only global teams linked to the timebox schedule will be available. See more on the [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.