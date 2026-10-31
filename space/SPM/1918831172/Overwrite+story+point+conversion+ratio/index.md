# Overwrite story point conversion ratio

## Preconditions

If the [Configurable Story Point conversion ratio](/cms_trial/space/SPM/1918407288/Resource-related+settings/) feature is enabled for a box type, you can overwrite the default **Story Point conversion ratio** within a given box.

Changing the configuration might turn off (hide) settings or features in the box configuration and within different modules.

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box configuration | Only a user with a minimum Box Admin security role can access and manage the box configuration.  Go to **box configuration** > **Resources** > **Story points**. Story points settings on the box configuration page. | For a particular box, you can enable and configure:   - Story point conversion ratio |

## Story point conversion ratio

When enabled, a user can overwrite the default **Story point conversion ratio** within a given box.

| **Configurable story point conversion ratio** | **Description** | **Affects** |
| --- | --- | --- |
| OFF | 1 story point = 1d for all boxes of a given type | All boxes of a given type:   - Existing - New |
| ON | Story point ratio can be overwritten:   - For individual boxes (of a given type) - In their box configuration |

## Overwrite the predefined ratio

The capacity derived from the workload, holiday, and absences can be converted from time units into Story points. This way, you can calculate the default capacity values of your teams and team members using story points.

To overwrite the predefined ratio:

1. Go to **box configuration > Resources > Story points**.
2. Enter the value.
3. Click **Save** to finish the process

![Screenshot of the Story point conversion ratio section in the box configuration.](/cms_trial/assets/2f18d8a2-f8df-48f0-868e-fa871b13523a.png)

### Conversion set to "0"

The conversion set to 0 can be useful in connection with the velocity report.

## Story points - Impact on resource capacity

Switch to the **Story Points** mode to convert the capacity of each resource presented on the resource grid into story points using the defined velocity. Using this view, you can display the capacity and committed story points at an individual and team level.

![Screenshot of switching to the Story Points effort mode in the Resources module.](/cms_trial/assets/c5cb512c-67cd-4175-a510-d80fd54473e1.png)

## Story points - Impact on team capacity

The converted capacity expressed in story points will become the default capacity calculated by the **Board module**. The capacity can be overwritten using capacity planning but it will not update related calendars.

For example, Iteration 1.1 has a duration of 10 days, and the ratio is set to 4h=1SP (1d=2SP). A team member's individual capacity is 10d x 2 SP = 20SP.

![Screenshot of the team's capacity planning in the Board module.](/cms_trial/assets/ce9d5fe4-4ee5-4ddb-88eb-ebf3e8988c48.png)