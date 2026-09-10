# DC to Cloud migration guide

We're excited to be a part of your journey with Time to SLA for Cloud and are here to assist you through the migration process. Here’s a comprehensive guide to make your transition smooth.

**Pre-migration checklist:**

- Review Data Center versus Cloud [feature differences](/cms_trial/space/TTSC/36831915/Time+to+SLA+feature+differences+between+Jira+Data+Center+and+Cloud/).
- Upgrade Time to SLA to version 11.5.0 or later. Migration will not work on earlier versions. From v11.5.0, Time to SLA uses Forge-based migration support, which is required for the Jira Cloud Migration Assistant (JCMA) to detect the app.
- Choose between JCMA (recommended) or CSV Export/Import. Use the JCMA to seamlessly migrate work item SLAs and configurations. If using the Export/Import method, be prepared to recalculate SLA data in small batches.
- Time to SLA custom fields are not migrated via JCMA, except for the [Duration field](/cms_trial/space/TTSC/36209166/DC+to+Cloud+migration+guide/). If your SLAs rely on custom fields, you must manually create them in Jira Cloud after the migration.
- Optionally, you can use Atlassian’s [App Usage for Jira](https://confluence.atlassian.com/adminjiraserver/explore-app-usage-1283490318.html) to review where Time to SLA is used before migration. This can help you identify custom fields, saved filters using TTS JQL functions, REST API usage, dashboards, workflows, and other app-related dependencies that may need to be migrated, recreated, or validated in Cloud. Keep in mind that App Usage is a discovery tool and does not migrate data or configurations.
- Ensure all SLA configurations are valid and compatible with Cloud before migration.

- At least one active goal per SLA.
- Different start and end conditions.
- No Workflow scope (use space/work item type scope).
- Avoid IDs in JQL; use names instead.

- Adjust unsupported Cloud notifications (for example, space notifications).
- Time to SLA can migrate work item SLA data only for work items that the app can access during migration. If work item security prevents app access, the secured work item SLA data won’t be migrated. For more information, refer to the [Troubleshooting](/cms_trial/space/TTSC/36209166/DC+to+Cloud+migration+guide/) section.

## Important considerations

### Comparing Data Center and Cloud features

Before you begin, review the [Data Center and Cloud feature comparison](/cms_trial/space/TTSC/36831915/Time+to+SLA+feature+differences+between+Jira+Data+Center+and+Cloud/) page to find details on features available in each environment and identify any limitations or adjustments needed post-migration.

#### Key differences in migration options

1. **Jira Cloud Migration Assistant (JCMA)**  
   JCMA is the preferred method to migrate work item SLAs and SLA configurations without recalculation, as JCMA maintains work item history and SLA continuity.
2. **CSV Export/Import**  
   Exporting via CSV only moves the work items without the full work item history. Using this option, SLAs won’t function due to missing history. Recalculate after import, but note this can be labor-intensive for large instances.

---

## Preparation steps before migration

1. **Update JCMA and Time to SLA**  
   Ensure both Jira Cloud Migration Assistant and Time to SLA are updated to the latest versions for compatibility and smoother migration.
2. **Thoroughly check SLA configurations**

   - Each SLA must have at least one active goal; otherwise, migration of the SLA will fail.
   - The SLA’s start and end conditions must be different.
   - Remove any Workflow scope in SLAs, as it's not supported in the Cloud. Instead, ensure SLAs are scoped to specific spaces and work item types.
   - When using the Jira Cloud Migration Assistant (JCMA), make sure to include both Time to SLA and the spaces that your SLAs depend on in the same migration plan.  
     This ensures that all SLA-related configurations (such as custom fields, statuses, and calendars) are successfully migrated and remain functional in Cloud.  
     For example, if your SLA in the Data Center uses custom fields or statuses from Space A, you must also select Space A during migration. Otherwise, the SLA configuration may not transfer correctly.  
     Below is an example of the JCMA selection screen, where you can choose which spaces and apps to include in your migration:

     ![JCMA selection screen showing Spaces and Apps selected for migration.](/cms_trial/assets/53c1c0c9-9bb6-43e2-8ddc-21fb24d98100.png)
3. **Ensure the JQL you used in the SLA configuration will also be valid in the Cloud:**  
   For example, avoid using IDs in JQL conditions within SLA settings, as IDs may not match in Cloud. Instead, use names (for example, field names, status names) for better compatibility.
4. **Mind the notification configuration differences:**  
   In Data Center, SLA notifications define both when something happens and what Time to SLA should do. In Cloud, this functionality is managed through [Actions](/cms_trial/space/TTSC/35881090/Actions/). During migration, supported Data Center notification configurations are converted into Cloud actions. Configurations that don't have an equivalent in Cloud aren't migrated.   
   Check out the table below for detailed information:

|  |  |  |
| --- | --- | --- |
| **Data Center configuration** | **After migration** | **Workaround** |
| **Fire an event** | No Cloud action is created. | You can use [Trigger Jira automation](/cms_trial/space/TTSC/1464075666/Use+SLA+actions+with+Jira+automation/) to recreate the required behavior. |
| Some recipient types available in Data Center aren't supported by Cloud actions.  This applies to:   - **Project lead** - **Component lead** - **Voters** - **Watchers** - **Project role** - **Custom email address** | During migration, unsupported recipients are skipped.   - If the notification includes both supported and unsupported recipients, the Cloud action is created with the supported recipients only. - If the notification includes only unsupported recipients, no Cloud action is created. | Recreate the action using a supported recipient type. If you need to preserve the original recipient logic, use [Trigger Jira automation](/cms_trial/space/TTSC/1464075666/Use+SLA+actions+with+Jira+automation/). |
| [**Automation notification settings**](https://appfire.atlassian.net/wiki/spaces/TTS/pages/49742237) | The automation-specific settings aren't carried over. | Recreate the required behavior in Jira Automation after migration. |

---

## Migration process

When you migrate to cloud with Jira Cloud Migration Assistant, you also migrate your work item SLAs. This means you don't need to perform a recalculation upon migration. However, when you use the Import/Export feature, you’ll need to recalculate. If you have a large number of work items, we strongly recommend using JCMA, as recalculating them afterward can be difficult.

### Option 1: Migrate using Jira Cloud Migration Assistant (JCMA)

To retain work item history and SLA continuity, use JCMA. This method preserves historical SLA data, work item data, and configurations.

1. **Start migration:**

   - Go to **Jira** **Settings** > **System** > **Migrate to Cloud**.
   - Select **Assess your Apps** and mark **Time to SLA** as **Needed in Cloud**.
2. **Follow JCMA prompts:**  
   JCMA will guide you through the migration process, ensuring all SLA configurations, calendars, and notifiers are migrated. For detailed steps, refer to [Atlassian’s JCMA guide](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/).  
   When JCMA asks which data to migrate, make sure to include both Spaces and Apps (Time to SLA) in the same selection. This step ensures all SLA-related configurations migrate together.
3. **Post-migration check:**  
   Once the migration is complete, you should see your SLAs, calendars, and SLA panels functioning normally within your cloud work items. JCMA ensures history is retained, so SLAs should remain fully functional on the cloud.

### Option 2: Export/Import method

This method only migrates SLAs and calendars and requires additional steps for recalculating SLA data.

1. **Migrate your instance with JCMA**  
   It's recommended to first migrate your entire instance with JCMA. This ensures all configurations used in your SLAs are migrated before importing SLAs and calendars.
2. **Export your SLAs and calendars**   
   Follow the provided instructions to export your SLAs and calendars from your Data Center instance.

   1. Go to **Import/Export** > **Export**.
   2. Select the SLAs you want to export.
   3. Select the calendars you want to export.
   4. Check your selections in the *Export* section, and click **Export** once you think they are ready.
   5. Your export will be downloaded in .json format automatically.
3. **Import your SLAs and calendars**   
   Follow the provided instructions to import your exported SLAs and calendars into your Cloud instance.

   - Go to **Import/Export** on the sidebar and click **Import**.
   - Upload the file you want to import, select its source, and specify where it’s coming from.
   - Select how you’d like to merge imported configurations with existing ones.
   - Select and match the components you want to import.
   - On the *Summary* screen, check if there are any mistakes in your selections. After you make sure everything is as it should be, click **Import**.
   - Once the process is done, the imported configurations appear on your related screens.
4. **Recalculate SLA data**   
   Since work item history is not migrated with this method, you'll need to recalculate SLA data for all your work items. We recommend using our [recalculation guide](/cms_trial/space/TTSC/35456416/Recalculation/) to perform this in smaller batches to avoid throttling issues.

---

## After the migration

1. **SLA panel visibility in Jira Cloud**  
   In Jira Cloud, the Time to SLA panel is not automatically displayed in work item views due to Forge limitations. After migration, the administrator needs to manually add the SLA panel to the work item layout so it’s visible to all users. Learn [how to add](/cms_trial/space/TTSC/2513797296/Changes+after+the+Forge+migration/) and [manage the panel](/cms_trial/space/TTSC/35815658/SLA+panel/) in Jira Cloud.

---

## Special case: SLAs using Duration custom fields

In Data Center, SLAs can be configured using Duration custom fields as goal values. These fields are not supported in cloud.

During the JCMA migration, a text custom field with the same name is created in cloud to preserve the configuration structure. However, Duration field values are not automatically migrated. Manual action is required to transfer these values after the migration.

### Manual transfer steps

Perform the following steps after migrating to the cloud with JCMA:

#### Step 1: Export Duration field values from Data Center

1. Go to **Issue Search** in Jira DC.
2. Run a JQL query such as:  
   `project = PROJECT_KEY AND ("TTS Duration 1" is not EMPTY OR "TTS Duration 2" is not EMPTY)`

   Add or remove `OR` clauses as needed.
3. Switch to **List View**.
4. Open the **Columns** dropdown and display only:

   - `Key`
   - `Summary`
   - Relevant TTS Duration fields
5. Click **Export** > **CSV (Current Fields)**.

#### Step 2: Import Duration values to cloud

1. In Jira Cloud, go to **Settings** > **System** > **External system import**.

   - If applicable, click **Switch to the old experience**.
2. Select **CSV** and upload the exported file.
3. Click **Next**, and select the target space.
4. On the mapping screen:

   - Map `Issue Key`, `Summary`, and TTS Duration fields.
   - **Do not map** `Issue ID`.
   - Check **Map field value** for all mapped fields.
5. Click **Next**, then **Begin Import**.

Repeat these steps for all spaces using SLAs with Duration fields.

## If you have already migrated TTS, but the instance has not been migrated yet

If you have already migrated Time to SLA but have not yet migrated the full instance, follow these steps:

1. Disable Time to SLA on the cloud side to prevent any data issues.
2. Run a new JCMA migration to migrate any spaces that you may have deleted in cloud during the first step.
3. Perform any necessary bulk imports or updates to ensure data consistency.
4. Enable Time to SLA again on the cloud side once the instance data is fully synchronized.
5. Complete the import of SLAs and calendars, if it wasn’t already completed in the previous steps.
6. Run recalculations in smaller batches following our [recalculation guide](/cms_trial/space/TTSC/35456416/Recalculation/) to avoid request overload.

---

## Troubleshooting

### Secured work item SLA data isn’t migrated

If your Jira Data Center instance uses work item security schemes, some work item SLA data may not be migrated to Cloud if Time to SLA can’t access the secured work items during migration.

In Jira Cloud, Time to SLA needs the `atlassian-addons-project-access` role to be included in the relevant work item security levels. This role exists only in cloud and can’t be added from the Data Center side before migration.

After migrating your projects to cloud, make sure this role is added to the required work item security levels. If the role is missing, uninstall and reinstall Time to SLA in Cloud to add the related role to all security levels. Then run SLA recalculation to regenerate the missing work item SLA data.

---

*In case you need any guidance or help during your migration process, don’t hesitate to* [*contact us*](https://appfire.atlassian.net/servicedesk/customer/portals)*– we'll be glad to help!*