# Epoch date functions

Functions for working with epoch dates.

```text
function _dateToEpochGMT(date dateToConvert) {
    date startDate = "1970-01-01";
    startDate = startOfDay(startDate);
    interval span = dateToConvert - startDate;
    return formatNumber(span["TOMILLIS"]/1000, "###");
}

function _epochToDateGMT(number epoch) {
    interval span = trim(epoch) + "s";
    date startDate = "1970-01-01";
    return startDate + span;
}
```