# Custom report example

## Overview

New to custom reports in Dashboard Hub? This article has you covered with a short training video and helpful code snippets you can use to build your first report. Follow along and start customizing with confidence.

### Watch the training video

The following training video uses the code snippets below to introduce many of Dashboard Hub’s custom report features. To get the most out of this experience, open Dashboard Hub and follow along.

### Code snippets

Use the following code snippets to follow along with the training video. For the best results, exit the code editor after every example and discard any existing drafts.

![Discard drafts in between examples.](/cms_trial/assets/c5985e77-0d70-4e4d-bf58-247520140d5e.png)

### Add text to the report

Report descriptor

```text
{
  type: 'view',
  style: { flexDirection: 'column', gap: 40 },
  children: [
    'here will be the table',  
    'beautiful barchart coming',  
  ]
}
```

### Display REST data

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  children: {  
    type: 'view',
    style: { flexDirection: 'column', gap: 40 },
    children: [
      { type: 'json' },
      'here will be the table',  
      'beautiful barchart coming',  
    ]
  }
}
```

### Create a table

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  children: {  
    type: 'view',
    style: { flexDirection: 'column', gap: 40 },
    children: [
      { type: 'json' },
      {
          type: 'table',
          path: '$.results[[0..10]]', 
          columns: [
            {
              header: 'Id',
              accessor: 'id.value',
            },
            {
              header: 'Name',
              accessor: 'name.first',
            },
            { 
              header: 'Birth',
              accessor: 'dob.age',
            },
            {
              header: 'Registered',
              accessor: 'registered.age',
            },
            {
              header: 'Gender',
              accessor: 'gender',
            },
            {
              header: 'Location',
              accessor: 'location.state',
            },
            {
              header: 'Phone',
              accessor: 'phone',
            },
            {
              header: 'Cell',
              accessor: 'cell',
            },
          ],
        },    
      'beautiful barchart coming',  
    ]
  }
}
```

### Customize the table

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  children: {  
    type: 'view',
    style: { flexDirection: 'column', gap: 40 },
    children: [
      { type: 'json' },
      {
          type: 'table',
          path: '$.results[[0..10]]', 
          columns: [
            {
              header: 'Id',
              accessor: 'id.value',
            },
            {
              header: 'Name',
              accessor: 'name.first',
              cell: {
                type: 'view',
                style: {
                  alignItems: 'center',
                  gap: 8,
                  fontWeight: '600',
                  whiteSpace: 'nowrap',
                },
                children: [
                  {
                    type: 'image',
                    style: {
                      width: 40,
                      height: 'auto',
                      borderRadius: '50%',
                    },
                    src: '{{picture.thumbnail}}',
                  },
                  '{{name.title}} {{name.first}} {{name.last}}',
                ],
              },
            },
            { 
              header: 'Birth',
              accessor: 'dob.age',
              cell: '{{$formatDate(dob.date)}} ({{dob.age}} y)',
            },
            { 
              header: 'Decade',
              accessor: 'decade',
            },
            {
              header: 'Registered',
              accessor: 'registered.age',
              cell: '{{$formatDate(registered.date)}} ({{registered.age}} y)',
            },
            {
              header: 'Gender',
              accessor: 'gender',
              cell: {
                type: 'text', 
                style: { fontSize: 20 },
                text: '{{$.gender="female"?"♂":"♀"}}',
              }
            },
            {
              header: 'Location',
              accessor: 'location.state',
              cell: '{{location.country}}, {{location.state}}',
            },
            {
              header: 'Phone',
              accessor: 'phone',
            },
            {
              header: 'Cell',
              accessor: 'cell',
            },
          ],
        },    
      'beautiful barchart coming',  
    ]
  }
}
```

### Populate the Decade column using JSONPath

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  path: '(\
    /* Calculate the decade of birth for each person */\
    $withDecades := $map($.results, function($p) { $merge([{ "decade": $substring($formatDate($p.dob.date), -4, 3) & "0" }, $p]) });\
    { "results": $withDecades }\
  )',  
  children: {  
    type: 'view',
    style: { flexDirection: 'column', gap: 40 },
    children: [
      { type: 'json' },
      {
          type: 'table',
          path: '$.results[[0..10]]', 
          columns: [
            {
              header: 'Id',
              accessor: 'id.value',
            },
            {
              header: 'Name',
              accessor: 'name.first',
              cell: {
                type: 'view',
                style: {
                  alignItems: 'center',
                  gap: 8,
                  fontWeight: '600',
                  whiteSpace: 'nowrap',
                },
                children: [
                  {
                    type: 'image',
                    style: {
                      width: 40,
                      height: 'auto',
                      borderRadius: '50%',
                    },
                    src: '{{picture.thumbnail}}',
                  },
                  '{{name.title}} {{name.first}} {{name.last}}',
                ],
              },
            },
            { 
              header: 'Birth',
              accessor: 'dob.age',
              cell: '{{$formatDate(dob.date)}} ({{dob.age}} y)',
            },
            { 
              header: 'Decade',
              accessor: 'decade',
            },
            {
              header: 'Registered',
              accessor: 'registered.age',
              cell: '{{$formatDate(registered.date)}} ({{registered.age}} y)',
            },
            {
              header: 'Gender',
              accessor: 'gender',
              cell: {
                type: 'text', 
                style: { fontSize: 20 },
                text: '{{$.gender="female"?"♂":"♀"}}',
              }
            },
            {
              header: 'Location',
              accessor: 'location.state',
              cell: '{{location.country}}, {{location.state}}',
            },
            {
              header: 'Phone',
              accessor: 'phone',
            },
            {
              header: 'Cell',
              accessor: 'cell',
            },
          ],
        },    
      'beautiful barchart coming',  
    ]
  }
}
```

### Add a bar chart

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  path: '(\
    /* Calculate the decade of birth for each person */\
    $withDecades := $map($.results, function($p) { $merge([{ "decade": $substring($formatDate($p.dob.date), -4, 3) & "0" }, $p]) });\
    { "results": $withDecades }\
  )',  
  children: {  
    type: 'view',
    style: { flexDirection: 'column', gap: 40 },
    children: [
      { type: 'json' },
      {
          type: 'table',
          path: '$.results[[0..10]]', 
          columns: [
            {
              header: 'Id',
              accessor: 'id.value',
            },
            {
              header: 'Name',
              accessor: 'name.first',
              cell: {
                type: 'view',
                style: {
                  alignItems: 'center',
                  gap: 8,
                  fontWeight: '600',
                  whiteSpace: 'nowrap',
                },
                children: [
                  {
                    type: 'image',
                    style: {
                      width: 40,
                      height: 'auto',
                      borderRadius: '50%',
                    },
                    src: '{{picture.thumbnail}}',
                  },
                  '{{name.title}} {{name.first}} {{name.last}}',
                ],
              },
            },
            { 
              header: 'Birth',
              accessor: 'dob.age',
              cell: '{{$formatDate(dob.date)}} ({{dob.age}} y)',
            },
            { 
              header: 'Decade',
              accessor: 'decade',
            },
            {
              header: 'Registered',
              accessor: 'registered.age',
              cell: '{{$formatDate(registered.date)}} ({{registered.age}} y)',
            },
            {
              header: 'Gender',
              accessor: 'gender',
              cell: {
                type: 'text', 
                style: { fontSize: 20 },
                text: '{{$.gender="female"?"♂":"♀"}}',
              }
            },
            {
              header: 'Location',
              accessor: 'location.state',
              cell: '{{location.country}}, {{location.state}}',
            },
            {
              header: 'Phone',
              accessor: 'phone',
            },
            {
              header: 'Cell',
              accessor: 'cell',
            },
          ],
        },    
      {
        type: 'view',
        children: [
          {
            type: 'chart',
            options: {
              chart: {
                //width: 200,              
                height: 200,
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
              categories: ['1960', '1970', '1980'],
              series: [
                {
                  chartType: 'bar',
                  name: 'Males',
                  stackId: 'a',
                  fill: '#FFBB28',
                  data: [6, 9, 2],
                },
                {
                  chartType: 'bar',
                  name: 'Females',
                  stackId: 'a',
                  fill: '#00C49F',
                  data: [9, 1, 34],
                },
              ],
            },
          },
        ],
        style: {
          flexDirection: 'column',
          height: '100%'
        },
      },  
    ]
  }
}
```

### Finalize the report

Report descriptor

```text
{
  id: 'users',
  type: 'rest',
  uri: 'https://tinyurl.com/mw23fjxx',
  path: '(\
    /* Calculate the decade of birth for each person */\
    $withDecades := $map($.results, function($p) { $merge([{ "decade": $substring($formatDate($p.dob.date), -4, 3) & "0" }, $p]) });\
    /* Extract decades range */\
    $decades := $sort($distinct($map($withDecades, function($p) { $p.decade })));\
    $malesPerDecade := $withDecades[gender="male"]{ decade: $count($) };\
    $malesSeries := $map($decades, function($d) { $lookup($malesPerDecade, $d) });\
    $femalesPerDecade := $withDecades[gender="female"]{ decade: $count($) };\
    $femalesSeries := $map($decades, function($d) { $lookup($femalesPerDecade, $d) });\
    { "results": $withDecades, "data": $withDecades, "decades": $decades, "malesSeries": $malesSeries, "femalesSeries": $femalesSeries }\
  )',
  children: [
    { type: 'json', path: '$.malesSeries', style: { display: 'none' }},
    {
      type: 'view',
      style: { flexDirection: 'column', gap: 40 },
      children: [
        {
          type: 'table',
          path: '$.results[[0..10]]', 
          columns: [
            {
              header: 'Id',
              accessor: 'id.value',
            },
            {
              header: 'Name',
              accessor: 'name.first',
              cell: {
                type: 'view',
                style: {
                  alignItems: 'center',
                  gap: 8,
                  fontWeight: '600',
                  whiteSpace: 'nowrap',
                },
                children: [
                  {
                    type: 'image',
                    style: {
                      width: 40,
                      height: 'auto',
                      borderRadius: '50%',
                    },
                    src: '{{picture.thumbnail}}',
                  },
                  '{{name.title}} {{name.first}} {{name.last}}',
                ],
              },
            },
            { 
              header: 'Birth',
              accessor: 'dob.age',
              cell: '{{$formatDate(dob.date)}} ({{dob.age}} y)',
            },
            { 
              header: 'Decade',
              accessor: 'decade',
            },
            {
              header: 'Registered',
              accessor: 'registered.age',
              cell: '{{$formatDate(registered.date)}} ({{registered.age}} y)',
            },
            {
              header: 'Gender',
              accessor: 'gender',
              cell: {
                type: 'text', 
                style: { fontSize: 20 },
                text: '{{$.gender="female"?"♂":"♀"}}',
              }
            },
            {
              header: 'Location',
              accessor: 'location.state',
              cell: '{{location.country}}, {{location.state}}',
            },
            {
              header: 'Phone',
              accessor: 'phone',
            },
            {
              header: 'Cell',
              accessor: 'cell',
            },
          ],
        },    
        {
          type: 'view',
          children: [
            {
              type: 'chart',
              options: {
                chart: {
                  //width: 200,              
                  height: 200,
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
                    fill: '#FFBB28',
                    data: '$.malesSeries',
                  },
                  {
                    chartType: 'bar',
                    name: 'Females',
                    stackId: 'a',
                    fill: '#00C49F',
                    data: '$.femalesSeries',
                  },
                ],
              },
            },
          ],
          style: {
            flexDirection: 'column',
            height: '100%'
          },
        },      
      ]
    }
  ]
}
```