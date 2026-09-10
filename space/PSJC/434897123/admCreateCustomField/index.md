# admCreateCustomField

## Description

Creates a new custom field, offering support also for setting its context and searcher.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateCustomField(fieldName, description, fieldType, fieldSearcher, projects, issueTypes) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createCF(fieldName, description, fieldType, fieldSearcher, projects, issueTypes) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldName | String | Yes | Custom field name. |
| description | String | Yes | Custom field description (can be blank). |
| fieldType | String | Yes | Custom field type (either key or name). |
| fieldSearcher | String | Yes | Custom field searcher (either key or name). If blank, the default custom field searcher for the given type will be considered. |
| projects | String [] | Yes | Projects context (project keys). If empty, global issue context will be considered. |
| issueTypes | String [] | Yes | Issue types context (either names or ids). If empty, all issue types will be considered. |

## Return Type

**String**

Returns the string id (customfield\_xxxxx) of the newly created custom field.

## Examples

### Example 1

Creating a single line text field with default searcher (Free Text Searcher) and global context:

```javascript
admCreateCustomField("Test Field", "test description", "Text Field (single line)", "", {}, {});
```

### Example 2

Creating a multi-line text field with blank description, specified searcher name (Free Text Searcher) and specified project and issue types context:

```javascript
admCreateCustomField("Test Field", "", "Text Field (multi-line)", "Free Text Searcher", {"DEMO", "TEST"}, {"Bug", "Improvement"});
```

### Example 3

Creating a date picker field with blank description, specified searcher key, and specified issue types ids context:

```javascript
admCreateCustomField("Test Field", "", "Date Picker", "com.atlassian.jira.plugin.system.customfieldtypes:daterange", {}, {1, 2, 3});
```

If the provided custom field searcher key or name is wrong, it will be ignored and the custom field will be created with no searcher configured.

## See also