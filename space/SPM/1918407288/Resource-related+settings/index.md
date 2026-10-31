# Resource-related settings

In this section, you can preconfigure the default resource settings of a given box type.

These include the following:

- Team allocation
- Team inheritance
- Configurable story point conversion ratio

Whenever you add a new box, you can select a box type - the default box type settings are applied to a newly created box.

Changing the configuration might turn off (hide) settings or features in the box configuration and within different modules.

## Security and access

Only users with the App admin security role can manage box types and access Administration.

To access this page:

1. Click the **wrench** **icon** at the top right and select**Box types** from the drop-down list.
2. Click a box type name to select it and open its settings.
3. On the left, go to **Resources** > **Basics** tab.

![contentId-1918407288](/cms_trial/assets/c681fbca-aeeb-4e6c-b6dd-5ba58d3c030a.png)

## Manually allocated teams

When enabled, a user can manually add new teams or assign existing teams within a box.

| **Manually allocated teams** | **Description** | **Affects** |
| --- | --- | --- |
| OFF | Teams cannot be added to a box. | All boxes of a given type:   - Existing - New |
| ON | Teams can be added to a box. |

## Auto-inherited upper-level teams

When enabled, all teams allocated to upper-level boxes are also automatically allocated to a box.

| **Auto-inherited upper-level teams** | **Description** | **Affects** |
| --- | --- | --- |
| OFF | Newly created Boxes of a given type do **NOT** automatically inherit teams from the upper level. | - Applies during box creation - Existing boxes are not affected by toggle changes   If the option was previously active, all teams which were automatically allocated to the Boxes of that type remain unchanged, but now they can be manually "Unassigned" from a lower level. This way, information about teams (capacity planning, objectives, etc) is still available in Boxes that have used it. |
| ON | Boxes inherit teams from upper-levels. |

## Configurable story point conversion ratio

When enabled, a user can overwrite the default [Story point conversion ratio](/cms_trial/space/SPM/1918831172/Overwrite+story+point+conversion+ratio/) within a given box.

| **Configurable story point conversion ratio** | **Description** | **Affects** |
| --- | --- | --- |
| OFF | 1 story point = 1d for all boxes of a given type | All boxes of a given type:   - Existing - New |
| ON | Story point ratio can be overwritten:   - For individual boxes (of a given type) - In their box configuration |