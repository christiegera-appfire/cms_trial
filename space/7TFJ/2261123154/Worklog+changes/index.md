# Worklog changes

![TryItButton (2).png](/cms_trial/assets/66cec0cc-104a-417c-9351-acb912bc7c6b.png)

## Endpoint specification

Developer documentation is available! This includes endpoint definitions and all current schemas. You can access it here: [Endpoint specification](https://timehubjra.7pace.com/swagger/index.html?urls.primaryName=7pace+REST+API+v1)

## Actions

```text
GET /api/v1/worklogs/changes
```

Retrieve a paginated list of worklog changes, including deleted worklogs, with optional filtering criteria. See **Get** below for more details.

Use the **editedAt.start** and **editedAt.end** to return a list of all changes for a specified timeframe.

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
GET /worklogs?authorId=1,2,3,4
```

No need to repeat the parameter. The server automatically splits the values based on commas.

## GET

Retrieve a paginated list of worklogs with optional filtering criteria.

### Returns

| **Name** | **Type** | **Notes** |
| --- | --- | --- |
| id | string | UUID. Does not change. |
| isDeleted | boolean | Flag indicating if the worklog has been deleted. |
| comment | string | Optional text entered by user, typically describing work performed. |
| startedAt | string | Date-time. UTC datetime when the user started the work being logged. |
| createdAt | string | Date-time. UTC datetime when the worklog was created in the system. |
| editedAt | string | Date-time. UTC datetime when the worklog was last modified. |
| assigneeId | string | The Jira User ID. The user to whom the worklog belongs. |
| authorId | string | The Jira User ID. The user who originally created the worklog. |
| accountId | string | The Jira Account ID. |
| editorId | string | The Jira User ID. The user who last edited the worklog. |
| duration | integer | Total time recorded for the worklog in seconds. |
| externalItemId | string | The Jira Item ID. The internal, immutable ID for the item associated to the worklog. |
| customFields | ref | See [Custom Fields](/cms_trial/space/7TFJ/1355415553/Working+with+Custom+Fields/). |

### Example response

```text
Response (200 OK)
{
    "result": [
        {
            "id": "<id_value>",
            "isDeleted": true,
            "comment": null,
            "duration": 3600,
            "startedAt": "2025-07-07T13:00:00",
            "createdAt": "2025-07-08T22:23:41.756Z",
            "editedAt": "2025-07-08T22:23:41.756Z",
            "assigneeId": <assignee_id>,
            "authorId": <author_id>,
            "accountId": <account_id>,
            "editorId": <editor_id>,
            "externalItemId": "1035962",
            "customFields": {
                "toggle": [],
                "dropdown": []
            }
        },
        {
            "id": "<id_value>",
            "isDeleted": false,
            "comment": "Setup a sandbox environment",
            "duration": 7200,
            "startedAt": "2025-07-07T16:28:01",
            "createdAt": "2025-07-07T22:28:24.108Z",
            "editedAt": "2025-07-07T22:28:24.108Z",
            "assigneeId": "<assignee_id>",
            "authorId": "<author_id>",
            "accountId": "<account_id>",
            "editorId": "<editor_id>",
            "externalItemId": "1035600",
            "customFields": {
                "toggle": [],
                "dropdown": []
            }
        }
    ],
    "_links": {
        "self": {
            "href": "https://timehubmdy.7pace.com/api/v1/worklogs"
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