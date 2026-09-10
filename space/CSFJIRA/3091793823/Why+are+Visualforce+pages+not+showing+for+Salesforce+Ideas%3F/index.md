# Why are Visualforce pages not showing for Salesforce Ideas?

## Summary

Creating a Visualforce page by following this [documentation](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754239/Configuring+Visualforce+components) and then adding the Visualforce page to the Idea object page layout will result in the Visualforce page **not** being displayed.

## Environment

- Confluence or JIRA version
- Add-on version

## Diagnostics Steps

Not applicable. 

## Cause

This is due to a limitation with Salesforce Ideas.

The Salesforce Ideas object page layout is **not customizable**. While it is possible to view changes in Preview mode, the actual page will not change according to your customizations.

**References:**

- <https://success.salesforce.com/ideaView?id=08730000000BpqD>
- <https://success.salesforce.com/answers?id=90630000000CnUIAA0>

## Workaround

Not applicable. 

## Resolution

As of this moment, there is no resolution or workaround for this case unless Salesforce allows customization for the Ideas page layout.