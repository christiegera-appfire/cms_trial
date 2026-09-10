# Known issue: Incorrect placement of validators and conditions after migration to Jira Cloud

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

### Overview

This article addresses a known issue where **Power Scripts** experienced an incorrect migration of workflow elements when moving from a Jira Data Center or Server instance to Jira Cloud using the **Jira Cloud Migration Assistant (JCMA)**.

The issue causes validators and conditions to be incorrectly placed as post functions in a workflow. This can lead to unexpected behavior, such as running a script that was designed to be a validator or a condition as a post-function.

This issue has been resolved in these versions of the Power Scripts app:

- Power Scripts for Jira Cloud v. 3.2.15
- Power Scripts for Jira Data Center v. 6.2.820.12 and v. 7.0.1000.7

---

### Symptoms

Users affected by this issue will observe the following behavior after migrating their instance to Jira Cloud:

- Upon inspecting the workflow in the Jira Cloud workflow editor, you might see your original SIL validators and conditions listed under the **Post Functions** tab.

---

### Root Cause

The underlying problem causing this behavior is a bug in certain versions of the Power Scripts app that was used during the JCMA migration. The migration process incorrectly handled the mapping of these workflow elements.

Specifically, the migration tool failed to properly categorize SIL workflow objects and placed them all as post functions, regardless of their original type (validator, condition, or post function). This bug has been fixed in:

- Power Scripts for Jira Cloud v. 3.2.15

See the Release notes for Power Scripts for Jira Cloud [version 3.2.15](/cms_trial/space/PSJC/2229469185/3.2.15+Release+notes/).

- Power Scripts for Jira Data Center v. 6.2.820.12 and v. 7.0.1000.7

See the Release notes for Power Scripts for Jira for [version 6.2.820.12](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/2219409409) and [version 7.0.1000.7](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/2219180061).

---

### Solution

If you have already migrated to Jira Cloud and are experiencing this issue, the only solution is to manually check your workflows.

1. Open the workflow editor for any affected workflows.
2. Go to the **Post Functions** tab and identify the SIL script post functions that were originally validators or conditions.
3. Remove the scripts that were originally validators or conditions.

If you are unable to perform the manual correction or are unsure which scripts are affected, please contact our support team.

---

### Workaround for post-migration workflow correction

If you have already migrated to Jira Cloud and are experiencing this issue, you can manually correct your workflows. An alternative to removing the SIL scripts is to rewrite them using Jira expressions. This approach provides a long-term solution that avoids dependency on the Power Scripts app for these specific workflow elements.

To use this workaround:

1. Open the workflow editor for any affected workflows.
2. Go to the **Post Functions** tab and identify the SIL script post functions that were originally validators or conditions.
3. **Create a new validator or condition** in the workflow.
4. Instead of using a SIL script, use the Jira expression option to rewrite the logic.
5. Remove the old SIL script from the **Post Functions** tab.

For detailed information and guidance on how to write Jira expressions, refer to the official [Atlassian Jira Expressions documentation](https://developer.atlassian.com/cloud/jira/service-desk/jira-expressions/).

---

### Prevention

The most effective way to prevent this issue is to ensure your Power Scripts apps are updated **before** you start the JCMA migration.

- **Before migrating to Jira Cloud:**

  - Update your **Power Scripts for Jira Data Center** app to version **6.2.820.12** or **7.0.1000.7** (or newer).
  - Ensure your **Power Scripts for Jira Cloud** app is at version **3.2.15** or newer.
- After a migration, always perform a thorough check of your migrated workflows to ensure all post functions are correctly placed.

---

### Additional information

- **When to contact support:** If you have already updated to a newer version and the issue persists, or if you need assistance with manually correcting your workflows, please contact our support team.
- **Related fixes:** This issue was addressed in the specific versions mentioned above. You can view the full release notes for a complete list of fixes and improvements.