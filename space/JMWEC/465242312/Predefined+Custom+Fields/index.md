# Predefined Custom Fields

This page explains how to access the value of Predefined custom fields using Nunjucks. Each field's structure is explained with examples. To understand how to *write* values into these fields see, [Text input for fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/) and [JSON input for fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/).

It is now possible to access any field of an issue by its *Field name* or *ID*. Click [here](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html) to know how to find the *ID* of custom fields.

**Example:**

`{{ issue.fields.Account.name }}` and `{{ issue.fields.customfield_10003.name }},` both return the *name* of the selected Tempo account.

When the field *name* contains a space or any special character, you need to use the array syntax to access the field:

**Example:**

`{{ issue.fields['Capture for JIRA Browser'] }}`

`{{ issue.fields['[CHART] Date of First Response'}}`

**In this page:**

### Capture for JIRA fields

#### Capture for JIRA Browser

- **Field name:** `Capture for JIRA Browser`
- **Description**: The Capture for JIRA Browser field is a string representation of a multi-line text describing the browser of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA Browser f*****ield**:

  - Capture for JIRA Browser field of the issue: `{{ issue.fields['Capture for JIRA Browser'] }}`

#### Capture for JIRA Document Mode

- **Field name:** `Capture for JIRA Document Mode`
- **Description**: The Capture for JIRA Document Mode field is a string representation of a multi-line text describing the document mode of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA Document Mode f*****ield**:

  - Capture for JIRA Document mode field of the issue: `{{ issue.fields['Capture for JIRA Document Mode'] }}`

#### Capture for JIRA jQuery Version

- **Field name:** `Capture for jQuery Version`
- **Description**: The Capture for JIRA jQuery Version field is a string representation of a multi-line text describing the jQuery version of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA jQuery Version f*****ield**:

  - Capture for JIRA jQuery version field of the issue: `{{ issue.fields['Capture for jQuery Version'] }}`

#### Capture for JIRA Operating System

- **Field name:** `Capture for JIRA Operating System`
- **Description**: The Capture for JIRA Operating system field is a string representation of a multi-line text describing the operating system of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA Operating System f*****ield**:

  - Capture for JIRA Operating System field of the issue: `{{ issue.fields['Capture for JIRA Operating System'] }}`

#### Capture for JIRA Screen Resolution

- **Field name:** `Capture for JIRA Screen Resolution`
- **Description**: The Capture for JIRA Screen Resolution field is a string representation of a multi-line text describing the screen resolution of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for Screen resolution*** **field**:

  - Capture for JIRA Screen resolution field of the issue: `{{ issue.fields['Capture for JIRA Screen Resolution'] }}`

#### Capture for JIRA URL

- **Field name:** `Capture for JIRA URL`
- **Description**: The Capture for JIRA URL field is a string representation of a multi-line text describing the URL of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA URL*** **field**:

  - Capture for JIRA URL field of the issue: `{{ issue.fields['Capture for JIRA URL'] }}`

#### Capture for JIRA User Agent

- **Field name:** `Capture for JIRA User Agent`
- **Description**: The Capture for JIRA User agent field is a string representation of a multi-line text describing the user agent of the page captured.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Capture for JIRA User Agent f*****ield**:

  - Capture for JIRA User Agent field of the issue: `{{ issue.fields['Capture for JIRA User Agent'] }}`

#### Raised during

- **Field name:** `Raised during`
- **Description**: The Raised during field is a string representation of a number which is the ID of the session the issue was raised in.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Raised during f*****ield**:

  - Raised during field of the issue: `{{ issue.fields['Raised during'] }}`

#### Test sessions

- **Field name:** `Test sessions`
- **Description**: The Test sessions field is a string representation of a number which is the ID of the session issue belongs to.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Test Sessions f*****ield**:

  - Test Sessions field of the issue: `{{ issue.fields['Test sessions'] }}`

#### Testing status

- **Field name:** `Testing status`
- **Description**: The Testing status field is a string representation of a text describing the status of the issue in a session.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Testing status f*****ield**:

  - Testing status field of the issue: `{{ issue.fields.customfield_xxxxx }}`

### Jira Software fields

#### Epic Color

- **Field name:** `Epic Color`
- **Description**: The Epic color field is a string representation of a text describing the color of the Epic.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Epic color*** **field**:

  - Epic color: `{{ issue.fields['Epic Color'] }}`

#### Epic Link

- **Field name:** `Epic Link`
- **Description**: The Epic link field is a string representation of the issue key.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Epic Link*** **field**:

  - Epic link: `{{ issue.fields['Epic Link'] }}`

#### Epic Name

- **Field name:** `Epic Name`
- **Description**: The Epic name field is a string representation of a multi-line text describing the name of the Epic.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Epic name*** **field**:

  - Epic name: `{{ issue.fields['Epic Name'] }}`

#### Epic Status

- **Field name:** `Epic Status`
- **Description**: The Epic status field is an object representing the status of the Epic.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Epic status*** **field**:

  - Epic status value: `{{ issue.fields['Epic Status'].value }}`
  - Epic status ID: `{{ issue.fields['Epic Status'].id }}`

#### Flagged

- **Field name:** `Flagged`
- **Description**: The Flagged field is an array of objects. Each object represents an option of the checkbox. By default, there's only one possible value: `Impediment`
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Flagged*****field**:

  - The value of the last option selected in the Flagged field

    ```text
    {{ issue.fields["Flagged"] | last | field("value") }}
    ```
  - Display the values of all selected options, separated by a comma:

    ```text
    {{ issue.fields["Flagged"] | join(",","value") }}
    ```
  - Test whether the issue has been flagged:

    ```text
    {{ issue.fields["Flagged"] | find({"value":"Impediment"}) != null }}
    ```

#### Sprint

- **Field name:** `Sprint`
- **Description**: The Sprint field is an array of strings.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Sprint*** **field**: Because each string is an internal representation of a Sprint, accessing this field is not of much use.

#### Story Points

- **Field name:** `Story Points`
- **Description**: The Story points field is a string representation of a number describing the number of story points.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Story points*** **field**:

  - Story points of the issue: `{{ issue.fields.customfield_xxxxx }}`
  - Increase the story points by 10:

    ```text
    {% set SP = issue.fields['Story Points'] %}
    {{ SP + 10 }}
    ```

### Jira Service Desk fields

#### Approvals

- **Field name: Approvals**
- **Description**: The Approvals field is a string representation of a multi-line text describing the search options for Jira Service Desk approvals information.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Approvals*** **field**: Accessing this field is not of much use.

#### Approvers

- **Field name:** `Approvers`
- **Description**: The Approvers field is an array of object. Each object represents an approver.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Approvers*** **field**:

  - Name of the last approver of the issue: `{{ issue.fields.Approvers | last |field("accountId") }}`
  - On reopening an issue, set the assignee to the user selected on the transition screen, only if the user belongs to the approvers. If not, set the assignee field to the first approver:

    **Example**

    ```text
    {% set assignee = issue.fields.Assignee.accountId %}
    {% set users = issue.fields.Approvers %}
    {% set var = false %}
    {% for user in users %}
    	{% if user.accountId == assignee %}
    		{% set var = true %}
    	{%endif%}
    {% endfor %}
    	{% set var = true %}
    {% if not var %}
    	{%set firstuser = users | first %}
    	{{ firstuser.accountId }}
    {%endif%}
    ```

    Select `Ignore empty value` option in the post-function configuration, so as to not clear the field if the value is empty or null.
  - Display all the users in the approvers field with their display name and email address separated by a hyphen:

    ```text
    {% set users = issue.fields.Approvers %}
    {% for user in users %}
    	{{ user.displayName }} - {{ user.emailAddress }}
    {% endfor %}
    ```

#### Customer Request Type

- **Field name:** `Customer Request Type`
- **Description**: The Customer request type field represents an object describing the information about the Service Desk used to create the ticket.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Customer request type*** **field**:

  - Name of the Customer request type: `{{ issue.fields['Customer Request Type'].requestType.name }}`
  - Description of the Customer request type: `{{ issue.fields['Customer Request Type'].requestType.description }}`

#### Organizations

- **Field name:** `Organizations`
- **Description**: The Organizations is a collection of objects. Each object represents an Organization.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Organizations*** **field**:

  - Name of the first Organization the issue belongs to: `{{ issue.fields.Organizations | first | field("name") }}`

#### Request participants

- **Field name:** `Request participants`
- **Description**: The Request Participants is an array of objects. Each object represents a participant.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Request Participants*** **field**:

  - Name of the first participant: `{{ issue.fields['Request participants'] | first | field("accountId") }}`

#### Satisfaction

- **Field name:** `Satisfaction`
- **Description**: The Satisfaction field is a string representation of a multi-line text describing the request feedback in Service Desk requests.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Satisfaction*** **field**:  Accessing this field is not of much use.

#### Satisfaction date

- **Field name:** `Satisfaction date`
- **Description**: The Satisfaction date field is a string representation of a datetime.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Satisfaction date*** **field**:
- - Satisfaction date of the issue: `{{ issue.fields['Satisfaction date'] }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

#### Time to first response

- **Field name:** `Time to first response`
- **Description**: The 'Time to first response' field is an object with the following field:

  - `completedCycles`, containing an array of objects. Each object represents a completed cycle.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Time to first response*** **field**:

  - Remaining time of the last completed cycle of the 'Time to first response' SLA:

    {{ issue.fields['Time to first response'].completedCycles | last | field('remainingTime.friendly') }}

#### Time to resolution

- **Field name:** `Time to resolution`
- **Description**: The Time to resolution field is an object with the following field:

  - `completedCycles`, containing an array of objects. Each object represents a completed cycle.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Time to resolution*** **field**:

  - Goal duration of the last completed cycle of the 'Time to resolution' SLA:

    {{ issue.fields['Time to resolution'].completedCycles | last | field("goalDuration.friendly") }}
  - Start time of the first completed cycle of the 'Time to resolution' SLA:

    {{ issue.fields['Time to resolution'].completedCycles | first | field("startTime.friendly") }}

### **Portfolio for JIRA fields**

#### Team

- **Field name:** `Team`
- **Description**: The Portfolio Team field is a string representing the ID of the Portfolio team.
- **Structure:**

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Portfolio Team*** **field**:

  - Portfolio Team field: `{{ issue.fields.Team }}`

### Tempo fields

#### Iteration

- **Field name:** `Iteration`
- **Description**: The Iteration field is a Tempo planner field
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Iteration*** **field**:

  - Iteration: `{{ issue.fields.Iteration}}`

#### Team

- **Field name:** `Team`
- **Description**: The Team field is a string representation of a number describing the ID of the tempo team.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Team*** **field**:

  - Tempo team ID: `{{ issue.fields.Team }}`

#### Tempo Account

- **Field name:** `Account`
- **Description**: The Tempo Account field is an object describing the Tempo account of the issue.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Account*** **field**:

  - Name of the tempo account: `{{ issue.fields.Account.name }}`
  - ID of the tempo account: `{{ issue.fields.Account.id }}`

### Others

#### [CHART] Date of First Response

- **Field name:** `[CHART] Date of First Response`
- **Description**: The [Chart] Date of First Response field is a string representation of a date.
- **Structure**:

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***[Chart] Date of First Response*** **field**:
- - [Chart] Date of First Response: `{{ issue.fields['[CHART] Date of First Response'] }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value