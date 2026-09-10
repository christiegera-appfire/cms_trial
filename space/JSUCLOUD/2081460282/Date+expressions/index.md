# Date expressions

This page explains how to write a date expression in JSU Automation Suite for Jira Workflows (JSU). Date expressions can be used in our validators, conditions, and preconditions.

## How to write a date expression in JSU

JSU reads a date expression using the following logic:

- Units should be entered in order, from largest to smallest, for example, `2y 6M 1w`.
- If a value doesn’t include the unit, JSU interprets it as minutes. For example, `4d 10` is interpreted as four days, 10 minutes.
- A unit can only be used once in an expression.
- The value and unit should be written without spaces, for example, `2w 1d`.
- Unless a unit is explicitly written as a negative value, it’s read as positive. For positive values, you can include the `+` if you prefer. For example, `4d` is the same as `+4d`. To express the negative value, write `-4`.
- JSU accepts the following expression units:

|  |  |
| --- | --- |
| `y` | years |
| `M` | months |
| `w` | weeks |
| `d` | days |
| `m` | minutes |
| `s` | seconds |

### Valid date expression examples

|  | **Expression** | **Meaning** |
| --- | --- | --- |
| ✅ | 2M 1w | two months, one week |
| ✅ | 1y | one year |
| ✅ | 10d 12h | 10 days, 12 hours |
| ✅ | 20 | 20 minutes |
| ✅ | -6d | minus six days |
| ✅ | +3M | three months |

### Date expression error examples

|  | **Expression** | **Error** |
| --- | --- | --- |
| ❌ | 2M 4y | The units are not in the correct order |
| ❌ | 1d 30m 5 | The missing unit for 5 is read as minutes, which is already used |
| ❌ | 4w 5d 1d | The day unit is used twice |
| ❌ | 1y 6 M | There is a space in the months expression |

### Recommended operators

It’s recommended that you use the greater than (`>`, `>=`) or less than (`<`, `<=`) operators instead of equal to (`=`) and not equal to (`!=`) when using date expressions.