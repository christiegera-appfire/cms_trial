# How to add dynamic custom error messages

This page explains when and how to add custom messages to your JSU validation rules.

You can add dynamic custom error messages to validation rules to help users resolve failed validation steps. There are two types of custom error messages: rule-level messages and branch-level messages.

### **Rule-level messages**

Add a rule-level error message to the general rule settings to provide more context for the error. If you leave this field empty, JSU will display a default message if the validation check fails.

**To add a rule-level message:**

1. In the *General* panel of the JSU Rule Builder - Validators, provide the message to display to users, for example, `Approver can’t be reporter`.

   ![Screen shot of the validator rule builder with a custom error message.](/cms_trial/assets/6adf4fb2-7fea-4098-9bac-945071397c83.png)

   If the validation check fails, the message displays during the transition. If there is no transition screen, the error message displays in a dialog at the bottom of the page.

   ![Screenshot of a custom error message shown on a transition screen in Jira.](/cms_trial/assets/7a1a4d05-ebc6-4a82-8dad-be0d587a9f27.png)

### Branch-level messages

You can add error messages for individual branches in the rule to provide better context about which step failed a check. Error messages added to a branch apply to the branch, not individual validators.

**To add a branch-level message:**

1. Click the *Validator fails* error panel.
2. In the *Fail with message* panel, add the error message to display to users. This message displays instead of the rule-level message only when the associated validation check fails. If there is no transition screen, the error message displays in a dialog at the bottom of the page.

   ![Screenshot of the Fail with message module in the JSU Rule Builder.](/cms_trial/assets/730f0519-93dc-4d8f-950c-6e4a0c54cefa.png)