# Formula Cards

## Overview

You can use our Formula Cards gadget to perform calculations on fields, and display the results in an Icon card for numbers or Donut card for percentages. This helps leverage your Jira data because you can’t do this natively in Jira. While Jira let’s you create custom fields, for example, to add the price per hour of your services, you can’t calculate the total amount you should charge for the hours billed in your project.

We also have a [Formula Cards gadget for monday.com](/cms_trial/space/RDD/199755988/Formula+Cards+-+monday.com/).

The Formula Cards gadget can load up to 2,500 work items for each variable.

![Dashboard Hub formula cards gadget](/cms_trial/assets/a4b2dd08-ccc7-4046-a8b9-9e6679353708.png)

---

## Create variables

Variables store values that can be referenced later in the formula. They are useful to separate data in meaningful sets, so you can refer to them in the formula or as the maximum value for the Donut Card visualization in %.

You can create up to five variables, use existing filters or new JQL queries, and aggregate the results with different functions in your fields.

![Dashboard Hub formula variables](/cms_trial/assets/37792c45-a426-4972-ae13-fe7fc41d971e.png)

### Aggregations

Aggregations are also common in the SQL domain. These functions take the values of grouped rows as input to return a calculated value. This gadget currently supports seven functions:

- **Count**: Counts the number of rows/elements in that group/field.
- **Count (distinct)**: Counts the number of only distinct (different) rows/elements in the group/field.
- **Sum**: Returns the sum of the sequence of numbers in the group/field.
- **Min**: Returns the smallest value of the range of values of the group/field.
- **Max**: Returns the largest value in the range of values of the group/field.
- **Mean**: The arithmetic mean, which sums the values of the grouped rows and divides the result by how many rows are being averaged.
- **Median**: Returns the middle value of the range of values of the group/field. If the number of values is even, then the mean of the two values in the middle is returned.

## Create cards

Cards display the result of a formula expression. This mathematical formula accepts any of the previously created variables, as well as integers and float numbers, for example -5, 100, 23.32, or -1,000,000.2.

Formula Cards use **decimal places**, not significant digits, for rounding. Fractional results are displayed with up to 2 decimal places. Whole numbers are shown without decimal places, for example, `42`, not `42.00`.

To construct the relationship of these elements, formulas accept **mathematical operators** like **+** (plus), **-** (minus), **\*** (multiplication), **/** (division), and **( )** (parenthesis).

![Dashboard Hub formula expression](/cms_trial/assets/75bd3c79-d9f9-4b3a-92a1-426b06212b16.png)

To present the result, you can choose between two views:

- **Icon Cards**, where an icon displays any result of the formula.
- **Donut Cards**, using percentages to represent the result in a donut chart.

![Dashboard Hub formula card types](/cms_trial/assets/535ad28f-d82b-4669-8a46-0378e57d23b1.png)

### View type: Icon Card

The Icon Card requires:

- A **label** (*mandatory*) to provide a meaningful description of the resulting number.
- A **prefix** and/or **suffix** (*optional*) to add units or extra information to the number.
- An **icon** (*mandatory*) to give a visual clue of the provided number.

![Dashboard Hub formula icon card](/cms_trial/assets/ebf2f503-854d-4702-a852-7f06b6c844f7.png)

### View type: Donut Card

The Donut Card requires:

- A **label** (*mandatory*) to provide a meaningful description of the resulting percentage.
- A **prefix** and/or **suffix** (*optional*) to add units or extra information to the number.
- A **max value** (*mandatory*) to indicate the maximum value of the percentage and paint the donut chart accordingly. If the max value is 100 and the result of the formula is 50, then, half of the donut will be painted in the selected color.
- A **color** (*mandatory*) to paint the donut chart.

![Dashboard Hub pending budget](/cms_trial/assets/561bb32e-18ad-4287-be1b-40273c2b9b99.png)

---

## Configuration

Give your gadget a meaningful name, so it is clear what it does and when to use it.

Fill out the rest of the fields as applicable, namely:

- The **data source**, where the source Jira instance is installed.

The **variables**, where each one**:**

- The **JQL** (Jira Query Language) query **or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). We recommend adding at least one clause, for example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns the query results, which are not fixed and could change over time.
- The **aggregations** to perform calculations -Count, Count (distinct), Sum, Min, Max, Mean, Median- over the results. Check the [aggregations](/cms_trial/space/RDD/146309496/Formula+Cards/) section.
- The **field** to select what you want to apply the calculation to, for example, Story Points.

The **cards**, where each one:

- The **view** type

  - **Icon Cards**, where you can visually display any result of the formula with an icon.
  - **Donut Cards**, where you can represent percentages in a donut chart.
- The **formula expression** accepts the previously created variables, integers, and float numbers, for example, a, b, -5, 100, 23.32 or -1,000,000.2, etc. And mathematical operators like **+** (plus), **-** (minus), **\*** (multiplication), **/** (division), and **( )** (parenthesis).
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring the rest of the gadgets one by one with the same default configuration

## Integrations

- Jira Software

- Jira Service Management