# "Connection with this name already exists" error even though there are no connections in Salesforce

## Problem

When trying to add a new connection to the installed package, an error is shown stating that a connection with that name already exists. However, there’s no connection with that name or no connection at all.

![error.png](/cms_trial/assets/c91ed0e5-b1d0-4ed7-ac63-68d172a7b107.png)

## Solution

This error is related to the storage limit being exceeded, most likely due to the amount or size of attachments added to Salesforce records. In order to solve this it is required to free some space from the instance and the limit will depend on your plan.

See [Help and Training Community](https://help.salesforce.com/s/articleView?id=sf.files_storage.htm&type=5) for more details.