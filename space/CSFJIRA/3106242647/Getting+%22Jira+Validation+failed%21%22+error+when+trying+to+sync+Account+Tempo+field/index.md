# Getting "Jira Validation failed!" error when trying to sync Account Tempo field

## Summary

You are unable to sync the Account Tempo field with the Account Id Salesforce field and hit to a "Jira validation failed!" error. This article provides the steps to sync the Account Tempo field with the account ID Salesforce field.

## Environment

- Jira Data Center
- Jira Cloud

## Diagnostics Steps

When the Account Tempo field is synced with the Account ID Salesforce field you will receive the following error from Tempo within the HAR file:

```text
"JIRA validation failed!": "io.tempo.jira__account": "Can not construct instance of java.lang.Long from String value '0014x00001N7ENZAA3': not a valid Long value\n at [Source: N/A; line: -1, column: -1]"
```

## Cause

Tempo will not be able to update the Tempo Account field without mapping the ID values of the Account Tempo field with the Salesforces Account Id values.

## Workaround

- N/A

## Resolution

1. Refer to [Tempo's REST API Documentation (4.0)](https://apidocs.tempo.io/) to get the ID values of the Tempo account.
2. Map the Tempo Account with the Account ID(Salesforce) and map the ID values.
3. In Jira, add the Tempo Account ID and map it to the Salesforce Account ID, then click **Save**.

   ![contentId-3106242647](/cms_trial/assets/1b879ef7-1dbc-404b-ba3f-34dbf736c065.png)
4. You will be able to sync the Tempo "Account" field with your Salesforce accounts successfully.