# Dependencies vs milestones

## Dependencies vs milestones

Dependencies are adjusted to account for a milestone being a point in time (Start date and End date on the same day). Milestones don't artificially make the path between linked tasks longer.

### Dependencies leading to milestones

When a milestone is a target of a dependency:

| **Task to milestone OR**  **Milestone to milestone** | **non-ASAP** | **ASAP** |
| --- | --- | --- |
| End → start | **Milestone date >= Task End Date** | **Milestone date = Task End Date** |
| End → end | regular dependency behavior | regular dependency behavior |
| Start → end | **Milestone date <= Task Start Date** | **Milestone date = Task Start Date** |
| Start → start | regular dependency behavior | regular dependency behavior |

**End to start** dependencies are adjusted to account for a milestone being a point in time (milestones have only one date).

When a milestone is a target:

- ASAP - the milestone date has to be the same as the source end date
- non-ASAP - the milestone date has to be the same or later than the source end date

![contentId-1918537271](/cms_trial/assets/3d0ad36b-951c-4735-a2d9-b18677624913.png)![contentId-1918537271](/cms_trial/assets/aa6b2698-e06e-4f9b-88b2-79da05c7df9b.png)

**Start to end** dependencies are adjusted to account for a milestone being a point in time (milestones have only one date).

When a milestone is a target:

- ASAP - the milestone date has to be the same as the source start date
- non-ASAP - the milestone date has to be the same or later than the source start date

![contentId-1918537271](/cms_trial/assets/ba32b572-73dd-4cc6-9ebd-351d02d2984f.png)![contentId-1918537271](/cms_trial/assets/9cb47e92-d7e3-4f02-8403-dd521057af87.png)

**End to end** dependencies behave normally.

![contentId-1918537271](/cms_trial/assets/51346cb6-35ae-4bf0-9fef-4d30ef6860d3.png)

**Start to start** dependencies behave normally.

![contentId-1918537271](/cms_trial/assets/af4943c3-f49d-4d7c-afe5-ae47bc755098.png)

### Dependencies from milestone to task

Dependencies from milestones to tasks behave normally (same as task → task dependencies).