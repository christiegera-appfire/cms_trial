# Formula Cards - monday.com

## Overview

[monday.com](http://Monday.com) cannot perform calculations on column values. While you can create columns to track data such as the hourly price of your services, the budget for a marketing campaign, or the hours worked on a project, **you cannot use the platform to calculate the total charge for the hours billed on a project**. Don't worry, we have a solution to your problem.

This gadget allows you to perform math calculations on column values **from any board from any workspace**. Display the result in Icon Cards (numerical results) or Donut Cards (percentage results).

Note that the maximum number of issues that the monday.com Formula Card gadget allows is fixed to 2500.

![Dashboard Hub formula cards monday](/cms_trial/assets/7de0f23b-29ef-4c47-a376-6c6cedf5c986.png)

## Create variables

Variables store values that can be referenced later in the formula. They are useful to separate data in meaningful sets, so you can refer to it easily later in the formula or as the maximum value for the Donut Card visualization in %.

You can create up to 5 variables, and **query any column from any board in any workspace**. In addition, you can filter the items by selecting multiple values of those columns, then, aggregate the result with different functions in your fields.

![Dashboard Hub formula cards monday variables](/cms_trial/assets/cf3dfe9a-c0ef-4ea5-890b-142d272138b2.png)

### Aggregations

Aggregations are also common in the SQL domain. These functions get the values of grouped items as the input of that function to return a calculated value. This gadget currently supports seven functions:

- **Count**. It counts the number of items in that column.
- **Count (distinct)**. It counts the number of only distinct (different) items in the column.
- **Sum**. It returns the addition of the sequence of the numbers of the column.
- **Min**. It returns the smallest value of the range of values of the column.
- **Max**. It returns the largest value of the range of values of the column.
- **Mean**. The arithmetic mean, sums the values of the grouped items and divides the result by how many items are being averaged.
- **Median**. It returns "the middle" value of the range of values of the column. If the number of values is even, then, the mean of the two values in the middle is returned.

## Create cards

Cards display the result of a formula expression in a nice-looking way. This mathematical formula **accepts any of the previously created variables, but also integers and float numbers** e.g., -5, 100, 23.32, or -1,000,000.2, etc.

To construct the relationship of these elements, formulas accept **mathematical operators** like **+** (plus), **-** (minus), **\*** (multiplication), **/** (division), and **( )** (parenthesis).

![Dashboard Hub formula expression](/cms_trial/assets/e209c062-4014-4fbc-b8e2-5bc5fc693fad.png)

To present the result, you can choose between two views:

- **Icon Cards**: An icon displays any result of the formula.
- **Donut Cards**: Percentages represent the result in a donut chart.

![Dashboard Hub formula card types](/cms_trial/assets/c88b5676-780b-4173-b0f6-19a82322aa88.png)

### View type: Icon Card

The Icon Card requires:

- A **label** (*mandatory*) to provide a meaningful description of the resulting number.
- A **prefix** and/or **suffix** (*optional*) to add units or extra information to the number.
- An **icon** (*mandatory*) to give a visual clue of the provided number.

![Dashboard Hub formula icon card](/cms_trial/assets/b663d550-fe82-4752-9aed-e44141471557.png)

### View type: Donut Card

The Donut Card requires:

- A **label** (*mandatory*) to provide a meaningful description of the resulting percentage.
- A **prefix** and/or **suffix** (*optional*) to add units or extra information to the number.
- A **max value** (*mandatory*) to indicate the maximum value of the percentage and paint the donut chart accordingly. If the max value is 100 and the result of the formula is 50, then, half of the donut is painted in the selected color.
- A **color** (*mandatory*) to paint the donut chart.

![Dashboard Hub Formula Cards monday.com chart preview](/cms_trial/assets/b5a769e0-4541-4b7f-8c21-2a7dd4683dcf.png)

## Configuration

Give your gadget a meaningful name so that it is clear what it does and when to use it. Fill out the rest of the fields as applicable, namely:

- The **data source**, indicates the <http://monday.com> account where you want to fetch the data from.

The **variables** for**:**

- The **workspace**, the **board,** andthe **column** where the items are located. Any workspace, board, and column can be selected.

  - The **filter** for the board items. You can filter the items in the column using the filtering mechanism.

![Dashboard Hub Formula Cards monday.com filter configuration](/cms_trial/assets/f8338816-757f-4fb3-977b-29642aa0a94c.png)

- The **Aggregations** to perform calculations -Count, Count (distinct), Sum, Min, Max, Mean, Median- over the results.
- **View Types**

  - **Icon Cards**: An icon displays any result of the formula.
  - **Donut Cards**: Percentages represent the result in a donut chart. The **formula expression** accepts the previously created variables, integers, and float numbers e.g., a, b, -5, 100, 23.32, or -1,000,000.2, etc. And mathematical operators like **+** (plus), **-** (minus), **\*** (multiplication), **/** (division), and **( )** (parenthesis).
- Indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option allows you to use the same default configuration for the remaining gadgets.

## Integrations

- :monday.com:

monday

We are working on our growing catalog of [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but drop us a line in case you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget is not included in any pre-defined dashboard.