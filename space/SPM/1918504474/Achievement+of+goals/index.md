# Achievement of goals

## Achievement of goals (old navigation)

Click to expand the guide

## Track Achievements

The **Achievement** feature helps you track the progress of your goals and calculate the planned vs. actual business value metric.

The Achievement metric is calculated for each timebox, based on one of the following:

- goal Status
- goal Business Value

The Business value should not be confused with any other measures, such as the associated effort or total story points related to a goal. The field values range from 0 to 10.

The Planned Business Value (PBV) of new goals scored during the planning meeting can be later compared with the Actual Business Value (ABV), once data is available. This is usually done during the 'Inspect and adapt' actions.

![count-by-business-value.png](/cms_trial/assets/b783e9b5-13b2-46e7-bc9f-85f47b6b4887.png)

## Configuration

App admins can enable the PBV vs ABV ratio calculation in **App Administration** > **Box types**  > **select the Box type to edit**  > **goals** > **Business Value**.

![business-value-toggles.png](/cms_trial/assets/76e2cfac-23c1-4e4d-a68c-55e09dc1b321.png)

## Achievement progress

### Achievement: None

![achievement-none.png](/cms_trial/assets/470612d1-1f8f-4c94-8af9-813c2167a900.png)

Achievement progress is not calculated.

![achievement-progress.png](/cms_trial/assets/e4a6fd59-3d24-462d-8fe3-498215d09a25.png)

### Achievement: Count by status

![count-by-status.png](/cms_trial/assets/cd2fad63-f2ef-4ad3-a555-3bcd6bfde7e3.png)

The calculation is executed per swimlane and per Box to which goals have been assigned:

![achievement-progress.png](/cms_trial/assets/e4a6fd59-3d24-462d-8fe3-498215d09a25.png)

The calculation is based on the number of goals achieved. The progress state of individual "Open" goals isn't taken into account—the goal either has been achieved or it hasn't.

#### The Formula

**Formula:**

Achievement progress = Number of regular Completed goals / Total number of regular goals (Open + Failed + Completed)

![achievement-progress-2.png](/cms_trial/assets/2014ce1e-c8ec-43f5-b9d5-b08dc0f312e9.png)

Abandoned goals are ignored in the calculation:

![achievement-33-percent.png](/cms_trial/assets/2e2e1f3a-f17e-4aef-b477-4e3cfd3edc96.png)

Uncommitted goals are ignored in the calculation:

![achievement-fifty-percent.png](/cms_trial/assets/089e9251-18d7-4c2e-a079-3d582dfeeb4a.png)

#### Swimlanes filter impacts the calculation

Only visible swimlanes are taken into account during the calculation.

[Unmapped block: nestedExpand]

### Achievement: Count by Business Value

![contentId-1918504474](/cms_trial/assets/87497dd0-b87b-43fc-8295-1ba905569bc4.png)

You can compare the  Planned and Actual business values, in which case the Uncommitted Team goals will not be included in the Achievement calculation. The App can calculate the ratio, which will be displayed in the Timebox header, thus creating a Team Performance report.

The results can be further rolled up and used to create a program predictability measure.

#### Edit business value

Keep in mind that the status of the Box determines the possibility to set the Business Value:

| **Timebox status** | **Actual BV** | **Planned BV** |
| --- | --- | --- |
| Not started | not editable | editable |
| In progress | editable | editable |
| Closed | not editable | not editable |

The [business value must be enabled](/cms_trial/space/SPM/1918701325/Objectives+-+Business+value+and+associated+work/) for a box type. Otherwise, PBV and ABV fields will be hidden.

PBV - Planned Business Value

ABV - Achieved Business Value

#### Calculating the Planned vs Actual Business Value

The PBVs of uncommitted goals are not included in the calculation. For example, the total ABV is 27 points, and the sum of PBV for the regular goals is 18. The ratio is 27/18\*100=150%

#### The Formula

**Formula****:**

**Total ABV / Total PBV \* 100**

All Completed, Open, Failed, and Abandoned goals are accounted for in the calculation.

The calculation is executed separately for each swimlane and for the entire Box:

- total ABV of all Box goals / total PBV of all Box goals
- total ABV of swimlane goals in a Box / total PBV of swimlane goals in a Box

5/5\*100 = 100%

![contentId-1918504474](/cms_trial/assets/3b1aae5a-87be-42a2-adae-e1c41f5feef6.png)

5/10\*100 = 50%

![contentId-1918504474](/cms_trial/assets/78563d60-6169-484d-b5ae-f2c2e4003c4e.png)

18/15\*100 = 120%

![contentId-1918504474](/cms_trial/assets/7affaf1e-3f6d-478b-a053-7d31eb2790c0.png)

5/4\*100 =125%

![contentId-1918504474](/cms_trial/assets/d9dd3db5-35be-4808-9b88-df16be19e155.png)

**PBV of uncommitted goals is taken into account (as an extra factor), and** **the ABV is counted****:**

16/12\*100 = 133%

![contentId-1918504474](/cms_trial/assets/6f75568c-1168-4be2-a5fa-df5d0eee0632.png)

**If the PBV total of a swimlane is 0, the swimlane's achievement calculation is 0%:**

![contentId-1918504474](/cms_trial/assets/ae95563d-a35c-48b1-bc87-6b09bfa1d8b1.png)

But the box calculation is still executed if normally (total ABV of all box goals / total PBV of all box goals)

27/10\*100 = 270%

![contentId-1918504474](/cms_trial/assets/9d220922-bf0d-4273-a67a-08fe40c7380d.png)

**If the box PBV is 0, the total for the Box and all swimlanes is 0%, regardless of ABV values:**

![image-20240925-115317.png](/cms_trial/assets/86ab5841-608c-462b-a3c9-6cbd7387875a.png)

#### Swimlanes filter impacts the calculation

Only visible swimlanes are taken into account during the calculation.

![contentId-1918504474](/cms_trial/assets/0ecdc5a7-5ff8-4b03-8036-c09f548821c3.png)

Collapsed swimlanes are still taken into account during the calculation as long as they are visible:

![image-20240925-115420.png](/cms_trial/assets/f8ac8d5c-c9e4-410d-8eb3-e474a7a4ecfc.png)

Hidden swimlanes are ignored in the calculation:

![image-20240925-115455.png](/cms_trial/assets/5be6c3b2-ba2e-466f-867b-98a763f127f8.png)

## Create reports

The goals module includes status-based reports on your goals. You can use bars or pie charts to show the actual progress for each box and team.

The reports can be generated at two levels, the upper and lower, and provide two separate sets of charts. For example, in the case of a SAFe ART, the upper level would be the Program Increment, and the lower one would be the Iteration level.

Goals assigned to sub-boxes do not roll up to the upper-level box.

![Icon leading to Reports highlighted](/cms_trial/assets/0a67369f-165d-40e9-821d-27c21254f641.png)

### Chart types

There are two chart types available:

#### Bar charts

![Reports option set to Bar](/cms_trial/assets/44ed36bf-319f-44d0-afc4-08bdf5d541c4.png)

Hover over a bar to display the number of goals in each column.

![Reports presented as bars](/cms_trial/assets/15a5fca8-b1db-4702-92dd-b4dc9752e194.png)

#### Pie charts

Hover over the charts to display the exact distribution of the goal statuses. You can also click on the legend to exclude categories.

![Report presented as pie chart](/cms_trial/assets/d78acbed-8b1c-4041-88b4-ba40b90cd086.png)

## Achievement of goals (new navigation)

Click to expand the guide

## Track achievements

The **Achievement** feature helps you track the progress of your goals and calculate the planned vs. actual business value metric.

The Achievement metric is calculated for each timebox, based on one of the following:

- Goal status
- Goal business value

The business value should not be confused with any other measures, such as the associated effort or total story points related to a goal. The field values range from 0 to 10.

The Planned Business Value (PBV) of new goals scored during the planning meeting can be later compared with the Actual Business Value (ABV), once data is available. This is usually done during the 'Inspect and adapt' actions.

![Screenshot of the Achievement option in the View menu of the Goals module.](/cms_trial/assets/1b273fe1-ae71-4fa9-bc40-dc983404bb97.png)

## Configuration

App admins can enable the PBV vs ABV ratio calculation in **App Administration** > **Box types**  > **select the Box type to edit**  > **Goals** > **Basics**.

![Screenshot of the Goals settings in the box type configuration.](/cms_trial/assets/c7eea95e-5465-4d82-9b9e-50f558ac237d.png)

## Achievement progress

### Achievement: None

Achievement progress is not calculated.

![Screenshot of the Achievement setting set to None in the Goals module.](/cms_trial/assets/3732e3fb-24ac-4498-831b-3765334fa16f.png)

### Achievement: Count by status

The calculation is executed per swimlane and per box to which goals have been assigned.

![Screenshot of the Achievement setting set to Count by status.](/cms_trial/assets/f0407e26-d7c0-48e4-93b1-3240eb1d61e7.png)

The calculation is based on the number of goals achieved. The progress state of individual "Open" goals isn't taken into account—the goal either has been achieved or it hasn't.

#### The Formula

**Formula:**

Achievement progress = Number of regular Completed goals / Total number of regular goals (Open + Failed + Completed)

- Abandoned goals are ignored in the calculation
- Uncommitted goals are ignored in the calculation

#### Swimlanes filter impacts the calculation

Only visible swimlanes are taken into account during the calculation.

### Achievement: Count by Business Value

You can compare the Planned and Actual business values, in which case the Uncommitted Team goals will not be included in the Achievement calculation. The App can calculate the ratio, which will be displayed in the Timebox header, thus creating a Team Performance report.

![Screenshot of the Achievement setting set to Count by Business Value.](/cms_trial/assets/5dc624ba-d577-4df3-90da-4d157c437ffd.png)

The results can be further rolled up and used to create a program predictability measure.

#### Edit business value

Keep in mind that the status of the Box determines the possibility to set the Business Value:

| **Timebox status** | **Actual BV** | **Planned BV** |
| --- | --- | --- |
| Not started | Not editable | Editable |
| In progress | Editable | Editable |
| Closed | Not editable | Not editable |

The [business value must be enabled](/cms_trial/space/SPM/1918701325/Objectives+-+Business+value+and+associated+work/) for a box type. Otherwise, PBV and ABV fields will be hidden.

PBV - Planned Business Value

ABV - Achieved Business Value

#### Calculating the Planned vs Actual Business Value

The PBVs of uncommitted goals are not included in the calculation. For example, the total ABV is 27 points, and the sum of PBV for the regular goals is 18. The ratio is 27/18\*100=150%

#### The Formula

**Formula****:**

**Total ABV / Total PBV \* 100**

All Completed, Open, Failed, and Abandoned goals are accounted for in the calculation.

The calculation is executed separately for each swimlane and for the entire Box:

- Total ABV of all box goals / total PBV of all box goals
- total ABV of swimlane goals in a box / total PBV of swimlane goals in a box

5/5\*100 = 100%

5/10\*100 = 50%

18/15\*100 = 120%

5/4\*100 =125%

**PBV of uncommitted goals is taken into account (as an extra factor), and** **the ABV is counted****.**

16/12\*100 = 133%

**If the PBV total of a swimlane is 0, the swimlane's achievement calculation is 0%.**

But the box calculation is still executed if normally (total ABV of all box goals / total PBV of all box goals).

27/10\*100 = 270%

**If the box PBV is 0, the total for the Box and all swimlanes is 0%, regardless of ABV values.**

#### Swimlanes filter impacts the calculation

Only visible swimlanes are taken into account during the calculation.

![Screenshot of the swimlanes drop-down menu in the Goals module.](/cms_trial/assets/a796efe6-beba-4bd3-9ef4-9992248149cc.png)

Collapsed swimlanes are still taken into account during the calculation as long as they are visible.

![Screenshot of the collapsed swimlanes in the Goals module.](/cms_trial/assets/72c90a35-430f-4b23-abb8-38eabb7bd54e.png)

Hidden swimlanes are ignored in the calculation.

![Screenshot of hidden swimlanes in the Goals module.](/cms_trial/assets/9afc1e6c-30a6-4f68-9eb7-ce183e91e6b9.png)

## Create reports

The Goals module includes status-based reports on your goals. You can use bars or pie charts to show the actual progress for each box and team.

The reports can be generated at two levels, the upper and lower, and provide two separate sets of charts. For example, in the case of a SAFe ART, the upper level would be the Program Increment, and the lower one would be the Iteration level.

Goals assigned to sub-boxes do not roll up to the upper-level box.

Switch to the **Reports view**.

![Screenshot of switching to the Reports view in the Goals module.](/cms_trial/assets/4b2bf7e7-41de-448b-9cf5-318f87990f1e.png)

### Chart types

There are two chart types available:

#### Bar charts

![Screenshot of the chart types in the Goals module.](/cms_trial/assets/1ea871af-3fc0-484e-a4bb-75745eac31b9.png)

Hover over a bar to display the number of goals in each column.

![Screenshot of the Bar chart in the Goals module.](/cms_trial/assets/1bb76d55-9091-418d-b5e0-c01a6c7547bc.png)

#### Pie charts

Hover over the charts to display the exact distribution of the goal statuses.

![Video of a pie chart in the Goals module.](/cms_trial/assets/34a1e8c4-f669-4cc4-aded-a8d5785a46f4.mp4)