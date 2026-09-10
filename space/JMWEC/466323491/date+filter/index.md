# date filter

When accessed from Nunjucks templates, Jira returns Date and Date/Time values as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-compliant string, such as: `2016-06-12T13:49:34.768+0200`. This applies to Date and Date/Time standard fields (e.g. `issue.fields.created`, `issue.fields.updated`, `issue.fields.duedate`, etc.), Date and Date Time Picker custom fields (e.g. `issue.fields["Change completion date"]`) as well as any date or date/time subfield of a field value (e.g. `issue.fields.comment.comments[0].created`). JMWE's  [now](http/wiki/spaces/JMWE/pages/78055921/Variables+and+functions+used+in+a+Groovy+expression#Others) variable, which represents the current date and time, also returns an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-compliant string.

However, being strings, Jira date/time values aren't easy to work with. To manipulate and format dates and times in Nunjucks, JMWE uses the [Moment.js](http://momentjs.com/) library. All the functions provided by the library, which are available to your Nunjucks templates through the `date` filter, return a Moment.js date object. A Moment.js date object is an object that encapsulates the current date and time, as well as time zone information, and can easily be manipulated and formatted for display.  JMWE's  nowObj variable, which represents the current date and time, returns a Moment.js date object.

Refer to the [official documentation](http://momentjs.com/) for more information about Moment.js.

## Converting a Jira date/time string to a Moment.js date object

You can convert a Jira date/time string to a Moment.js date object using the `clone` method of the Moment.js library. For example:

`"2018-02-14" | date("clone")` returns a Moment.js date object.

When rendered in a {{...}} block, a Moment.js date object is output as a string representing the specified moment in milliseconds.

`{{ "2018-02-14" | date("clone") }}` outputs `1518566400000`

## Converting a Moment.js date object to a Jira date/time string

You can convert a Moment.js date object to a string representing a date/time object using the date filter. For example:

`nowObj | date` returns the current date/time as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-compliant string such as `2018-02-14T00:00:00Z`.

To format a Moment.js date object to a more human-readable string, use the `date(format)` form of the filter.

## Date calculations

You might want to manipulate a date before setting it to a field. For example, you might want to set the *Original estimate* to the difference of the *Created* and *Due date*. Below are some methods to help with these manipulations.

### **add**

**Description:**

Adds time to a date.

**Syntax:**

`{{ DATE | date('add' , Number , String) | date }}`

`{{ DATE | date('add' , Duration) | date }}`

`{{ DATE | date('add' , Object) | date }}`

**Examples:**

Assuming `{{ now }}` is `2016-10-17T08:38:16.625Z`

| Input | Details | Output |
| --- | --- | --- |
| `{{ now | date('add' , 3 , 'days') | date }}` | The String can be 'days' or shorthand 'd' | `2016-10-20T08:38:16Z` |
| `{{ now | date('add' , 3 , 'days') | date('add' , 1 , 'M') | date }}` | You can add multiple keys at the same time | `2016-11-20T08:38:16Z` |
| `{{ now | date('add' , {months:2, days:3}) | date }}` | You can also pass them in object literal | `2016-12-20T08:39:17Z` |

The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively.

When decimal values are passed for days and months, they are rounded to the nearest integer. Weeks, quarters, and years are converted to days or months, and then rounded to the nearest integer.

### **subtract**

**Description:**

Subtracts time from a date.

**Syntax:**

`{{ DATE | date('subtract' , Number , String) | date }}`

`{{ DATE | date('subtract' , Duration) | date }}`

`{{ DATE | date('subtract' , Object) | date }}`

**Examples:**

 Assuming `{{ now }}` is `2016-10-17T08:41:47.658Z`

| Input | Details | Output |
| --- | --- | --- |
| `{{ now | date('subtract' , 3 , 'days') | date }}` | The String can be 'days' or shorthand key 'd' | `2016-10-14T08:51:47Z` |
| `{{ now | date('subtract' , 3 , 'days') | date('add' , 1 , 'M') | date }}` | You can add multiple keys at the same time | `2016-11-14T08:51:47Z` |
| `{{ now | date('subtract' , {months:4, days:13}) | date }}` | You can also pass them in object literal | `2016-06-04T08:51:47Z` |

The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarters, months, weeks, days, hours, minutes, seconds and milliseconds respectively.

When decimal values are passed for days and months, they are rounded to the nearest integer. Weeks, quarters, and years are converted to days or months, and then rounded to the nearest integer.

### **startOf**

**Description:**

Sets a date to the start of a unit of time.

**Syntax:**

`{{ DATE | date('startOf' , String) | date }}`

**Examples:**

 Assuming `{{ now }}` is `2016-10-17T08:41:47.658Z`

| Input | Output |
| --- | --- |
| `{{ issue.fields.duedate | date('startOf' , 'year') | date }}` | `2016-01-01T00:00:00Z` |
| `{{ issue.fields.duedate | date('startOf' , 'quarter') | date }}` | `2016-10-01T00:00:00Z` |

The units of time that can be passed are:

| Unit | Sets to |
| --- | --- |
| year | January 1st, 12:00 am this year |
| month | Beginning of this month, 12:00 am |
| quarter | Beginning of the current quarter, 1st day of the month |
| week | Start of this week, 12:00 am |
| isoWeek | Start of this week, according to ISO 8601, 12:00 am |
| day | 12:00 am today |
| date | 12:00 am today |
| hour | Now, but with 0 mins, 0 secs, 0 ms |
| minute | Now, but with 0 seconds and 0 milliseconds |
| second | Now, but with 0 milliseconds |

### **endOf**

**Description:**

Sets a date to the end of a unit of time.

**Syntax:**

`{{ DATE | date('endOf' , String) | date }}`

**Examples:**

 Assuming `{{ now }}` is `2016-10-17T08:41:47.658Z`

| Input | Output |
| --- | --- |
| `{{ issue.fields.duedate | date('endOf' , 'year') | date }}` | `2016-12-31T23:59:59Z` |
| `{{ issue.fields.duedate | date('endOf' , 'quarter') | date }}` | `2016-12-31T23:59:59Z` |

The units of time that can be passed are:

| Unit | Sets to |
| --- | --- |
| year | December 31st, 23:59 pm this year |
| month | End of this month, 23:59 pm |
| quarter | Ending of the current quarter, 31st day of the month |
| week | End of this week, 23:59 pm |
| isoWeek | End of this week, according to ISO 8601, 23:59 pm |
| day | 23:59 pm today |
| date | 23:59 pm today |
| hour | Now, but with 59 mins, 59 secs, 1000 ms |
| minute | Now, but with 59 seconds and 1000 milliseconds |
| second | Now, but with 999 milliseconds |

### clone

**Description:**

This method takes a date [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) as input and creates a [Moment.js](https://momentjs.com/) date object.

**Syntax:**

`{{ DATE | date("clone") }}`

**Examples:**

| Format | Output |
| --- | --- |
| `{{ now | date("clone") }}` | `1503391995754` |
| `{{issue.fields.created | date("clone") }}` | `1503318155861` |
| `{% set newDate = now | date("clone") %}{{newDate}}` | `1503392291416` |

### daysInMonth

**Description:**

[daysInMonth()](http://momentjs.com/docs/#/displaying/days-in-month/) method can be used to display the number of days in the current month.

**Syntax:**

`{{ DATE | date('daysInMonth') }}`

**Examples:**

If the Due date is `24/Nov/16`: `{{ issue.fields.duedate | date('daysInMonth') }}` will display `30`

### **diff**

**Description:**

Get the difference in milliseconds

**Syntax:**

`{{ DATE | date('diff' , Moment) }}`

**Examples:**

 Assuming `{{ now }}` is `2018-01-04T10:27:23.047Z`and `{{issue.fields.created}}` is `2018-01-04T10:54:53.499+0100`

| Input | Output |
| --- | --- |
| `{{ now | date('diff', issue.fields.created) }}` | `1976836` |

To get the difference in another unit of measurement, pass that measurement as the second argument. The supported measurements are `years`, `months`, `weeks`, `days`, `hours`, `minutes`, and `seconds.`

| Input | Output |
| --- | --- |
| `{{ now | date('diff', issue.fields.created, 'minutes') }}` | `32` |
| `{{ now | date('diff', issue.fields.created, 'days') }}` | `0` |

### **businessDiff**

**Description:**

Calculates the difference between the input date and the specified date, in *business days*, i.e. excluding Saturdays and Sundays. It applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("businessDiff", [otherDate] ) }}

**Parameters:**

otherDate: A string representing a date, or a Moment.js date object. If not specified, uses the current date/time.

**Examples:**

{{"2018-10-13" | date("businessDiff")}} returns a string representing the difference between the input date and current date in *business days*.

{{ "2018-10-13" | date("businessDiff", "2018-05-13") }} returns 110 business days.

{{ "2018-05-13" | date("businessDiff", "2018-10-13") }} returns -110 business days

{{ issue.fields.created | date("businessDiff") }} returns the business days between the issue creation date and now

### **businessAdd**

**Description:**

Adds a specific number of days to a date, skipping non-business days. This applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("businessAdd", amount ) }}

**Parameters:**

amount: The number of business days to add.

**Examples:**

{{ "2018-02-15" | date("businessAdd",2) | date("YYYY-MM-DD") }} returns 2018-02-19.

{{ issue.fields.duedate| date("businessAdd",2) | date("YYYY-MM-DD") }} returns a date adding two business days to the issue Due date

### **businessSubtract**

**Description:**

Subtracts a specific number of days to a date, skipping non-business days. This applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("businessSubtract", amount ) }}

**Parameters:**

amount: The number of business days to add.

**Examples:**

"2018-02-19" | date("businessSubtract",2) | date("YYYY-MM-DD") returns 2018-02-15.

{{ issue.fields.duedate| date("businessSubtract",2) | date("YYYY-MM-DD") }} returns a date subtracting two business days to the issue Due date.

### **nextBusinessDay**

**Description:**

Returns the next business day after the specified date. This applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("nextBusinessDay") }}

**Examples:**

"2018-02-16" | date("nextBusinessDay") | date("YYYY-MM-DD") returns 2018-02-19.

{{ issue.fields.created | date("nextBusinessDay") | date("YYYY-MM-DD") }} returns the next business day after the issue creation.

### **prevBusinessDay**

**Description:**

Returns the business day before the specified date. This applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("prevBusinessDay") }}

**Examples:**

"2018-02-19" | date("prevBusinessDay") | date("YYYY-MM-DD") returns 2018-02-16

{{ issue.fields.created | date("prevBusinessDay") | date("YYYY-MM-DD") }} returns the previous business day before the issue creation.

### **isBusinessDay**

**Description:**

Returns true if the specified date is a business day. This applies to a string representing a date, or a Moment.js date object.

**Syntax:**

{{ <StringOrMoment.jsDateObject> | date("isBusinessDay") }}

**Examples:**

{{ "2018-02-13" | date("isBusinessDay") }}returns true

{{ issue.fields.created | date("isBusinessDay") }} returns true if the issue is created on a business day.

## Date formatting

You might want to display a date in specific format after or before manipulating it. [Moment.js](http://momentjs.com/docs/#/displaying/) provides some methods to display a date in different formats.

### format

**Description:**

This method takes a string of tokens and replaces them with the corresponding values. If the field (on which the method is applied) is invalid the result is an Invalid date string.

**Syntax:**

`{{ DATE | date(format) }}`

**Examples:**

| Format | Output |
| --- | --- |
| `{{ now | date }}` | `2016-10-14T07:26:27Z` |
| `{{ now | date('dddd, MMMM Do YYYY, h:mm:ss a') }}` | `Fri, October 14th 2016, 7:26:27 am` |
| `{{ issue.fields.duedate | date ('YYYY MMMM') }}` | `2016 October` |

**List of tokens:**

|  | Token | Output | Example |
| --- | --- | --- | --- |
| Token | Output |
| Month | M | 1 2 3 .... 11 12 | `{{ now | date ('M') }}` | `October` |
|  | Mo | 1st 2nd 3rd .... 11th 12th | `{{ now | date ('Mo') }}` | `10th` |
|  | MM | 01 02 03 .... 11 12 | `{{ now | date ('MM') }}` | `10` |
|  | MMM | Jan Feb Mar ... Nov Dec | `{{ now | date ('MMM') }}` | `Oct` |
|  | MMMM | January February ... December | `{{ now | date ('MMMM') }}` | `October` |
| Quarter | Q | 1 2 3 4 | `{{ now | date ('Q') }}` | `4` |
|  | Qo | 1st 2nd 3rd 4th | `{{ now | date ('Qo') }}` | `4th` |
| Day of Month | D | 1 2 3 4 5 .... 28 29 30 31 | `{{ now | date ('D') }}` | `14` |
|  | Do | 1st 2nd 3rd... 30th 31st | `{{ now | date ('Do') }}` | `14th` |
|  | DD | 01 02 03 .... 30 31 | `{{ now | date ('DD') }}` | `14` |
| Day of Year | DDD | 1 2 ... 364 365 | `{{ now | date ('DDD') }}` | `288` |
|  | DDDo | 1st 2nd 3rd .... 364th 365th | `{{ now | date ('DDDo') }}` | `288th` |
|  | DDDD | 001 002 003 ... 364 365 | `{{ now | date ('DDDD') }}` | `288` |
| Day of Week | d | 0 1 2 3 4 5 6 | `{{ now | date ('d') }}` | `5` |
|  | do | 0th 1st 2nd 3rd 4th 5th 6th | `{{ now | date ('do') }}` | `5th` |
|  | dd | Su Mo Tu We Th Fr Sa | `{{ now | date ('dd') }}` | `Fr` |
|  | ddd | Sun Mon Tue Wed Thu Fri Sat | `{{ now | date ('ddd') }}` | `Fri` |
|  | dddd | Sunday Monday ... Saturday | `{{ now | date ('dddd') }}` | `Friday` |
| Day of Week (Locale) | e | 0 1 2 3 4 5 6 | `{{ now | date ('e') }}` | `5` |
| Day of Week (ISO) | E | 1 2 3 4 5 6 7 | `{{ now | date ('E') }}` | `5` |
| Week of Year | w | 1 2 3 .. 52 53 | `{{ now | date ('w') }}` | `42` |
|  | wo | 1st 2nd .. 52nd 53rd | `{{ now | date ('wo') }}` | `42nd` |
|  | ww | 01 02 03 ... 52 53 | `{{ now | date ('ww') }}` | `42` |
| Week of Year (ISO) | W | 1 2 3 .. 52 53 | `{{ now | date ('W') }}` | `42` |
|  | Wo | 1st 2nd .. 52nd 53rd | `{{ now | date ('Wo') }}` | `42nd` |
|  | WW | 01 02 03 ... 52 53 | `{{ now | date ('WW') }}` | `42` |
| Year | YY | 70 71 72 ... 29 30 | `{{ now | date ('YY') }}` | `16` |
|  | YYYY | 1970 1971 ... 2029 2030 | `{{ now | date ('YYYY') }}` | `2016` |
|  | Y | 1970 1971 ... 9999 +10000 +10001  **Note:** This complies with the ISO 8601 standard for dates past the year 9999 | `{{ now | date ('Y') }}` | `2016` |
| Week Year | gg | 70 71 ... 29 30 | `{{ now | date ('gg') }}` | `16` |
|  | gggg | 1970 1971 ... 2029 2030 | `{{ now | date ('gggg') }}` | `2016` |
| Week Year (ISO) | GG | 70 71 ... 29 30 | `{{ now | date ('GG') }}` | `16` |
|  | GGGG | 1970 1971 ... 2029 2030 | `{{ now | date ('GGGG') }}` | `2016` |
| AM/PM | A | AM PM | `{{ now | date ('A') }}` | `AM` |
|  | a | am pm | `{{ now | date ('a') }}` | `am` |
| Hour | H | 0 1 2 .. 23 24 | `{{ now | date ('H') }}` | `7` |
|  | HH | 00 01 02 03 ... 23 24 | `{{ now | date ('HH') }}` | `07` |
|  | h | 1 2 3 ... 11 12 | `{{ now | date ('h') }}` | `7` |
|  | hh | 01 02 03 .. 11 12 | `{{ now | date ('hh') }}` | `07` |
|  | k | 1 2 3 ... 23 24 | `{{ now | date ('k') }}` | `7` |
|  | kk | 01 02 03 .. 23 24 | `{{ now | date ('kk') }}` | `07` |
| Minute | m | 0 1 2 .. 58 59 | `{{ now | date ('m') }}` | `26` |
|  | mm | 00 01 02 .. 58 59 | `{{ now | date ('mm') }}` | `26` |
| Second | s | 0 1 2 .. 58 59 | `{{ now | date ('s') }}` | `27` |
|  | ss | 00 01 02 .. 58 59 | `{{ now | date ('ss') }}` | `27` |
| Fractional Second | S | 0 1 2 .. 8 9 | `{{ now | date ('S') }}` | `6` |
|  | SS | 00 01 ... 98 99 | `{{ now | date ('SS') }}` | `67` |
|  | SSS | 000 001 ... 998 999 | `{{ now | date ('SSS') }}` | `672` |
|  | SSSS ... SSSSSSSSS | 000[0..] 001[0..] ... 998[0..] 999[0..] | `{{ now | date ('SSSS ... SSSSSSSSS') }}` | `6720 ... 672000000` |
| Time zone | z or zz | EST CST ... MST PST | `{{ now | date ('z') }}`  `{{ now | date ('zz') }}` | `UTC Coordinated Universal Time` |
|  | Z | -07:00 -06:00 ... +06:00 | `{{ now | date ('Z') }}` | `+00:00` |
|  | ZZ | -0700 -0600 ... +0600 | `{{ now | date ('ZZ') }}` | `+0000` |
| Unix Timestamp | X | 1360013296 | `{{ now | date ('X') }}` | `1476436377` |
| Unix Millisecond Timestamp | x | 1360013296123 | `{{ now | date ('x') }}` | `1476436377284` |

If you would like to add strings in format strings, you need to wrap the characters in square brackets. For example: `{{ now | date ('[The issue was resolved on] Do MMMM YYYY dddd') }}` will display, `The issue was resolved on 14th October 2016 Friday.`

### tz

**Description:**

You can parse and display dates in any timezone. By default this method will print the date in the timezone of the current user (the user running the transition). See [here](http://momentjs.com/timezone/docs/) for all the available functions.

The list of possible time zones is available [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

This filter uses the Jira API to retrieve the logged-in user’s timezone. However, this will only work if the user has set their profile’s Local Time setting to be visible to “Anyone”. If this has not been set correctly, the **tz** filter will return the instances system time.

**Syntax:**

`{{ DATE | date('tz') }}`

**Examples:**

| Format | Output |
| --- | --- |
| `{{ now | date('tz') }}` | 2017-07-21T06:26:46+02:00 |
| `{{ now | date('tz',"Asia/Kolkata") | date('dddd, MMMM Do YYYY, h:mm:ss a') }}` | `Fri, October 14th 2016, 7:26:27 am` |
| `{{ issue.fields.duedate | date('add',10,"days") | date('tz',"America/Los_Angeles") | date ('YYYY MMMM DD') }}` | 2017 June 05 |

### fromNow

**Description:**

[fromNow()](http://momentjs.com/docs/#/displaying/fromnow/) method can be used to display the *time* from now.

**Syntax:**

`{{ DATE | date('fromNow') }}`

**Examples:** If Due date is `24/Nov/16` and Created is `13/10/16`

| Input | Output |
| --- | --- |
| `{{ issue.fields.duedate | date('fromNow') }}` | `in a month` |
| `{{ issue.fields.created | date('fromNow') }}` | `a day ago` |

You can remove the suffix 'ago' by passing true to the method. For example: `{{ issue.fields.duedate | date('fromNow' , true) }}` will display: `a month`

The string displayed for each length of time is listed below:

| Range | Key | Sample Output |
| --- | --- | --- |
| 0 to 45 seconds | s | a few seconds ago |
| 45 to 90 seconds | m | a minute ago |
| 90 seconds to 45 minutes | mm | 2 minutes ago ... 45 minutes ago |
| 45 to 90 minutes | h | an hour ago |
| 90 minutes to 22 hours | hh | 2 hours ago ... 22 hours ago |
| 22 to 36 hours | d | a day ago |
| 36 hours to 25 days | dd | 2 days ago ... 25 days ago |
| 25 to 45 days | M | a month ago |
| 45 to 345 days | MM | 2 months ago ... 11 months ago |
| 345 to 545 days (1.5 years) | y | a year ago |
| 546 days+ | yy | 2 years ago ... 20 years ago |

### from x

**Description:**

[from()](http://momentjs.com/docs/#/displaying/from/) method can be used to display the *time* from x (time other than now).

**Syntax:**

`{{ DATE | date('from' , 'x') }}`

**Examples:**

If you want to find the time from the *Due date* to the *Created* date:

| Input | Output |
| --- | --- |
| {% set due = issue.fields.duedate %} {% set cre = issue.fields.created %} {{ due | date('from' , cre) }} | `in a month` |

You can remove the suffix 'month' by passing true to the method: `{{ due | date('from' , cre , true) }}` will display: `a month.`

### toNow

**Description:**

[toNow()](http://momentjs.com/docs/#/displaying/tonow/) method can be used to display the time to now.

**Syntax:**

`{{ DATE | date('toNow') }}`

**Examples:**

If the Due date is `24/Nov/16`, `{{ issue.fields.duedate | date('fromNow') }}` will display: `a month ago`

If the issue created date is `13/10/16`, `{{ issue.fields.created | date('fromNow') }}` will display: `in a day`

The string displayed for each length of time is listed below:

| Range | Key | Sample Output |
| --- | --- | --- |
| 0 to 45 seconds | s | in seconds |
| 45 to 90 seconds | m | in a minute |
| 90 seconds to 45 minutes | mm | in 2 minutes ... in 45 minutes |
| 45 to 90 minutes | h | in an hour |
| 90 minutes to 22 hours | hh | in 2 hours ... in 22 hours |
| 22 to 36 hours | d | in a day |
| 36 hours to 25 days | dd | in 2 days ... in 25 days |
| 25 to 45 days | M | in a month |
| 45 to 345 days | MM | in 2 months ... in 11 months |
| 345 to 547 days (1.5 years) | y | in a year |
| 548 days+ | yy | in 2 years ... in 20 years |

### to x

**Description:**

[to()](http://momentjs.com/docs/#/displaying/to/) method can be used to display the time to x (time other than now).

**Syntax:**

`{{ DATE | date('to' , 'x') }}`

**Examples:**

If you want to find the time to the due date to the created date:

```text
{% set due = issue.fields.duedate %}
{% set cre = issue.fields.created %}
{{ cre | date('to' , due) }}
```

This will display, `in a month.`

The string displayed for each length of time is listed below:

| Range | Key | Sample Output |
| --- | --- | --- |
| 0 to 45 seconds | s | in seconds |
| 45 to 90 seconds | m | in a minute |
| 90 seconds to 45 minutes | mm | in 2 minutes ... in 45 minutes |
| 45 to 90 minutes | h | in an hour |
| 90 minutes to 22 hours | hh | in 2 hours ... in 22 hours |
| 22 to 36 hours | d | in a day |
| 36 hours to 25 days | dd | in 2 days ... in 25 days |
| 25 to 45 days | M | in a month |
| 45 to 345 days | MM | in 2 months ... in 11 months |
| 345 to 547 days (1.5 years) | y | in a year |
| 548 days+ | yy | in 2 years ... in 20 years |

You can remove the suffix 'in' by passing `true` to the method: `{{ cre | date('to' , due, true) }}` will display: `a month.`

### locale

**Description:**

This method takes a string representing a date, or a Moment.js date and sets the locale to use to format the date.

**Syntax:**

{{ DATE | date("locale") }}

**Examples:**

"2018-02-14T06:49:17Z" | date("locale") | date("LLLL") returns the full date in the current user's locale.

"2018-02-14T06:49:17Z" | date("locale", "fr") | date("LLLL") returns mercredi 14 février 2018 06:49