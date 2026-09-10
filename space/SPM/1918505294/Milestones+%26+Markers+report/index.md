# Milestones & Markers report

## About the Milestones & Markers report

![milestones-markets.png](/cms_trial/assets/5cd7a97e-d496-4f6d-a5f7-f8e7bdd4e67c.png)

**This report lets you keep track of all your Milestones & Markers in one place.**

- You could create a report in a Portfolio Box to track multiple projects.

  ![Milestones in Project Portfolio](/cms_trial/assets/022317fb-812d-4b4d-a489-1806e9669bac.png)
- You could use it in the main project Box to track a single project.

  ![safe-art-smart-house-milestones.png](/cms_trial/assets/8ad48c20-d859-4b70-b32b-a7273cb1de5d.png)

## What does the report show?

The report shows:

- **current and future information**

  - milestones
  - markers
- **Past information**

  - milestones that are not "Done"

Past markers are not displayed.

Past milestones in the "Done" status are not displayed.

| **Element** | **Description** |
| --- | --- |
| Name | Name of the element |
| End date | Current end date of the element |
| Baseline | Deviation from the baseline:   - If a baseline hasn't been created, the field remains empty - If a baseline exists, the app calculates the difference (number of days) between the baseline end date and the current end date Dates highlighted in Milestones panel   - 0d → task on schedule (baseline date = end date) Green milestone   - -Xd → task behind schedule (baseline date < end date) Red milestone   - +Xd → task ahead of schedule (baseline date > end date) Purple milestone |
| Source | Box the item was created in. |

- "today" marker is always visible

  ![Today milestone](/cms_trial/assets/9f8ae255-e90b-40d0-b14e-749aa851280d.png)
- color of milestones corresponds to their setup in the Gantt module

  ![marker-first-row.png](/cms_trial/assets/be5fb876-f330-48e0-9dd6-cb0a29618e16.png)![Markers, Stage II](/cms_trial/assets/2cbb77bd-dcf4-4169-9f7d-fda699a30a82.png)
- color of markers corresponds to their setup

  ![progress-check-a.png](/cms_trial/assets/6a2e9430-d8f1-40bc-81e5-c199bb7c86b0.png)

### Markers

Inheritance from upper levels:

- Markers from lower-level Boxes are not visible.
- **Markers from upper-level Boxes are visible**.

In the "source" column, you can see what Box a marker is from. Markers from upper-level Boxes are included in the report.

![Supplementary Program](/cms_trial/assets/9586d544-54ba-49fe-a3be-be29646339bc.png)![supplementary-program-ii.png](/cms_trial/assets/c91524ba-946b-449c-b5f2-8d1de95893a9.png)

Markers from lower-level Boxes are not included.

![markers-from-lower-level.png](/cms_trial/assets/71dde819-a639-4021-9ad8-b12d3f8310ba.png)

### Milestones

Inheritance from lover levels:

- Milestones from lower-level Boxes are visible
- Markers from upper-level Boxes are not visible.

In the "source" column, you can see what Box a milestone is from. Milestones from lower-level Boxes are included in the report.

![Comparing views of milestones](/cms_trial/assets/e91ac585-8b85-4941-a70e-e24571829641.png)![program-a-cross.png](/cms_trial/assets/819d8ab5-9dbe-4d6a-b7e0-1baccee23f93.png)

Milestones from upper levels are not included.

![milestones-from-upper-level.png](/cms_trial/assets/7fd19849-f447-4d23-b501-e305d51f820e.png)

## Report configuration

Report configuration/ edit/ delete information can be found on [Report configuration](/cms_trial/space/SPM/1918766118/Report+configuration/). Report management works the same for all reports.

### Available fields

![Milestones and Markers window, Show milestones and markers option](/cms_trial/assets/1c7c42a2-c92c-4d4b-bbe9-95580ef99729.png)

| **Element** | **Description** |
| --- | --- |
| **Name** | The report name is displayed in the header of each report. |
| **Content** | You can select one of the three options:   - Show milestones and markers - Show milestones only - Show markers only |