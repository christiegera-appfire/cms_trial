# Query and transform your data with JSONata

## Overview

[JSONata](https://jsonata.org/) is a data query and transformation language designed for processing JSON data. It is used to preprocess, merge, and format data retrieved from APIs, allowing developers to perform complex calculations and data manipulations. You can try it out with the [JSONata Exerciser](https://try.jsonata.org/).

## Key features of JSONata

1. **Data Transformation:** Modify and enhance JSON data by adding calculated fields.
2. **Merging Data:** Combine information from multiple JSON data sources.
3. **Advanced Query Functions:** Perform calculations using functions like `map`, `filter`, `distinct`, and `sort`.
4. **Debugging Support:** Explore and debug the data processing context using debug tools.
5. **Data Visualization Integration:** Use transformed JSON data to create dynamic visualizations.

---

## Step-by-step guide

Building a data-based custom report always consists of the same set of steps:

- Fetch the data and output to a JSON node, possibly from different data sources.
- Process the data: discard the unused parts; adapt, aggregate, or process the data.
- Pipe the processed data into rendering nodes.

### Fetch data from an API endpoint

1. Use a REST node to fetch data from an API endpoint. This example will generate data for three people.

```json
{
  type: 'rest',
  uri: 'https://randomuser.me/api/?results=3',
  id: 'people',

  children: [
    {type: 'json'}
    ]
}
```

In this example, we are using a node of type json.

```json
{type: 'json'}
```

Therefore, we can display the entire JSON response from the REST API in our report. Whenever you need to view the data format from the REST API, you can use a JSON node.

Download the JSON descriptor here:

![contentId-1549304032](/cms_trial/assets/4d422c84-1084-478b-8429-6cb5b7da221b.json5)

![Dashboard Hub Query and transform your data with JSONata report preview](/cms_trial/assets/a6bf6e39-047a-46d2-be5e-e6e0f5cbd274.png)

1. Determine the new data you want to calculate, such as the decade of birth, based on the date of birth.
2. Use JSONata functions to perform the necessary calculations. The `map` function is commonly used to iterate over each record in the `results` array.
3. Store the calculated data in a new key within the original data structure. For example, add a "decade" key to each record in the `results` array.
4. Perform additional calculations if needed, such as extracting distinct decades from the enriched data and sorting them. Store these values in separate keys, like `decades`.

This generates a sorted list of the decades in which these three people were born. This example displays only two decades because two of the people generated in Step 1 were born in 1980.

Note that the API returns random users, so the results will change in each iteration.

```json
{
  type: 'rest',
  uri: 'https://randomuser.me/api/?results=3',
  id: 'people',
  path: '(\
    /* Calculate the decade of birth for each person */\
    $withDecades := $map($.results, function($p) { $merge([{ "decade": $substring($formatDate($p.dob.date), -4, 3) & "0" }, $p]) });\
    \
    /* Extract decades range */\
    $decades := $sort($distinct($map($withDecades, function($p) { $p.decade })));\
    \
    { "data": $withDecades, "decades": $decades }\
  )',
  children: [
    {type: 'json'}
    ]
}
```

![Dashboard Hub JSONata transformed custom report preview](/cms_trial/assets/a49a78d9-0eab-438c-8e09-8109145580e8.png)

### Add a chart

1. Add a chart node to the report (see [Advanced Knowledge you need to build reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)).
2. Define the chart's dimensions and appearance.
3. Set the style of the chart's grid.
4. Customize the axes' appearance.
5. Populate the X-axis values using data from the report context, such as the `decades` key.
6. Use JSONata functions to calculate the values for each data series in the chart. For example, calculate the number of male and female records per decade. Using the code below, the report displays a bar chart showing the number of males and females born in each decade.

```json
data: '$map($.decades, function($d) {\
              $count(\
                $map(\
                  $filter(\
                    $filter($.data, function($p) { $p.gender = "male"}),\
                    function($p) { $d = $p.decade}),\
                  function($v) {$v.decade}))})',
          },
```

Full descriptor that displays a bar chart counting the number of males and females born in each decade.

```json
{
  type: 'rest',
  uri: 'https://randomuser.me/api/?results=300',
  id: 'people',
  path: '(\
    /* Calculate the decade of birth for each person */\
    $withDecades := $map($.results, function($p) { $merge([{ "decade": $substring($formatDate($p.dob.date), -4, 3) & "0" }, $p]) });\
    \
    /* Extract decades range */\
    $decades := $sort($distinct($map($withDecades, function($p) { $p.decade })));\
    \
    { "data": $withDecades, "decades": $decades }\
  )',
  children: [
    {
      type: 'json'
    },
    {
      type: 'chart',
      options: {
        chart: {
          width: 700,
          height: 400,
          
        },
        cartesianGrid: {
          stroke: "#eee",
          strokeDasharray:"5 5",
          vertical: false
        },
        xAxis: {
          axisLine: false,
          tickLine: false
        },
        yAxis: {
          axisLine: false,
          tickLine: false
        },
      },
      data: {
        categories: '$.decades',
        series: [
          {
            chartType: 'bar',
            name: 'Males',
            stackId: 'a',
            fill: '#82ca9d',
            data: '$map($.decades, function($d) {\
              $count(\
                $map(\
                  $filter(\
                    $filter($.data, function($p) { $p.gender = "male"}),\
                    function($p) { $d = $p.decade}),\
                  function($v) {$v.decade}))})',
          },
          {
            chartType: 'bar',
            name: 'Females',
            stackId: 'a',
            fill: '#8884d8',
            data: '$map($.decades, function($d) {\
              $count(\
                $map(\
                  $filter(\
                    $filter($.data, function($p) { $p.gender = "female"}),\
                    function($p) { $d = $p.decade}),\
                  function($v) {$v.decade}))})',
          },
        ],
      },
    },
  ]
}
```

![Dashboard Hub Query and transform your data with JSONata chart preview](/cms_trial/assets/e79964e5-3ceb-4cb0-b2f2-a88391ffff77.png)

---

## Debug mode

1. Turn on **Debug mode** to view additional buttons for inspecting the report context.

   ![Dashboard Hub JSONata query result table](/cms_trial/assets/8aeb6c92-e144-46bb-9b07-0805d68a9a8e.png)
2. Right-click in the *Report Description Editor* and select **Inspect** to access the console.
3. Explore the JSON context at various levels:

   - Root context: Contains global data sources and metadata.
   - Node context: Contains data specific to the current processing node.

---

## Best practices

- **Start Small:** Begin with simple queries to understand the structure of your data.
- **Leverage Debug Mode:** Use the debug tools to trace errors and verify transformations.
- **Use the node:type=json:** Use this as a debugger to output data from context, for example, a JSON node as a child of REST node will print the result of fetching data from the remote.
- **Refine the data:** Use the path property until you achieve the expected outcome. You can use <https://try.jsonata.org/> to iterate quickly. Once you have your outcome, you can replace it elsewhere for example, in `path` in the rest node, or in an interpolation. Remember the jsonPath expression is just a JSON transformation function.
- **Utilize functions:** JSONata provides a wide range of built-in functions for advanced data manipulation.
- **Reuse and optimize:** Store reusable queries in variables to simplify and optimize transformations.

  ![Diagram illustrating the process described on this page.](/cms_trial/assets/d9771dc7-a963-4f1d-9dcb-ca744208494c.png)

---

## Common functions in JSONata

| Function | Description | Example |
| --- | --- | --- |
| `$map` | Maps a function to each element in an array. | `$map(data, $p -> $p.name)` |
| `$filter` | Filters elements based on a condition. | `$filter(data, $p -> $p.age > 20)` |
| `$merge` | Merges objects into a single object. | `$merge([$a, $b])` |
| `$distinct` | Returns unique values from an array. | `$distinct(data)` |
| `$sort` | Sorts an array. | `$sort(data)` |
| `$count` | Counts elements in an array. | `$count(data)` |

## JSONata

Explore the full potential of JSONata by visiting their official documentation for detailed guidance and advanced examples: <https://docs.jsonata.org/overview.html>.