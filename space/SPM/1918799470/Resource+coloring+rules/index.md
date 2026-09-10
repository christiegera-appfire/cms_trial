# Resource coloring rules

Set the colors that will appear when the % threshold for resource workload versus capacity is exceeded.

![image-20250325-143345.png](/cms_trial/assets/abbd5844-324d-4438-b57e-e8198b7611e8.png)

## Secrutiy and access

Only a user with the App Admin security role can access and manage the box type configuration.

Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Resources** > **Coloring rules**.

### Default coloring rules

The table presents coloring rules for the new and old views of the Resources module.

| **Resources module view** | **Description** |
| --- | --- |
| New Resources module view | In the new Resources module view, new coloring rules are applied to:   - Individuals, projects, and skills:    - Green - utilization under 100%   - Red - utilization is above 100% - Teams:    - Green - 0% to 80% utilization   - Yellow - 80 to 101% utilization   - Red - 101% or higher utilization |
| Old Resources module view | The following coloring rules apply in the old Resources module view.  Out of the box, when the workload is:   - Less than 75% of the capacity, the bar will change to green color (under-allocation). - Between 75% and 100% of the capacity, the bar will change to an orange color (moderate allocation). - Over 100% of the capacity, the bar will change to red color (overallocation). |

### Custom settings

Custom settings are created per box type. Make sure that all the box types you use have been set up correctly. Coloring rules are automatically applied to all boxes of a given type.

You can define custom coloring rules for all scope types - own-scope, sub-scope, and none-scope boxes.

To define the levels and colors of the grid in the Resources module:

1. Go to **Administration** > **Box types** > **click on a selected box type** > **Resources** > **Coloring rules.**

![Screenshot of the Coloring rules page in the box type configuration.](/cms_trial/assets/177f1ccc-657b-488a-954b-525b4ba94168.png)

#### Manage coloring rules

The beginning of a range automatically becomes the end of the previous range. Click the **Edit** icon to make changes. Only the beginning value of a range can be edited.

![Screenshot of editing coloring rules in the box type configuration.](/cms_trial/assets/4f483061-719f-4a77-9ecf-3c325be665c6.png)

#### Outcome - threshold values

The end value of a range doesn't belong to it (when it is also the start of another range).

**Example**: When the value is 75%, the assigned color is yellow.

![Screenshot of the edge value in the configuration of coloring rules for a box type.](/cms_trial/assets/68c1cea8-736f-4cfc-85db-f385ba580f48.png)

See the table for more information.

| **Range** | **Outcome** |
| --- | --- |
| image-20241205-094718.png | Values from 0 to <50 are green:   - 0 included - 50 **not** included (<50) |
| Values from 50 to <75  are yellow:   - 50 included - 75 **not** included (<75) |
| Values from 75 to <100 are orange:   - 75 included - 100 **not**included (<100) |
| Values 100 and above are red:   - 100 included |

### Limitations

- There always must be at least two rows left. It is impossible to delete all existing rows.
- The beginning of the first range is always "0". The end of the last range is always infinity.