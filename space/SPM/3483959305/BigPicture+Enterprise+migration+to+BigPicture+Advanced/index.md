# BigPicture Enterprise migration to BigPicture Advanced

## Impact of BigPicture Advanced on BigPicture Enterprise

BigPicture Enterprise works as an extension to BigPicture. With the introduction of app editions for BigPicture for Jira Cloud, there is no immediate impact or required action for existing BigPicture Enterprise customers. You can continue using the app and renew your current licenses as usual.

Over time, the BigPicture Advanced plan will replace the BigPicture Enterprise app. This change is designed to simplify app management, streamline license renewals, and make it easier for you to understand and choose the right plan.

At present, BigPicture Enterprise and the BigPicture Advanced plan offer **full feature parity**.

BigPicture Enterprise Cloud is no longer available for purchase and is **planned to be sunset in 2027**. The exact date will be confirmed and communicated to all customers once finalized.

**We recommend enabling the Advanced plan in BigPicture and uninstalling the BigPicture Enterprise app**. Your data is safe and preserved, ensuring access to the latest updates, improvements, and features.

- Try BigPicture Advanced **free for 30 days** at no extra cost. **BigPicture Enterprise** and **BigPicture Advanced** have the same pricing (except for Jira instances with up to 10 users).
- **BigPicture Enterprise** will be discontinued at the end of Q3 2027.
- We're simplifying our product line to make advanced features easier to find and manage in one place. One license lets you switch between PPM and SPM at any time to fit your organization's needs.
- Migrate in just a few steps while keeping your existing data.

### Migration steps

The migration flow for clients with an active BigPicture Enterprise license is described below.

1. Follow the steps provided by Atlassian (<https://support.atlassian.com/organization-administration/docs/installing-and-managing-app-access/#Upgrade-app-edition>) and start a free trial for the Advanced plan.

![Connected app in Jira.png](/cms_trial/assets/5fa53ba4-8db8-4410-bac5-58dda8605909.png)

Customers on an **annual billing cycle** will have to contact a **Customer Advocate** to upgrade. This is a requirement on Atlassian’s side.

1. Open BigPicture. You will know you have switched to the Advanced plan based on:

   1. The **logo on the Home page** will change from yellow to blue (change visible to all users).

      ![BigPicture homepage.png](/cms_trial/assets/10b0362a-f9d4-4392-b645-1a4ee002b6b1.png)
   2. The app plan under the **License tab** in App Configuration shows you are on the advanced plan (visible only to a Jira admin).

      ![Screenshot 2026-04-14 at 15.38.08.png](/cms_trial/assets/e7a6bb7b-a830-4abd-80fe-ed55858368d2.png)
2. All your data and settings remain unchanged. You will see no changes in the app's configuration, data, or structure.

### Exceptions

We are unifying all app global permissions into a single management location. Access to the OKR and Priorities modules remains temporarily managed in Jira global permissions. These permissions cannot be migrated automatically. We plan to remove this limitation by **mid-Q3 2026.**

Customers who have changed the default Jira global permissions related to the OKR and Priorities modules might be affected and need to reconfigure their permissions manually.

1. **OKR module**: we use a legacy permissions check to access the module ONLY for clients (who installed BigPicture Enterprise before November 28, 2025). When you switch to Advanced, these OKR permissions will be empty and overwrite existing BigPicture Enterprise permissions (resulting in a splash screen when navigating to the module). Verify and adjust these permissions.

Only legacy clients will be affected; all in-module settings and permissions for OKRs will remain unchanged.

![Screenshot 2026-04-14 at 16.11.52.png](/cms_trial/assets/d0a2e935-a7b9-480a-86e4-3ad9e9f68e50.png)

| **BigPicture Enterprise Jira Global permissions** | **BigPicture Advanced Jira Global permissions** |
| --- | --- |
| *In use when you have BigPicture Standard and BigPicture Enterprise.* | *In use when you have BigPicture Advanced with or without BigPicture Enterprise.* |
| **Administer OKRs (Obsolete)** | **Administer BigPicture Advanced OKRs (Obsolete)** |
| **View and modify OKRs (Obsolete)** | **View and modify BigPicture Advanced OKRs (Obsolete)** |

1. **Priorities module**: When you switch to Advanced, the Priorities module permissions reset to default and overwrite existing BPE permissions. Verify and adjust permissions if you ever changed them from the default.

With default permissions, all users will be affected.

![Screenshot 2026-04-14 at 15.54.32.png](/cms_trial/assets/0a22c7c2-e042-445f-a9fe-6acc7dd56bd6.png)

| **BigPicture Enterprise Jira Global permissions** | **BigPicture Advanced Jira Global permissions** |
| --- | --- |
| *in use when you have BP Standard and BPE* | *in use when you have BP Advanced with or without BPE* |
| **Administer BigPicture Enterprise Priorities** | **Administer BigPicture Advanced Priorities** |
| **Manage BigPicture Enterprise saved views** | **Manage BigPicture Advanced saved views** |
| **Access BigPicture Enterprise priority poker** | **Access BigPicture Advanced priority poker** |

1. After verifying your data and reconfiguring OKR and Priorities modules permissions if needed, you’re free to **uninstall BigPicture Enterprise** from your Jira instance.

   1. There is no limit to how long you can keep BigPicture Enterprise installed with BigPicture Advanced enabled, but we highly recommend **uninstalling BigPicture Enterprise before the trial for the Advanced plan ends** to avoid double payment.
2. For licensing questions or any other help, [contact our support](https://appfire.atlassian.net/servicedesk/customer/portal/11).