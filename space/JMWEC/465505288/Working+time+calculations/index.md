# Working time calculations

The date filters in JMWE Nunjucks template allow you to perform working time calculations using various working time methods. You can run these date and time calculations based on *working days* and *working times* that are defined using the `workingTime` and `holidays` variables.

This document provides the usage details of these working time methods.

Before using any working time method, you must define the working times and holidays. If not, the following default values are used:

- Working times - Monday to Friday, 9:00 am to 6:00 pm
- No holiday

## Working times settings

Consider an example work schedule:

- Monday, 9:00 am to 1:00 pm and 2:00 pm to 6:00 pm
- Tuesday to Thursday, 9:00 am to 6:00 pm
- Friday, 9:00 am to 1:00 pm
- Saturday and Sunday, non-working days

Use the following syntax to define it:

```text
{%set workingTime = {
  monday:['09:00:00','13:00:00','14:00:00','18:00:00'],
  tuesday:['09:00:00','18:00:00'],
  wednesday:['09:00:00','18:00:00'],
  thursday:['09:00:00','18:00:00'],
  friday:['09:00:00','13:00:00']
} %}
```

### Holidays settings

Consider an example where *every* Jan 1st and Dec 25th are holidays including Feb 29th, 2024. Use the following syntax to define them:

```text
{%set holidays = ['*-01-01','*-12-25','2024-02-29']%}
```

The date format used is *yyyy-mm-dd* (4 digits for the year, 2 digits for the month, from 1 to 12, 2 digits for the day of the month). You can use '\*' instead of an actual year, month, or day to denote that the definition applies to every year, month or day, respectively*.*

## Supported methods

This section lists all the supported working time methods in detail. Consider the following work times and holiday settings for the example syntax and output listed in the following table:

```text
{%set workingTime = {
  monday:['09:00:00', '13:00:00','13:30:00','17:30:00'],
  tuesday:['09:00:00', '13:00:00','13:30:00','17:30:00'],
  wednesday:['09:00:00', '13:00:00','13:30:00','17:30:00'],
  thursday:['09:00:00', '13:00:00','13:30:00','17:30:00'],
  friday:['09:00:00', '13:00:00','13:30:00','17:30:00']
} %}
{%set holidays = ["*-01-14","*-01-15","*-01-26","*-08-15"]%}
```

| **Method name** | **Description** | **Parameters** | **Example syntax** | **Output** |
| --- | --- | --- | --- | --- |
| `isWorkingDay` | Determines if the day of the current instance is a working day. | N/A | `{{ now | date("isWorkingDay") }}` | `true` |
| `isWorkingTime` | Determines if the day and time fall inside working days and hours. | N/A | `{{ issue.fields.created | date("tz") | date("isWorkingTime") }}` | `true` |
| `nextWorkingDay` | Returns a new moment representing the next day considered to be a working day. | N/A | `{{ issue.fields.created | date("nextWorkingDay") | date("YYYY-MM-DD") }}` | `2021-01-19` |
| `nextWorkingTime` | Returns either the same moment if the day and time fall inside working days and hours, or a new moment representing the start of the next day considered to be a working day. | N/A | `{{ issue.fields.created | date("tz") | date("nextWorkingTime") | date }}` | `2021-01-18T09:00:00+05:30` |
| `addWorkingTime` | Adds an amount of working time to the input date and time. | - `amount`: A number of days, hours, minutes,... to add. - `unit`: The unit of the duration amount. One of seconds, minutes, hours, days, weeks, months, years | Add 30 min to *issue creation time*, in the logged-in user’s current time zone:  `{{ issue.fields.created | date("tz") | date("addWorkingTime", 30, "minutes") | date }}` | `2021-01-18T09:30:00+05:30` |
| `subtractWorkingTime` | Subtracts an amount of working time from the input date and time. | - `amount`: A number of days, hours, minutes,... to add. - `unit`: The unit of the duration amount. One of seconds, minutes, hours, days, weeks, months, years | Subtract 30 min from *issue creation time*, in the logged-in user’s current time zone:  `{{ issue.fields.created | date("tz") | date("subtractWorkingTime", 30, "minutes") | date }}` | `2021-01-13T17:00:00+05:30` |
| `workingDiff` | Calculates the difference between two moments, counting only working time. | - `otherDate`: A string representing a date, or a [Moment.js](/cms_trial/space/JMWEC/466323491/date+filter/) date object. If missing, the current date and time will be used (now). - `timePeriod`: A string representing the time period in which the difference should be calculated. Possible values are: years, months, weeks, days, hours, minutes, and seconds. If missing, milliseconds will be returned. | Difference between *now* and *Issue creation date* (both in the logged-in user’s current time zone)  `{{ now | date("tz") | date("workingDiff", issue.fields.created | date("tz"), "minutes") }}` | `960` |

Ensure to use the current logged-in user’s timezone (`date("tz")`while calling the working time methods, wherever applicable. If not, you might not see the results as expected.

### Additional examples

| **Example** | **Syntax** | **Returns** |
| --- | --- | --- |
| Subtract 4 working hours from the specified time with the following definitions:   - Standard working time except for Mondays and Tuesdays between 9:00 am and 6:00 pm - Holidays as Dec 25th and Jan 1st | ```text {%set workingTime = {     monday:["09:00","18:00"],     tuesday:["09:00","18:00"] } %} {%set holidays = ["*-12-25","*-01-01"]%} {{ "2021-09-14T11:00:00Z" | date("subtractWorkingTime", 4, "hours") | date }} ``` | `2021-09-13T16:00:00+00:00` |
| Add 2 working days to *now,* in the logged-in user’s current time zone with the following definitions:   - Standard working time except for Fridays between 9:00 am and 1:00 pm - Holidays as Oct 19th | ```text {%set workingTime = {   friday:['09:00:00','13:00:00'] } %} {%set holidays = ['*-10-19']%} {{now | date('tz') | date('addWorkingTime', 2, 'days') | date}} ``` | `returns 2 working days from now, in the current user's time zone.` |
| Difference between the issue creation time and *now* with the following definitions:   - Standard working time except for Mondays and Tuesdays between 9:00 am and 6:00 pm - Holidays as Dec 25th and Jan 1st | ```text {%set workingTime = {     monday:["09:00","18:00"],     tuesday:["09:00","18:00"] } %} {%set holidays = ["*-12-25","*-01-01"]%} {{ now | date("tz") | date("workingDiff", issue.fields.created     | date("tz"), "hours") }} ```  returns the number of working hours since the issue's creation, *in the current user's time zone*. | `returns the number of working hours since the issue creation, in the current user's timezone` |

### Additional links

- [Date filter](/cms_trial/space/JMWEC/466323491/date+filter/)
- [Duration filter](/cms_trial/space/JMWEC/465243069/duration+filter/)
- [moment.js methods](https://github.com/lennym/moment-business-time#moment-business-time)