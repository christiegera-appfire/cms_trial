# Configure queues

## **About queues**

Queues allow you to display and manage a list of issues in Rich Filter Results gadgets. They are ideal for organizing support requests (by support agent, service desk, request type, etc.) and for managing lists of issues in general.

Queues are based on configurable JQL queries that further filter the issues returned by the rich filter. One or multiple queues can be displayed in a *Rich Filter Results* gadget, and each queue can use one or multiple [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) to display its issues. Each queue also has its own sorting criteria, independent of the others.

Here are some of the main features of the queues displayed in *Rich Filter Results* gadgets:

- Queues are displayed as tabs; users can simply switch between them with one click.
- Each queue has, next to its name, a colored badge with the count of the issues it contains. This informs users about the queues that require attention and action.
- The queues displayed in the same gadget are independent of the current view, page, and sort order.
- When you switch from one queue to another, the list of issues displayed is refreshed, as are the issue counts of all the queues in the gadget.
- Additional options (described below) control the queue's behavior: static and fixed-order.

![queues dash.png](/cms_trial/assets/6169b0d7-dd27-4b8b-956a-e4270fb3f9fb.png)

## **Queues key attributes**

You can add new and see existing queues and their configuration in the *Queues* section of your rich filter.

![Queues tab.png](/cms_trial/assets/44bb7348-748d-4f36-a10b-f584a5b16048.png)

The **key attributes** of a queue are:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | Each queue has a name used to identify and display the queue. It is required and must be unique among the queues within the rich filter. |
| **Color** | The selected color will display the queue in *Rich Filter Results* gadgets. |
| **JQL** | This is an additional JQL query for the queue. It defines the list of issues in the queue. Optionally, an ORDER BY clause can be used to set the default order of the issues in the queue.  Remember, the issues in the queue are already filtered by the base Jira filter, as configured in the [General section](/cms_trial/space/RFCDOC/783941695/Details+configuration/) of the rich filter.  Since the queue is based on JQL, it can, of course, be cross-project. |
| **Views** | The views used to display the queue's issues in *Rich Filter Results* gadgets. By default, the queue uses all the views defined in the rich filter (the option *Show all views* is selected).  The list of views can be customized (by selecting the option *Customize shown views*). You can add, remove, or reorder (by drag and drop) the views to be displayed. |
| **Static queue** | The issues displayed by static queues cannot be filtered out by quick filters in *Rich Filter Controller* gadgets. Use this option if the issues displayed by this queue should always be visible.  This can be useful for queues displaying issues that require immediate attention. You don't want issues in these queues to be easily filtered out or hidden. |
| **Fixed-order queue** | The order in which the issues are displayed by fixed-order queues in *Rich Filter Results* gadgets cannot be altered by clicking column headers. Use this option if the queue should always display the issues in a specific and immutable order, as configured in the queue (i.e., with an ORDER BY clause in the JQL field).  This can be useful for support queues that agents must manage in a particular order, which should not be changed intentionally or accidentally. |

## **Adding and editing queues**

The *Queues* section of your rich filter lets you perform the following operations:

### **1. Add a new queue**

1. Click **Create queue** at the top-right of the page.

   ![create queues.png](/cms_trial/assets/c53f1c45-5bee-41cb-9a3c-ad4ff47f68b6.png)
2. Type a **Name** and a **JQL** query, select a color and the views, and optionally check the queue behavior options, then click **Create**.

   ![contentId-783942406](/cms_trial/assets/012339d9-9b0b-47e1-b6a6-e0a76320f747.png)

You can reorder your customized views list by drag and drop.

You can add up to 100 queues in each rich filter.

### 2. **View or edit a queue**

Click the **Edit** (▢) icon next to a queue to view or edit its configuration. Depending on your rights, you can edit or only view the queue.

![contentId-783942406](/cms_trial/assets/ee620f1a-cc7c-41ad-b293-3a8e8aa5377a.png)

### 3. **Reorder the queues**

Hold the pointer over the queue's **Grid** (▢) icon, then drag the queue up or down to its new position.

![contentId-783942406](/cms_trial/assets/a4e741df-0a0b-4a81-8867-25ec13ec4282.png)

### 4. **Delete a queue**

Click the **Delete** (▢) icon next to the queue’s name.

![contentId-783942406](/cms_trial/assets/46adc35e-8cc4-425e-ad51-bf9954d0c266.png)

**See also:**

[The Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) 