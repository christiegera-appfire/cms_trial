# Create and manage snapshots

### What’s included in a snapshot

A snapshot is a packaged state of your Jira Cloud projects and their configuration elements that you can export and later deploy to any Jira Cloud site. Snapshots let you prepare, review, and reuse configurations without immediately running a deployment.

Snapshots support the configuration elements [listed here](/cms_trial/space/CMJC/193855959/Supported+configuration+elements/).

---

### Prerequisites

Before creating a snapshot:

- Install and license CMJ Cloud on your Jira Cloud site.
- Make sure you have **Site admin** or **Organization admin** permissions.
- Use a supported Jira Cloud plan (Standard, Premium, or Enterprise).
- Have an Atlassian **API token** for your Atlassian account.

---

### Create a snapshot

The following video will show you how to create a CMJ snapshot.

Alternatively, you can follow our step-by-step guide for some more detailed explanations:

1. In your Jira Cloud site, go to **Apps > Configuration Manager > Snapshots**.
2. If you haven’t created or uploaded any snapshots yet, you’ll see a **New snapshot** button on the page. Otherwise, you can use the **New Snapshot** button in the top-right corner to create a snapshot.

   ![Snapshots page showing the New snapshot button used to create a new snapshot.](/cms_trial/assets/02e45bc1-e473-4e1d-af48-fe03c38e2a1f.png)
3. On the *New snapshot* page, choose what you want to capture:

   - **Specific elements** – Select individual projects and configuration elements for a custom snapshot.
   - **Everything supported** – Include all currently supported projects and configuration elements in the snapshot.

![New snapshot scope page with the Specific elements and Everything supported options available for creating a snapshot.](/cms_trial/assets/6b81c502-a8bb-4a74-b349-03faf39fbfa2.png)

1. Enter a name for your snapshot.
2. If you selected:

   - **Specific elements** - click **Select** below the snapshot name field and choose the projects and configuration elements you want to include in the snapshot.  
     💡 *You only need to select the items you want to include. Any required dependencies are added automatically during snapshot creation.* [*Learn more*](#How-dependencies-work)

     ![Configuration elements selector for choosing items to include in a snapshot.](/cms_trial/assets/aa8d421d-b33f-4d6e-a0df-b986f081ec43.png)
   - **Everything supported** - proceed to the next step.

1. When you’re ready with your selections, click **Next**.
2. You’ll move to the last part of the creation process, where you have to write a **Description** for the snapshot.

   ![Take snapshot page with the Description and Label field for the snapshot.](/cms_trial/assets/4fcd2e1d-40c4-4526-8131-733564675e52.png)
3. (Optional) Add a label in the **Labels** field.

   ![Take snapshot page showing the optional Description and Labels fields filled in before taking a snapshot.](/cms_trial/assets/73f36215-ac09-456c-8f79-898e0894dc5c.png)
4. (Optional) To set up scheduled snapshots, click **Edit** next to the **Frequency** field and configure a recurring schedule. [Learn more](#Schedule-recurring-snapshots)
5. Finally, click **Take snapshot** to start the export process.
6. After the snapshot is created, you'll be taken to the **Snapshot Summary** tab, where you can review the snapshot details and the number of configuration elements it contains. You can also switch to the **Scope** tab to review all the projects and configuration elements included in the snapshot.

---

### How dependencies work

When creating a snapshot using **Specific elements**, you only need to select the projects and configuration elements you want to include.

During snapshot creation, CMJ automatically analyzes your selection and includes any required dependencies. This helps ensure that the deployed configuration works as expected, without requiring you to manually recreate missing components.

For example, if you select a workflow, CMJ also includes the configuration elements that the workflow depends on, such as statuses, screens, and workflow schemes.

After the snapshot is created, you can review all included configuration elements on the **Summary** and **Scope** tabs.

---

### Schedule recurring snapshots

You can configure CMJ Cloud to automatically create new versions of a snapshot on a recurring schedule. This is useful when you want to observe configuration changes over time without manually creating a new snapshot version each time.

You can set the schedule when creating a snapshot or configure it later from the *Snapshot summary* screen.

#### Schedule a snapshot during creation

On the *Take snapshot* page, the **Frequency** section shows how often the snapshot will be created. By default, the snapshot is created just once.

![Frequency section on the Take snapshot page showing the current snapshot schedule.](/cms_trial/assets/9e6615d5-8b0e-4e8e-b7de-9ad489025008.png)

To set up scheduled snapshots:

1. Next to **Frequency**, click **Edit**.
2. In the **Snapshot frequency** dialog, open the **Repeat** menu.

   ![Snapshot frequency dialog showing the Repeat menu for selecting a recurrence schedule.](/cms_trial/assets/2fcd84e6-df6b-426f-9af9-8d4cc599087d.png)
3. Choose how often you want CMJ to take the snapshot:

   - **Do not repeat** – Create the snapshot only once.
   - **Daily** – Create a new snapshot every day.
   - **Weekly** – Create a new snapshot on one or more selected days of the week.
   - **Biweekly** – Create a new snapshot every two weeks.
   - **Monthly** – Create a new snapshot on the selected day of each month.
4. Configure the available scheduling options for the selected frequency, such as the day and time.
5. Click **Save**.

The initial snapshot is created when you click **Take snapshot**. CMJ then creates new versions of the same snapshot according to the schedule you configured.

#### Schedule snapshots on an existing snapshot

You can add, change, or disable the schedule after a snapshot has been created.

1. Go to **Apps** > **Configuration Manager** > **Snapshots**.
2. Open the snapshot you want to manage.
3. On the *Summary* screen, click the **Calendar** button in the upper-right corner.
4. In the **Snapshot frequency** dialog, change the recurrence, days, or time as needed.
5. Click **Save**.

To stop creating scheduled versions, select **Do not repeat** and save your changes.

Changing the schedule doesn’t change the snapshot scope. Each scheduled version captures the configuration from the snapshot’s existing scope, consistent with how CMJ currently creates new versions of an existing snapshot.

---

### Manage snapshots

In the *Snapshots* page, you can view a list of all your snapshots that have either been created or uploaded to the current Jira Cloud instance. You can use the search bar and the associated filters (Projects, Boards, Status, Created) to easily navigate to specific snapshots.

Additionally, you can use the manage options (…) for each snapshot to take the following actions:

- **Take snapshot** to update the data for your snapshot’s scope (Cloud snapshots only)
- **Deploy** a snapshot to this or another Jira Cloud instance.
- **Open** a snapshot to review its details in the *Snapshot summary* screen.
- **Delete** a snapshot you no longer need.

![Snapshots list showing the Manage options menu.](/cms_trial/assets/c40d5c95-8fb8-4063-bd06-8af6db73e894.png)

---

### Snapshot scope summary screen

When you open a snapshot from the list, you’ll see its details. Here, you can use the **Take Snapshot** button to create an up-to-date version of this snapshot with the exact same scope. If any projects or configuration elements are no longer available in your Jira Cloud instance, they’ll also be removed from your snapshot scope when a new version is created.

You can use the **Calendar** button in the upper-right corner to schedule new snapshot versions automatically or manage an existing schedule.

![Summary screen with the Calendar button for managing the snapshot schedule.](/cms_trial/assets/45f5f8dc-b7e7-47c4-b463-d4bb5aafbba8.png)

On the *Summary* tab, you’ll have the following sections:

**Details**

Here you can find information like the snapshot’s description, labels (if any), status, source instance, creation date, and who created it.

**Deployments**

In this section, you can find information on whether and where the snapshot has been deployed. Also, you can use the **Deploy** button to start a deployment with this snapshot scope.

**Configurations**

This section contains information about what configuration elements are included in the snapshot scope and how many of each you can find. [Learn more about the supported configuration elements](#What%E2%80%99s-included-in-a-snapshot)

![Summary tab displaying snapshot details and a summary of included configuration elements.](/cms_trial/assets/01f7a3f9-427d-47cf-8814-9f7a6b64f5ff.png)

On the *Comparison* tab, you can analyze the differences between two versions of the same snapshot scope. [Learn more about comparisons](https://support.appfire.com/space/CMJC/3417473252/Compare+snapshots)

![Comparison tab that can show differences between two versions of the same snapshot.](/cms_trial/assets/154e509a-3c4a-4bc2-850f-1477c8f0e0bd.png)

On the *Scope* tab, you’re able to view the snapshot’s original scope and whether any changes have occurred to it (for example, in the screenshot below, you can see that one of the projects has been deleted and is no longer available for this version of the snapshot scope). When you create a new snapshot version, you’ll be using the exact scope you find here; you won’t need to select anything.

![Scope tab listing the spaces and configuration elements included in the snapshot scope.](/cms_trial/assets/4e6eac8c-7f51-4113-92fe-4353f5dd2626.png)