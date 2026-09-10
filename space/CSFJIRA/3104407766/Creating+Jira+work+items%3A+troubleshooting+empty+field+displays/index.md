# Creating Jira work items: troubleshooting empty field displays

## Problem

When you try to create a Jira work item from the Jira Issues (NextGen) Lightning Component in Salesforce, you might encounter an issue where:

- No fields appear when clicking **Required Fields** or **More Fields to Review**.
- The **Create** button remains unclickable.
- In some Salesforce instances, you might see a **Component Error** message.

![Connector for Salesforce & Jira Create Issue dialog showing empty fields and unclickable Create button](/cms_trial/assets/255e9f6f-a932-42d4-b177-09d9f7d36753.png)

## Reason

This typically occurs when there's a mismatch between your mappings and your current Salesforce fields. The Connector can't pull information from fields that have been:

- Renamed
- Deleted
- Recently removed

## Solution

To solve the issue, you have two options to get things working again:

1. If a field was renamed or permanently deleted:

   - Remove the conflicted mapping that's trying to access the missing field
2. If a field was recently removed but still exists:

   - Restore the missing field in Salesforce

![Connector for Salesforce & Jira mapping configuration showing field removal option](/cms_trial/assets/335e3b63-639f-45d8-b63e-aefa49d17fed.png)