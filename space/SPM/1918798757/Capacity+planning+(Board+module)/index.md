# Capacity planning (Board module)

## Capacity planning - Board module (old navigation)

Click to expand the guide

## About capacity planning in the Board module

In this view, you can set the capacity for both the team members and the team. Team capacity can be calculated automatically based on the members' capacities.

Team capacity is mostly used during commitment-driven sprint planning. Team capacity serves as the basis on which the team can decide how many backlog items they can tackle in the course of a sprint. You can set the capacity for the entire team upfront, or calculate it on the basis of each team member's individual capacity. At the iteration level, you can overwrite individual team members' capacities or overwrite the entire team capacity directly.

Team capacity becomes visible after turning on the [Totals](/cms_trial/space/SPM/1918666880/Aggregations/) functionality:

- In each Timebox
- In each team's individual Timebox

## Security

Only the **Box Admin** and **Editor** have full access to the capacity planning feature of the Board module.

A **Box viewer** has read-only access to the panel.

## Capacity Planning panel

Click on the icon at the top to go to the Capacity planning view.

![contentId-1918798757](/cms_trial/assets/97b488a3-e275-422e-ab85-06ca142a99af.png)

## Default capacity

Initial capacity values are calculated based on the availability of particular resources and include the sum of working days from the workload plan in a given Timebox (e.g. Iteration), non-working days as defined in the holiday plan, and days off as set in Administration > Resource Manager.

Capacity can be quantified as story points or man-days. Let's assume an iteration lasts 10 working days (two weeks), and the team consists of 3 members. The number of man-days in this iteration is 3 x 10 = 30. If, for example, this iteration includes 2 days off for each team member as defined in the holiday plan, the number of available man-days will be adjusted accordingly, 30 - 3x2 = 24. If one team member is taking 3 extra days off in this time, the team's capacity will be 24 - 3 = 21.

You can only plan capacity at the lower level.

### How is team capacity calculated?

**Team capacity per day (sum of individual capacities of team members per day) multiplied by the duration of a Box** (such as Iteration).

For example, when:

- daily capacity of "Team Alfa" = 3 story points
- "Iteration 1.2 = 11 workdays
- Planned capacity for Iteration 1.2 = 11x3 = 33 story points

![contentId-1918798757](/cms_trial/assets/904a02af-b366-47bf-9bf5-1c32724cd6b9.png)

#### To check the daily capacity of a team

Go to the **resources module** and adjust the view as follows:

- Team view selected

  ![image-20250225-100850.png](/cms_trial/assets/4ce236cc-66e6-4863-b803-f8ad1db622e2.png)
- Show all teams

  ![image-20250225-100837.png](/cms_trial/assets/50a02d7a-ef2c-49ae-8a51-6acfd81b6c3f.png)
- Effort mode → story points

  ![image-20250225-100814.png](/cms_trial/assets/8e49b5a6-0538-44ae-9454-c1a71c0d2f24.png)
- View → capacity + values on the heatmap

  ![image-20250225-100754.png](/cms_trial/assets/7cb6f60d-b1ee-4dfb-bcf5-734e4db748ea.png)
- Aggregation → daily

  ![image-20250225-100742.png](/cms_trial/assets/fed8dde5-5b4e-44d4-a9ff-5594586111bc.png)

The capacity row will display a value for a given day.

![contentId-1918798757](/cms_trial/assets/e50b9595-6cf3-4d4f-b9ad-e21e41a89334.png)

## Manually overwrite the values

**Box Editor**and **Box Admin** can overwrite the values.

### Capacity planning tab

![contentId-1918798757](/cms_trial/assets/fb6fd63e-307a-4f8f-bc62-914a3888d8f9.png)

**Please note that overwriting the values does not modify** [**the Workload plans**](/cms_trial/space/SPM/1918506352/Workload+plans/)**.**

**Calculations in the Resources module are NOT affected by changes made in this view.**

Even though capacities are automatically calculated based on workload, holiday, and absence plans, you can manually overwrite them.

Once you click on a value, you can change it.

![image-20250225-102701.png](/cms_trial/assets/74a3cebc-0478-484d-9df2-695402dcfcf2.png)

#### Highlighting Changes

To see which values are the default values (based on workload plans) and which have been manually overwritten, click the **Highlight changes**button:

![contentId-1918798757](/cms_trial/assets/35d9f9eb-1500-4cc1-884f-919fb7190557.png)

Manually overwritten values are highlighted in orange:

![image-20250225-102721.png](/cms_trial/assets/489e8f88-8362-4023-9c0f-cfbbb50b7e15.png)

#### Restoring Base Capacity

If you change any value but wish to revert your change to the base number, you can do this by clicking on the orange triangle in the corner. The Capacity calculation based on workload plans/ holiday plans/ absences will be restored.

![contentId-1918798757](/cms_trial/assets/34a7a624-cb9b-48b9-ac91-852d545fb056.png)

### Board view

Capacity allocation in Story points can be edited directly in the main Board module view.

![contentId-1918798757](/cms_trial/assets/425217e8-3a74-482b-bcba-b1824e0cee38.png)

The "edit" button appears when you move the cursor.

![contentId-1918798757](/cms_trial/assets/8f358647-6d08-4253-b983-e8bcef16d93d.png)

Enter the new value and hit "Save".

![contentId-1918798757](/cms_trial/assets/0ecd190c-4483-4085-b849-f75d3114be7d.png)

## Capacity Planning from the main view

Capacity values can be edited only in the **Story Points mode**.

To see and edit the values adjust the view as follows:

![contentId-1918798757](/cms_trial/assets/00810ca4-c95b-403c-802a-839df17e473e.png)

1. Hover your mouse over the capacity value. A pencil icon will appear

   ![image-20250225-101025.png](/cms_trial/assets/892acecb-1741-4f74-9515-7f1438c91daf.png)
2. Click the icon:

   ![image-20250225-101012.png](/cms_trial/assets/ed9b487f-5e68-4202-ae36-cb80a6f1eaae.png)
3. Enter the new value and save changes:

   ![image-20250225-100953.png](/cms_trial/assets/40a6a78c-5063-479b-b81a-c4b3a07c277b.png)

### Limitations

- Values can't be changed for Closed Boxes.
- Only **Story Points** values can be changed.
- Only **team capacity** can be changed. Box capacity must be edited in the Capacity Planning panel.

![contentId-1918798757](/cms_trial/assets/b2b15b1d-22e7-441d-9201-7458d8aed2a8.png)

## Limitations

You can't manually change capacity in the **Closed Boxes**.

## Capacity planning - Board module (new navigation)

Click to expand the guide

## About capacity planning in the Board module

In this view, you can set the capacity for both the team members and the team. Team capacity can be calculated automatically based on the members' capacities.

Team capacity is mostly used during commitment-driven sprint planning. Team capacity serves as the basis on which the team can decide how many backlog items they can tackle in the course of a sprint. You can set the capacity for the entire team upfront or calculate it based on each team member's individual capacity. At the iteration level, you can overwrite individual team members' capacities or overwrite the entire team capacity directly.

Team capacity becomes visible after turning on the [Aggregation](/cms_trial/space/SPM/1918666880/Aggregations/) functionality:

- In each timebox
- In each team's individual timebox

## Security

Only the **Box Admin** and **Editor** have full access to the capacity planning feature of the Board module. A **Box viewer** has read-only access to the panel.

## Capacity planning panel

Click **Board** > **Capacity planning**.

![Screenshot of the Capacity planning panel in the Board module.](/cms_trial/assets/3ee961e8-1e9b-497c-9d9f-af373d81b710.png)

## Default capacity

Initial capacity values are calculated based on the availability of particular resources and include the sum of working days from the workload plan in a given timebox (e.g. Iteration), non-working days as defined in the holiday plan, and days off as set in Administration > Resources.

Capacity can be quantified as story points or man-days. Let's assume an iteration lasts 10 working days (two weeks), and the team consists of 3 members. The number of man-days in this iteration is 3 x 10 = 30. If, for example, this iteration includes 2 days off per team member as defined in the holiday plan, the number of available man-days will be adjusted accordingly: 30 - 3x2 = 24. If one team member is taking 3 extra days off in this time, the team's capacity will be 24 - 3 = 21.

You can only plan capacity at the lower level.

### How is team capacity calculated?

**Team capacity per day (sum of individual capacities of team members per day) multiplied by the duration of a box** (such as an Iteration).

For example, when:

Daily capacity of "Team Alfa" = 3 story points

"Iteration 1.2 = 11 workdays

Planned capacity for Iteration 1.2 = 11x3 = 33 story points

#### To check the daily capacity of a team

Go to the **Resources module** and adjust the view as follows:

1. In the Resources module, go to the **Team** view.
2. Select all teams.
3. Under **Modes**, select **Story points**.
4. Under **View**, check the **Capacity** and **Values on heatmap** options.
5. Set aggregation to **Daily**.
6. The capacity row will display a value for a given day.

## Manually overwrite the values

**Box Editor**and **Box Admin** can overwrite the values.

### Capaci planning panel

**Please note that overwriting the values does not modify** [**the Workload plans**](/cms_trial/space/SPM/1918506352/Workload+plans/)**.**

**Calculations in the Resources module are NOT affected by changes made in this view.**

Even though capacities are automatically calculated based on workload, holiday, and absence plans, you can manually overwrite them.

Once you click on a value, you can change it.

![image-20250225-102701.png](/cms_trial/assets/74a3cebc-0478-484d-9df2-695402dcfcf2.png)

#### Highlight changes

To see which values are the default values (based on workload plans) and which have been manually overwritten, click the **Highlight changes**button.

![Screenshot of the Highlight changes button in the Capacity planning panel in the Board module.](/cms_trial/assets/6dbb8c34-97b7-41a8-89ab-ff52c29a9eea.png)

Manually overwritten values are highlighted in orange.

![Screenshot of manually overwritten capacity values in the Board module.](/cms_trial/assets/5914e0f6-24ea-4d08-82f8-b29649819d38.png)

#### Restore base capacity

If you change any value but wish to revert your change to the base number, you can do this by clicking on the orange triangle in the corner. The Capacity calculation based on workload plans/ holiday plans/ absences will be restored.

![Screenshot of restoring base capacity in the Board module.](/cms_trial/assets/dc8479ab-5a37-4280-ad21-f5ce61e7c4e1.png)

### Board view

Capacity allocation in Story points can be edited directly in the main Board module view. Go to **View** > **Aggregation**.

![Screenshot of the Board module with the Aggregation option expanded.](/cms_trial/assets/50f46fa8-e335-488b-9aab-46aef8ebffe0.png)

The **Edit** button appears when you move the cursor. Enter the new value and click **Save**.

![Screenshot of editing the capacity in the Board module.](/cms_trial/assets/25339229-4dc8-4a25-a0f7-8e88e28ebb88.png)

#### Limitations

- Values can't be changed for closed boxes.
- Only **Story Points** values can be changed.
- Only **team capacity** can be changed. Box capacity must be edited in the Capacity Planning panel.