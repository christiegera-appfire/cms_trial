# Create a Jira work item from Salesforce

This page guides you on creating a Jira issue from a Salesforce record.

By creating a Jira issue from Salesforce, you can easily communicate with teams in Jira by bringing the same information from the Salesforce record to a Jira issue.

For example, when a Salesforce agent needs to escalate a case to the development team in Jira, they can create the Jira issue from inside the case and:

- Set the Jira issue priority to *High*, matching the Case's priority *High*.
- Set the Jira issue component to *UI*, matching the Case Reason *Installation*.
- Review the information being sent to Jira, before creating the Jira issue.

## Before you start

- Your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) and [entity and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) in Jira.
- Your administrator has configured [the Visualforce pages](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/) required for the Salesforce object.

## Create a Jira issue

1. In a Salesforce record, click **Create.**

   ![create jira.png](/cms_trial/assets/a513372b-d477-42bf-9ddb-ef599c63f5ce.png)

   The **Create Jira Issue** window appears.  

   [Unmapped macro: inline-media-image — no content to fall back on]

   - Select the desired **Jira Project** and **Issue Type.**  
     All field and value mappings set by your administrator will be used to create the Jira issue.
2. You can choose to toggle the following options:  
   (Some combinations are not possible and cannot be selected. Refer to the help provided under the *What Will Happen?* panel.)

   - **View Only** - Manual and automatic synchronization will be disabled
   - **Auto Pull** - Changes to the association Jira issue will be pulled automatically to this record
   - **Auto Push** - Changes to this record will be pushed automatically to associated Jira issues, given respective triggers are installed
3. You can also choose what to do after the Jira issue is created by choosing from the following options:  

   [Unmapped macro: inline-media-image — no content to fall back on]

   - **Do nothing**
   - **Pull from Jira**
4. When you are satisfied, click **Create**.  
   Alternatively, click **Review & Create** to review the fields and values to be sent to Jira.  

   [Unmapped macro: inline-media-image — no content to fall back on]

   ![create Jira issue.png](/cms_trial/assets/5e7f2863-ccb6-45ef-87ff-a48720f0e544.png)

   You can always add, edit, or delete the values if necessary. For more information, see [Notes on Supported Fields](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/).
5. Upon successful creation, Issue created successfully message will be shown.  

   [Unmapped macro: inline-media-image — no content to fall back on]

   [Unmapped macro: legacy-content — no content to fall back on]

## Notes on supported fields

The **Review & Create** dialog box will:

- Render fields that appear in the original *Create Issue* dialog in Jira, respective to the project and issue type selected.
- Show fields regardless mapped or not.
- Automatically populate the field value if it's part of the [value mapping](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) set by your administrator.
- Render fields of these types:

  - Text fields like Summary and Description
  - Priority
  - Components
  - Versions
  - Labels
  - Numbers
  - Select lists
  - Checkboxes
  - Radio buttons
  - Date
  - Date Time
- Render the following fields in the following order (after which, any other fields would be rendered in no specific order):

  - summary
  - description
  - priority
  - components
  - versions
  - fixVersions
  - labels
  - epic
  - sprint

## Related information

- [Configure an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)