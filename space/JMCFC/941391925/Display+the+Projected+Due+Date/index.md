# Display the Projected Due Date

## Scenario

You require a field that displays the projected due date for an issue based on its priority; the due date is calculated using values within the script that add a number of days, skipping weekends (Saturday and Sunday), to the date the issue was created.

## Resolution

This solution uses the *Scripted Datetime*custom field type which uses the issue’s *Priority* value to automatically calculate a due date. It adds a specific number of days to the issue's Create Date value. The custom field is also configured to use the *Priority* value as a dependency - if that value is changed, the custom field will automatically be recalculated!

**Note**: the script included below uses hard-coded values to set the value of the custom field; based on the issue’s *Priority* value, the script adds a set number of days to the issue’s *Created* date. Depending on your workflow, the number of days added may be different and these values should be updated in the script provided below.

You are viewing the documentation for **Jira Cloud**.

| On This Page |
| --- |

## Steps to Create

### 1. Create a *Scripted datetime* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields**. In the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Scripted datetime** and click **Next**.
7. Select the screens to which the new custom field should be added. Click **Next**.
8. Configure the field (Figure 1, right):

   1. In the script editor, enter the following:

      ```javascript
      // Creates a Date object from a date string plus some number of days (exclude weekends)
      function date(from, nod) {
        let c1 = new Date(from);

        let weeks = Math.floor(nod / 5);
        let remDays = nod % 5;

        // Adding whole weeks
        c1.setDate(c1.getDate() + weeks * 7);

        // Run a loop and check each day to skip a weekend
        for (let i = 1; i <= remDays; i++) {
          c1.setDate(c1.getDate() + 1);
          while (c1.getDay() === 6 || c1.getDay() === 0) { // 6 is Saturday, 0 is Sunday
            c1.setDate(c1.getDate() + 1);
          }
        }

        // Skip ending weekend
        while (c1.getDay() === 6 || c1.getDay() === 0) {
          c1.setDate(c1.getDate() + 1);
        }

        // move to 0:00
        c1.setHours(0, 0, 0, 0);

        return c1;
      }

      // extract the created and priority fields from the issue
      const from = await api.issue.getField(issue, "created")
      const priorityObj = await api.issue.getField(issue, "priority")
      const priority = priorityObj?.name
      console.log('created on: ', from)
      console.log('priority: ', priority)
      // Add some number of days to the created date based on the priority
      switch (priority) {
        case "Highest":
        case "High":
          return date(from, 2);
        case "Medium":
          return date(from, 4);
        case "Low":
        case "Lowest":
        default:
          return date(from, 5);
      }
      ```
   2. In the **Dependencies on other fields** field, select **Sprint**.
9. Optionally, you can test the results of the script by entering an issue ID in the **Test with issue** field and clicking **Test**.
10. Click **Save**.

![Jira Misc Custom Fields (JMCF) Cloud projected due date field configuration](/cms_trial/assets/0a230649-c623-405b-b916-0ecca1b7a930.png)

### 2. Configure Custom Field Context (Optional)

When a custom field is created, it is added to the selected screens, but it is also added to *every issue type* and *every project*. If a custom field should only be added to specific issue types and/or projects, you need to edit the custom field context.

1. Open the custom field configuration:

   1. From the My Custom Fields page, click the **Contexts** link for the new custom field.
   2. Through the native Jira menus:

      1. In the upper right corner of the Jira window, click **Settings** ( ⚙️ ) and select **Issues**.
      2. In the left-hand panel, click **Custom fields**.
      3. Locate your new custom field in the list and click **Action** at the far right. Select **Contexts and default value**.
2. Update the context for your custom field as necessary:

   1. To add a new context, click **Add new context**.
   2. To update the existing context, click **Edit context** or **Edit Configuration**.
   3. For specific steps on modifying contexts, see this page: <https://support.atlassian.com/jira-cloud-administration/docs/edit-a-custom-field-context/>

![Jira Misc Custom Fields (JMCF) Cloud custom field context modification dialog](/cms_trial/assets/b75fa62f-ab07-42fa-b432-dcae29285357.png)