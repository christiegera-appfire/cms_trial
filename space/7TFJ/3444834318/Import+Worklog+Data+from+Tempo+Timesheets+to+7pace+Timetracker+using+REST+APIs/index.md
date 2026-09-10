# Import Worklog Data from Tempo Timesheets to 7pace Timetracker using REST APIs

![image for instruction.png](/cms_trial/assets/a8a7df0c-9349-40e5-9b18-9774a25522cb.png)

This guide explains how to perform a one-time historical import of your worklog data from **Tempo Timesheets** (Jira Cloud) into **7pace Timetracker** using the REST APIs of both platforms.

---

## Import Process High-Level Overview

The import process consists of the following stages:

1. Initial configuration of source Tempo Timesheets and target 7pace Timetracker - a series of actions to ensure accurate migration of all needed data.
2. Background migration of all historical worklogs up to a specified cut-off date - creating a readonly copy of historical worklogs in 7pace up to a specific date.
3. Starting to use 7pace Timetracker as a daily time-tracking tool.

To complete the import, you will need to write a script that pulls data from Tempo, transforms it, and pushes it to 7pace, using the public REST APIs of both products.

### API Technical Specifications

| **Platform** | **API Documentation** |
| --- | --- |
| Tempo API | <https://apidocs.tempo.io/> |
| 7pace Timetracker | <https://timehubjra.7pace.com/swagger/index.html> |

The proposed migration strategy is to specify a cut-off date for using 7pace Timetracker.

For example, if a cut-off date is February 15, 2026, all worklogs up to and including February 15, 2026 will be migrated to 7pace in **read-only mode**. From the following day, February 16, 2026, users are expected to log their time using 7pace Timetracker, without adding new data to the previously used solution.

## Configure worklogs access for importing user

Migration will be executed on behalf of a specific user, and the pool of migrated worklogs **is limited by this user's permissions**. **Administrators are also subject to this limitation**. To access more worklogs, the user must have proper permissions in place. As described in this article, the user must configure one of the following permissions <https://help.tempo.io/kb/latest/worklog-of-users-not-visible>

#### All worklogs in the instance

Assign the user a role in “Permission Roles,” as shown in the screenshot below.

Caution: The UI for adding the user to the group is not intuitive. You may need to enter the full email address to display the Jira user's full name.

![image for instruction.png](/cms_trial/assets/a8a7df0c-9349-40e5-9b18-9774a25522cb.png)

#### More granular permissions

All of the below require “[Browse Projects](https://help.tempo.io/timesheets/latest/project-permissions) permission for the Jira project”:

- Tempo team level
- Tempo project level
- Jira project level

## Set up authentication

To enable the script to interact with both Tempo and 7pace APIs, set up authentication tokens with the required permission scopes.

### Tempo API Token

Token must be created by a user who can access **all data intended for migration**.

1. Go to: *Tempo Timesheets → Settings → Data Access → API Integration → New Token.*
2. Select the Custom Access radio-button. Check appropriate scopes:

   1. *Worklogs scope* → *View worklogs*
3. Fill in all required fields and click the Confirm button.
4. The token has been created. Make sure to **copy the token in the pop-up and store it in a secure place**, as the value is not accessible after the window is closed.

### 7pace Timetracker API Token

Token must be created by a user who has **7pace role “Admin” assigned**.

1. Go to: *7pace Timetracker → Settings → API Tokens → Create token.*
2. Fill in all required fields and click the Create button.
3. The token has been created. Make sure to **copy the token on the pop-up and store it in a secure place**, as the value is not accessible after the window is closed.

## Migrate Tempo work attributes → 7pace Custom Fields

7pace Timetracker offers Custom Fields to extend each worklog with data beyond standard fields. Use the following instructions to migrate Tempo Work Attributes definitions.

The table below shows which Tempo “Work Attributes” can be mapped to 7pace “Custom Fields.” For data types that are currently *Not supported*, consider serializing the data into the text Description field in a 7pace worklog, or discarding the data from migration.

| **Tempo** | **7pace** |
| --- | --- |
| Checkbox | Toggle |
| Static list | Dropdown |
| Account | *Not supported* |
| Dynamic Dropdown | *Not supported* |
| Input Field | *Not supported* |
| Numeric Input Field | *Not supported* |

### Attributes Migration Process

Tempo provides an endpoint to list all work attributes:

`GET https://api.tempo.io/4/work-attributes`

For each supported attribute, create a corresponding custom field using the instructions below. Use the following table to determine how to map and create corresponding 7pace custom fields.

Keep in mind that 7pace currently allows **up to 10 enabled custom fields**.

When 7pace Timetracker is installed, a default required custom field “Billable” is defined. Make sure to confirm it exists by using endpoint: *GET /api/v2/settings/customFields*   
If having such field is undesired, remove it with endpoint: *DELETE /api/v2/settings/customFields/{customFieldId}*

#### Common Fields for All Types

| Tempo Field | 7pace Field | How to Map |
| --- | --- | --- |
| `key` (text) | `id` (text) | Do not migrate this field. Instead for each migrated Tempo attribute, make sure you map `key` to the 7pace field `id` returned by the endpoint for worklog migration. |
| `name` (text) | `name` (text) |  |
| `required` (boolean) | `mandatory` (boolean) |  |
|  | `enabled` (boolean) | Set to `true` |
|  | `description` (text) | Optional: describe how this field should be used |

#### Additional fields for Tempo attributes with `type = CHECKBOX` (-> 7pace Toggle)

| Tempo Field | 7pace Field | How to Map |
| --- | --- | --- |
|  | `default` (boolean) | The default state (true/false) for the toggle. |

Use endpoint `POST /api/v2/settings/customFields/toggle` to create a 7pace custom field of this type.

#### Additional fields for Tempo attributes with `type = STATIC_LIST` (-> 7pace Dropdown)

| Tempo Field | 7pace Field | How to Map |
| --- | --- | --- |
| `values` (text[])  `names` (text[]) | `options` | For each object in `value`, find a corresponding entry in `names`.  Example:  **Tempo**  ```text "values": [   "e0f529b3-267c-4887-b6b8-2ecd3716dddc",   "990fcd94-70ef-41b3-8f3b-c8bf55ba2348" ], "names": {   "e0f529b3-267c-4887-b6b8-2ecd3716dddc": "abc",   "990fcd94-70ef-41b3-8f3b-c8bf55ba2348": "def" } ```  **7pace**  ```text "options": [   {     "value": "abc",     "color": "#DE350B"   },   {     "value": "def",     "color": "#4C9AFF"   } ] ``` |

Use endpoint `POST /api/v2/settings/customFields/dropdown` to create a 7pace custom field of this type.

## Historical Worklogs Migration

After completing the configuration steps, start the historical read-only worklog migration.

Worklogs should be migrated in chunks (i.e.: daily, week-by-week or monthly), to ensure the ability to checkpoint the process and enable easier error management if issues occur. Migration should be executed **going backwards from the cut-off date**, for example: first batch should cover worklogs from February 15, 2026, second from February 14, 2026, … . This strategy prioritizes migration of the most recent worklogs. While the process continues migrating older data in the background, **users could potentially start using the solution already**.

Each migration batch should follow the steps described below.

### Step 1: Exporting Worklogs from Tempo

Tempo provides an endpoint to bulk-export worklogs.

**Tempo Endpoint:**   
`GET https://api.tempo.io/4/worklogs`

**Query Parameters:**

- `from`: Start date (e.g., `2023-01-01`)
- `to`: End date (e.g., `2023-01-31`)
- `limit`: Set to `1000`
- `offset`: Used for pagination (start at `0`)
- `orderBy`: set to `START_DATE_TIME` to order worklogs from most recent to oldest

**Example Request:**

```text
curl --request GET 'https://api.tempo.io/4/worklogs?from=2026-05-31&to=2026-06-04&offset=0&limit=1000&orderBy=START_DATE_TIME' \
  --header 'Authorization: Bearer YOUR_TEMPO_TOKEN'
```

**Data:** Worklogs are embedded in the `results` array.

**Pagination**: Check the `metadata.next` field in the response. If it exists, use that URL to fetch the next page of results until no more pages are returned for your date range.

Consult Tempo API docs for reference: <https://apidocs.tempo.io/#tag/Worklogs/operation/getWorklogs>

---

### Step 2: Mapping the Data

For each worklog returned by Tempo, you need to map its fields to the format expected by the 7pace API.

| Tempo Field | 7pace Field | How to Map |
| --- | --- | --- |
| `issue.id` (integer) | `externalItemId` (text) | Pass the value directly, treating the number as a text value. |
| `timeSpentSeconds` (integer) | `duration` (integer) | Pass the seconds directly. |
| `description` (text) | `comment` (text) | Pass the text directly. |
| `author.accountId` (text) | `assigneeId` (text) | Pass the Jira Cloud account ID directly |
| `startDate` (text) + `startTime` (text) | `startedAt` (text) | Combine them into an ISO 8601 string without a timezone. *(See Timezones below)* |

#### Handling Timezones

Tempo returns `startDate` (e.g., `"2023-01-05"`) and `startTime` (e.g., `"14:30:00"`) **in the author's local timezone**.

7pace Timetracker stores time without enforcing a global timezone so that times are displayed exactly as the author intended.

**What you need to do:**   
Simply combine Tempo's date and time into a single string with a `T` in the middle: `YYYY-MM-DDTHH:mm:ss`. **Do not add a timezone offset** (like `+00:00` or `Z`).

*Example:* Tempo `"2023-01-05"` and `"14:30:00"` becomes `"2023-01-05T14:30:00"` in 7pace.

#### Mapping Custom Fields

Tempo work attributes can be mapped to 7pace custom fields by passing the `customFields` array in your payload.

**Example Payload with Custom Fields:**

```text
{
  "duration": 3600,
  "comment": "Working on the new feature",
  "startedAt": "2023-01-05T14:30:00",
  "assigneeId": "557058:295406f3-a1fc-4733-b906-dd15d021bd79",
  "externalItemId": "10024",
  "customFields": [
    {
      "type": "toggle",
      "id": "7pace-toggle-field-id",
      "value": true
    },
    {
      "type": "dropdown",
      "id": "7pace-dropdown-field-id",
      "value": {"id": "<option-id>"}
    }
  ]
}
```

---

### Step 3: Importing into 7pace

Once your data is mapped, send it to the 7pace Public REST API to create the worklogs.

**7pace Endpoint:** `POST https://timehubjra.7pace.com/api/v2/worklogs/migrated`

**Example Payload:**

```text
{
  "duration": 3600,
  "comment": "Working on the new feature",
  "startedAt": "2023-01-05T14:30:00",
  "assigneeId": "557058:295406f3-a1fc-4733-b906-dd15d021bd79",
  "externalItemId": "10024"
}
```

**Example Request:**

```text
curl --request POST 'https://timehubjra.7pace.com/api/v2/worklogs/migrated' \
  --header 'Authorization: Bearer YOUR_7PACE_TOKEN' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "duration": 3600,
    "comment": "Working on the new feature",
    "startedAt": "2023-01-05T14:30:00",
    "assigneeId": "557058:295406f3-a1fc-4733-b906-dd15d021bd79",
    "externalItemId": "10024"
  }'
```

---

## Best Practices, Constraints, and Known Issues

When writing your import script, keep the following limits and behaviors in mind to ensure a smooth migration.

### Tempo API Rate Limiting

- Tempo enforces a strict limit of **5 requests per second**. Wait at least 1,000ms between requests to be safe. If you hit a **429 Too Many Requests** error, your script should pause for at least 1-2 seconds with exponential backoff before retrying.
- If your script repeatedly ignores 429 errors and continues sending requests at a high rate, Tempo may temporarily block your IP address.

### 7pace API Rate Limiting

- 7pace might enforce a limit of **200 requests per minute**. Requests beyond this limit will be rejected with **HTTP 429** response status code. In such case, it is advised to slow down migration process to match the rate.
- It is allowed to migrate the source data using parallel processes, keeping in mind the rate limit that applies to all processes in total.

### Import History Tracking

The 7pace public API does not natively deduplicate historical imports. If you run your script twice for the same date range, you will create duplicate worklogs. **Ensure your script tracks which Tempo worklogs have already been successfully imported** (e.g., by logging the `tempoWorklogId` locally).

### Prevent Duplicated Worklogs in 7pace Timetracker on API Errors

Although uncommon, the 7pace REST API may occasionally return a transient error status code. If this happens during an operation that creates or updates a resource (such as a worklog or a setting), we recommend that you:

1. **Confirm whether the change actually took effect.** For example, if a create worklog request appears to fail, use the GET endpoint to check that a worklog with the same metadata does not already exist.
2. **Retry the failed operation** only if the resource was not created or updated.

Following this guidance helps prevent duplicate worklogs in cases where the server saved the data but the client received an error—for example, when the failure occurred while sending the response back to the client.

### Duplicated Worklogs in 7pace Timetracker

When 7pace Timetracker is installed on a customer instance, worklogs from the native Jira time tracker from the last 30 days are automatically imported to 7pace. This also applies to any new or updated worklogs.

Tempo exports its own worklogs to Jira by default, though in limited content and capacity. Due to the import capability described above in 7pace, time managers might see worklogs attributed to the user “Timesheets by Tempo - Jira Time Tracking”.

Therefore, when worklogs are migrated as described in section “Historical Worklogs Migration”, over the period of last 30 days, worklogs could be duplicated in 7pace:

- One set of worklogs created by migration API (“Historical Worklogs Migration"),
- Another set of worklogs created by automated import from Jira native time tracker.

The most reliable way to permanently remove such duplicates is to **remove original worklogs in Tempo** after the migration to 7pace is complete. This will remove worklogs in Jira and in 7pace in an upstream cascade.

For more information about Tempo ↔︎ Jira synchronization, see: <https://help.tempo.io/timesheets/latest/syncing-data-between-jira-and-tempo>

### 7pace Worklogs Are Appearing in Tempo

Customers may observe that worklogs created in 7pace Timetracker also appear in Tempo Timesheets. 7pace Timetracker synchronizes its worklogs to the Jira native time tracker. This, combined with Tempo Timesheets still being active and importing Jira native worklogs, may result in data appearing in Tempo.

#### Scenario 1: Users Start Entering Their Data in 7pace

This is the regular flow. Currently it is not possible to stop synchronization from happening.

#### Scenario 2: Historical Worklogs Have Been Created Using Non-Migration API

The 7pace REST API migration-specific endpoint for creating worklogs, `POST api/v2/worklogs/migrated`, by default prevents pushing worklogs from 7pace to Jira.

If the endpoint `POST api/v2/worklogs` was used to create worklogs during migration, their export will not be suppressed. This will most likely cause duplicated data in Tempo, as 7pace worklogs will overlap with historical Tempo worklogs.

Deleting such worklogs from Tempo will cascade the deletion of corresponding worklogs in 7pace!

‌