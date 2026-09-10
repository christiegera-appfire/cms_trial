# JsonValidationError List 'attachment' is undefined on object

## Purpose

When performing a manual push or pull action, the attachments are not being pushed/pulled to Jira upon issue creation.

The error seen when attachment data is not fetched:

![contentId-3091793702](/cms_trial/assets/a9a307c8-6309-40ae-8c59-dc0c6d09ec51.png)

## Answer

1. In Jira, click on the **gear icon** on the top right of the navigation bar > **Work items** → select the **Field** **configurations** (under Fields section) option from left sidebar.
2. Select the field configuration name > search for "Attachment" in the search box.
3. If the **Actions** section shows the word "Show", this means the attachment field is hidden.
4. Click **Show** to unhide the attachment field.

   ![contentId-3091793702](/cms_trial/assets/10387a0c-e7f3-4dca-a267-89ac0d41d5a3.png)
5. Check if the field is linked to the correct screen. If the screen does not show up, read this [documentation](https://support.atlassian.com/jira-cloud-administration/docs/add-a-custom-field-to-a-screen/) to link the attachment field to the appropriate screen.