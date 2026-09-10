# What happens to new and old associations when you remove the current bindings and mappings?

## **Use case**

Your organization wants to stop linking new Salesforce records to Jira projects, but you still need existing Jira issues to send updates back to Salesforce.

How do you maintain existing connections while preventing new ones?

**Without bindings/mappings, the connector cannot:**

- Push data to Salesforce
- Pull data from Jira
- Create new records
- Associate existing records

| **On this site:** |
| --- |

## Recommended solution: Project filtering

The best way to tackle this is project filtering in the Salesforce package configuration rather than removing bindings entirely. This method lets you control visibility and access without breaking existing integrations.

1. Filter specific projects from the Lightning component.   
   For detailed instructions, see [Filter Projects in the Create Jira Issue dialog box](/cms_trial/space/CSFJIRA/1873511284/Filter+projects+in+the+Create+Jira+Issue+dialog+box/).
2. Set your Jira issue to be not editable.

   - Add the **jira.issue.editable** property to the status (not the transition).
   - Set the **jira.issue.editable** property value to **false.**
3. Configure Salesforce.

   - Create a readonly record type.
   - Assign this record type to profiles when the record is closed (or in another end status)

## What happens if you remove the mappings

If you remove mappings and bindings, the Connector cannot push data, pull data, create records, or associate records for both new and existing connections.

If you choose to remove mappings and bindings instead of using project filtering, here's what you'll experience:

- The associations appear in Jira under the **Connector for Salesforce** association tab.
- The appear button shows the Salesforce information.
- The **Configure** button remains available (but you cannot change the configuration).
- The **Push** and **Pull** buttons are disabled.

  ![image-20250915-080855.png](/cms_trial/assets/1c42e3dd-2c5a-4e18-b64a-ef139b652ee6.png)

#### You cannot create a Salesforce object

If mappings or bindings are missing, you encounter the following error when trying to create new Salesforce objects. The system cannot establish the necessary connections without these configurations.

![image-20240812-195451.png](/cms_trial/assets/946ca38a-5db6-4021-8555-7863df410a6f.png)

#### You cannot associate

Without proper bindings, you cannot create new associations between Salesforce records and Jira work items.

![image-20240812-195532.png](/cms_trial/assets/67be5e91-fa97-4778-8df3-3e5809194d9a.png)

**If you try to push from Salesforce from an existing association**

Existing associations can’t push updates if you remove the underlying mappings and bindings.

![image-20240812-195206.png](/cms_trial/assets/c51590cc-83d6-4e64-9651-a208f40ebd75.png)

#### Configure button

The **Configure** button shows limited options. The system maintains the connection but restricts modification capabilities.

![image-20240812-200114.png](/cms_trial/assets/b15ff502-3928-4c6f-a992-ce41d59768bc.png)

## What happens if you remove the bindings:

- The **Push**, **Pull**, **Configure**, and **Details** buttons are greyed out for old associations.
- The **Create** and **Associate** buttons are not visible.

![image-20240812-195503.png](/cms_trial/assets/9b2550f8-7a7a-4469-a890-f72c04e699ab.png)