# Edit membership

You can edit the **start date** of a membership entry using inline editing.

The end date is calculated automatically based on the next membership entry and can't be manually changed.

**Limitations**: you can't edit the value if the team was inherited. Changes have to be made in the box the team was created in.

![Scfreenshot of editing the start date of a team member's membership.](/cms_trial/assets/d65aff3d-c055-43cb-8f50-b09049a1ff74.png)

### Availability

Open the list of membership entries for a team member by clicking on their username:

![image-20240119-101935.png](/cms_trial/assets/82144067-5ef3-421a-8b89-48a5a0939234.png)

You can edit the availability value of a membership entry.

![image-20240119-101950.png](/cms_trial/assets/e8943dd3-5f1c-4fb8-bcfe-e3ddd183c93f.png)

**Limitations**: you can't edit the value if the team was inherited. Changes have to be made in the box the team was created in.

You can set availability for each team member. Availability impacts the capacity.

Capacity = working hours specified in the [Workload Plans](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297700790) - non-working days (in other words, how much total work can a resource do in a period of time. If Kate works 8h a day and there are 4 working days in a particular week, her capacity for that week is 32h).

Calculation of individual capacity takes into account team member's availability across all teams they're a part of (if Kate is assigned 50% availability in Agile team, her capacity as an individual for the 4 day week mentioned above is 16h. Team Agile gains 16h of capacity because of Kate during that week. In other words, half of Katie's capacity got allocated to team effort).

Once a user is archived, the related capacity and availability are set to 0.

Currently, there is no validation of availability across different teams - as a result, the total availability across different teams may exceed 100%.

Individual capacity in the Resources module is calculated dynamically and changes depending on the Team Filter you use.

See the example

For example, Albingo is assigned to the TeamiOS starting on the 7th of July for 50% of his time. Albingo is working full-time 8h/d as specified in the Workload Plan.

His daily capacity is 8h\*50% = 4h. The 4h capacity applies to both the individual and team, as Albingo is the only member of the iOS Team. Since there are no tasks assigned to Albingo, the Capacity on the 1st of June = Remaining capacity = 4h.

![contentId-1918833928](/cms_trial/assets/8a8de3ab-0af9-4aa6-8ea4-ffcffc07433b.png)

In the team-centric view, on the 1st of June the Capacity = Remaining capacity = 4h, as there are no tasks assigned to Albingo.

![contentId-1918833928](/cms_trial/assets/55d1a14b-079a-4cb3-adc0-d9e1df33a19e.png)