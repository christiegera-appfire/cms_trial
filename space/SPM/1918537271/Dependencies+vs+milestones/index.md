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

"**End to start**" dependencies are adjusted to account for a milestone being a point in time (has a single date).

When a milestone is a target:

- ASAP - the milestone date has to be the same as the source end date
- non-ASAP - the milestone date has to be the same or later than the source end date

![contentId-1918537271](/cms_trial/assets/c9a80829-7e8e-49c6-966f-2aa4fc0da58a.png?version=1&modificationDate=1689671058822&cacheVersion=1&api=v2&width=900&height=214)![contentId-1918537271](/cms_trial/assets/c77763b9-f168-4d47-b886-46f3e5f613c6.png?version=1&modificationDate=1689670921197&cacheVersion=1&api=v2&width=900&height=179)

"**Start to end**" dependencies are adjusted to account for a milestone being a point in time (has a single date).

When a milestone is a target:

- ASAP - the milestone date has to be the same as the source start date
- non-ASAP - the milestone date has to be the same or later than the source start date

![contentId-1918537271](/cms_trial/assets/30fdb622-884c-4d61-980c-fed2e1699b59.png?version=1&modificationDate=1689671274708&cacheVersion=1&api=v2&width=900&height=232)![contentId-1918537271](/cms_trial/assets/23c2644b-ac82-40c3-a487-f22fe77cdcab.png?version=1&modificationDate=1689671179987&cacheVersion=1&api=v2&width=900&height=194)

"**End to end**" dependencies behave normally.

![contentId-1918537271](/cms_trial/assets/8ac4347f-0892-4ae8-beff-8b9235bd5c1e.png?version=1&modificationDate=1689671388366&cacheVersion=1&api=v2&width=900&height=220)

"**Start to start**" dependencies behave normally.

![contentId-1918537271](/cms_trial/assets/364fb17f-e063-4fa8-a6ba-e3e8407f7251.png?version=1&modificationDate=1689671450101&cacheVersion=1&api=v2&width=900&height=234)

### Dependencies from milestone to task

Dependencies from milestones to tasks behave normally (same as task → task dependencies).