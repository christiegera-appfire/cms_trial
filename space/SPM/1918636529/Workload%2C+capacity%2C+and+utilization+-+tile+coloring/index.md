# Workload, capacity, and utilization - tile coloring

## Coloring

The tile colors indicate whether resources are over-allocated or under-allocated. The new view in the Resources module introduces updated coloring rules, where each tile color corresponds to a specific level of resource utilization.

### Utilization calculation

[Unmapped macro: mathblock — no content to fall back on]

- workload based on task information:

  - original estimate
  - story points
- capacity (one of the two kinds of capacity is used for the calculation)

  - team-based capacity- capacity based on individual memberships in teams
  - Total capacity - capacity based on workload plans, holiday plans, and absences

### Individuals, projects, and skills

- **green** - utilization under 100%
- **red** - utilization is above 100%

**Note**: yellow is **NOT** used to indicate approaching over-allocation.

![Individuals, projects, skills - utilization coloring.png](/cms_trial/assets/2524a8c2-ea84-4a6a-81ed-6132c06244a8.png)

**Example**: if a person has been assigned 7.8h of workload and their capacity is 8h, the grid cell is green

![image-20240819-084728.png](/cms_trial/assets/fef6d0df-0d1d-4235-aafc-02e8ab70c812.png)

### Teams

- **green** - 0% to 80% utilization
- **yellow** - 80 to 101% utilization
- **red** - 101% or higher utilization

![Teams - utilization coloring.png](/cms_trial/assets/3dbc0436-a68b-49fd-9446-4f2b55d3c52d.png)

**Example**:

![image-20240819-085900.png](/cms_trial/assets/7276ef10-06da-4370-9c12-2214ce9ee5b0.png)

## Grouping

When [grouping](/cms_trial/space/SPM/1918830289/Group+tasks/) is enabled, the coloring rules for the Teams and Individual swimlanes are applied.