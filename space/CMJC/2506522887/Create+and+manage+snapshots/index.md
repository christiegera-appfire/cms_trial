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

The following video will show you just how easy it is to create a CMJ snapshot.

Alternatively, you can follow our step-by-step guide for some more detailed explanations:

1. In your Jira Cloud site, go to **Apps > Configuration Manager > Snapshots**.
2. If you haven’t created or uploaded any snapshots yet, you’ll see a **New snapshot** button on the page. Otherwise, you can use the **New Snapshot** button in the top-right corner to create a snapshot.

   ![Snapshots page showing the New snapshot button used to create a new snapshot.](/cms_trial/assets/d92a3046-0fac-4862-8735-6648ad82fcb8.png)
3. On the *New snapshot* page, choose what you want to capture:

   - **Specific elements** – Select individual projects and configuration elements for a custom snapshot.
   - **Everything supported** – Include all currently supported projects and configuration elements in the snapshot.

![New snapshot scope page with the Specific elements and Everything supported options available for creating a snapshot.](/cms_trial/assets/9c4da9d4-564d-4bf3-a96c-557d58ecee10.png)

1. Enter a name for your snapshot.
2. If you selected:

   - **Specific elements** - click **Select** below the snapshot name field and choose the projects and configuration elements you want to include in the snapshot.  
     💡 *You only need to select the items you want to include. Any required dependencies are added automatically during snapshot creation.* [*Learn more*](#How-dependencies-work)

     ![Configuration elements selector for choosing items to include in a snapshot.](/cms_trial/assets/923b0d1d-a2af-4feb-a292-c5d0518fb650.png)
   - **Everything supported** - proceed to the next step.

1. When you’re ready with your selections, click **Next**.
2. You’ll move to the last part of the creation process, where you have to write a **Description** for the snapshot.

   ![Take snapshot page with the Description and Label field for the snapshot.](/cms_trial/assets/56d4fe04-ea73-427d-aa4f-3cb173399ce5.png)
3. (Optional) Add a label in the **Labels** field.

   ![Take snapshot page showing the optional Description and Labels fields filled in before taking a snapshot.](/cms_trial/assets/c41c9d5b-4b89-4f48-a090-ec22a79a4780.png)
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

![Frequency.png](/cms_trial/assets/b11ff4d8-7c86-4523-ae64-d42db6432e80.png)

To set up scheduled snapshots:

1. Next to **Frequency**, click **Edit**.
2. In the **Snapshot frequency** dialog, open the **Repeat** menu.

   ![Repeat.png](/cms_trial/assets/3874c892-d90e-4172-a3d0-03c208ff3879.png)
3. Choose how often you want CMJ to take the snapshot:

   - **Do not repeat** – Create the snapshot only once.
   - **Daily** – Create a new snapshot every day.
   - **Weekly** – Create a new snapshot on one or more selected days of the week.
   - **Biweekly** – Create a new snapshot every two weeks.
   - **Monthly** – Create a new snapshot on the selected day of each month.
4. Configure the available scheduling options for the selected frequency, such as the day and time.
5. Click **Save**.

The initial snapshot is created when you click **Take snapshot**. CMJ then creates new versions of the same snapshot according to the schedule you configured.

#### Schedule snapshots on an already existing snapshot

You can add, change, or disable the schedule after a snapshot has been created.

1. Go to **Apps > Configuration Manager > Snapshots**.
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

![Snapshots list showing the Manage options menu.](/cms_trial/assets/fb1f1918-ea96-435b-a1e8-4d31dd8bcd7b.png)

---

### Snapshot scope summary screen

When you open a snapshot from the list, you’ll see its details. Here, you can use the **Take Snapshot** button to create an up-to-date version of this snapshot with the exact same scope. If any projects or configuration elements are no longer available in your Jira Cloud instance, they’ll also be removed from your snapshot scope when a new version is created.

You can use the **Calendar** button in the upper-right corner to schedule new snapshot versions automatically or manage an existing schedule.

![Calendar.png](/cms_trial/assets/d3d60a1d-301d-4bd5-8da8-4e47a475af7d.png)

On the *Summary* tab, you’ll have the following sections:

**Details**

Here you can find information like the snapshot’s description, labels (if any), status, source instance, creation date, and who created it.

**Deployments**

In this section, you can find information on whether and where the snapshot has been deployed. Also, you can use the **Deploy** button to start a deployment with this snapshot scope.

**Configurations**

This section contains information about what configuration elements are included in the snapshot scope and how many of each you can find. [Learn more about the supported configuration elements](#What%E2%80%99s-included-in-a-snapshot)

![Summary tab displaying snapshot details and a summary of included configuration elements.](/cms_trial/assets/f181d3e8-6447-46d4-afa8-a781f6b2e678.png)

On the *Comparison* tab, you can analyze the differences between two versions of the same snapshot scope. [Learn more about comparisons](https://support.appfire.com/space/CMJC/3417473252/Compare+snapshots)

![Comparison tab that can show differences between two versions of the same snapshot.](/cms_trial/assets/6d115970-a522-473d-9328-5e8fd43d0771.png)

On the *Scope* tab, you’re able to view the snapshot’s original scope and whether any changes have occurred to it (for example, in the screenshot below, you can see that one of the projects has been deleted and is no longer available for this version of the snapshot scope). When you create a new snapshot version, you’ll be using the exact scope you find here; you won’t need to select anything.

![Scope tab listing the spaces and configuration elements included in the snapshot scope.](/cms_trial/assets/b501bb88-1f0b-4553-bab7-f111507206f4.png)