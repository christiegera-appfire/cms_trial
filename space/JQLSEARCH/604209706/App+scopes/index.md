# App scopes

JQL Search Extensions for Jira requires various application scopes to function correctly. Application scopes give access to Jira data. The following list explains the required scopes and how the data is used.

| **Scope name** | **Description** | **How the app uses the scope** |
| --- | --- | --- |
| READ | View, browse, and read information from Jira. | - reads issue fields - fetches fields configuration - performs searches - reads previously saved issues metadata - reads the app’s metadata |
| WRITE | Create or edit content in Jira, but not delete content. | - saves the app’s metadata against an issue - saves the app’s metadata |
| DELETE | Delete content in Jira. | - deletes the app’s metadata from an issue - deletes the app’s metadata |
| ACT\_AS\_USER | Access content using the permissions of the user running the app. | - performs search as a user (helps with security of data) - saves filter as a user - deletes a user’s filter |
| ACCESS\_EMAIL\_ADDRESSES | Get the email addresses of users. | - obtains the email of a person who initiated a transactional action, for example, triggered the Jira indexing. |