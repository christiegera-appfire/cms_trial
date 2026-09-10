# Calculated Field formulas

## Formulas

Formulas are constructed by combining operators, values, and functions in a way that yields a single value. Different elements in the formula give different numbers of values:

- Literal values, fields, and mathematical functions all result in **one value**
- Relation functions can result in **multiple values**, depending on the number of issues that are involved
- Operators or aggregating functions **reduce multiple values into one**

A formula must result in a single value, so `subtasks('Quantity')` is invalid, but `sum(subtasks('Quantity'))` is valid.

### Literal values

You can use constant values in your formulas; their format determines their type.

### Number

To use a number constant, use the number itself, for example, `12000` or `42.86`.

### Text

Text is required for certain functions. Text cannot be used to calculate something. To make a text value, use single quotes `'`, for example `'this is a text'` or `'causes'`.

### Fields

You can use any custom field of type *number*, or text fields that contain a number. JSU converts texts that consist only of a number to a number type.

To use a custom field, type its name, for example, `Budget` or `Quantity`.

If your field’s name contains spaces or special characters, you must surround it with double quotes, for example, `“Story Points”`. Quotes are optional for values without spaces or special characters, for example, `"Quantity"`.

### Operators

Operators combine two values. The following operators are supported:

| **Operator** | **Description** | **Example** |
| --- | --- | --- |
| `+` | Addition | `12 + Quantity` |
| `-` | Subtraction | `15 - Rating` |
| `*` | Multiplication | `Result * Factor` |
| `/` | Division | `"Write off percentage" / 100` |
| `^` | Potentiation: Raises the first value to the power of the second, e. g. 28 | `2 ^ 8` |
| `%` | Percentage: As on a calculator, you can add or subtract a percentage to/from a value. | `Price - 10%` |

## Parentheses

Parentheses can be used to group operations to override operator precedence. `2 * 3 + 3` equals 9, but `2 * (3 + 3)` equals 12.

## Functions

Functions are versatile. We provide the following types:

- **Mathematical** functions enable more calculations.
- **Aggregating** functions, allow you to combine multiple values into one; this is necessary to reduce the results of some relation functions.
- **Relation** functions fetch values from other related issues so you can get values from subtasks, for example.

Jira automatically rounds values to three decimal places. Keep this in mind when you require precise results.

| **Mathematical Function** | **Description** | **Example** |
| --- | --- | --- |
| `round(number, decimals)` | Rounds the passed value to the specified number of significant decimal digits. | - `round(15.386, 2)` = `15.39` - `round(15.5, 0)` = `16` |
| `floor(number)` | Rounds the passed value to the nearest lower integer. | - `floor(16.34)` = `16` |
| `ceiling(number)` | Rounds the passed value to the nearest higher integer. | - `ceiling(16.34)` = `17` |
| `abs(number)` | Gives the absolute value, i. e. the positive value. | - `abs(-15)` = `15` - `abs(15)` = `15` |
| `signum(number)` | Normalises negative values to -1, zero to 0, and positive values to 1. | - `signum(-255)` = `-1` - `signum(0)` = `0` - `signum(135)` = `1` |
| `mod(dividend, divisor)` | Calculates the remainder of the dividend when divided by the divisor. | - `mod(13, 2)` = `1` |
| **Aggregating Function** | **Description** | **Example** |
| `sum(number…)` | Sum of the passed values | - `sum(1, 4, 5)` = `10` |
| `avg(number…)` | Average of the passed values | - `avg(3, 5, 7)` = `5` |
| `min(number…)` | Smallest of the passed values | - `min(-12, 0, 346)` = `-12` |
| `max(number…)` | Largest of the passed values | - `max(-135, 0, 1)` = `1` |
| **Relation Function** | **Description** | **Example** |
| `subtasks(field)` | Retrieves the values of the passed field from all subtasks.  Must be aggregated before using outside of a function. | - `avg(subtasks("Story Points"))` |
| `parent(field)` | Retrieves the values of the passed field from the parent of a subtask. | - `parent("Quantity")` |
| `issuesInEpic(field)` | Retrieves the values of the passed field from all issues in an epic.  Must be aggregated before using outside of a function. | - `min(issuesInEpic("Budget"))` |
| `epic(field)` | Retrieves the values of the passed field from the epic of an issue. | - `epic("Price")` |
| `linkedIssues(linkName, field)` | Retrieves the values of the passed field from all linked issues.  Must be aggregated before using outside of a function.  The link type must be given in single quotes: `‘causes’` | - `max(linkedIssues('causes', "Percentage"))` |

## Advanced use cases

### Setting a boundary on values

What if you must ensure the value of the Calculated Field “Price” stays above 0, but is at most 20? A minimum bound can be set by using `max` and a maximum using `min`. The price is calculated using the “Net Price” field and the “VAT” field.

1. First, we calculate the price, which can be done using `"Net Price” + VAT%`.
2. We then want to set the upper bound of 20, so we get `min(”Net Price” + VAT%, 20)`.
3. Finally, we need the lower bound, so we get `max(min(”Net Price”) + VAT%, 20), 1)`.

### Ensuring entered numbers are integers

You have a field requesting the “Number of Participants” on a transition screen. Your subsequent calculations require this number to be an integer. To ensure this, you use a Calculated Field post function on the same transition.

1. The post function will write to the “Number of Participants” field.
2. We want to operate on the same field, so we start with the formula `“Number of Participants”`.
3. We then want to ensure that it is a whole number; we do this by rounding. We round up in this case: `ceiling(”Number of Participants”)`.

If the number is already a whole number, it is unchanged. If someone enters `15.3` for example, it is rounded up to the next whole number, and we get `16`.  
Because we write the result to the same field during the transition, for example, `Number of Participants`, the same field is adjusted with a whole number input.

## Multiple values

The mathematical functions can also operate on multiple values that are returned by the relation functions. For example, you can round all the values returned by a subtask.

`avg(round(subtasks('Number of Affected Systems'), 0))`

The functions accept the lists in the following ways:

- `round(number_list, decimals)`
- `floor(number_list)`
- `ceiling(number_list)`
- `abs(number_list)`
- `signum(number_list)`
- `mod(dividend_list, divisor)`

The function is then applied to each element in the list, and a list with the new values is returned. The mathematical functions do not reduce the list in size; the only way to do that is to use an aggregating function.