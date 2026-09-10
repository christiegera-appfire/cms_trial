# Custom Reports variable contexts

## Context variables in JSONPath/JSONata expressions

Context variables such as `$`, `$current`, `$root`, and `$initial` are used in JSONPath or JSONata expressions. See [JSONata documentation](https://jsonata.org/) for syntax and usage details.

A report is structured in three stages:

1. **Data fetching**: Sources include REST APIs, documents, and input variables.
2. **Data processing**: JSONPath/JSONata expressions are used to transform or extract data. Context variables apply at this stage.
3. **Component rendering**: Data is displayed using nodes such as `text`, `image`, or `table`.

## Where JSONPath expressions are valid

Expressions can be used in two main ways:

- **Dynamic attributes**: Any node attribute starting with `$` can use JSONPath.

  ```text
  {
    "type": "text",
    "style": { "color": "$.results[0].color" },
    "text": "$.results[0].text"
  }
  ```
- **Interpolated properties**: Some nodes support text templates with `{{expression}}` syntax.

  ```text
  {
    "type": "image",
    "src": "http://myapi.com/customers/{{$.customer.id}}.gif"
  }
  ```

---

### Debugging tips

Use `{ "type": "json" }` as a child of a REST node to inspect context data. This is a useful pattern for debugging and may be documented officially in future updates.

## $current

When you make an API call and transform the data using the REST node, the call stores a new context. By default, the data from that call is only available in the children of the current context. This also applies to the **selector** nodes, which do transform data.

Current Variables are accessed by children of an originating node declaration, using a format of `{{$.var_name}}` or `{{var_name}}` (either is functionally equivalent),like the example below:

![Node showing an example 'age' variable.](/cms_trial/assets/6c72b489-74ad-4a50-84ba-084c3c456ab5.png)

![Dashboard Hub Custom Reports variable contexts editor](/cms_trial/assets/c00000b2-b1a3-4c19-b6da-152198bd4830.png)

## Current context in a Custom Reports gadget

Each rest node in a Custom Reports gadget generates its own data context.

Once the data that has been retrieved by the node is available it will be stored in this new context that will be accessible using the $ symbol.

For example:

```text
{
  type: 'rest',
  uri: 'https://api.spaceflightnewsapi.net/v4/reports/?limit=3',
  id: 'spaceflight',
  children: [
    {
      type: 'json'
    },
    {
        type: 'list',
        path: '$.results',
        style: {
            display: 'block',
            margin: 4,
            padding: 4,
            border: '1px dashed red',
            borderRadius: 5,
        },
        item: [
            {
                type: 'view',
                children: [
                    {
                        type: 'text',
                        text: '{{title}}',
                    },
                ],
            },
        ],
    },
  ],
}
```

We can setup a rest node this way.

We are calling an open API that returns this data:

```text
{
  "count": 1415,
  "next": "https://api.spaceflightnewsapi.net/v4/reports/?limit=3&offset=3",
  "previous": null,
  "results": [
    {
      "id": 1662,
      "title": "Starliner arrives safely back on Earth",
      "authors": [],
      "url": "https://starlinerupdates.com/starliner-arrives-safely-back-on-earth/",
      "image_url": "https://boeing-jtti.s3.amazonaws.com/wp-content/uploads/2023/02/13165520/docking_with_earth_in_background_out_window.png",
      "news_site": "Boeing",
      "summary": "Boeing’s Starliner landed safely at 12:01 a.m. Eastern time on Saturday, Sept. 7 (1o:01 p.m. Mountain time, on Friday, Sept. 6).  After an extended stay at the International Space Station, Starliner’s reusable crew module touched down at its designated landing site, White Sands Space Harbor at the U.S. Army’s White Sands Missile Range in New [&#8230;]",
      "published_at": "2024-09-07T04:14:32Z",
      "updated_at": "2024-09-07T04:18:06.656360Z"
    },
    {
      "id": 1661,
      "title": "Starliner heads back to Earth",
      "authors": [],
      "url": "https://starlinerupdates.com/starliner-heads-back-to-earth/",
      "image_url": "https://boeing-jtti.s3.amazonaws.com/wp-content/uploads/2023/02/13165520/docking_with_earth_in_background_out_window.png",
      "news_site": "Boeing",
      "summary": "Boeing’s Starliner spacecraft undocked from the International Space Station on Friday, Sept. 6, with separation confirmed at 6:04 p.m. Eastern time. The reusable crew module is expected to land at 12:01 a.m. Eastern time (10:01 p.m. Mountain time) Saturday at White Sands Space Harbor at the U.S. Army’s White Sands Missile Range in New Mexico. [&#8230;]",
      "published_at": "2024-09-06T22:05:02Z",
      "updated_at": "2024-09-06T22:08:02.942704Z"
    },
    {
      "id": 1660,
      "title": "Boeing’s confidence remains high in Starliner’s return with crew",
      "authors": [],
      "url": "https://starlinerupdates.com/boeings-confidence-remains-high-in-starliners-return-with-crew/",
      "image_url": "https://boeing-jtti.s3.amazonaws.com/wp-content/uploads/2023/02/13165520/docking_with_earth_in_background_out_window.png",
      "news_site": "Boeing",
      "summary": "Since Starliner’s Crew Flight Test (CFT) launch on June 5, Boeing and NASA have conducted extensive testing of its propulsion system in space and on the ground. Those tests include: 7 ground tests of a Reaction Control System (RCS) thruster pulled from the Starliner-1 Service Module: 1 launch-to-docking test with more than 1,000 pulses to [&#8230;]",
      "published_at": "2024-08-02T23:32:46Z",
      "updated_at": "2024-08-02T23:41:45.178189Z"
    }
  ]
}
```

You can access this from any child node using the following syntax:

- `$.results` accesses the entire list of results (in this case, three results).
- `$.results.[0``]` accesses the first element of the results list.
- `$.results.[2].title` accesses the `title` attribute of the third element (lists are 0-indexed). For example: `"Boeing’s confidence remains high in Starliner’s return with crew"`.

In this example, the only child node for this REST node is a list node.

Using the `path` attribute, we specify that `"results"` is the root of the data the list node will process.

For each value in the list, a text node is generated showing only the `title`. You can experiment by changing it to use, for example, `news_site`, and observe how the output changes.

Here is another example using a different API.

```text
{
  type: 'rest',
  uri: 'https://www.thecolorapi.com/scheme?format=json&hex=9369c4',
  id: 'scheme',
  children: [
    { type: 'json'},
    {
          type: 'list',
          path: '$.colors',
          style: {
              display: 'block',
              margin: 4,
              padding: 4,
              border: '1px dashed red',
              borderRadius: 5,
          },
          item: [
              {
                  type: 'view',
                  children: [
                      {
                          type: 'text',
                          text: '{{name.value}}',
                      },
                  ],
              },
          ],
      },
  ]
}
```

Here we are doing almost the same, but using a different API that returns the data in this format (the output has been limited for the sake of simplicity):

```text
{
  "mode": "monochrome",
  "count": 3,
  "colors": [
    {
      "hex": {
        "value": "#54337A",
        "clean": "54337A"
      },
      "rgb": {
        "fraction": {
          "r": 0.32941176470588235,
          "g": 0.2,
          "b": 0.47843137254901963
        },
        "r": 84,
        "g": 51,
        "b": 122,
        "value": "rgb(84, 51, 122)"
      },
      "hsl": {
        "fraction": {
          "h": 0.744131455399061,
          "s": 0.41040462427745666,
          "l": 0.3392156862745098
        },
        "h": 268,
        "s": 41,
        "l": 34,
        "value": "hsl(268, 41%, 34%)"
      },
      "hsv": {
        "fraction": {
          "h": 0.744131455399061,
          "s": 0.5819672131147541,
          "v": 0.47843137254901963
        },
        "value": "hsv(268, 58%, 48%)",
        "h": 268,
        "s": 58,
        "v": 48
      },
      "name": {
        "value": "Minsk",
        "closest_named_hex": "#3F307F",
        "exact_match_name": false,
        "distance": 961
      },
      "cmyk": {
        "fraction": {
          "c": 0.3114754098360658,
          "m": 0.5819672131147543,
          "y": 0,
          "k": 0.5215686274509803
        },
        "value": "cmyk(31, 58, 0, 52)",
        "c": 31,
        "m": 58,
        "y": 0,
        "k": 52
      },
      "XYZ": {
        "fraction": {
          "X": 0.29372627450980393,
          "Y": 0.2476156862745098,
          "Z": 0.4849466666666667
        },
        "value": "XYZ(29, 25, 48)",
        "X": 29,
        "Y": 25,
        "Z": 48
      },
      "image": {
        "bare": "https://www.thecolorapi.com/id?format=svg&named=false&hex=54337A",
        "named": "https://www.thecolorapi.com/id?format=svg&hex=54337A"
      },
      "contrast": {
        "value": "#ffffff"
      },
      "_links": {
        "self": {
          "href": "/id?hex=54337A"
        }
      },
      "_embedded": {}
    },
    {
      "hex": {
        "value": "#6D419F",
        "clean": "6D419F"
      },
      "rgb": {
        "fraction": {
          "r": 0.42745098039215684,
          "g": 0.2549019607843137,
          "b": 0.6235294117647059
        },
        "r": 109,
        "g": 65,
        "b": 159,
        "value": "rgb(109, 65, 159)"
      },
      "hsl": {
        "fraction": {
          "h": 0.7446808510638298,
          "s": 0.41964285714285715,
          "l": 0.4392156862745098
        },
        "h": 268,
        "s": 42,
        "l": 44,
        "value": "hsl(268, 42%, 44%)"
      },
      "hsv": {
        "fraction": {
          "h": 0.7446808510638298,
          "s": 0.5911949685534591,
          "v": 0.6235294117647059
        },
        "value": "hsv(268, 59%, 62%)",
        "h": 268,
        "s": 59,
        "v": 62
      },
      "name": {
        "value": "Royal Purple",
        "closest_named_hex": "#6B3FA0",
        "exact_match_name": false,
        "distance": 29
      },
      "cmyk": {
        "fraction": {
          "c": 0.3144654088050314,
          "m": 0.5911949685534591,
          "y": 0,
          "k": 0.3764705882352941
        },
        "value": "cmyk(31, 59, 0, 38)",
        "c": 31,
        "m": 59,
        "y": 0,
        "k": 38
      },
      "XYZ": {
        "fraction": {
          "X": 0.37998078431372545,
          "Y": 0.31820078431372545,
          "Z": 0.6312988235294118
        },
        "value": "XYZ(38, 32, 63)",
        "X": 38,
        "Y": 32,
        "Z": 63
      },
      "image": {
        "bare": "https://www.thecolorapi.com/id?format=svg&named=false&hex=6D419F",
        "named": "https://www.thecolorapi.com/id?format=svg&hex=6D419F"
      },
      "contrast": {
        "value": "#ffffff"
      },
      "_links": {
        "self": {
          "href": "/id?hex=6D419F"
        }
      },
      "_embedded": {}
    },
    {
      "hex": {
        "value": "#8657BC",
        "clean": "8657BC"
      },
      "rgb": {
        "fraction": {
          "r": 0.5254901960784314,
          "g": 0.3411764705882353,
          "b": 0.7372549019607844
        },
        "r": 134,
        "g": 87,
        "b": 188,
        "value": "rgb(134, 87, 188)"
      },
      "hsl": {
        "fraction": {
          "h": 0.7442244224422441,
          "s": 0.42978723404255326,
          "l": 0.5392156862745099
        },
        "h": 268,
        "s": 43,
        "l": 54,
        "value": "hsl(268, 43%, 54%)"
      },
      "hsv": {
        "fraction": {
          "h": 0.7442244224422441,
          "s": 0.5372340425531915,
          "v": 0.7372549019607844
        },
        "value": "hsv(268, 54%, 74%)",
        "h": 268,
        "s": 54,
        "v": 74
      },
      "name": {
        "value": "Fuchsia Blue",
        "closest_named_hex": "#7A58C1",
        "exact_match_name": false,
        "distance": 358
      },
      "cmyk": {
        "fraction": {
          "c": 0.2872340425531915,
          "m": 0.5372340425531915,
          "y": 0,
          "k": 0.26274509803921564
        },
        "value": "cmyk(29, 54, 0, 26)",
        "c": 29,
        "m": 54,
        "y": 0,
        "k": 26
      },
      "XYZ": {
        "fraction": {
          "X": 0.4717913725490196,
          "Y": 0.408958431372549,
          "Z": 0.751570980392157
        },
        "value": "XYZ(47, 41, 75)",
        "X": 47,
        "Y": 41,
        "Z": 75
      },
      "image": {
        "bare": "https://www.thecolorapi.com/id?format=svg&named=false&hex=8657BC",
        "named": "https://www.thecolorapi.com/id?format=svg&hex=8657BC"
      },
      "contrast": {
        "value": "#ffffff"
      },
      "_links": {
        "self": {
          "href": "/id?hex=8657BC"
        }
      },
      "_embedded": {}
    }
  ]
}
```

Current contexts are not available to ancestors or siblings; they are encapsulated inside the REST node that defines them.

To access data from a different current context, you must navigate from the root context.

![Custom report current context examples.](/cms_trial/assets/82c6feb6-833f-4c99-b969-9c90e9496c74.png)

## $root

When you make an API call and transform the data using the rest or select node (type: rest or type: select), and you want the data from that call to be available anywhere in the custom report, it must be stored in the root. To accomplish this, use the **id** tag.

In the example below, there are two API calls, one for colors and another for random users. They are both stored in an **id** tag and can be referenced anywhere in a custom report.

```text
  type: 'rest',
  uri: 'https://www.thecolorapi.com/scheme?format+jason&hex+9e5eaf',
  id: 'scheme',
},
//random people mock data
{
  type: 'rest',
  uri: 'https://randomuser.me/api//results=100',
  id: 'people',
  path 'results',
```