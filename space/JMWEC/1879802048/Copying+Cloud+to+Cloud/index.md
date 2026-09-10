# Copying Cloud to Cloud

Unfortunately, no automated option currently exists for migrating JMWE configurations from one Jira Cloud instance to another. The only option for moving JMWE extensions to another Cloud instance is to manually copy them; this page details recommendations on the order of migration.

**BEFORE YOU BEGIN**

- ***It is easiest - but not necessary - to do the migration when using multiple monitors so that side-by-side comparisons can be done.***
- Please review this page entirely.
- The steps detailed below are the best *recommendations* for the order in which extensions should be migrated.
- Please reach out to [Appfire Support](#) if you have any questions or encounter any issues.
- For obvious reasons, **test your destination instance thoroughly** before considering the migration complete.

## Planning the migration

It is highly recommended that you recreate specific categories of extensions in full before moving to the next set; for example, recreating **all** Shared Actions before configuring individual workflows or other Actions that utilize those Shared Actions will prevent missing Shared Actions in your destination. Overall, the recommended order of operations is:

1. Recreate any [Live Fields](https://appfire.atlassian.net/wiki/spaces/LF) configurations
2. Recreate [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) and [Shared Nunjucks templates](/cms_trial/space/JMWEC/465473979/Shared+Nunjucks+Templates/)
3. Recreate [Scheduled Actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/) and [Event-based Actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/)
4. Lastly, migrate any workflows and rebuild any extensions that have been added directly to them.

Please see the sections below for specific steps and considerations for copying each of the above to your new instance.

**Note**: If your source instance does not include an extension or Action in the list above, it is generally safe to skip that step. However, it is highly recommended that you check the JMWE Administration pages for each type of Action and extension to verify that nothing needs to be copied!

## Install and setup JMWE at the destination

Before beginning any work, please verify that JMWE Cloud has been installed on your new instance. Additionally, you should copy any specific app settings by checking the [JMWE Configuration](/cms_trial/space/JMWEC/466288938/JMWE+Configuration/) page on your source and setting those options on your destination.

## Recreate Live Fields

Live Fields should be recreated before any other Action or extension - if a Live Field is used in a post function it needs to exist before that post function is created, no matter where the post function exists!

To recreate Live Fields, open the Live Fields administration page in your source instance by going to **Apps > Live Fields**. For each of your Live Fields configurations, open it by selecting **Edit** from the Action Menu ( ▢ ). In your destination instance, open **Live Fields** and click **Create live fields** in the upper right corner of the window; this will start a new configuration. Copy each of the configurations from your source instance to your destination.

## Shared actions and Shared Nunjucks templates

[Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) and [Shared Nunjucks templates](/cms_trial/space/JMWEC/465473979/Shared+Nunjucks+Templates/) are single configurations that can be used in multiple places. Their power - configure and update in one place but use in many places! - is the reason they should be copied to your destination first. Recreating these before adding any other extensions means that they will automatically be available when copying other Actions or configuring your workflows.

To copy these, log into both your source and destination Jira Cloud instances, and go to their respective JMWE Administration pages; click **Settings** > **Apps** in the upper right corner and then select the appropriate administration page (e.g. **Shared actions**). Work down the list, copying the full configuration for each to your destination instance.

For [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/):

1. Make sure the name of the action is identical to the source action.
2. Copy every post function included in the Shared action in the same order they appear in the source instance.
3. Verify that the configuration of each post function in the destination is identical to the source.

For [Shared Nunjucks templates](/cms_trial/space/JMWEC/465473979/Shared+Nunjucks+Templates/):

1. Make sure the name of the template is identical to the source template.
2. Copy the Nunjucks code exactly from one instance to the other, and **test each template** before saving it.

**Note**: It is important to test each Nunjucks template before saving it! If your template references a custom field that has not been recreated in the destination instance, testing it will flag the missing field!

## Recreate Actions

Similar to Shared actions above, recreating [Scheduled actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/) and [Event-based actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/) should be done one at a time, following the same recommendations:

1. Make sure the name of the Action is identical to the source instance.
2. Ensure that the schedule for the action, or the event that triggers it, is identical in the destination as configured in the source.
3. Copy every post function included in the Action in the same order they appear in the source instance.
4. Verify that the configuration of each post function in the destination is identical to the source.

**Note**: If *any* of your post functions include Nunjucks in their configurations, it is important to test each Nunjucks template before saving the post function! If your template references a custom field that has not been recreated in the destination instance, testing it will flag the missing field!

## Rebuilding workflows

Before adding extensions directly to workflows, you’ll need to either recreate your Workflows or [migrate](https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/) them to your destination instance. Once your workflows have been recreated in the destination, you can use the [JMWE Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) administration page to work through the list of extensions that exist on each workflow in your source. Go to **Apps > Jira Misc Workflow Extensions** and select **JMWE workflow extensions** in the right-hand panel.

Open each post function in your source by clicking its name and using the **Workflow & Transition issue** section, edit the appropriate workflow in your destination instance. Select the appropriate transition and add the extension type for the extension you are viewing (Post function, Condition, or Validator).

To guarantee the most seamless migration, it is highly recommended that you thoroughly test each workflow after all of its extensions are duplicated in the destination instance. This will help prevent missing extensions or Actions in each workflow independently, but also verify that any dependencies downstream from a workflow are resolved before they cause errors.