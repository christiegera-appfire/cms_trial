# Connection configuration page doesn't load or is unresponsive

## Summary

If you are facing an issue where the Connection configuration page does not load or is unresponsive, then it might have been caused by importing invalid mapping data into the database.

## Environment

- Connector for Salesforce & Jira Cloud

## Diagnostics Steps

The Connection configuration page does not load or is unresponsive. You may also experience synchronization errors and bindings do not work as expected.

## Cause

Invalid mapping data in the database may have been caused by the following reasons:

- Importing a JSON file with invalid mappings
- Importing a file with huge JSON data which caused the database to truncate the JSON data

## Workaround

Not applicable.

## Resolution

If your bindings still work as expected and all synchronization activity also works as expected, then simply go to the **Mappings** screen and click **Save**. The Connector will then clean up any junk data from the JSON file in the DB.

**HOWEVER:**

If you experience synchronization errors and bindings do not work as expected, then most likely a JSON file with a very large amount of data was imported into the database and some data was inadvertently truncated, thus causing a lot of errors.

In this scenario, you will have to [manually reconfigure the mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754325/Configuring+Entity+Mappings+and+Field+Mappings) if you want the synchronization to work properly with the bound project.