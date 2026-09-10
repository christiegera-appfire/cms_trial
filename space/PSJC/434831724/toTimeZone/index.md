# toTimeZone

## Description

Converts a date to the specified time zone.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toTimeZone(date, timeZone) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies the date to convert. |
| timeZone | String | No | Specifies the time zone using a format compatible with TimeZone. See TimeZone for more details. |

## Return Type

**Date**

## Example

```javascript
desc = "";
date d = toDate(2012, 01, 20, 0, 0, 0, 0, "GMT-8");
string format = "dd-MMM-yyyy HH:mm:ss Z";
desc += formatDate(d, format) + " converted to " + formatDate(toTimeZone(d, "GMT+2"), format);
```

Outputs to description: 20-Jan-2012 00:00:00 -0800 converted to 20-Jan-2012 10:00:00 +0200

## See also