# Send Reporter/Assignee name to Salesforce

## Purpose

We will discuss how to send the Reporter field from Jira to Salesforce without value mapping of Jira Id and Salesforce ID. For more information about Value mapping , please check this documentation, [Configuring Entity Mappings and Field Mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754325/Configuring+Entity+Mappings+and+Field+Mappings).

This came to be because value mapping of 100+ reporters(and Assignee) is not scalable.

This can be used for any Jira ID field like (Assignee). Or any field that is sent as an ID .

## Answer

### 1. Create a Jira Custom Field

First let's create a Text field (single line)

![contentId-3091924782](/cms_trial/assets/3caaf8fe-0cf3-4bea-b1a5-3e36f5324a52.png?version=1&modificationDate=1678858807789&cacheVersion=1&api=v2)

### 2. Salesforce Custom Field

Then create a custom field in Salesforce (Any text field will do). I will use the object "Case" as example.

- Click the **Cog** icon > **Setup** > **Object Manager** > on the **Quick find box** type "Case".
- Select **Field & Relationships**.
- Click **New** just beside the Quick find box.
- In the next windows, select the **Text** option and click **Next** on the top right.

  ![contentId-3091924782](/cms_trial/assets/a599f5be-2c5b-4f0b-a1e3-71b5787f1083.png?version=1&modificationDate=1678858807858&cacheVersion=1&api=v2)
- Name the new field (on this example I called it RichTextField2) and the length of the field (i selected 255 as example, it could be lower). Click **Next**.

![contentId-3091924782](/cms_trial/assets/3972274c-2c31-40e1-a7a5-3fa80e717a42.png?version=1&modificationDate=1678858807723&cacheVersion=1&api=v2)

- Then, Establish the Field-level security (for this, click the **Visible** box , which will select all the profiles). Click **Next**.
- Add the field to the Layout. By default, it will be added to all the Case layouts. Click **Save**.

### 3.- Binding

- Bind those two fields bidirectionally (this can be changed based on the use case). For that you need to go to **Apps** > **Salesforce** > **Bindings**.

More information about entity mapping can be in [Configuring Entity Mappings and Field Mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754325/Configuring+Entity+Mappings+and+Field+Mappings).

![contentId-3091924782](/cms_trial/assets/d6ab168f-268c-4ed1-acd2-5e8973a5dd2a.png?version=1&modificationDate=1678858807159&cacheVersion=1&api=v2)

### 4.- Automation Rule

Create an Automation Rule

![contentId-3091924782](/cms_trial/assets/41cfab1a-b3fe-4f0b-bb0a-882bbfbc3d74.png?version=1&modificationDate=1678858807579&cacheVersion=1&api=v2)

This rule is going to be executed every time the Reporter changes.

On the custom field we use the smart value - {{reporter.displayName}} - To translate the reporter ID to a name.

### 5.- How it looks

This is the Jira Reporter Field :

![contentId-3091924782](/cms_trial/assets/a1d4d813-af43-4d54-8390-ef72d5049940.png?version=1&modificationDate=1678858807302&cacheVersion=1&api=v2)

This is the Jira Custom Reporter field:

![contentId-3091924782](/cms_trial/assets/c7fa8eb5-66bf-4fee-b3ee-6e61b89478bd.png?version=1&modificationDate=1678858807370&cacheVersion=1&api=v2)

And the Salesforce text field will look like this:

![contentId-3091924782](/cms_trial/assets/8889ba71-cd8d-4d9a-878d-9ba9ab8324f8.png?version=1&modificationDate=1678858807438&cacheVersion=1&api=v2)

### 6.- Using the Assignee field instead of the Reporter field.

The same automation can be used with the Assignee field. Instead of using the **{{reporter.displayName}}** we use the **{{assignee.displayName}}.**