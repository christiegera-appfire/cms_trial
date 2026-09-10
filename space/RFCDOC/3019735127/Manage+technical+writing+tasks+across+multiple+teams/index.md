# Manage technical writing tasks across multiple teams

Writers' work is often spread across multiple development teams and tracked in separate Jira projects. Without a unified view, managing documentation requests, release notes, video progress, and content reviews leads to constant context switching, making it harder to spot bottlenecks, balance workloads, and stay aligned with development cycles.

This article walks you through building a Technical Writing dashboard using Rich Filters for Jira Dashboards. The result is a single, filterable dashboard that gives your team a real-time overview of all their work across every project, along with an easy way to report progress.

![Tech writer dashboard](/cms_trial/assets/1a12e29e-1f68-4304-8808-99135586907f.webp)

## Before you start

Make sure you are using Jira Cloud and that all projects are on the same Jira instance.

## Use case

You have a centralized team of technical writers creating documentation, release notes, microcopy, and video tutorials for multiple development teams. Your writers need to track their assignments across various Jira projects, monitor individual workloads, handle documentation review requests, and support marketing campaigns.

Rich Filters for Jira Dashboards solve this by letting you aggregate and filter issues across multiple projects in a single view. Because rich filters are based on a standard Jira filter, the issues listed can span all your Jira projects and product teams.

The *Technical Writing* dashboard consists of the following gadgets:

- **Rich Filter Controller** -the main control panel, letting writers slice the data using static, dynamic, and smart filters (details in the *Configure filters* section below).

  ![Rich Filter Controller ](/cms_trial/assets/de0b4638-c17f-433f-8355-ca8ab8cdffb4.png)
- **Writers tasks** (Rich Filter Results gadget) - a comprehensive list of work, showing the Assignee, Pod, Status, Summary, Project, and Last comment.

  ![Writer tasks (Rich Filter Results gadget) ](/cms_trial/assets/ae1096bc-f386-44b1-b98c-a3f7ac47a528.png)
- **Rich Filter Flexi Charts** - a bar chart showing issue count by status (for example, Backlog, To Do, In Progress, In Review) so the team can quickly spot bottlenecks in the publishing pipeline.

  ![Rich Filter Flexi Charts ](/cms_trial/assets/7f884fe9-8f6a-482a-bfb1-65cb21a73807.png)
- **Pods** (Rich Filter Smart Gauges gadget)- a gauge chart that shows the percentage and exact number of issues assigned to each pod, so you can monitor workload distribution.

  ![Pods (Rich Filter Smart Gauges gadget)](/cms_trial/assets/25e31e36-850b-46b0-a2a7-ce2196d0b518.png)
- **Assignees** (Rich Filter Flexi Chart) - a breakdown of all issues by assignee, showing how many each team member is handling.

  ![Assignees (Rich Filter Flexi Chart)](/cms_trial/assets/c59d6163-ae6f-4e72-aee4-7f8c1ffdaefe.png)
- **Content by type** (Rich Filter Simple Counter) - a dedicated counter for video tutorials, microcopy work, and release notes.

  ![Content by type (Rich Filter Simple Counter) ](/cms_trial/assets/e2544147-6c93-4b59-b6ef-9e5eca2776a4.png)
- **Videos by Team Member** (Rich Filter Pie Chart) - a breakdown of video tutorial issues by assignee.

  ![Videos by team member (Rich Filter Pie Chart) ](/cms_trial/assets/4a2b3ab6-46f6-4d0a-926e-caece88ad35e.png)

---

## Create the rich filter and Jira dashboard

The rich filter is the foundation of the dashboard. It defines the pool of Jira issues that all gadgets will draw from.

1. Create a new rich filter based on a Jira filter that returns all the documentation and technical writing work items you want to manage.

   ![Create new rich filter ](/cms_trial/assets/b09ad997-5734-4b2e-a3df-85ef1e366f0e.png)

   If you need guidance on creating rich filters and dashboard basics, see [Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942749).
2. Create a new dashboard and name it *Technical writing.*
3. Set **Viewers** to *My organization* so everyone in your company can view it.
4. Select the **Two-column** layout.

### Add gadgets

Add the following gadgets to your dashboard. In each case, select your *Technical Writing* rich filter as the **Rich filter** value, then click **Submit**:

**Left column:**

1. Rich Filter Controller (Main).
2. Rich Filter Results gadget and name it: *Writers tasks.*
3. Click **Done** to exit dashboard edit mode.

### Configure filters

Filters control what all the gadgets on the dashboard display. Static filters offer one-click buttons; dynamic filters expose individual Jira fields for ad hoc filtering; smart filters group tickets by custom logic (in this case, by pod, which is a team of writers working together).

To configure them, open your rich filter configuration.

1. Go to the *Static filters* tab of your rich filter config.
2. Create three static filters:

   1. *Recently updated* with the *JQL* `updated >= -30d`.
   2. *Assigned to me*, with the *JQL* `assignee = currentUser()`.
   3. *Recently resolved* with the *JQL* `statusCategory = Done AND resolutiondate >= -2w`
3. Go to the *Dynamic filters*tab and add filters for the following Jira fields: Assignee, Status, Priority, Project, Sprint, Product, Updated, and Labels.
4. Go to the *Smart filters*tab and create a smart filter called *Teams* to categorize tickets by the writer pods.

   1. Add a separate clause for each pod. (The JQL `assignee in membersOf("team-name")` filters issues to show only those assigned to members of your existing Jira groups, so you must use your organization's actual group names for it to work):

| Pod | Color | JQL |
| --- | --- | --- |
| Fab 4 | Purple | `assignee in membersOf("fab4")` |
| Pod 2 | Green | `assignee in membersOf("pod2")` |
| D&D | *Red* | `assignee in membersOf("dd")` |
| Connection Collective | Orange | `assignee in membersOf("connectioncollective")` |
| Sprintbusters | Blue | `assignee in membersOf("sprintbusters")` |
| Peas in a pod | Pink | `assignee in membersOf("peasinapod")` |

b. Go back to your dashboard and refresh it.   
Your controller should display all static, dynamic, and smart filters. Additionally, you can customize the shown filters, adding colors and custom sections.

![customize the shown filters](/cms_trial/assets/de0b4638-c17f-433f-8355-ca8ab8cdffb4.png)

### Set up your views

Views define which columns appear in each Rich Filter Results gadget.

1. Go to the *Views* tab of your rich filter config.
2. Create your view: *All work* with the columns: *Assignee, Pods, Status, Summary, Project, Last comment*.

   ![Rich Filter Results view showing Assignee, Pod, Status, Summary, Project, and Last comment columns.](/cms_trial/assets/0173c4cb-5a56-4a9d-a84f-a1ef0ae52b95.png)

3. Go back to your dashboard and refresh it.   
The Writers Tasks gadget now displays all the columns defined in the view.

![Writer Tasks Rich Filter Results gadget displaying the configured view with task columns.](/cms_trial/assets/4cbdbc74-6a70-48c2-8f7a-1c3d5ef4a8e6.png)

### Set up custom values

Labels on work items (`video`, `ux-writing`, `releasenotes`) let you break out specific content types in your counters and charts. Custom values translate those labels into named metrics you can reference across gadgets.

1. Go to the *Custom values* tab and create the following custom values:

| **Name** | **Base value** | **JQL** |
| --- | --- | --- |
| Microcopy | *Issue Count* | `labels = ux-writing` |
| Video | *Issue Count* | `labels = video` |
| Release notes | *Issue Count* | `labels = releasenotes` |

### Set up your charts and counters

Add the following gadgets to your dashboard. In each case, select your *Technical writing* rich filter as the **Rich filter** value. Configure each gadget to display the right data in the right format.

1. Rich Filter Flexi Charts and name it: *Rich Filter Flexi Charts.*

   1. **Chart type**: *Bar*
   2. **Statistic type**: *Status*
   3. **Value**: *Issue Count*  
      Flexi Chart gadget shows the distribution of issues depending on their status, allowing you to spot bottlenecks in the publishing pipeline.

**Right column:**

1. Rich Filter Smart Gauges gadget and name it: *Pods.*

   1. **Smart filter**: *Pods*
   2. **Computation mode**: *Use smart clauses as gauge filters*
   3. **Value**: *Issue Count*
   4. **Layout**:  *Gauge*  
      The gadget shows the percentage and exact number of issues assigned to each team, so you can monitor workload distribution.
2. Rich Filter Flexi Chart and name it: *Assignees.*

   1. **Chart type**: *Donut*
   2. **Statistic type**: *Assignee*
   3. **Value**: *Issue Count*  
      The chart visualizes how the work is spread among the writers.
3. Rich Filter Counter and name it: *Content by type.*

   1. **Values**: *Video,* *Microcopy,* and *Release notes* custom values  
      You can now easily see how many new releases are prepared, accompanied by the video and microcopy tasks.
4. Rich Filter Pie Chart and name it: *Videos by Team Member.*

   1. **Working query**: `labels=video`
   2. **Chart type**: *Donut*
   3. **Statistic type**: *Assignee*
   4. **Value**: *Issue Count*  
      The gadget provides a preview for new videos published by the writers.

With this setup, your technical writing team has a single, always-current view of their entire workload. By using this layout, your technical writing team can seamlessly manage their workload, prioritize reviews, and keep all development pods well documented.