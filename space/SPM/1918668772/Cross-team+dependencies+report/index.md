# Cross-team dependencies report

## About the Cross-team dependencies report

The Cross-team dependenciesreport lets you identify project areas handled by two different teams, where coordination of work can be crucial.

![new-report-choose.png](/cms_trial/assets/72eac9ec-f791-4823-8df3-ebeee657d127.png)

The Cross-team dependencies report is in the form of a matrix and presents the names of projects or iterations that:

- are assigned to a given program or project
- have at least one incoming or outgoing dependency (note - both dependency tasks must be open).

![team-dependencies.png](/cms_trial/assets/e7fcfc6f-c080-4fce-968f-b6d3d126a483.png)

The intersection of the matrix's rows and columns shows the number of cross-team dependencies in the entire project (including iterations).

The more dependencies, the color changes from green to yellow to red.

If a team is not allocated to the Box or has no dependencies, it will not be shown in the report.

If there are no cross-team dependencies between Boxes, the report will present "No data."

**Contrary to the Dependencies report:**

- This report displays parent-child dependencies (marked as CP).
- This report **does not** present dependencies between tasks of the same team (in the fields on the matrix diagonal).

When you click the report field, you will see detailed information about each dependency (divided into inbound and outbound dependencies).

![team-dependencies-team.png](/cms_trial/assets/00c0ea0e-0eb1-4b2a-86de-18ba75b113ab.png)

The report presents soft dependencies (S) and strong dependencies (SE, EE, ES, SS).

The digits between the team names indicate the number of dependencies.

![team-dependencies-end-to-start.png](/cms_trial/assets/d76a864b-8688-4dac-a210-631f908dadd1.png)

Status is abbreviated:

![to-do-status.png](/cms_trial/assets/214a1fb9-5411-4dde-ba30-dda1ce7194c8.png)

## Report configuration

You can rename your report using the report configuration.

![team-dependencies-report-configuration.png](/cms_trial/assets/7324e473-4650-45f5-ab84-c2df153835c2.png)

## Export

[BigTemplate](https://appfire.atlassian.net/wiki/spaces/BTc) addon is required.

You can export information of a given cell into .xlsx.

![team-dependencies-export.png](/cms_trial/assets/82970ac2-3cfc-44a7-9825-0dbd970f6feb.png)

The file is a flat list (items are grouped per Team). The following information on both the source and target tasks of a dependency:

- Team name
- task key
- task status
- summary
- dependency type

![team-name-excel.png](/cms_trial/assets/64926fe8-1c62-40e5-8336-c786e6f35beb.png)