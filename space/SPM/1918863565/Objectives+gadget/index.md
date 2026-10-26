# Objectives gadget

**Depreciated** **by Atlassian**

[Atlassian ended support for gadgets in Confluence 7.0](https://confluence.atlassian.com/doc/gadgets-moved-to-a-marketplace-app-from-confluence-9-2-onwards-1431545691.html) and completed their removal in Confluence 9.0 to reduce technical debt.

In Confluence 9.0, pages that were using gadgets show a grey ‘Unknown macro’ placeholder where gadgets were embedded.

BigPicture **Objectives gadget** is now available for Jira Cloud and Jira Data Center.

Similarly to the Objectives module:

- The Objectives gadget presents the read-only content - you can see the status of Objectives for a selected Box;
- The Objectives gadget allows you to move horizontally along the timeline.

![image-20240307-121408.png](/cms_trial/assets/f8fc5442-4b97-4f4f-aa65-4fb195559bd6.png)

## Objectives gadget configuration

To configure the gadget:

1. Click the **'…'** option in the top right corner.
2. Choose **Configure**. You can select the Box that will mirror data from the Objectives module in BigPicture.

![image-20240307-121900.png](/cms_trial/assets/57f6db27-8297-45ab-84bd-53a2e83d9fc5.png)

1. Set the **Refresh interval** to a desired timeframe.
2. Set the **Height** to a desired size.

![image-20240307-101912.png](/cms_trial/assets/2f50855a-faf3-422a-a4f7-ecc40bd39bb2.png)

### Box

Select the Box to serve as the gadget's data source. The list of Boxes will only include the ones you have access to.

**Security role**

The user’s security role needs to be set to the **Box viewer** at the minimum.

### Refresh Interval

You can set the gadget information refresh interval to:

- Never
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours