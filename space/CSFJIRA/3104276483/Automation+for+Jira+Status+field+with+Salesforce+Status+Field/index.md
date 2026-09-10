# Automation for Jira Status field with Salesforce Status Field

## Purpose

We will discuss how to map a custom Jira Status field to Salesforce Status field, and how to do automation to be able to change the Read-only Status field in Jira.

But first, there are some things needed:

- Jira Status custom field (Select List -single choice).
- Values must be the same on both sides.
- If values are not the same, mapping is needed.
- Automation Rule.
- Make sure that the transitions between the selected statuses are available as per Atlassian Documentation (<https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/#Adding-a-transition-to-a-workflow).> Else, the status in Jira will not change. The Status does not change section at the bottom of this page provides more information.

This automation can be one way (Salesforce to Jira) and the first section will show that, Or bidirectionally by adding and changing the sync direction of the mapping (shown in Complete the loop section).

## Answer

1. Create a Custom Field

We will name it Jira Status and add the following Options(these options are the ones I have on my Salesforce instance. These values can be different, if they are, you will need to do value mapping and map the Salesforce Fields to their counterpart in Jira)

Jira field values

![contentId-3104276483](/cms_trial/assets/c7357d54-eac3-47a7-8cb9-6226e8b45117.png)

- Salesforce field values

  ![contentId-3104276483](/cms_trial/assets/76ad3332-5837-46ca-af42-0c29f6c97fe4.png)

1. Binding/Mapping

We add the field mapping with Bidirectional Sync

![contentId-3104276483](/cms_trial/assets/dd199463-704c-4b96-83d9-3f7d21dc5249.png)

- Value Mapping

If both sides have the same values, there is no need to do the value mapping.

If the values are not the same between Jira Status and Salesforce status, we need to do value mapping. (this is an example)

![contentId-3104276483](/cms_trial/assets/21151f36-79cb-4dd0-beac-aac21fcf9fcc.png)

1. Automation

To change the Status field we use the following Automation rule.

First we need to create the rule in the cog icon → System → Automation → Global Automation (bulleted)

          Then we create the rule and as first option we choose "Field value changed"

          When : Value changes for Jira Status (Jira Status is the custom field we've created)

![contentId-3104276483](/cms_trial/assets/3bec3974-cea9-4698-9e29-0cf223897a5e.png)

Now we add an If block and as many Else-if as necessary. This is per Jira Status value ( in this example we use 4)

The If block condition type should be  "Issue Fields Condition" .

![contentId-3104276483](/cms_trial/assets/a1459aab-22a3-4135-9392-b91795b6eed1.png)

Inside the IF statement we add a THEN: transition the issue to (the first one on this example should be Backlog).

![contentId-3104276483](/cms_trial/assets/08555226-cc48-43c7-b26d-acc0c45367ce.png)

Another Else-if with Issue fields condition.

![contentId-3104276483](/cms_trial/assets/be39cf8d-88c5-4c88-83f0-f05ab0a0b577.png)

Inside the Else-IF statement we add another THEN: transition the issue to.

![contentId-3104276483](/cms_trial/assets/a1ab56db-46f1-4e56-a557-3a50b81bfc21.png)

Another Else-if with Issue fields condition and another THEN: transition the issue to.

![contentId-3104276483](/cms_trial/assets/47ea00f3-e23e-4f23-ae53-8d045489802a.png)![contentId-3104276483](/cms_trial/assets/039b2bf9-8efa-46cb-9737-d5fb680fdff4.png)

Keep adding them till you have all the statuses like this.

![contentId-3104276483](/cms_trial/assets/01db39cc-d5c4-4336-ab3b-b7754bcb30b9.png)

After adding all the else-if blocks we need to turn the automation ON.

You can test if the automation works by changing the field in Jira. Change it to "Backlog" and the Status field should change to "Backlog". If the automation fails , check the automation audit logs.

At the end you will see that when you change the Status in Salesforce (Example: from Backlog to In Progress), it will change the Status Read-only field in Jira to that value.

Complete the loop (Heading)

To have this automation both ways (Bidirectionally and get the Status field value into Salesforce), you need to change the Mapping sync direction like this:

![contentId-3104276483](/cms_trial/assets/121b8962-6d6c-4871-94fa-581b73493d44.png)

With that configuration, the Status from Salesforce will be sent to the intermediary Jira Status field. The automation will match and change the Read-only Status Field to that value.

Then if you change the Status field in Jira, it will change the Salesforce field and the Salesforce field will update the intermediary field to the Same Status.

## Hide Jira Status field from the Edit Screen

To avoid the misuse of the new Jira Status Field (since changing that field manually in Jira will change the Status field) we can hide it from the screen by using the Issue Layout.

- Go to Project Settings → Issue layout
- Select the Issue Type → Edit layout
- Move the Jira Status field to the right (drag and drop)

Now the Jira Status field will be hidden.

## Possible Errors

"Destination status could not be resolved. If using a smart-value ensure this resolves to a numeric status ID or untranslated name for issues"

When creating the Automation rule you might encounter this error. To fix this you need to change the Actor in the Automation Rule into your user or any user who has permission to apply this transition.

This could also happen if the Actor is set to someone without the permissions for Automation.

In the Automation click on "Rule Details" and change the Owner.

![contentId-3104276483](/cms_trial/assets/3d42d337-cbcf-4290-9e50-6d34365ecac1.png)

## Status does not change

After the Salesforce update, if the status in Jira does not change, it means that there is no transition step available for the selected status.

Check the Jira issues if a transition to the status is available. If yes, the status is shown in the drop-down list.

Click "View workflow" to view all available transitions of the statuses in the project's workflow.

![contentId-3104276483](/cms_trial/assets/bedb53a1-6493-4000-8d3b-af9977b3095b.png)