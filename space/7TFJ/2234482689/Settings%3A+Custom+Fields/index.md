# Settings: Custom Fields

![TryItButton (2).png](/cms_trial/assets/54e26556-c792-4371-baaa-7d9562ead8b8.png)

## Endpoint specification

Developer documentation is available! This includes endpoint definitions and all current schemas. You can access it here: [Endpoint specification](https://timehubjra.7pace.com/swagger/index.html?urls.primaryName=7pace+REST+API+v1)

## Actions

```text
GET /api/v1/settings/customFields
```

Custom field settings describe available fields for your account, such as toggles and dropdowns.

## Query parameters

This endpoint currently has no parameters.

## GET

Custom field settings describe available fields for your account, such as toggles and dropdowns. Worklogs (from `/worklogs`) only store field IDs and their values.

To reconstruct the full custom field information, you need to:

1. Fetch the settings once.
2. When reading a worklog, match `customFields.toggle.id` or `customFields.dropdown.id` against the list from `/settings/customFields`.
3. This lets you display the field’s name, value, and type correctly.

Returns an array of objects.

| **Name** | **Type** | **Notes** |
| --- | --- | --- |
| toggle | array | See **Toggles**, below. |
| dropdown | array | See **Dropdowns**, below. |

### Example return

```text
Response (200 OK)
{
    "result": {
        "customFields": {
            "dropdown": [
                {
                    "options": [
                        {
                            "id": "opt-1",
                            "value": "Design",
                            "color": "#4C9AFF",
                            "used": 2
                        },
                        {
                            "id": "opt-2",
                            "value": "Documentation",
                            "color": "#5243AA",
                            "used": 0
                        },
                        {
                            "id": "opt-3",
                            "value": "Requirements",
                            "color": "#DE350B",
                            "used": 0
                        }
                    ],
                    "id": "dropdown-uddw",
                    "name": "Activity Type",
                    "enabled": true,
                    "mandatory": false,
                    "description": "How is this work categorized?"
                }
            ],
            "toggle": [
                {
                    "default": false,
                    "id": "toggle-8dk9",
                    "name": "Billable",
                    "enabled": true,
                    "mandatory": true,
                    "description": "Is this time billable to the client?"
                }
            ]
        }
    }
}
```

## Toggles

The objects in this array include all toggle fields created through the custom fields functions. See [Working with custom fields](/cms_trial/space/7TFJ/1355415553/Working+with+Custom+Fields/) for more information.

### Returns

Returns an array of objects.

| **Name** | **Type** | **Notes** |
| --- | --- | --- |
| id | string | The ID of the toggle custom field. Match to the [Worklogs](/cms_trial/space/7TFJ/2233401473/Worklogs/) customField ID to see the value for a specific worklog. |
| value | boolean |  |

## Dropdowns

The objects in this array include all dropdown fields created through the custom fields functions. See [Working with custom fields](/cms_trial/space/7TFJ/1355415553/Working+with+Custom+Fields/) for more information.

### Returns

Returns an array of objects

| **Name** | **Type** | **Notes** |
| --- | --- | --- |
| id | string | The ID of the dropdown custom field. Match to the [Worklogs](/cms_trial/space/7TFJ/2233401473/Worklogs/) customField ID to see the value for a specific worklog. |
| value | array | Array of strings. |