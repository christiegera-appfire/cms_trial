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

Image — asset pipeline pending  
Individuals, projects, skills - utilization coloring.png

**Example**: if a person has been assigned 7.8h of workload and their capacity is 8h, the grid cell is green

Image — asset pipeline pending  
image-20240819-084728.png

### Teams

- **green** - 0% to 80% utilization
- **yellow** - 80 to 101% utilization
- **red** - 101% or higher utilization

Image — asset pipeline pending  
Teams - utilization coloring.png

**Example**:

Image — asset pipeline pending  
image-20240819-085900.png

## Grouping

When [grouping](/cms_trial/space/SPM/1918830289/Group+tasks/) is enabled, the coloring rules for the Teams and Individual swimlanes are applied.