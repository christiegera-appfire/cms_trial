# User-created Custom Fields

This page explains how to access the value of User-created custom fields of different field types using Nunjucks. Each field's structure is explained, with examples. To understand how to *write* values into these fields see, [Text input for fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/) and [JSON input for fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/).

It is now possible to access any user-created custom field of an issue by its *Field name* or *ID*. Click [here](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html) to know how to find the *ID* of custom fields.

**Example:**

`{{ issue.fields.Projectpicker.name }}` and `{{ issue.fields.customfield_10302.name }},` both return the *name* of the selected Project.

When the field *name* contains a space or any special character, you need to use the array syntax to access the field:

**Example:**

`{{ issue.fields['Multi user picker'][0].displayName }}`

### Select list

#### Checkboxes / Multi-select list

- **Description**: A field of the type *Checkboxes/Multi-select list*, is an array of objects. Each object represents an option of the checkbox/select list.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Checkboxes/Multi-select list type**:

  - The value of the last option:

    ```text
    {{ issue.fields['Multi-select field'] | last | field("value") }}
    ```
  - Display the values of all selected options, separated by a comma:

    ```text
    {{ issue.fields['Checkboxes field'] | join("," , "value") }}
    ```
  - Test whether a specific option is selected:

    ```text
    {{ issue.fields["Checkboxes field"] | find({"value":"Impediment"}) != null }}
    ```

#### Radio buttons / Single select list

- **Description**: A field of *Radio buttons/Single select list* type is an object describing the selected option.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Radio buttons/Single select list type**:

  - The value of the option: `{{ issue.fields['Single select field'].value }}`

#### Cascading

- **Description**: A field of *Cascading type* is an object representing parent of the cascading with one field:

  - `child`, an object representing the child of the parent.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Cascading type**:

  - The value of the parent of the cascading field: `{{ issue.fields["Cascading field"] }}`
  - The value of the child of the cascading field: `{{ issue.fields["Cascading field"] | field("child.value) }}`
  - Display the parent and child of the cascading field values separated by a comma:

    ```text
    {{ issue.fields['Cascading field'].value }},{{ issue.fields['Cascading field'].child.value }}
    ```

### Groups

#### Single Group Picker

- **Description**: A field of *Single group picker* type is an object that represents the selected group
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Single Group picker type:**

  - Name of the group: `{{ issue.fields['Single group picker field'].name }}`
  - ID of the group: `{{ issue.fields['Single group picker field'].groupId }}`

#### Multi-Group Picker

- **Description**: A field of *Multi-group picker* type is an array of objects. Each object represents a single group.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Multi-group picker type**:

  - Name of the first group:

    ```text
    {{ issue.fields['Multi group picker field'] | first | field("name") }}
    ```
  - ID of the first group:

    ```text
    {{ issue.fields['Multi group picker field'] | first | field("groupId") }}
    ```

### Users

#### Single User picker

- **Description**: A field of *Single user picker* type field is an object that represents the selected user.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Single user picker type**:

  - Display name of the user: `{{ issue.fields['Single user type field'].displayName }}`

#### Multi-user picker

- **Description**: A field of *Multi-user picker type* is an array of objects. Each object represents a single user.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of multi-user type**:

  - Display the users' *username* separated by a comma: `{{ issue.fields['Multi user type field'] | join("," , "accountId") }}`

### Versions

#### Single version picker

- **Description**: A field of *Single version picker* type is an object that represents a single selected version.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Single Version picker type**:

  - Name of the version: `{{ issue.fields['Single version picker field'].name }}`

#### Multi-version picker

- Description: A field of *Multi version picker type* is an array of objects. Each object represents a single version.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Multi version picker type**:

  - First version name: `{{issue.fields['Multi version picker type field'].name}}`
  - Last version name:

    ```text
    {{ issue.fields['Multi version picker type field'] | last | field("name") }}
    ```

    '|' is the pipe operator and 'last' is the filter. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Join the *names* of the version/s, separated by commas: `{{issue.fields['Multi version picker type field'] | join("," , "name")}}`

### Text

#### Single-line text field type

- **Description**: A field of *Single line text type* is a string representation of a single-line text describing the text field.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Single-line text field type**:

  - The text of the field: `{{ issue.fields['Single line text field'] }}`

#### Multi-line text field type

- **Description**: A field of *Multi-line text type* is a string representation of a multi-line text describing the read-only text.is a string that represents a multi-line text.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Multi-line text field type**:

  - The text of the field: `{{ issue.fields['Multi line text'] }}`

### Date/Time picker

#### Date picker type field

- **Description:** A field of *Date picker type* is a String representing the date in [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) format.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Date picker type:**

  - The value of the Date picker field:`{{ issue.fields['DP'] }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

#### Date time picker type field

- **Description:** A field of *Date time picker type* is a String representing the date in [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) format.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Date picker type:**

  - The value of the Date time picker type field:`{{ issue.fields['DTP'] }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

### Others

#### Numeric field

- **Description:** A field of *Numeric type* is a number.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Numeric type**:

  - The value of the field: `{{issue.fields['Numeric field'] }}`
  - The value of the numeric field minus one:

    ```text
    {{ issue.fields['Numeric field'] - 1 }}
    ```

#### Project picker type

- **Description**: A field of *Project picker type* is an object describing a project.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of Project picker type**:

  - Name of the project: `{{ issue.fields['Project picker type field'].name }}`

#### URL field type

- **Description:**A field of *URL type* is a string representation of a URL.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing a field of URL type:**

  - The value of the URL field: `{{ issue.fields['URL field'] }}`