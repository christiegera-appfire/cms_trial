# Troubleshooting: Tasks not showing up in a box

## Problem

Tasks that should be displayed in a box, as defined by the scope, are unavailable.

## Solution

If tasks aren’t showing up as expected after defining scope:

- Make sure the correct data source is connected (**Spaces**, **Boards**, and/or **Filters**):

  ![Work items from Jira page showing projects, boards, and filters.](/cms_trial/assets/69d76a4f-c2c5-442b-8a77-539fe8453b21.png)
- Check that **Labels** and **JQL query** aren’t removing the items you’re looking for:

  ![Additional filters for work items.](/cms_trial/assets/a9528549-d2ea-4875-9280-b0871fb6e7e3.png)
- Confirm that the **Scope owner** (the person who added the data source) can still access the Jira project or filter. If they don’t, the box can lose visibility into that data.