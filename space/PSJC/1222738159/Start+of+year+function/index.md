# Start of year function

Returns a date for the begining of the year like 2024-01-05 00:00:00.

```text
function startOfYear() {
    int weeks = week(startOfMonth(currentDate())) - 1;
    interval weeksIntvl = trim(weeks) + "w";
    return startOfMonth(currentDate()) - weeksIntvl;
}
```