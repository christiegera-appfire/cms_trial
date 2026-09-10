# Set Ticket Priority Based on Asset Attributes

## Scenario

When an ticket is opened in Jira Service Management, you want to set the Priority of the ticket based on the attached Asset’s attributes.

**Note**: This use case requires **Jira Service Management** and uses a custom **Asset** field. For more information on creating and configuring Assets in JSM, see [this page](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-the-assets-objects-field/).

## Resolution

This requires that a custom field for an **Asset** has been added to your project; it can have any name and can represent any type of Asset, but it must be an Asset object to successfully use the steps as outlined. By accessing the Asset’s attributes, you can update the ticket’s priority when the ticket’s Asset meets specific critera; for example, if you have a networking device Asset with a Priority attribute set to ‘Critical’, any tickets created that have that Asset attached can automatically be assigned the highest priority.

**Note**: the steps below use an example Asset object with an attribute of **Priority**. You will need to modify the included script for your specific JSM setup.

Additionally, the script uses Jira Cloud’s Asset API to access the attribute values because these values are not accessible using the [insightFieldValue](/cms_trial/space/JMWEC/465373638/Custom+filters/) custom Nunjucks filter. In order to access the attribute values through the Cloud API, you will need to provide your Atlassian username and an Access Token within the Nunjucks script.

## Steps to Create

### 1. Add the Assets object custom field

Verify that your Jira project has a custom Assets object field, and that that field has been added to all necessary screens. Additionally, you will need to verify that it has been fully configured per the Atlassian instructions. If that custom field does not exist, create one and add it wherever is necessary for your processes; see this page for more information: <https://support.atlassian.com/jira-service-management-cloud/docs/set-up-the-assets-object-field/> .

### 2. Add *Set issue fields* post-function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
   3. Select ***Set issue fields (JMWE app)*** from the list of post-functions and click **Add**.

**Note**: In this example, the ticket’s priority should be set when the ticket is created, so the **Create** Transition is selected. You should adjust this to your process needs.

![JMWE for Jira Cloud transition editing interface for assetbased priority setting](/cms_trial/assets/4570f909-715e-457e-a38d-bebcb82bdcc7.png)

### 3. Configure the post-function

Set the following configurations (Figure 2, right):

1. **Issue(s) to operate on** - Set **Target issue(s)** to *Current Issue*.
2. **Set fields**

   1. From the **Add field(s)** pulldown menu, select **Priority**. The Priority field will be added to the list of fields that will be updated by the post function.
   2. For the Priority field’s configurations, set the **Options** as needed.
   3. Also under the Priority field, use the following script for the **Value**:

      ```text
      {% set assetURL = issue | insightFieldValue( "customfield_xxxxx", true ) | first | field("links.self") %}
      {% set assetPriority = assetURL 
        | callRest(options = { "auth": 
          { "username": "your email address tied to your Atlassian account",
            "password": "your Atlassian API token value" 
          }
        })
        | field("attributes") 
        | filter({"objectTypeAttributeId":"the object attribute ID"}) 
        | field("objectAttributeValues") 
        | first 
        | field("value") 
      %}
      {% if assetPriority == "Critical" %}
      Highest
      {% else %}
      Medium
      {% endif %}
      ```
3. **Conditional execution** - Set as needed.
4. **Run As** - Set as needed; it is recommended to leave the default *Add-on user* value unless required for specific reasons.
5. **Delayed execution** - Set as needed.
6. Click **Add.**

## Nunjucks script for ‘Value’

The script for the **Value**, above, will depend on your instance configuration and includes several placeholder values that you will need to update:

- `customfield_xxxxx`: This should be the ID of the Asset custom field in JSM.
- `username`: The email address used to log in to your Atlassian account.
- `password`: The value of an Atlassian API token; you can generate a new token using the instructions at <https://id.atlassian.com/manage-profile/security/api-tokens>.
- `objectTypeAttributeId`: The Asset object’s attribute ID. You can view the ID of the Asset attribute by selecting your Asset object from the list under the **Assets** section of JSM, and browsing the Attributes section. In this example, the attribute is called **Priority**, so the Attribute ID for Priority would be used.

**Additionally**, the script uses the value of ‘Critical’ to determine whether the ticket should be assigned a Priority of **Highest** or **Medium** (default values for the Priority field). You should replace these values as necessary based on your JSM configuration.

![JMWE for Jira Cloud post function configuration for setting ticket priority](/cms_trial/assets/3d389007-fe81-4929-b6bc-c28c16720b07.png)

### You’re done!

Now, when a JSM ticket is created for an Asset that is considered mission critical (a value of **Critical** for the Asset attribute **Priority**), the ticket will automatically be assigned a Priority of **Highest**. If the asset is not Critical, the standard value of **Medium** is used.