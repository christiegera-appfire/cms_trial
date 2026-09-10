# Store metric in a custom field

The **Store metric in custom fields** feature is disabled and will be retired soon

Due to operational changes and platform updates, the **Store metric in custom fields** feature is now disabled and will be permanently retired after December 10, 2025.

### **What’s NOT changing**

Foxly’s prioritization metrics inside the app will continue to work exactly as they do today.

### **What is changing**

- The **Store values in a custom field** feature is no longer available. The checkbox is disabled.
- After 10 December 2025, Foxly will remove the **Jira custom fields** that were created to duplicate metric values outside the app. These fields are marked lockedand include the description “Field dynamically added by Foxly”.

  - Only places where you use these fields **outside Foxly** will be affected, such as JQL filters, issue screens, Jira automation, dashboards, reports, or gadgets.
  - Once the fields are removed, any filters, automations, or dashboards that rely on them will stop working.

#### **How to identify which fields will be removed**

To identify which fields will be removed, go to:

1. **Jira admin settings** > **Work items** > **Fields** > **type “Foxly” in the search box**.
2. Look for Foxly-created dynamic fields with the locked label. **Only these fields will be deleted.**

![Jira admin Fields settings filtered by Foxly showing dynamic fields marked as locked](/cms_trial/assets/f3df4f34-8efa-4f11-8bee-9ab91b6820ed.png)

### **Recommended action**

- Review your workflows, dashboards, and automations that use Foxly-created dynamic Jira fields, and update them to remove dependencies on these fields.

You can continue using:

- Priority score fields
- Your [own Jira custom fields](/cms_trial/space/FOX/846594061/Connect+custom+fields+to+Foxly/) in prioritization formulas

Having Foxly metrics stored in the custom field unlocks the ability to search for issues by metrics, create reports, and automate.

For example, if your team is already using story points to estimate tickets and you would like to include them in the Priority score calculation, you can create an Automation rule in Jira. Let’s examine what custom fields are available and how to switch them on.

**Automation examples**

The [4 ways to automate your Jira backlog prioritization](https://jexo.io/blog/automating-backlog-prioritization-jira/) article covers four examples of how you can use Automation for Jira and Foxly. There, you can learn more about how to connect Story points to Foxly, how flagged tickets can influence your priority score, and more.

## Store metrics in a custom field

The column under **Label name** is the metric label, and the column under **Value** is the metric value.

![Effort metric Label name and Value image](/cms_trial/assets/87208473-9c1d-4fd5-8b76-131670d16cac.png)

Metric custom fields are created in the following format:

- `[Metric name] - [Priority model name] Value`
- `[Metric name] - [Priority model name] Label`

For example, if you’re using an *ICE* priority model and enable the custom field for **Ease** metric the following custom fields will be generated:

- `Ease - ICE Value` where the numeric representation of the metric is stored.
- `Ease - ICE Label` where the labels of the metrics are stored (examples: XS, M, L in case of **Ease** metric).

| **Metric type** | `[Metric name] - [Priority model name] Value` | `[Metric name] - [Priority model name] Label` |
| --- | --- | --- |
| **Rating** | The numerical value of the metric | Numbers from 1-5 representing the number of stars |
| **Label** | The numerical value of the metric | The text label of the metric |
| **Short text** | The numeric value of the metric | The text label of the metric |
| **Number** | The number imputed from Foxly | *Not present* |

## Enabling Metric custom fields

You can choose which metrics you want to enable as custom fields in Foxly settings.

You can enable custom fields for up to 50 Foxly Metrics.

1. Navigate to **Foxly** > **Customize**.
2. In the *Edit Template* section, click the metric.
3. Select the checkbox **Store values in custom field***.*
4. Click **Save changes** and **Save in all projects** to enable the custom field in all projects that use this template.

![Effort metrich showing the Store values in custom field option selected.](/cms_trial/assets/a980006e-d0b2-4857-9c07-0c8dafadcb23.png)

If you’re using **Next-gen projects,** you need to follow the steps in Atlassian’s [Announcing support for app issue fields in next-gen projects](https://community.atlassian.com/t5/Jira-articles/Announcing-support-for-app-issue-fields-in-next-gen-projects/ba-p/1431506) page to enable custom fields in them.