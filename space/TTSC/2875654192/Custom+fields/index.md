# Custom fields

Time to SLA lets you create SLA-powered custom fields that display SLA information directly inside Jira work items.

![SLA Fields page showing a list of configured SLA custom fields and their details.](/cms_trial/assets/0866ab47-3a96-4fa1-bfa3-abc48c86b754.png)

**Tip:**

Refer to the fields created above to see examples of how you can use this feature.

These fields behave like standard Jira custom fields. Once added to a screen, you can use them in:

- JQL searches
- Dashboards
- Automation rules
- Reports

## Who can create SLA fields

Only Jira administrators can access and create SLA fields. SLA fields are Jira custom fields, and Jira only allows admins to create and manage custom fields.

![Administration menu in Time to SLA with the SLA Fields option selected from the dropdown.](/cms_trial/assets/1b9e93f2-ffef-4e23-9802-3ce6f7c98dff.png)

If you don’t see the SLA Fields section, check that you have Jira admin permissions.

## Where to create SLA fields

You can create SLA fields in two ways:

### Option 1: From the Time to SLA administration

Go to:

**Apps** > **Time to SLA** > **Administration > SLA Fields**

This is the recommended place for managing SLA-specific field types.

### Option 2: From Jira custom field settings

You can also create SLA fields from Jira’s native custom field page:

1. Navigate to the Jira admin panel using the cog icon in the top navigation and select **Work items**.
2. In the *Fields* section in the side navigation, select**Fields**, then **Create new field**.
3. In the panel that opens, select one of the TTS fields.

## Available SLA field types

Time to SLA currently supports the following field types.

### SLA Indicator

Displays the current SLA status in the work item view. For example:

- Breached
- In progress
- Met

When you click the information icon next to the field, you can view detailed SLA data, including all related SLAs and their current states. Use this field when agents need to quickly understand whether an SLA is on track or breached.

![Jira work item view with the Delivery indicator set to Breached.](/cms_trial/assets/4fee7bbc-9d37-4afd-bf83-2f5d20837740.png)

![SLA details panel showing multiple SLAs with their current states.](/cms_trial/assets/9c3921c8-c17e-4919-91ea-3764c307a344.png)

### SLA Date

Displays a selected SLA date value in the work item. You can configure the field to store:

- SLA target date
- SLA start date
- SLA end date

![Jira work item displaying SLA QA target latest and earliest fields in the details panel.](/cms_trial/assets/42a3a685-04fc-4e36-9e60-1e2852389edc.png)

### SLA Duration

Displays how long each selected SLA has been running (or has run), expressed as a duration.

![Work item view showing SLA duration values for time to resolution and first response.](/cms_trial/assets/3b7aa29e-3acf-4d22-b70f-06e2cadb46f3.png)

### Dynamic Calendar

This field lets you select a goal calendar directly from a Jira work item. Instead of assigning a fixed calendar inside the SLA configuration, you can let users dynamically define which calendar should apply to a specific work item.

![Work item details panel with a dynamic calendar field showing Team A SLA calendar in the Details panel.](/cms_trial/assets/508276b8-8080-4c48-918b-bf4e442068af.png)

### Optimize the number of SLA fields

To reduce the number of custom fields, you can group SLAs that won’t appear on the same work item into a single SLA field. For example, if you have separate SLAs for different spaces, such as IT Support, HR Requests, and Finance Approvals, you don’t need to create a separate SLA field for each space. Since these SLAs apply to different project scopes, they can share one SLA field.

This helps keep your custom fields organized while still showing the right SLA information on the relevant work items.

## Important: After creating a field

After you create the field, it won’t automatically be applied to all existing work items. For the custom field to attach to a work item, calculate its SLA value, and become visible in the work item navigator, dashboards, queues, or gadgets, **the work item must be opened at least once**.

The field becomes populated **only** **after** the work item is viewed.

**Why this happens**

Jira custom fields are calculated and stored when a work item is accessed. They do not automatically recalculate in the background for all existing work items. Once the work item is opened:

- Time to SLA calculates the SLA value.
- The custom field is updated.
- The update appears in the work item history (However, custom field value changes do not appear in the Jira work item history).

This behavior is expected and cannot be disabled.

If you don’t see the field, make sure that:

- It is in scope for the correct project and work item type
- It is added to the relevant screens
- It is included in the work item layout

If you're unsure why the field is not appearing, use Jira’s **Find your field** action on the work item view to identify the missing configuration.

For detailed steps, refer to Atlassian’s documentation on [creating](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and [managing fields and screens](https://support.atlassian.com/jira-cloud-administration/docs/find-your-custom-fields/).