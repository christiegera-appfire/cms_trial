# Format a number as currency scripted field

## Problem

You would like to display a numeric custom field as currency.

## Solution

This script assumes there is a [SIL alias](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/) for the custom field containing the number value.

```text
return formatNumber(someNumber, "$###,###.0#");
```

Example output: `$16,546,987.21`