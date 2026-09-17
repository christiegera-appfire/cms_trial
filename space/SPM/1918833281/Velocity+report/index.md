# Velocity report

## About the Velocity report

![story-point-chart.png](/cms_trial/assets/d17cf5da-ac28-43a6-9725-8158ae0003da.png)

## What does the report show?

Velocity value is presented on the Velocity chart in the form of a trend line.

The average value calculated for a selected sprint.

The velocity value calculated for the last sprint is additionally displayed at the end of the chart.

**The report is based on story points**.

- Grey column - team capacity in a given period
- Green column - story points of done tasks

Data breakdown is based on program structure (Box structure). The velocity report shows two columns for each sub-Box (such as Iteration).

**The report is generated per team.**

### Grey column - team capacity calculation

**"Planned" value (grey column) = capacity of a team per sub-Box time period**

Planned value is taken from the capacity planning tab in the Resources module. This value is always initially calculated based on the availability of team resources in a given period but can be manually overridden in the capacity planning tab of the Board module.

![safe-team-alfa-2.png](/cms_trial/assets/12c638b5-c8d6-4a88-9c55-b308466554e7.png)![safe-chart-compare.png](/cms_trial/assets/469a88d6-48e7-4fbd-b695-866a95fa6521.png)How to check if the values were manually changed?

Go to the **Board module > capacity planning tab > Highlight changes.** Manually adjusted values will be indicated in orange.

![afe-highlight-changes.png](/cms_trial/assets/35233b99-ce0c-43ec-bce4-715a8f0fef42.png)

If the value was not manually overridden → "**Planned" value (grey column) =** **Team capacity per day (sum of individual capacities of team members per day) multiplied by the duration of a Box** (such as Iteration).

For example, when:

- daily capacity of "Team Alfa" = three story points
- "Iteration 1.2” = 11 workdays
- Planned capacity for Iteration 1.2 = 11x3 = 33 story points

  ![velocity-compare.png](/cms_trial/assets/7320fc36-997a-4633-907e-288c3a191a81.png)

### Green column - done tasks sum

Only tasks in "Done" status are included in the calculation.

**Example**:

![safe-art-compare-2.png](/cms_trial/assets/15383f75-3d9b-4f3c-8959-d2cab3c7be55.png)

Iteration 1.1 contains four done tasks assigned to "Team Alfa".

Story point sum = 5 + 3 + 2 + 6 = 16

![storypoint-sum.png](/cms_trial/assets/3e9a8c27-11b6-45fc-8b22-ce946bd253d9.png)

## Scope of the report

When you create a Velocity report :

- **information is broken down to the lowest available Box level**
- a report is created in a particular Box - **only sub-Boxes nested under that Box are included**
- **all Boxes in the report are from the same level**

See examples below.

#### **Case 1 - report created in the main program Box**

| **Report created in "SAFe ART (Smart house)"** | **Result** |
| --- | --- |
| **lowest available level** | **Iteration** (2nd level under the main program Box) |
| **Included Boxes** | **all Iterations** (all are nested under the main program Box) |
| **all on the same level** | All Iterations are on the same level in the Box hierarchy (2nd level under the main program Box) |

![case-2-report.png](/cms_trial/assets/1bbb1f9f-e772-4b33-a7bf-580e7a41fde2.png)

Resulting report:

![case-2-resulting-report.png](/cms_trial/assets/25145d47-871d-4781-98fd-a4c83dedfc1e.png)

#### Case 2 - report created in a Program Increment

| **Report created in "Program Increment 1"** | **Result** |
| --- | --- |
| **lowest available level** | **Iteration** (2nd level under the main program Box) |
| **Included Boxes** | **3 Iterations** (nested under the "Program Increment 1" - Iterations nested under other Program Increments are not included) |
| **all on the same level** | All Iterations are on the same level in the Box hierarchy (2nd level under the main program Box) |

![case-2-resulting-reports.png](/cms_trial/assets/4c57a646-0564-4e0d-882f-3905d426e472.png)

Resulting report:

![case-2-resulting-reports-2.png](/cms_trial/assets/f6837a2e-fce0-450b-918c-c2da891631ed.png)

## Report configuration

Report configuration/ edit/ delete information can be found on [Report configuration](/cms_trial/space/SPM/1918766118/Report+configuration/). Report management works the same for all reports.

### Available fields

![velocity-report-configuration-2.png](/cms_trial/assets/685950e5-2e58-4875-8f46-f29f8feb5ad3.png)

| **Element** | **Description** |
| --- | --- |
| **Name** | The report name is displayed in the header of each report. |
| **Show iterations with empty capacity** | When selected, Boxes with team capacity = 0 are included in the report team-capacity.png When team capacity = 0?   - team memberships of all members have ended - individuals in the team have no capacity (for example, if everyone has time-off, team capacity = 0) |
| **Show the velocity line on the chart** | checkbox, checked by default |
| **The number of iterations used to calculate velocity** | numeric field, integers only, from 1 to 9, default value = 3 |
| **Project**(conditional field) | This field is available in Portfolio Boxes (more information below). If a Velocity report is added to a Portfolio Box containing multiple projects, you will need to specify which project the report should be generated for. velocity-report-project-highlight.png |
| **Team** | The report is generated for the selected team. |

## Conditions

- tasks must be assigned to teams
- tasks must have a "story points" value
- **lower-level sub-Boxes must exist** (otherwise, the report will be empty)
- lower-level sub-Boxes must have their scope type set to "sub-scope" (in most cases, those will be Program Increments and Iterations).

### Tasks without a team

Tasks that have not been assigned to a team are not accounted for in the calculation (are ignored).

### scope type = sub-scope

The report is based on lower-level Boxes. Their scope type must be set to "sub-scope".

- Own scope → tasks are added directly to the scope of the Box (such as a program Box)
- Sub-scope → Box doesn't have its own scope - it simply displays a section of the parent scope (for example. tasks are added to the main project Box and later divided into Program Increments and Iterations). If you add a task to such Box, it is automatically added to its parent.

In most cases, the scope type of Program Increments and Iterations is set to "sub-scope".

![safe-art-type-column.png](/cms_trial/assets/965110fc-2d49-4d0e-9025-71f851922931.png)

### Project in a portfolio Box

A Portfolio Box can contain multiple program Boxes, each with its scope.

Portfolio Box scope type must be set to "None".

![project-portfolio-hybr.png](/cms_trial/assets/c6658bc8-0cdc-452f-80d3-de83faea6bba.png)

A Velocity report cannot be generated for multiple separate program Boxes.

You can create a Velocity report in a Portfolio Box, but you will need to limit the report to one project.

![velocity-project.png](/cms_trial/assets/ec967bca-a518-4634-a931-fbf3451797d9.png)

## Story Point conversion set to "0"

When a team is still learning to estimate its velocity, the conversion ratio changes from sprint to sprint. You may prefer to show the velocity of future iterations as unknown (=0) and wait for the scrum master to later enter the correct value based on historic data (capacity planning tab of the Board module).

Example:

Story Point conversion = 0

![velocity-for-team-alfa.png](/cms_trial/assets/da63c238-6476-4d47-9206-0750e90103da.png)

The planned capacity of a team = 0 until manually changed

![safe-art-team-alfa.png](/cms_trial/assets/c890b486-aa5b-4a06-99d9-033bb5d32b1f.png)

## Additional use cases - possible mistakes

### Case 3 - no lower-level Boxes

| **Report created in "Iteration 1.1"** | **Result** |
| --- | --- |
| **lowest available level** | **none** |
| **Included Boxes** | **none** |
| **all on the same level** | **n/a** |

Iteration 1.1 has no child Boxes:

![contentId-1918833281](/cms_trial/assets/72dc6d52-a1ce-465b-aefe-380da26be4eb.png)

The Velocity report created in Iteration 1.1 is empty.

![iteration-1-1.png](/cms_trial/assets/8dba5a5a-fb5c-4278-bb1f-cae8288dda01.png)

### Case 4 - Iteration under Iteration

| **Report created in "SAFe ART (Smart house)"** | **Result** |
| --- | --- |
| **lowest available level** | **Iteration** (3rd level under the main program Box) |
| **Included Boxes** | **Iteration 1.3.1** (the only 3rd level Box nested under the main program Box) |
| **all on the same level** | Other iterations are on the 2nd level - they won't be included |

Depending on the setup, you could create a structure like this:

![iteration-1-3-1.png](/cms_trial/assets/004874c6-dac3-444f-81ab-7605d61996c7.png)

In this case, Iteration 1.3.1 is the lowest level under SAFe ART (Smart house). The report includes only Boxes on the same level, so all other Iterations are omitted:

![safe-smart-house.png](/cms_trial/assets/c7d5f147-01c0-451b-9737-ed6cc3815296.png)