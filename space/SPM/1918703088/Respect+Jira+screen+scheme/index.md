# Respect Jira screen scheme

The **Respect Jira screen scheme** toggle does not stop BigPicture from updating Jira values.

It only prevents you from changing the value in the app when it cannot be adequately reflected in Jira.

This toggle applies to all fields.

**Toggle off:** Bi-directional sync is not required but will be performed when possible.

**Toggle on:** Bi-directional sync is required. When the toggle switch is on, the App lets you change a task's field value only if it can be reflected in Jira. When a field isn't available for a Jira issue, you can't edit it in BigPicture.

### Exception - Mapped fields

Even when mapped fields cannot be updated by BigPicture (because they haven't been added to the project's Jira screen scheme), you can still edit them in BigPicture. The bi-directional sync isn't required, as it's carried out when possible.

![contentId-1918703088](/cms_trial/assets/59be9055-7a50-4ab7-90cf-0ea3742ea488.png)