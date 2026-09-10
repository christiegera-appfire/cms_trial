# Interval to hours function

Convert the interval value from a worklog or other source to hours.

```text
function intervalToHours(interval time) {
    int m = time["TOMILLIS"];
    int hours = m/(1000*60*60);
    return hours;
}
```