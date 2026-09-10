# How to correct discrepancies between Foxly metrics and Jira custom fields created from Foxly

If a Foxly metric has a custom field linked to it and is configured as **required** in Jira, then any update to the metric—adding, renaming, or deleting metric options (custom field options that were created before)—will cause a discrepancy.

If there is a discrepancy between a Foxly metric and Jira custom field, you will receive the following warning message when saving the prioritization template:

![Error message in Foxly](/cms_trial/assets/e2f9f55d-19f9-4899-8c8e-325c6b27b0b0.png)

Use the following steps to correct the discrepancy:

1. [Make Foxly custom field not-required (optional) in Jira field configuration](https://support.atlassian.com/jira-cloud-administration/docs/change-a-field-configuration/#:~:text=issue%20view.-,Make%20a%20field%20required%20or%20optional,-Depending%20on%20your).
2. Go to Foxly and uncheck the checkbox for the metric to be **stored in the custom field**.
3. Save the template.
4. Go back to Foxly and select **store in the custom field**.
5. Save the template.
6. Add the field back to Jira.
7. Make the field **required** again in Jira field configuration.

![How to enable Jira custom field in Foxly](/cms_trial/assets/c8f6a176-4ace-412b-b9df-a883c79f4f16.png)

Read more about [storing metric in a custom field](/cms_trial/space/FOX/602538203/Store+metric+in+a+custom+field/).