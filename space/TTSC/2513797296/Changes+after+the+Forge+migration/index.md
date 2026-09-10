# Changes after the Forge migration

Time to SLA for Jira Cloud runs on [Atlassian’s Forge platform](https://developer.atlassian.com/platform/forge/). The move to Forge changed some product behavior, including how you access the SLA panel, how the Dynamic Calendar field works, and how some existing links and integrations behave.

This page summarizes the changes that may affect customers who used Time to SLA before the Forge migration.

If you installed Time to SLA after the Forge migration, use the current feature documentation linked from each section for setup and configuration instructions.

## Changes that may require action

The following changes may require updates to existing configurations, scripts, integrations, or user workflows.

| **Area** | **Change after migration** | **What you may need to do** |
| --- | --- | --- |
| **SLA panel visibility** | The SLA panel no longer appears automatically in every work item after the Forge migration. | Open **Time to SLA** from the work item when you need the panel. Jira administrators can configure the panel to appear automatically. |
| **Dynamic Calendar field change** | Forge uses a new Dynamic Calendar custom field. The field has a different Jira field ID and stores the calendar ID instead of the calendar name. | Update Jira automation rules, scripts, REST API requests, and integrations that reference the previous field or value format. |
| **Periodic report links** | Links in periodic report emails sent before the Forge migration use the previous app URLs. | Emails sent before the migration contain outdated links that won’t open correctly. Emails sent after the migration include new, fully functional links. No action is needed for future emails. |
| **In-app links** | URLs used by Time to SLA changed as part of the Forge migration. | Replace bookmarks or saved links created before the migration. |
| **Time zone handling** | Time values in several areas follow your device’s system time zone instead of your Jira profile settings. | This affects **SLA start**, **target**, and **end dates** shown on the **SLA panel**, **SLA history** tab, and **Detail report**. It also applies to the request creation dates shown on the **recalculation**, **background reports**, and **periodic reports** pages.  These changes only affect how times are displayed, not how SLAs are calculated. |
| **Mute SLA settings** | The setting has been relocated. | Now found under **Settings** > **General Settings** > **Apps** > **TTS Mute SLA**. |
| **Initial setup time (New installations)** | A short waiting period occurs after installation. | After installing Time to SLA for the first time, users need to wait around 3 minutes for the app to complete its initial setup.  This delay is caused by Forge platform limitations and is expected behavior, so it does not indicate a performance issue. |
| **SLA panel colors** | Minor tone adjustments for visual consistency. | No functional changes. |
| **Dynamic calendar** | A new **Create custom field** button has been added. | Lets you create and link SLA time fields directly during goal creation. |
| **Impersonating users** | Forge does not currently support Jira’s **Log in as another user** functionality in the same way as Connect. | If an administrator impersonates another user, Time to SLA may not reflect that user’s actual permissions correctly. Test with the actual user account when you need to verify Time to SLA permissions or behavior. |
| **Jira mobile phone app support** | Due to a current Forge platform limitation, the SLA panel is not supported on mobile. | Use Jira in a web browser to view the SLA panel. |

## SLA panel visibility

### How to reopen the SLA panel for everyone (admins)

If you’re a Jira administrator, you can make the SLA panel visible on all work item pages by default.

1. Open any Jira work item.
2. Click the **Time to SLA icon** in the top menu.

   ![A screenshot showing where the Time to SLA icon is in the top menu.](/cms_trial/assets/f6ac8ed7-2105-4082-80ad-34c0c5af9573.png)
   - If you don’t see it, click the Jira **⋯** menu. The **Time to SLA** option may appear there, depending on the number of apps installed in your instance.
3. When the SLA panel section appears, click the **⋯** button next to it.

   ![A screenshot showing where the Show for all work items option is in the work item page..](/cms_trial/assets/b4d30b36-2537-49a3-b690-fcef2c5721df.png)
4. Select **Show for all work items**.

Once enabled, the SLA panel will appear automatically on all work items for all users in your project.

### How to reopen the SLA panel in a work item (users)

If you’re not an administrator, you can still open the SLA panel for a specific work item.

1. Open a Jira work item.
2. Click the **Time to SLA icon** in the top menu.

   ![A screenshot showing where the Time to SLA icon is in the top menu.](/cms_trial/assets/f6ac8ed7-2105-4082-80ad-34c0c5af9573.png)
   - If you don’t see it, click the Jira **⋯** menu. The **Time to SLA** option may appear there, depending on the number of apps installed in your instance.

The SLA panel will appear in the work item view.

This enables the SLA panel **only** for the current work item. You can repeat this step on any work item where you want to use Time to SLA.

## Dynamic Calendar field change

As part of our move to Forge Remote, we will introduce a new Dynamic Calendar field that replaces the existing Dynamic Calendar field used today. After the migration:

- Your calendar data will be automatically migrated,
- Your existing calendars continue working as before. **However, the new field will have a completely different ID and stores a different value format, so you must update references in any automation or integration that uses it.**

### 🚨 Action required: Update automations or scripts that use this field

If you set or read the Dynamic Calendar field in Jira Automation, ScriptRunner, REST API, or any integration, you must:

1. Use the new field ID
2. Use the calendar ID as the field value (instead of calendar name)

Follow the steps outlined below to perform these actions.

#### Step 1: Find your new Dynamic Calendar field ID

1. Go to **Jira** > **Settings** > **Work items** > **Fields**.
2. Search for **TTS – Dynamic Calendar (MIGRATED)**.
3. Note the new field ID (for example, `customfield_12345`).

#### Step 2: Find your calendar ID

Currently, the Calendar ID is visible only in the calendar’s URL.

1. Open **Time to SLA** > **Calendars**
2. Click the calendar you want to use.
3. Look at the browser URL. It will include:

```text
.../calendars/{calendarId}/view
```

**Example:**

![A screenshot showing how to find your calendar ID in the browser URL.](/cms_trial/assets/5c247749-6595-43fa-8054-821a8577fe28.png)

```text
dd8714a8-fc1a-4a47-8842-158e3993d042
```

Use this value in your automations and scripts.

#### Step 3: Update the Dynamic Calendar field value format

The new field no longer accepts calendar names. It must be set using the calendar ID.

**Example JSON or payload pattern for setting the field value in automation/scripts:**

```json
{
  "fields": {
    "customfield_10982": [
      "29977122-2e91-4dfc-b040-debffc1f9080"
    ]
  }
}
```

- Replace `customfield_12345` with the actual migrated calendar field ID.
- Replace `"aaaa-zzzz-vvv-ddd"` with the calendar ID of the calendar you want to set on the work item.

## Impersonating users

If your Jira admins use **Log in as another user** to troubleshoot issues or test the app experience, be aware that this flow is not fully supported on Forge.

Due to a current Atlassian Forge limitation (tracked in [ECO-244](https://jira.atlassian.com/browse/ECO-244)), Time to SLA may not evaluate permissions as if the impersonated user were actually logged in. This can affect app behavior, especially in the SLA panel.

### What this means

When an administrator impersonates another user:

- Time to SLA may still behave according to the administrator’s context instead of the impersonated user’s context.
- As a result, TTS permissions may not work as expected.
- The SLA panel is the area most likely to be affected.

### Recommendation

To verify the real user experience, test with an actual user account with the intended permissions, rather than relying on impersonation.

## Jira mobile phone app support

Because of Atlassian limitations (tracked in [FRGE-1492](https://ecosystem.atlassian.net/browse/FRGE-1492)), the Time to SLA panel doesn’t render in the Jira mobile app after the move to Forge. Use Jira in a desktop or mobile phone browser whenever you want to view with the Time to SLA panel.

---

## Need help?

If you have any questions or feedback about the migration, [contact our support team](https://apps.appf.re/crt/support).