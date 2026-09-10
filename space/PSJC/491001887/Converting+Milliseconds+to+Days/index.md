# Converting Milliseconds to Days

Time and dates are stored in milliseconds are stored in Jira following Java convention. How do we convert milliseconds into something useful?

## Background

I often find it useful to begin (for sake of conversation) this post from Stack Overflow. In the accepted answer, it has a simple equation for converting [milliseconds to days.](https://stackoverflow.com/questions/7829571/milliseconds-to-days)

```text
days = milliseconds / 1000 millis in a second * 60 seconds in a minute * 60 minutes in an hour * 24 hours * 7 days
```

## Example Scripts

Below are some examples of how we can convert intervals into days and hours. Because of the [Type Conversion](/cms_trial/space/PSJC/496205872/Type+conversion/) feature of SIL, both numbers and intervals can be used in an equation to calculate days, hours and minutes. The [trunc() function](/cms_trial/space/PSJC/434766239/trunc/)returns only whole numbers.

|  |
| --- |
| ```text number durationMillis = due - created; interval durationInterval = due - created; number days = trunc(durationMillis / (1000 * 60 * 60 * 24), 0); number hours = trunc(durationInterval / (1000 * 60 * 60), 0); number minutes = trunc(durationInterval / (1000 * 60), 0);   runnerLog(durationMillis); runnerLog(durationInterval); runnerLog(days); runnerLog(hours); runnerLog(minutes); ``` |

## Accounting for 8 Hour Days

For certain durations, Jira considers one day equal to 8 hours. By following the logic found our example equation from the "Background" section, we would divide by 8 as demonstrated below:

|  |
| --- |
| ```text days = millis / (1000 millis * 60 seconds * 60 minutes * 8 hours) ``` |

At other times you may find it necessary to divide by 3 (because 24 hours divided by 8 is 3).

|  |
| --- |
| ```text interval example = "2w 4d 4h"; number hours = trunc(example / (1000 * 60 * 60), 0); number jiraHours = hours/3; runnerLog(jiraHours); ``` |

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.