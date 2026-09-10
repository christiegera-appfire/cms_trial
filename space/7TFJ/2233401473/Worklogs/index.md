# Worklogs

![TryItButton (2).png](/cms_trial/assets/ee18b6e3-73a1-4159-a074-dfbc60f22a1a.png)

## Endpoint specification

Developer documentation is available! This includes endpoint definitions and all current schemas. You can access it here: [Endpoint specification](https://timehubjra.7pace.com/swagger/index.html?urls.primaryName=7pace+REST+API+v1)

## Actions

```text
GET /api/v1/worklogs
```

Retrieve a paginated list of worklogs with optional filtering criteria. See **Get** below for more details.

```text
POST /api/v1/worklogs
```

Create a new worklog entry. See **Post** below for more details.

```text
PUT /api/v1/worklogs/<worklog id>
```

Update a worklog using the worklog ID. See **Put** below for more details.

```text
DELETE /api/v1/worklogs/<worklog id>
```

Delete a worklog using the worklog ID. See **Delete** below for more details.

## Query parameters

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| before | string | Cursor for pagination of results. Returns results before the specified cursor. |
| after | string | Cursor for pagination of results. Returns results after the specified cursor. |
| externalItemId | array of strings | Filter by external item IDs |
| assigneeId | array of strings | Filter by assignee IDs |
| authorId | array of strings | Filter by author IDs |
| startedAt.start | datetime | Start of worklog date range |
| startedAt.end | datetime | End of worklog date range |
| editedAt.start | datetime | Start of edit date range |
| editedAt.end | datetime | End of edit date range |
| createdAt.start | datetime | Start of create date range |
| createdAt.end | datetime | End of create date range |

### Passing Arrays in Queries

- When passing arrays (e.g., authorId, assigneeId, externalItemId), use comma-separated values:

```text
GET /api/v1/worklogs?authorId=1,2,3,4
```

No need to repeat the parameter. The server automatically splits the values based on commas.

## GET

Retrieve a paginated list of worklogs with optional filtering criteria.

### Returns

| **Name** | **Type** | **Notes** |
| --- | --- | --- |
| id | string | UUID. Does not change. |
| comment | string | Optional text entered by user, typically describing work performed. |
| startedAt | string | Date-time. UTC datetime when the user started the work being logged. |
| createdAt | string | Date-time. UTC datetime when the worklog was created in the system. |
| editedAt | string | Date-time. UTC datetime when the worklog was last modified. |
| assigneeId | string | Jira User ID. The user to whom the worklog belongs. |
| authorId | string | Jira User ID. The user who originally created the worklog. |
| accountId | string | Jira Account ID. |
| editorId | string | Jira User ID. The user who last edited the worklog. |
| duration | integer | Total time recorded for the worklog in seconds. |
| externalItemId | string | Jira Work Item ID. The internal, immutable ID for the work item associated to the worklog.   [note icon] **Note**: this is not the issue key seen in the Jira UI (for example, "ABC-123"), but the internal ID used by Jira. |
| customFields | ref | See [Custom Fields](/cms_trial/space/7TFJ/2234482689/Settings%3A+Custom+Fields/). |

### Example response

```text
Response (200 OK)
{
    "result": [
        {
            "id": "<id_value>",
            "comment": null,
            "duration": 3600,
            "startedAt": "2025-07-07T13:00:00",
            "createdAt": "2025-07-08T22:23:41.756Z",
            "editedAt": "2025-07-08T22:23:41.756Z",
            "assigneeId": <id_value>,
            "authorId": <id_value>,
            "accountId": <id_value>,
            "editorId": <id_value>,
            "externalItemId": "1035962",
            "customFields": {
                "toggle": [],
                "dropdown": []
            }
        },
        {
            "id": "b44e5547-0910-496e-a549-c5f8eefeac32",
            "comment": "Setup a sandbox environment",
            "duration": 7200,
            "startedAt": "2025-07-07T16:28:01",
            "createdAt": "2025-07-07T22:28:24.108Z",
            "editedAt": "2025-07-07T22:28:24.108Z",
            "assigneeId": <id_value>,
            "authorId": <id_value>,
            "accountId": <id_value>,
            "editorId": <id_value>,
            "externalItemId": "1035600",
            "customFields": {
                "toggle": [],
                "dropdown": []
            }
        }
    ],
    "_links": {
        "self": {
            "href": "https://timehubjra.7pace.com/api/v1/worklogs"
        }
    },
    "pageInfo": {
        "startCursor": "MA==",
        "endCursor": "NA==",
        "hasNextPage": false,
        "hasPreviousPage": false
    }
}
```

## POST

Create a new worklog entry. To set custom fields, provide the custom field ID and the value for that worklog. See [Settings: Custom fields](/cms_trial/space/7TFJ/2234482689/Settings%3A+Custom+Fields/) for more information on retrieving custom field data. When using custom fields, all custom fields must be represented in the request body regardless of the value to be set.

### Example request body

```text
{
  "comment": "Setup of test environment",
  "startedAt": "2025-07-01T12:00:00",
  "assigneeId": "<id_value>",
  "duration": 3600,
  "externalItemId": "423432",
  "customFields": {
    "toggle": [
      {
        "id": "toggle-8dk9",
        "value": false
      }
    ],
    "dropdown": [
      {
        "id": "dropdown-uddw",
        "value": [
          "opt-1"
        ]
      }
    ]
  }
}
```

### Example response

```text
{
    "worklog": {
        "id": "<id_value>",
        "comment": "Setup of test environment",
        "duration": 3600,
        "startedAt": "2025-07-01T12:00:00",
        "createdAt": "2025-07-30T19:47:58.038Z",
        "editedAt": "2025-07-30T19:47:58.038Z",
        "assigneeId": "<id_value>",
        "authorId": "<id_value>",
        "accountId": "<id_value>",
        "editorId": "<id_value>",
        "externalItemId": "423432",
        "customFields": {
            "toggle": [
                {
                    "value": false,
                    "id": "toggle-8dk9"
                }
            ],
            "dropdown": [
                {
                    "value": [
                        "opt-1"
                    ],
                    "id": "dropdown-uddw"
                }
            ]
        }
    }
}
```

![7pace Timetracker for Jira successful worklog POST request in Postman](/cms_trial/assets/fc6ed515-470b-43ee-af73-d548262fdc14.png)![7pace Timetracker for Jira successful worklog POST response](/cms_trial/assets/64edf9a4-5821-4b32-b3c5-7edead2b4491.png)

## PUT

Update a worklog using the worklog ID. When making an update, you must include the entire worklog object, changing the values for fields you want to update and including the fields you do not want to change (passing the original values). It is highly recommended that you use GET to retrieve the worklog then make the necessary changes with a PUT action.

### Example request body

Using the example POST from above, update the **duration** value and the custom field **toggle-8dk9**.

```text
{
    "comment": "Setup of test environment",
    "duration": 4800,
    "startedAt": "2025-07-01T12:00:00",
    "assigneeId": "<assignee_id>",
    "externalItemId": "423432",
    "customFields": {
        "toggle": [
            {
                "value": true,
                "id": "toggle-8dk9"
            }
        ],
        "dropdown": [
            {
                "value": [
                    "opt-1"
                ],
                "id": "dropdown-uddw"
            }
        ]
    }
}
```

### Example response

```text
{
    "worklog": {
        "id": "<id_value>",
        "comment": "Setup of test environment",
        "duration": 4800,
        "startedAt": "2025-07-01T12:00:00",
        "createdAt": "2025-07-30T19:47:58.038Z",
        "editedAt": "2025-07-31T16:57:05.205Z",
        "assigneeId": "<assignee_id>",
        "authorId": "<author_id>",
        "accountId": "<account_id>",
        "editorId": "<editor_id>",
        "externalItemId": "423432",
        "customFields": {
            "toggle": [
                {
                    "value": true,
                    "id": "toggle-8dk9"
                }
            ],
            "dropdown": [
                {
                    "value": [
                        "opt-1"
                    ],
                    "id": "dropdown-uddw"
                }
            ]
        }
    }
}
```

![7pace Timetracker for Jira successful worklog PUT request in Postman](/cms_trial/assets/0693707b-3f4a-4c4e-aa29-85d9c11e51d4.png)

## DELETE

Delete a worklog using the worklog ID.

### Example response

![7pace Timetracker for Jira successful worklog DELETE request in Postman](/cms_trial/assets/e6108a99-5fe3-42e3-9498-1cb28df52fb2.png)