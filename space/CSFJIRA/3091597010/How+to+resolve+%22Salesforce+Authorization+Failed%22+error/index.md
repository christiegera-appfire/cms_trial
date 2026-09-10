# How to resolve "Salesforce Authorization Failed" error

## Summary

A "Salesforce authorization failed" error is generated while trying to integrate Salesforce and Jira.

![contentId-3091597010](/cms_trial/assets/42e74fe2-38a4-4ee4-9e01-afc6041d5fc9.png)

## Environment

- Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

This error is normally caused by a problem with the Salesforce integration user credentials. They either expired or the user was disabled.

NEW

## Resolution

Revoke the Connection from within both Salesforce and Jira to force creation of a new token.

You can use the same steps as shown in this KB - [How to change the Salesforce integration user](/cms_trial/space/CSFJIRA/2256308548/How+to+change+the+Salesforce+integration+user/).