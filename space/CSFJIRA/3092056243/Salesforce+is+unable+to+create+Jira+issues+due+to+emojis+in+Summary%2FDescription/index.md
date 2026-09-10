# Salesforce is unable to create Jira issues due to emojis in Summary/Description

## Summary

When a Jira issue's Summary or Description contains an emoji, an error will trigger and the issue will not be created. This happens when issues are being created from the Salesforce environment containing the emojis to the Jira issue.

## Environment

- Jira version 8.20 or prior
- MySQL database 5.5.3 or prior

## Diagnostics Steps

1. Create a Jira issue with an emoji in the Description/Summary field.
2. Creation will fail, create a support zip file for this.
3. Check the zip file for an error similar to the following:

#### **Error**

```text
Incorrect string value: '\xF0\x9F\x98\x8A\x0D\x0A...' for column 'DESCRIPTION' at row 1
```

## Cause

This issue is related to an existing bug regarding MySQL 5.5.3 or prior which does not support 4 byte UTF8 characters. There's a reference to this in the following Atlassian ticket:

- [https://jira.atlassian.com/browse/JRASERVER-44069](https://jira.atlassian.com/browse/JRASERVER-44069?__hstc=72543820.01f99528af9bc253f8dffa62573b705b.1668666715733.1671418725475.1671538723098.12&__hssc=72543820.9.1671538723098&__hsfp=973777814)

## Workaround

Upgrade the MySQL version as mentioned in the knowledge base [here](https://confluence.atlassian.com/fishkb/migrate-mysql-database-to-utf8mb4-character-encoding-962356253.html).​​

## Resolution

Not applicable.