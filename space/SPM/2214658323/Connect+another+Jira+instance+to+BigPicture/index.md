# Connect another Jira instance to BigPicture

## Connect another Jira instance to BigPicture (old navigation)

Click to see the instructions

Connecting another instance allows BigPicture on your primary instance to integrate data from more than one Jira instance.

To use additional Jira Cloud instances, you need to:

- connect them to the app
- add them to the scope of your boxes

### Prerequisites

Before you add a connection, make sure that:

- You’re an administrator of the primary Jira Cloud instance.
- You have an account on the Jira Cloud instance you want to connect, with the **Administer** and **User Picker** permissions.

## **Steps required to add another Jira Cloud instance:**

1. Navigate to **App configuration** → **Integrations** → **Connections** within BigPicture on your primary Jira Cloud instance.

   ![Screenshot of the Connections tab in BigPicture Integrations.](/cms_trial/assets/87fb0a3a-88ca-434b-b0e3-7cdfd88d8832.png)
2. Click the **+ Add new connection** option.
3. Choose the **Jira Cloud** option.

   ![Screenshot of the Add new connection button in BigPicture Integrations.](/cms_trial/assets/f3bbcf2c-18b7-4fb9-a023-a07e00071e4b.png)

1. You can also initiate adding an instance in **box configuration** → **Tasks** → **Work items from Jira**:

   ![Screenshot of the Add new integration button in the box configuration.](/cms_trial/assets/06344810-b56b-4643-b109-091a457de45b.png)
2. You’ll be redirected to another page, where you’ll need to select the instance you want to connect to your primary instance.

   ![Screenshot of selecting an additional instance to connect with the primary instance in BigPicture.](/cms_trial/assets/4e0113fa-895c-4e21-8f87-070861a86def.png)
3. When selected, click **Accept**.
4. Once the connection is successful, you will see a message to configure the field mapping between your primary Jira Cloud instance and a connected Jira Cloud instance. Field mapping is not automatically created or copied, therefore you have to configure field mapping for each newly connected Jira instance. For more information, go to [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/).

   1. Click **Map fields** to start field mapping configuration now. You’ll be redirected to the **App configuration** → **General** → **Fields** page.
   2. Click **Start working** if you want to continue working without configuring field mapping now.

      ![Screenshot of the Field mapping configuration message that appears once the connection is set.](/cms_trial/assets/27ae95ff-027c-4fa2-a731-0a1ccd7bced8.png)
5. You can see your connected instance on the **Connections** page.

   ![Screenshot of the Connections page when another instance is connected.](/cms_trial/assets/53945680-cd4c-4d71-9b86-e0df4feb7a49.png)

## **Create the webhook on the secondary Jira Cloud instance**

To create the webhook connection on the secondary Jira Cloud instance, you’ll need a webhook URL provided by our Support team. Contact [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) to get the required URL before creating the webhook.

We’re working on enabling automatic webhook registration to eliminate this manual step in the future.

1. Return to the **secondary Jira Cloud** instance browser tab.
2. Navigate to **Jira settings** → **System** and then **WebHooks**.
3. Click to **Create a WebHook**.

   ![Screenshot of creating. anew Webhook in Jira.](/cms_trial/assets/2296c3d8-30b7-4234-874f-193e0cb3d6f6.png)
4. Name the webhook.
5. Ensure the webhook is **enabled**.

   ![Screenshot of providing Webhook details in Jira.](/cms_trial/assets/6797a565-bdbe-4133-95ef-e92ba931afba.png)
6. Paste the webhook URL provided by our [Support team](https://appfire.atlassian.net/servicedesk/customer/portal/11) into the URL field.
7. Select all the checkboxes for the events that should trigger the webhook.
8. The exception is **Exclude body**, which should be left **unchecked**.
9. To confirm, click **Create**.

## Connect another Jira instance to BigPicture (new navigation)

Click to see the instructions

Connecting another instance allows BigPicture on your primary instance to integrate data from more than one Jira instance.

To use additional Jira Cloud instances, you need to:

- connect them to the app
- add them to the scope of your boxes

### Prerequisites

Before you add a connection, make sure that:

- You’re an administrator of the primary Jira Cloud instance.
- You have an account on the Jira Cloud instance you want to connect, with the **Administer** and **User Picker** permissions.

## **Steps required to add another Jira Cloud instance:**

1. Navigate to **App configuration** → **Integrations** → **Connections** within BigPicture on your primary Jira Cloud instance.

   ![Screenshot of the Connections tab in BigPicture Integrations.](/cms_trial/assets/87fb0a3a-88ca-434b-b0e3-7cdfd88d8832.png)
2. Click the **+ Add new connection** option.
3. Choose the **Jira Cloud** option.

   ![Screenshot of the Add new connection button in BigPicture Integrations.](/cms_trial/assets/f3bbcf2c-18b7-4fb9-a023-a07e00071e4b.png)

1. You can also initiate adding an instance in **box configuration** → **Tasks** → **Work items from Jira**:

   ![Screenshot of the Add new integration button in the box configuration.](/cms_trial/assets/06344810-b56b-4643-b109-091a457de45b.png)
2. You’ll be redirected to another page, where you’ll need to select the instance you want to connect to your primary instance.

   ![Screenshot of selecting an additional instance to connect with the primary instance in BigPicture.](/cms_trial/assets/4e0113fa-895c-4e21-8f87-070861a86def.png)
3. When selected, click **Accept**.
4. Once the connection is successful, you will see a message to configure the field mapping between your primary Jira Cloud instance and a connected Jira Cloud instance. Field mapping is not automatically created or copied, therefore you have to configure field mapping for each newly connected Jira instance. For more information, go to [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/).

   1. Click **Map fields** to start field mapping configuration now. You’ll be redirected to the **App configuration** → **General** → **Fields** page.
   2. Click **Start working** if you want to continue working without configuring field mapping now.

      ![Screenshot of the Field mapping configuration message that appears once the connection is set.](/cms_trial/assets/27ae95ff-027c-4fa2-a731-0a1ccd7bced8.png)
5. You can see your connected instance on the **Connections** page.

   ![Screenshot of the Connections page when another instance is connected.](/cms_trial/assets/53945680-cd4c-4d71-9b86-e0df4feb7a49.png)

## **Create the webhook on the secondary Jira Cloud instance**

To create the webhook connection on the secondary Jira Cloud instance, you’ll need a webhook URL provided by our Support team. Contact [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) to get the required URL before creating the webhook.

We’re working on enabling automatic webhook registration to eliminate this manual step in the future.

1. Return to the **secondary Jira Cloud** instance browser tab.
2. Navigate to **Jira settings** → **System** and then **WebHooks**.
3. Click to **Create a WebHook**.

   ![Screenshot of creating. anew Webhook in Jira.](/cms_trial/assets/2296c3d8-30b7-4234-874f-193e0cb3d6f6.png)
4. Name the webhook.
5. Ensure the webhook is **enabled**.

   ![Screenshot of providing Webhook details in Jira.](/cms_trial/assets/6797a565-bdbe-4133-95ef-e92ba931afba.png)
6. Paste the webhook URL provided by our [Support team](https://appfire.atlassian.net/servicedesk/customer/portal/11) into the URL field.
7. Select all the checkboxes for the events that should trigger the webhook.
8. The exception is **Exclude body**, which should be left **unchecked**.
9. To confirm, click **Create**.