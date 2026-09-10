# Get started with Custom Reports

## Overview

In this guide, we’ll walk you through creating your first Custom Report by connecting to an open REST API. Follow these simple steps to set up your datasource, fetch data, and display it on your dashboard!

Open REST API: <https://randomuser.me/api/?results=3>

JSON response

```json
{
  "results": [
    {
      "gender": "male",
      "name": {
        "title": "Mr",
        "first": "Jorge",
        "last": "Silveira"
      },
      "location": {
        "street": {
          "number": 7521,
          "name": "Rua Mato Grosso "
        },
        "city": "Sertãozinho",
        "state": "Pernambuco",
        "country": "Brazil",
        "postcode": 50956,
        "coordinates": {
          "latitude": "-78.6841",
          "longitude": "-111.5651"
        },
        "timezone": {
          "offset": "-10:00",
          "description": "Hawaii"
        }
      },
      "email": "jorge.silveira@example.com",
      "login": {
        "uuid": "8e1c6c97-2bef-49ab-a78e-c33da2c768c6",
        "username": "orangetiger800",
        "password": "hockey1",
        "salt": "iR39MNR4",
        "md5": "63159ddf43eaf10dfdb3a18890b79c81",
        "sha1": "0976fa72a02acb372c016d93e0eac41cece323f4",
        "sha256": "4bf3fd9358288c55092cfe84b8006e29edd5997b39ae2a1c519e09d8109b710c"
      },
      "dob": {
        "date": "1955-11-25T16:33:33.509Z",
        "age": 69
      },
      "registered": {
        "date": "2006-01-03T05:01:02.181Z",
        "age": 18
      },
      "phone": "(61) 7435-7446",
      "cell": "(76) 9063-4030",
      "id": {
        "name": "CPF",
        "value": "017.416.111-43"
      },
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/84.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/84.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/84.jpg"
      },
      "nat": "BR"
    },
    {
      "gender": "female",
      "name": {
        "title": "Ms",
        "first": "Cherly",
        "last": "Duncan"
      },
      "location": {
        "street": {
          "number": 697,
          "name": "Ranchview Dr"
        },
        "city": "Hervey Bay",
        "state": "Australian Capital Territory",
        "country": "Australia",
        "postcode": 2902,
        "coordinates": {
          "latitude": "-9.3319",
          "longitude": "55.4757"
        },
        "timezone": {
          "offset": "-11:00",
          "description": "Midway Island, Samoa"
        }
      },
      "email": "cherly.duncan@example.com",
      "login": {
        "uuid": "b9f0b661-5111-4c62-9312-750b23f01b70",
        "username": "beautifulostrich428",
        "password": "frogman",
        "salt": "jRcWz5Ya",
        "md5": "0990a44618b955a0199f7c1fc326a7be",
        "sha1": "829f81f80c77e40da83598ef71d1f323659bbd34",
        "sha256": "ad94362a9975468361a2432108c9431613aa8396341f3914727c809d46cdc1d4"
      },
      "dob": {
        "date": "1961-12-15T19:39:29.052Z",
        "age": 62
      },
      "registered": {
        "date": "2016-09-19T21:53:28.884Z",
        "age": 8
      },
      "phone": "09-3882-7235",
      "cell": "0408-363-067",
      "id": {
        "name": "TFN",
        "value": "762794031"
      },
      "picture": {
        "large": "https://randomuser.me/api/portraits/women/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/women/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/8.jpg"
      },
      "nat": "AU"
    },
    {
      "gender": "male",
      "name": {
        "title": "Mr",
        "first": "Ceyhun",
        "last": "Pekkan"
      },
      "location": {
        "street": {
          "number": 5966,
          "name": "Necatibey Cd"
        },
        "city": "Siirt",
        "state": "Ağrı",
        "country": "Turkey",
        "postcode": 70616,
        "coordinates": {
          "latitude": "-15.3614",
          "longitude": "-124.7833"
        },
        "timezone": {
          "offset": "-1:00",
          "description": "Azores, Cape Verde Islands"
        }
      },
      "email": "ceyhun.pekkan@example.com",
      "login": {
        "uuid": "b0c6ec05-1a54-4b1f-adc4-b3580d5b51ab",
        "username": "redgorilla214",
        "password": "adams",
        "salt": "vOfO1wXP",
        "md5": "7fb5b32ba8ec53b3502aca1b6c3c78f8",
        "sha1": "71fc56c61d633e1be82e2d35c9201b1ef23be025",
        "sha256": "8bf87045fc3aa9a651ff0790863963b141586f39a40650e914a2cc9073d93d79"
      },
      "dob": {
        "date": "1983-06-30T11:50:27.717Z",
        "age": 41
      },
      "registered": {
        "date": "2017-12-15T16:54:49.189Z",
        "age": 6
      },
      "phone": "(648)-443-0757",
      "cell": "(258)-232-5598",
      "id": {
        "name": "",
        "value": null
      },
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/12.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/12.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/12.jpg"
      },
      "nat": "TR"
    }
  ],
  "info": {
    "seed": "0a2165d5cb728937",
    "results": 3,
    "page": 1,
    "version": "1.4"
  }
}
```

![random_users-table.png](/cms_trial/assets/913f4223-f1b2-4951-8f9c-728bc7526f9b.png)

## Add a Datasource

1. In the **Custom Reports** dashboard view, click the **More actions** ellipses.
2. Select **Add datasource**
3. Provide a meaningful name for your datasource, such as **Random User - No Auth** for this example.
4. Enter the API endpoint URL in the provided field `https://randomuser.me`
5. Set Authentication type: **No Auth** for this example. To understand each authentication type more thoroughly, see [Authentication types in Custom Reports datasources](/cms_trial/space/RDD/1545601193/Authentication+types+in+Custom+Reports+datasources/).
6. Click **Add**.

If you need to learn more about datasources in Dashboard Hub, see [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/).

![DH-more-actions-add-datasource.png](/cms_trial/assets/87055a83-5c16-4a9a-92ed-80291efc6a75.png)![add_datasource_random_user.png](/cms_trial/assets/76b24b68-2cce-4e36-927f-e5c06ea97583.png)

## Add the Custom Reports gadget

1. Open Dashboard Hub in Jira.
2. If you have not created a dashboard,

   1. Click the dashboard dropdown in the left corner or click the **More actions** ellipses in the top right corner, and select **Create dashboard.**
   2. Name your dashboard, then click **Create**.
   3. Click **Add Gadget**.
3. If you already have a dashboard, click **Edit**.
4. Click **Add Gadget**.
5. Type **Custom Reports** in the search bar in the gadget catalog or navigate to the **Custom Reports** section in the left-hand navigation panel.
6. Locate the **Custom Reports** gadget, then click **Add**.
7. Click **Open Editor**.

![add_custom_report_gadget.jpg](/cms_trial/assets/a4c8548b-8149-42d8-a46c-87d64b102321.jpg)

## Example: random users in a table

Copy the JSON content in the following code block on the right. This simple report displays three random people in a table with three columns.

### How it works

1. **Data Fetching**

```json
 uri: 'datasource://random_DS/api/?results=3',
```

The REST API at <https://randomuser.me/api/?results=3> returns a JSON object containing random user details.

The uri section starts with **datasource://random\_DS**, which is the name we use to refer to our datasource field, and follows the rest of the URI **/api/** .

Then we use a query param `?results=3` to return three random users from that API.

![datasource.png](/cms_trial/assets/4efea46d-19e4-4aa3-9666-d86200a36155.png)

1. **Data Parsing and display**

The gadget processes the returned JSON and extracts the *results* array.

```json
path: 'results',
```

A node **type: 'table'** is generated with three columns:

- The Name column displays the user’s picture and full name (title, first, and last).

  - **header: 'Name'**
  - **src: '{{picture.thumbnail}}'**
  - **'{{name.title}} {{name.first}} {{name.last}}'**
- The Age columndisplays the user’s age.

  - **header: 'Age',**
  - **cell: '{{dob.age}}'**
- The Country column displays the user’s country.

  - **header: 'Country',**  
    **cell: '{{location.country}}'**

The dot notation is used to traverse paths in the JSON response.

```json
{
  type: 'rest',
  uri: 'datasource://random_DS/api/?results=3',
  children: [
    {
      type: 'table',
      path: 'results',
      style: {
        flex: 1
      },
      columns: [
        {
          header: 'Name',
          cell: {
            type: 'view',
            style: {
              alignItems: 'center',
              gap: 8,
              fontWeight: '800'
            },
            children: [
              {
                type: 'image',
                style: {
                  width: 40,
                  height: 'auto',
                  borderRadius: '50%'
                },
                src: '{{picture.thumbnail}}'
              },
              '{{name.title}} {{name.first}} {{name.last}}'
            ]
          }
        },
        {
          header: 'Age',
          cell: '{{dob.age}}'
        },
        {
          header: 'Country',
          cell: '{{location.country}}'
        }
      ]
    }
  ]
}
```

Download this JSON response here:

![contentId-1528825149](/cms_trial/assets/5dd71262-68f1-4f94-af27-79089714cb92.json5)

1. **Style**

You need to be familiar with CSS to better style your reports, for example:

```json
style: {
    flex: 1
}
```

This is part of Flexbox styling (ref), commonly used in web development to define how elements are laid out and behave within a flexible container.

---

```text
type: 'image',
style: {
    width: 40,
    height: 'auto',
    borderRadius: '50%'
},
```

This sets the image's width to 40 pixels, automatically adjusts its height to maintain its original aspect ratio, and rounds the image into a circle by applying a radius of 50% of its dimensions.

## Save and publish your report

1. Use the live **Preview** panel to review the final output.
2. Click **Save,** and your report is ready to be [shared](https://appfire.atlassian.net/wiki/label/RDD/sharing) with your colleagues.

## Troubleshooting common issues

1. Error: Cannot connect to datasource:

   - Double-check the API URL and ensure it uses HTTPS.
   - Verify your authentication credentials and token expiration.
2. Visualization problems:

   - Ensure all required fields are correctly mapped in the visualization editor.
3. Use the [**Debug Mode**](/cms_trial/space/RDD/1549304032/Query+and+transform+your+data+with+JSONata/) (toggle in the editor toolbar) to inspect data and ensure the JSON structure matches the visualization requirements.

## Advanced knowledge

To move to the next level of Custom Reports, you should learn:

- [**JSONata**](https://jsonata.org/): JSON query and transformation language.
- **CSS**: To style your reports.
- [**Recharts**](https://recharts.org/en-US/): The composable charting library built on React components behind our charts.

## Next steps

- [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/)
  - [Authentication types in Custom Reports datasources](/cms_trial/space/RDD/1545601193/Authentication+types+in+Custom+Reports+datasources/)
- [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/)
- [Query and transform your data with JSONata](/cms_trial/space/RDD/1549304032/Query+and+transform+your+data+with+JSONata/)
- [Nodes as building blocks for Custom Reports](/cms_trial/space/RDD/1548747137/Nodes+as+building+blocks+for+Custom+Reports/)