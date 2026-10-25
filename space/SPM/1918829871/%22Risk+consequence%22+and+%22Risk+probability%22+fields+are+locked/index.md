# "Risk consequence" and "Risk probability" fields are locked

Atlassian's REST API allows the plugin to add **Select List (single choice)**type of fields on installation only when they are locked, which means you can't:

- change their name and description
- edit their possible values
- remove them
- change their Context

![Field information for Risk consequence](/cms_trial/assets/68c3c36b-3b7b-4f6b-b9d0-b7c366b464a1.png)

**You can:**

- change the Risk field mapping in the configuration of the App (to use another field)

  ![App Configuration](/cms_trial/assets/12d26dbb-1b78-4d09-9dbc-daebab37bb02.png)
- create a custom field that better meets your needs and use it for field mapping
- associate the Locked fields with various screens to use them in your projects