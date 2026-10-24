# Capacity per period report

## About the Capacity per period report

Generate a capacity report for a given period.

| **Field** | **Description** |
| --- | --- |
| Name | Name of the report. |
| Category | You can group capacity by:   - total (this report allows you to see a total sum calculated for a given period of time, which is not possible in the Resources module. The capacity/workload total lets you easily see if a workload in a given project is above or below capacity) - per skill - per team - per user. |
| Value | Conditional field (unavailable for the reports in the "total" category).  Select a skill, team, or user the report will be generated for. |
| Aggregation | You can aggregate capacity data by:   - total - week - month. |
| Start/end date | Optional field. Specify the time window a report will cover. Data outside of the specified period is omitted in the calculation. |

![Capacity chart](/cms_trial/assets/a077e78b-aa1b-4db2-9a93-6b3b4f021265.png)

## Report data

The report data is expressed as a number of hours.

The report is based on:

- Capacity (as calculated in the Resources module - if capacity was overwritten in the capacity panel of the Board module it is ignored)
- Workload (workload is based on the Original Estimate, but can be overwritten).

| **Column** | **Data** |
| --- | --- |
| 1st column | Total capacity |
| 2nd column | Distributed workload (used capacity) |
| 3rd column | Remaining capacity (when the distributed workload exceeds total capacity, the number can be negative) |

### Workload

Workload is based on the Original Estimate.

In the "manual" contouring mode you can distribute more or fewer workload hours than the Original Estimate suggests. **Only the distributed workload is taken into account when generating a report.**

![Contouring mode set to Manual](/cms_trial/assets/34f63d23-70b1-4f36-ada1-677440dbe5b5.png)

Workload contouring can affect the report.

Expand an example

The Original Estimate is set to 8h.

![Original estimate set to 8](/cms_trial/assets/87efaf54-7029-4681-a2f0-8b446172f27a.png)

Task duration is 4 days (based on the start/end dates).

![A task highlighted in Resources panel](/cms_trial/assets/3d3f98b3-3a14-4098-982d-a70d188d2380.png)

The task Begins on the last two working days of the month.

![Resource panel, workload highlighted](/cms_trial/assets/68e67235-12f5-4583-982b-44a6283c2911.png)

The workload contouring is set to "front-loaded".

![Countouring mode, front loaded](/cms_trial/assets/030aaf45-36b4-4670-84af-a9ecf6fe17f6.png)

Result:

In a monthly report, the entire workload is distributed to April. The task contributes zero workload to the May report.

![Workload for a week](/cms_trial/assets/68f9d6db-8e78-4153-855d-1b342b2bcf65.png)

### Limitations

The report covers only data that fits within the Box period. Using the 'date range' filter won't expand the report beyond the start/end date of the Box. If the period of your tasks extends beyond the Box period, modify the Box start/end date to encompass all your tasks.

## Portfolio box

In a portfolio, you need to select the Box a report will cover.

![Capacity report form, Project highlighted.](/cms_trial/assets/39555215-cb48-49e6-9b12-39b217121043.png)![Portfolio in project tree](/cms_trial/assets/ffd243b4-5120-41d7-95c6-ca43ceade0bc.png)