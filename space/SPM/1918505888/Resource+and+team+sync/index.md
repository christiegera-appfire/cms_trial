# Resource and team sync

## How does resource synchronization work?

Which Resource attributes are synchronized with Tempo? When synchronizing Resources, BigPicture synchronizes Workload and Holiday Plans. Regarding other attributes (name, surname, avatar, etc.), those are being pulled directly from Jira, as both BigPicture and Tempo are Jira plugins and use the same pool of information.

![image-20240122-085327.png](/cms_trial/assets/3e663f62-4148-4fff-9a3f-aa5395592e57.png)

### Resource synchronization rules

Rules that apply to Resource synchronization are a bit different from the rules of Workload and Holiday Plans Synchronization. Still, the differences are subtle since, as we’ve already mentioned, both plugins use Resource data, which is predefined in the user base in Jira, and both pool the same data. This means that for both Tempo and BigPicture we are capable of finding the Jira user which represents the same Resource.   
Below is a table that summarizes and describes the rules of Resource synchronization. Those that differ in Workload and Holiday Plan synchronization from Resource synchronization are marked with a blue color.

It is worth mentioning that as Resources are dependent on W&H Plans, the BigPicture performs the implicit synchronization of Workload and Holiday Plans during a Resource synchronization.

| **Action performed in Tempo** | **What will happen with the** **data in BigPicture** **during the synchronization?** |
| --- | --- |
| Adding a Resource | - If in BigPicture the Resource already exists for the same user in Jira, the Resource will become synchronized, and its status will become synchronized with its counterpart in Tempo, meaning the Resource will be assigned to the Workload and Holiday Plan which was predefined and assigned to in Tempo plugin. - If in BigPicture the Resource does not exist for the same Jira user, then with data pulled from Tempo, a new external synchronized Resource will be created. |
| Resource Modification | - If the corresponding Resource is synchronized, then changes will be synchronized. - If the corresponding Resource is overwritten, then changes will be ignored. |
| Deleting Resource | - The corresponding Resource changes its status to 'native’ (regardless if it was synchronized or overwritten) |

| **Action performed in BigPicture** | **What will happen with** **the external Resource** **(coming from Tempo)?** |
| --- | --- |
| Adding a new Resource | - Nothing will happen with the external Resource. It will be added as a native one. |
| Adding an external Resource | - This operation cannot be performed |
| Modifying a native Resource | - Nothing will happen to external Resources. It will be modified and will still hold a ‚native’ status. |
| Modifying an external Resource | - If the Resource is synchronized, then changes will be applied, and the Resource will change its status to ‚overwritten’. - If the Resource is already ‚overwritten’ then changes will be applied without a status change.   Warning: It is possible to switch ‚overwritten’ Resource back to its ‚synchronized’ state by clicking the ‚Resynchronize with Tempo’ button in the detailed view of that specific Resource. |
| Deleting a native Resource | - This operation cannot be performed |
| Deleting an external Resource | - This operation cannot be performed |

### Questions and answers

#### If I decide to overwrite a Workload/Holiday Plan, will that automatically overwrite Resources linked to that Workload/Holiday Plan?

You are probably wondering how would BigPicture act in a case when:

1. You’ve synchronized Workload Plan, Holiday Plans, and Resources with Tempo which creates dependency in which in BigPicture you have synchronized Resources that are assigned to synchronized Workload and Holiday Plans.
2. You’ve modified in BigPicture one of the synchronized Workload Plans (or Holiday Plans) which made it become "overwritten".

#### Will that make Resources (linked to it)‚ overwritten’ too?

The answer is: "No." Changing the status of W/H Plans from synchronized to overwritten will not affect the Resources assigned to them. Then, It is possible to have a synchronized Resource assigned to an overwritten Workload / Holiday Plan.

#### Which resources will be synchronized?

Only resources with active data in Tempo—such as Team, Workload, or Holiday Plan assignments—will be synchronized. Users who appear on the Tempo **Manage Staff** page and lack this information are standard Jira users with no Tempo data available for synchronization with BigPicture.

## How does the team synchronization work?

Team names are used. The following Team Tempo attributes are synced:

- Team Name
- Team Summary
- Team Members who are Jira users (including Team Members added via Jira groups). A Team Member is synchronized with all its Memberships, including:

  - Joining Date
  - Leaving Date
  - Skill
  - Availability

The following team Tempo attributes are **NOT** synchronized:

- Team Mission Team Lead (a user who is the team leader)
- Team Program (Program in Tempo is a group of Teams; each Team Tempo can belong to a maximum of 1 such group)
- Team Members who are not Jira users (Tempo allows you to add such "virtual" Members)
- Permissions Links to Boards and Projects

During Team Synchronization, all Skills with Tempo are also synchronized, and missing Resources are also created (as NATIVE).