# duration filter

In the Nunjucks templates of JMWE to create, manipulate and format durations, JMWE uses the duration objects of the [Moment.js](http://momentjs.com/) library. All the functions provided by the library, that are available to your Nunjucks templates through the `duration` filter, return a Moment.js duration object. A Moment.js duration object is an object that represents the length of time in milliseconds, and can easily be manipulated and formatted for display. Refer to the [official documentation](https://momentjs.com/docs/#/durations/) for more information about Moment.js.

## Duration creation

### duration

**Description:**

Creates a [Moment.js duration](https://momentjs.com/docs/#/durations/) object from a duration number, or a string representing a duration. This duration object can then be used with the other duration filters. It returns a number representing the specified duration in the specified unit. If not specified, and the input is a number, it will be interpreted as a number of milliseconds.

**Syntax:**

`{{ NumberOrString | duration([unit] }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `unit` | The unit of the duration number. One of `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `years`. If not specified, and the input is a number, it will be interpreted as a number of milliseconds. The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively. |

**Examples:**

| **Format** | **Output** |
| --- | --- |
| `{{ 3 | duration("minutes") }}` | 3 |
| `{{ "2:30:00" | duration }}` | `9000000` |
| `{{ {days:2,hours:12} | duration }}` | `216000000` |

2} | duration

## Duration formatting

You might want to display duration in a specific format. [Momentjs](http://momentjs.com/docs/#/displaying/) provides some methods to display duration in different formats.

### humanize

**Description:**

Formats a [Moment.js duration](https://momentjs.com/docs/#/durations/) object into a user-friendly string. To format it in a specific locale (language), use the [duration("locale")](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449479059/duration+filter#locale)filter first. It applies to a [Moment.js duration](https://momentjs.com/docs/#/durations/) object, as returned by the `duration([unit])`filter.

**Syntax:**

`{{ durationObject | duration("humanize" [,relative]) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `relative` | If `true`, the duration will be formatted as a relative duration from now (e.g. 3 hours ago). Default is `false`. |

**Examples:**

| **Format** | **Output** |
| --- | --- |
| `{{ 3 | duration("hours") | duration("humanize") }}` | `3 hours` |
| `{{ 3 | duration("hours") | duration("humanize", true) }}` | `in 3 hours` |
| `{{ -3 | duration("hours") | duration("humanize", true) }}` | `3 hours ago` |
| `{{ issue.fields.created | date("diff") | duration | duration("humanize", true) }}` | `3 months ago` |

### locale

**Description:**

Specifies a locale to use for a subsequent `duration("humanize")` filter.

**Syntax:**

`{{ durationObject | duration("locale", locale) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `locale` | A two-letter locale identifier, such as `en` or `fr` |

**Examples:**

| **Format** | **Output** |
| --- | --- |
| `{{ 2 | duration("hours") | duration("locale", "fr") | duration("humanize") }}` | `2 heures` |
| `{{ 1 | duration("minutes") | duration("locale", "es") | duration("humanize") }}` | `un minuto` |

## Duration calculations

You might want to manipulate a duration before setting it to a field. For example, you might want to set a custom field to the difference of the *Original estimate* and *Time Spent.* Below are some methods to help with these manipulations.

### **add**

**Description:**

Adds time to a [Moment.js duration](https://momentjs.com/docs/#/durations/).

**Syntax:**

`{{ durationObject | duration('add' , amount [, unit ] ) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `amount` | The amount of time to add. Can be a number or another Moment.js duration object |
| `unit` | The unit of the amount parameter. One of `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `years`. If not specified, and the amount parameter is a number, it will be interpreted as a number of milliseconds. The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively. |

**Examples:**

| **Input** | **Details** | **Output** |
| --- | --- | --- |
| `{{ 3 | duration("days") | duration("add", 6, "days") }}` | Returns the duration in milliseconds. | `777600000` |
| `{{ 3 | duration("hours") | duration("add", -6, "hours") | duration("humanize", true) }}` | The number can be negative. Apply the `duration("humanize")` filter to display the duration as a relative time. | `3 hours ago` |
| `{{ 5 | duration("months") | duration('add' , {months:2, days:3}) | duration ("humanize") }}` | You can also pass them in object literal | `7 months` |
| `{{ issue.fields.timeoriginalestimate | duration | duration("add",1,"hours") }}` | Add an hour to the Original estimate of the issue. | Duration in milliseconds. For example `14400000`when the Original estimate is 3 hours |
| `{{ issue.fields.timeestimate | duration | duration("add",issue.fields.timespent) | duration("humanize", true)) }}` | Adds the Remaining estimate and the Time Spent on the issue. | Duration as a relative time. For example `in 4 hours`when the Remaining estimate is 3 hours and Time Spent is 1 hour. |

### **subtract**

**Description:**

Subtracts time from a [Moment.js duration](https://momentjs.com/docs/#/durations/).

**Syntax:**

`{{ durationObject | duration('subtract' , amount [, unit ] ) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `amount` | The amount of time to subtract. Can be a number or another Moment.js duration object |
| `unit` | The unit of the amount parameter. One of `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `years`. If not specified, and the amount parameter is a number, it will be interpreted as a number of milliseconds. The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively. |

**Examples:**

| **Input** | **Details** | **Output** |
| --- | --- | --- |
| `{{ 3 | duration("days") | duration("subtract", 6, "days") }}` | Returns the duration in milliseconds. | `-259200000` |
| `{{ 3 | duration("days") | duration("subtract", -6, "days") | duration("days") }}` | The number can be negative. Apply the duration filter to display the duration in days. | 9 |
| `{{ 5 | duration("months") | duration('subtract' , {months:2, days:3}) | duration ("humanize", true) }}` | You can also pass them in object literal | `in 3 months` |
| `{{ issue.fields.timeoriginalestimate | duration | duration("subtract",1,"hours") }}` | Subtracts an hour to the Original estimate of the issue. | Duration in milliseconds. For example  `7200000` when the Original estimate is 3 hours |
| `{{ issue.fields.timeestimate | duration | duration("subtract",issue.fields.timespent) | duration ("humanize", true) }}` | Subtracts the Remaining estimate and the Time Spent on the issue. | Duration as a relative time. For example  `in 2 hours` when the Remaining estimate is 3 hours and Time Spent is 1 hour. |

### **get**

**Description:**

Returns a part of the [Moment.js duration](https://momentjs.com/docs/#/durations/) (milliseconds, seconds, minutes, ...)

**Syntax:**

`{{ durationObject | duration([unit]) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `unit` | The unit of the number to return. One of `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `years`. The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively. |

**Examples:**

| **Input** | **Output** |
| --- | --- |
| `{{ 3 | duration("hours") | duration("get", "hours")` `}}` | `3` |
| `{{ "2:30:00" | duration | duration("get", "minutes") }}` | `30` |
| `{{ issue.fields.timeestimate | duration | duration("get", "hours") }}` | `Hours in the Remaining Estimate of the issue` |

### **as**

**Description:**

Converts a [Moment.js duration](https://momentjs.com/docs/#/durations/) into a number of milliseconds, or seconds, or minutes, ...

**Syntax:**

`{{ durationObject | duration([unit]) }}`

**Parameters:**

| **Parameter** | **Description** |
| --- | --- |
| `unit` | The unit of the number to return. One of `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, `years`. The shorthand keys are: 'y', 'Q', 'M', 'w', 'd', 'h', 'm', 's' and 'ms' for years, quarter, months, weeks, days, hours, minutes, seconds and milliseconds respectively. |

**Examples:**

| **Input** | **Output** |
| --- | --- |
| `{{ 3 | duration("hours") | duration("as", "minutes") }}` | `180` |
| `{{ "2:30:00" | duration | duration("as", "minutes") }}` | `150` |
| `{{ issue.fields.timeestimate | duration | duration("as", "hours") }}` | `Remaining Estimate of the issue in hours` |