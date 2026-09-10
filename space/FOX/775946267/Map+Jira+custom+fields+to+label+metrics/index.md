# Map Jira custom fields to label metrics

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

![Jira admin Fields settings filtered by Foxly showing dynamic fields with locked labels](/cms_trial/assets/743e3943-0214-4e61-8408-90afb97dd28c.png)

### **Recommended action**

- Review your workflows, dashboards, and automations that use Foxly-created dynamic Jira fields, and update them to remove dependencies on these fields.

You can continue using:

- Priority score fields
- Your [own Jira custom fields](/cms_trial/space/FOX/846594061/Connect+custom+fields+to+Foxly/) in prioritization formulas

To keep using a label style you like in Foxly, you can map custom field values to match those labels.

## Map example

To map a Jira custom field called **shirt** (the type of this field is short text).

1. Click the *Priorities* **tab** > **Customize**.

   ![Screenshot of the Priority Matrix showing the Customize button.](/cms_trial/assets/626b388c-86ce-47f1-b21e-c3e4db023ae9.png)
2. The settings of the prioritization template appear. In this example, the *Quick Wins*template is used. Click the **Effort label** and select **Store values in custom field**.

   ![Screenshot of the Effort label with example label names and values.](/cms_trial/assets/5eded27d-d590-4abd-bfec-ba141a57dd7c.png)
3. Click **Save Changes**.
4. Click **Project settings** > **Automation**.
5. Click **Create a rule**.The *Field value changed*section appears.

   ![Screenshot of the Automation window showing the Field value changed section.](/cms_trial/assets/ec4f9a65-2223-4266-8d22-4ebf3ab7c03f.png)
6. Search and select the custom field **Shirt***,* then click **Save**.
7. Click **Add component** and select **New branch** > **Branch rule**.  
   ℹ️ With the Branch rule, you can only update a Foxly metric label when it matches the right condition.
8. To assign the XS label to the metric label in Foxly, use the JQL condition:

   ```text
   "shirt[Short text]" ~ "XS"
   ```
9. Set an action to update the label field in Foxly:

   ```text
   {
   "fields":
   {
   "customfield_10127" : 1
   }
   }
   ```

   ℹ️ Since the metric in Foxly is a custom field, you must add a **custom field ID** in the *Additional fields* section.In this example, the label is **Effort - Quick Wins**.To learn more about finding custom field IDs, see [Get custom field IDs for Jira and Jira Service Management](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html).
10. The JSON must be written with the **custom field ID**andthe **value ID**. In this example, **Effort** is the metric, **Quick Wins** is the template, and the value ID is **1**.

    ![Screenshot of the Score formula field and the Effort label. ](/cms_trial/assets/9401a501-fb45-430d-99ac-5aa7aee5f7dd.png)
11. Create a Branch rule for each **Effort** value metric and change JQL conditions accordingly:

    ![Screenshot of the Automation page with an example of creating a Branch rule.](/cms_trial/assets/88cdb745-1381-41e1-a599-6643e7c82bee.png)