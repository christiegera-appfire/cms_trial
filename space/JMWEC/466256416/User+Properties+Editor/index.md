# User Properties Editor

The **User property editor** allows you to add, modify, or remove properties associated with any Jira user in your instance; a user property is a key-value pair that is stored in Jira. These properties can then be used in the [*Set field value from User Property*](https://appfire.atlassian.net/wiki/spaces/JMWE/pages/461931016) post-function. This post-function allows you to set another field’s value from the user properties of the current user.

The value of the user property should be provided as a *text* value. For more information about the value type expected by this post-function for different field types, see [Expected value for different field types](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).

To access the User Properties Editor:

1. Log in to your Jira Cloud instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **Apps**.
3. Click **User properties editor** under *JIRA MISC WORKFLOW EXTENSIONS*.

**Please note**: the properties accessible through the **User properties editor** are different from the User Properties that you can edit through Jira’s **User Management** section.

## Add a User Property

![JMWE for Jira Cloud user properties editor with property management interface](/cms_trial/assets/9c290350-c046-4f39-9b52-65db8e6c15bf.png)

To add a user property:

1. Open the **User properties editor** (Figure 1, right).
2. Click the **Select a user** pulldown menu to open search.
3. Search for a user, then select them from the list or results.
4. Enter the name of the property in the **Key** field.
5. Enter the value of the user property in the **Value** field.
6. Click **Add** to add the property for the selected user.
7. The new property will be added to the list of properties.

It is **highly recommended** that you only ever edit or delete user properties that have been set manually using the **User property editor**. Modifying or removing system properties can have unintended consequences.

## Edit a User Property

To edit an existing user property:

1. Open the **User properties editor** (Figure 1, above).
2. Click the **Select a user** pulldown menu to open search.
3. Search for a user, then select them from the list or results.
4. Hover over the value in either the **Key** or **Value** column and click the pencil icon [tts pencil icon] .
5. Update the value as needed, then click **Update**.

## Delete a User Property

To delete an existing user property:

1. Open the **User properties editor** (Figure 1, above).
2. Click the **Select a user** pulldown menu to open search.
3. Search for a user, then select them from the list or results.
4. To the right of the property, click **Delete**.
5. The property is removed.