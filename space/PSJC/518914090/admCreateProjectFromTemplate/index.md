# admCreateProjectFromTemplate

## Description

Creates a new project using one of the many available [project templates](/cms_trial/space/PSJC/532447906/Project+Template+Keys/) for Jira Cloud.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateProjectFromTemplate(template\_key, key, name, description, url, category, defaultUser, assign\_to\_def\_user[,permissionScheme, issueSecurityScheme, notificationScheme]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createProjectFromTemplate(template\_key, key, name, description, url, category, defaultUser, assign\_to\_def\_user[,permissionScheme, issueSecurityScheme, notificationScheme]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| template\_key | string | Yes | The project template key. See [this page](/cms_trial/space/PSJC/532447906/Project+Template+Keys/) for a list of possible values. |
| key | string | Yes | The project key. The value must be unique. |
| name | string | Yes | The project name. The value must be unique. |
| description | string | Yes | The project description. |
| url | string | Yes | The project URL. Leave blank if no URL is available. |
| category | string | Yes | The project category. Leave blank if no category is available. |
| defaultUser | string | Yes | The default project assignee. |
| assign\_to\_def\_user | boolean | Yes | Set to true to assign issues to the user by default. In this case, you must specify a user. |
| permissionScheme | string | No | The permission scheme ID or name. Leave blank if no permission scheme is available. |
| issueSecurityScheme | string | No | The issue security scheme ID or name. Leave blank if no issue security scheme is available. |
| notificationScheme | string | No | The notification scheme ID or name. Leave blank if no notification scheme is available. |

## Return Type

**Boolean**

Returns true if the project has been created.

## Examples

### Example 1

```javascript
string TEMPLATE_KEY="com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking";
string KEY = "NEWPRJ";
string NAME = "New Project";
string DESCRIPTION = "My project";
string URL = "https://appfire.atlassian.net/wiki/spaces/APPFIRE/overview";
string CATEGORY = "TEST";
string DEFAULT_USER = "juser";
boolean ASSIGN_TO_DEF_USER = false;

return admCreateProjectFromTemplate(TEMPLATE_KEY, KEY, NAME, DESCRIPTION, URL, CATEGORY, DEFAULT_USER, ASSIGN_TO_DEF_USER);
```

### Example 2

```javascript
return admCreateProjectFromTemplate("com.atlassian.servicedesk:simplified-general-service-desk-it",
            "SMPRJ",
            "Service Desk Project",
            "My project",
            "https://appfire.atlassian.net/wiki/spaces/APPFIRE/overview",
            "TEST",
            "juser",
            false
            "Default Permission Scheme",
            "Simplified Issue Security Scheme",
            "Default Notification Scheme");
```

## See also