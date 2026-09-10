# SLA conditions

The SLA conditions feature lets you set up rules that trigger SLA events based on various criteria within a work item’s lifecycle. These conditions are designed to ensure that work items are addressed and resolved in accordance with customer expectations.

### Types of SLA conditions

There are four primary types of SLA conditions: **Start**, **End**, **Reset**, and **Pause**. Start, Stop, and Reset conditions are called "point conditions." They define a point within a work item’s lifetime, such as when the work item was assigned or when the status changed to Open. You can add more than one condition.

Start and End conditions are mandatory for every SLA, while Reset and Pause conditions are optional. The choice of using Reset and Pause conditions depends on your specific use case.

For each condition, you can either choose from common conditions, which are widely used conditions inspired by real-world scenarios, to save time, or if your condition doesn't fit any of them, you can explore all other condition types.

![Time to SLA SLA conditions page with start and stop conditions](/cms_trial/assets/8335c40e-0c27-4f59-9308-d2cc5efcfeb9.png)

#### **Start conditions**

Start conditions define the initiation of an SLA and can be triggered by events such as a change in work item status, modification of a field value, reaching a specified date in a date field, or the addition of a comment to a work item.

For example, to start an SLA when a work item’s status changes, follow these steps:

1. Go to **SLAs**, and click **+ SLA**.
2. After completing SLA Setup and SLA Goals, proceed to SLA Conditions.
3. Scroll to the *SLA Condition*, and click the **+** **Start Condition** button.
4. Click **+ More Condition Types**.
5. Select **Status is changed**.
6. Decide whether you want the condition to be triggered when the SLA enters or leaves a selected status (Open, Reopened, etc.).
7. Select a status or statuses that the SLA requires to start.

In Jira Cloud instances, there can be more than one status with the same name and different IDs appearing in the status dropdown menus due to Next-Gen projects creating their own workflows. To circumvent this issue, we have consolidated all statuses with the same name in our status menus. For example, if you want an SLA to start with the In Progress status, there will be one In Progress status in the dropdown menu, and selecting this would suffice.

1. Click **Confirm**, and the status will now appear in the box.

Check out the screenshots below to see some examples:

![Time to SLA SLA conditions start condition configuration](/cms_trial/assets/62c003cc-1d99-4fea-92da-80d1bfc02a31.png)

![Time to SLA SLA conditions pause condition configuration](/cms_trial/assets/c1845def-db2b-450f-a271-b7f7633a8d53.png)

#### **End conditions**

End conditions signify the completion of an SLA. It is mandatory to define at least one End condition for every SLA. The configuration steps mirror those of the Start conditions. Check out the screenshots below to see some examples:

The SLA End Date **is NOT a deadline**!It is just the date of a work item for the chosen date field.

![Time to SLA SLA conditions stop condition configuration](/cms_trial/assets/7d94110c-879f-4f1f-8cca-d7cf5255fe75.png)

![Time to SLA SLA conditions reset condition configuration](/cms_trial/assets/8a112f73-65d7-44ae-a22b-64061a77bfb0.png)

#### **Reset conditions**

The reset conditions feature lets you set criteria for restarting an SLA. This means that under specific circumstances, the SLA timer can be reset, and the counting process begins anew. It's important to note that the new SLA will only start counting from the beginning if the specified start condition is satisfied.

In simpler terms, the reset function lets you decide when an SLA should start over. Each SLA definition can have its own unique resetting options based on your preferences. If your chosen conditions change, the SLA is automatically reset. If the SLA is already in progress but hasn't concluded, triggering a reset action will restart it. During this reset, the start time is set to the current moment, and the elapsed duration is reset to zero.

You can reset an SLA based on different events, such as changes in status, field values, comments, or when a specific date is reached. For example, using the "Date field is reached" option lets you schedule when the reset should occur.

An alternative way to use the Reset SLA option is from the [Issue actions](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=ttsc&title=Using%20Time%20to%20SLA%20Issue%20Actions&linkCreation=true&fromPageId=35456221) dropdown menu, which enables you to perform work-item-specific actions.

You can also select whether you want a finished SLA to be reset. Your options for resetting finished SLAs are:

![Time to SLA SLA conditions warning condition configuration](/cms_trial/assets/ae3c4bdb-0d81-4c7e-93ae-a335fc598aac.png)

1. **Do nothing –** After your SLA finishes, it won’t be reset.
2. **Reset SLA durations and restart SLA –** After your SLA finishes, the elapsed time will be reset, and the SLA will start counting again.
3. **Reset SLA durations and invalidate previous cycles –** After your SLA finishes, the elapsed time will be reset and the SLA Panel will be hidden. The SLA won’t start counting again until the next SLA start condition is met.

It's crucial to note:

- A finished SLA is a closed contract, and a reset cannot change that.
- A finished contract might be reactivated from zero with a reset.
- A finished contract might be completely invalidated with a reset. Even in SLAs that are in the first cycle, the SLA can start from zero with a new START event.

The configuration steps are similar to those of the Start conditions. Check out the screenshots below to see some examples:

![Time to SLA SLA conditions list with grouped condition rules](/cms_trial/assets/10ef24b0-f123-440e-80bd-8bbf4140417c.png)

![Time to SLA SLA conditions condition editor with JQL rule](/cms_trial/assets/247c26c8-5a3c-45eb-bf89-157cd14b8455.png)

![Time to SLA SLA conditions rule details with calendar options](/cms_trial/assets/5ecf716b-f983-43bb-9655-0a5be2573804.png)

#### **Pause conditions**

Pause conditions introduce intervals during a work item’s lifecycle where the SLA countdown is temporarily halted. This is useful in situations where work is on hold; for example, when waiting for customer input or pending approvals.

Pause functionality is especially helpful for teams working across different time zones or under contracts that define SLA terms based on conditions outside of the team’s control. You can also configure the system to pause during company holidays or on specific days of the week.

In Time to SLA, you can configure SLAs to pause based on status, field values, or other SLAs. You can define pause conditions using the following options:

![Time to SLA SLA conditions pause condition example](/cms_trial/assets/3c2cdf28-b5ec-4bbe-bd90-7e3a3ca06a76.png)

1. **Status is any of the selected status(es) –** Choose from various statuses (e.g., To Do, In Progress, Done, etc.). When the SLA enters one of these specified statuses, the countdown halts, and it resumes only upon exiting that status.
2. **The field value satisfies a condition –** To pause the SLA based on a specific field value, set the desired field for the statuses where the SLA should be paused. Numerous field options are available for customization.
3. **Triggered by another SLA –** Use this feature to connect your SLA to another SLA. For example, you can configure the condition to have your SLA pause when the SLA it’s connected to pauses.

   ![Time to SLA SLA conditions condition list with calendar and status options](/cms_trial/assets/9d899951-24cc-40a3-8186-b240fe740970.png)

The SLA countdown **does not pause** if the SLA goal is set as a negotiation date.

Check out the screenshots below to see some examples:

![Time to SLA SLA conditions condition values panel](/cms_trial/assets/ef27d646-cff6-4670-8f93-0a3f4be6757b.png)

![Time to SLA SLA conditions condition editor with field values](/cms_trial/assets/d4cdb00a-60ea-4b24-9ec6-3bdc1136feff.png)

If multiple pause intervals are defined, all of them will be applied to the SLA simultaneously. For instance, if "assignee is EMPTY" and "team is EMPTY" are defined as pause conditions, the SLA will be paused when either the assignee is EMPTY, the team is EMPTY, or both are EMPTY.

You can see what a paused SLA looks like on the SLA Panel below:

![Time to SLA SLA conditions overview with status timeline](/cms_trial/assets/3212cae5-3c0b-4947-879f-cd9229f46cbd.png)

**How pauses affect SLA breaches**

Before the SLA is breached:

- The countdown stops when a pause condition is triggered.
- The time spent in the paused state is excluded from the SLA duration.
- The SLA target date is recalculated based on remaining time.

After the SLA is breached:

- The SLA remains marked as breached.

  - The target date is not recalculated.
  - The pause is still logged for visibility and auditing purposes, but has no effect on breach status or SLA metrics.
- This ensures that breached SLAs are treated consistently, and deadlines are not extended after a breach occurs.

### Logical connectors

Conditions can be connected using logical operators, with the default being the OR (“Any of the following conditions”) operator, meaning the SLA starts when any of the conditions are met. Alternatively, you can use the AND (“All of the following conditions”) operator. In this case, the SLA will start only when all conditions within a group are met.

#### **“OR” connector**

When you create a new condition by clicking the **Add** button, it uses the “OR” connector by default. If you add more conditions using the same method, a dropdown that lets you select between "Any of the following conditions" (OR) and "All of the following conditions" (AND) logics will appear.

![Time to SLA SLA conditions compact rule example](/cms_trial/assets/7957926a-2bc4-41ad-90d7-546e34bdca4a.png)

![Time to SLA SLA conditions compact start rule example](/cms_trial/assets/71b0f9ca-5778-47d8-97a7-4966b36ca4f8.png)

#### **“AND” connector**

For the “AND” connector to work, “All of the following conditions” needs to be selected.

![Time to SLA SLA conditions compact pause rule example](/cms_trial/assets/7bf6448e-a5fb-4ab6-b8f2-7dd91f06b97c.png)

![Time to SLA SLA conditions compact stop rule example](/cms_trial/assets/d7779073-c112-4577-a4d5-320607104d25.png)

![Time to SLA SLA conditions compact reset rule example](/cms_trial/assets/fbc306df-1b4a-4e70-b1dd-43be18556496.png)

Please note that Reset conditions connected with the "All of the following connections" connector **cannot have** different "Behavior on finished SLAs" selections. Otherwise, Time to SLA won’t be able to determine the appropriate response when SLAs are completed.

### Grouped conditions

Grouped Conditions allow you to construct intricate SLA use cases by organizing conditions into logical groups with specific connectors. This feature enhances the flexibility of your configurations, enabling you to address complex scenarios effectively.

To create a new group, navigate to the condition you want to include in the group and click the ellipsis ("**...**") button. From the options presented, choose **Create grouped condition**.

![Time to SLA SLA conditions compact warning rule example](/cms_trial/assets/c5db2b87-7ef7-4e2e-a8a5-6e810d098829.png)

![Time to SLA SLA conditions expanded rule with multiple fields](/cms_trial/assets/4ceb5b31-66c9-42e5-9f9c-b25d6b003129.png)

Upon creation, each group is evaluated independently with its own set of logical functions. You can create as many groups as needed for your specific use case; however, **ensure that your connectors make logical sense to avoid potential issues**.

#### Example 1:

![Time to SLA SLA conditions expanded rule with JQL and field criteria](/cms_trial/assets/ba37b2b4-16f2-4ef8-ad02-ac28df22bb01.png)

In this example, there are two groups under the Pause condition: Group A and Group B. Group A and Group B have the “AND” connector, but they are connected to each other with the “OR” connector.

This means that for this work item to be paused:

- The status needs to be “Waiting for customer” **AND** there must be a label containing “need-customer-response”.

**OR**

- The status needs to be “Waiting for approval” **AND** the Approver groups custom field must contain “jira-servicemanagement-users” or “jira-software-users”.

#### Example 2:

![Time to SLA SLA conditions expanded rule with multiple condition groups](/cms_trial/assets/cc44063f-0031-419b-8047-79574ea46743.png)

This example could be about when to start a **Time to First Response** SLA. In this example, the SLA will start if the priority is changed to Highest, High, Medium, Low, or Lowest, and either the assignee is set and the status is changed to “Open”, or the status is changed to “Work in progress” and the assignee is set.

Let’s represent the conditions mathematically:

- *P*: Priority is changed to Highest, High, Medium, Low, or Lowest.
- *A*: Assignee is set.
- *S*: Status is changed to “Open”.
- *W*: Status is changed to “Work in Progress”.

The SLA will start if:

*P*∧((*A*∧*S*)∨(*W*∧*A*))