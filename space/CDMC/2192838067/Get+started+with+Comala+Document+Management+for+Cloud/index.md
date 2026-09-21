# Get started with Comala Document Management for Cloud

**Action required: Upgrade to the Forge version**

Atlassian will end [support](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps) for the Connect framework in late 2026. After that date, the Connect version of Comala Document Management for Confluence Cloud will no longer receive security updates, new features, or ongoing support.

To continue receiving updates and support, you must upgrade to the Forge version of Comala Document Management. [Learn more about the upgrade.](https://support.appfire.com/space/CDMC/3412264373/End+of+support+for+the+Connect+framework)

Comala Document Management adds review and approval workflows to Confluence Cloud. Teams can assign reviewers, set deadlines, and track a document's lifecycle. Integrated reporting tools provide oversight of all status changes and approvals within a space.

**Before you start: Set up Comala Document Management**

If you are new to Comala Document Management Cloud, follow these steps to set up your environment:

1. **Installation and setup:** [Install the app](/cms_trial/space/CDMC/2192870167/Installation/) and configure global permissions.
2. **Space activation:** Enable Comala Document Management for specific Confluence spaces. See [Onboarding](/cms_trial/space/CDMC/2192869918/Onboarding/).

## Get your first document signed off

Run one page through a full review to see how the app works. You apply a workflow, assign the page for review/approval, approve it, and finish with a live status and a complete audit trail.

1. Open a page in a space where Comala Document Management is enabled, or create a test page. When the app is on, a **Document Management** indicator appears in the page byline.
2. In the page byline, select the **Document Management** status indicator to open the *Workflow State* dialog.

   ![Workflow State Dialog with the Apply to Content and Apply to Space options.](/cms_trial/assets/2aed087a-ae28-4827-a4d2-ddf50eda4a68.png)
3. Select **Apply to Content**, then pick a workflow. Comala ships with ready-made example workflows, so choose one that includes a review and an approval, then select **Apply Workflow**.

   ![image-20260914-201044.png](/cms_trial/assets/eb7d6c7b-a0dd-4ae6-adb3-d98e08d3ce88.png)
4. Confirm the first state (for example, **In Review**) in the page byline.

   ![image-20260914-201208.png](/cms_trial/assets/5db3043a-ce03-4f1a-89e3-01d77b2e810b.png)
5. In the dialog, assign a reviewer. To test the full flow yourself, assign your own account. Reviewers are notified by email and an on-screen alert.
6. As a reviewer, open the dialog and select **Approve**.

   ![image-20260914-201431.png](/cms_trial/assets/93494a2b-5efc-4798-a995-91d9303efa43.png)
7. The status badge changes to **Approved** in the byline.

   ![image-20260915-041038.png](/cms_trial/assets/82f3d043-2013-4144-b7ac-e453fcc62a4d.png)
8. Go to **Space Apps > Comala Document Management > Document Report** to review the audit trail. The report lists each page’s title, applied workflow, scope, workflow state, and reviewers (click a reviewer to see who approved and when). If your workflow uses due dates, an **Expiration** column also appears.

![image-20260629-053807.png](/cms_trial/assets/06ab5c84-e0c3-47c9-99c9-64862e8d60f7.png)

Your page now shows a live status and records every decision. No spreadsheets, no email chase.

## What else you can do

### See status on every page

Each page with an active workflow shows its current state in the byline. Anyone who opens the page knows whether it is in review or approved.

![image-20260616-132413.png](/cms_trial/assets/0b5abab9-19ba-4aac-b50c-a2bb4dca39b3.png)

[Learn more about workflow states](/cms_trial/space/CDMC/2193066115/States/)

### Review and approve in one dialog

Assign reviewers, set deadlines, and record decisions from the Workflow State dialog. Reviewers act without leaving the page.   
You can also require reviewers to authenticate their decisions using [e-signature capabilities](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) to ensure secure and verifiable approvals.

![Add Approval dialog displaying configuration options for approval settings, outcome criteria, and reviewers.](/cms_trial/assets/2b7df553-8121-4ad4-85e7-c9f7043970b1.png)

[Learn more about approvals](/cms_trial/space/CDMC/2193195490/Approvals/)

### Automate with triggers

Triggers run actions on workflow events, such as emailing a reviewer, locking a page during approval, or setting an expiry date on approved content.

![image-20260629-053111.png](/cms_trial/assets/e0ef5397-6f92-46a9-9afd-533b54f03d52.png)

[Learn more about triggers](/cms_trial/space/CDMC/2192967825/Triggers/)

### Customized notifications

Comala Document Management sends email notifications for key events. On-screen notifications appear for users assigned to approve a page.

For example,

- Assignees are notified when assigned to review a page or blog
- Notifications are sent when the expiry date is reached for content with the *Content Expiry workflow*.

![CDM workflow notifications.](/cms_trial/assets/0a9921ce-bdea-46fd-967d-a8ad085a7910.png)

[Learn more about notifications](/cms_trial/space/CDMC/2193001238/Notifications/)

## Tips

- **Reuse a workflow across teams:** Use parameters, such as default reviewers, deadlines, and messages, so one workflow fits many spaces without rebuilding it. See [Workflow parameters](/cms_trial/space/CDMC/2192837939/Parameters/).
- **Apply once for a whole space:** Enable a workflow at the space level so every new page starts in review automatically.
- **Report across spaces:** Export the Document Report or Document Activity to CSV to merge spaces or build custom dashboards.

## Next steps

- [Create and edit workflows](/cms_trial/space/CDMC/2193162391/Create+and+edit+workflows/): Build your own stages, triggers, and parameters.
- [Apply workflows](/cms_trial/space/CDMC/2192870271/Apply+workflows/): Compare page-level and space-level workflows.

## Migrating from Data Center?

Planning a Cloud migration? Start here:

[Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/) – Key differences between DC and Cloud  
[Migration support from Appfire](https://appfire.atlassian.net/servicedesk/customer/portal/11/group/1236) – Guided migration assistance