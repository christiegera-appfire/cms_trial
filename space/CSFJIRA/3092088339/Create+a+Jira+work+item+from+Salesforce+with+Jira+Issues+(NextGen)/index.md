# Create a Jira work item from Salesforce with Jira Issues (NextGen)

This page guides you on how to create a Jira work item from a Salesforce record.

By creating a Jira work item from Salesforce, you can easily communicate with teams in Jira by bringing the same information from the Salesforce record to a Jira work item.

For example, when a Salesforce agent needs to escalate a Case to the development team in Jira, they can create the Jira work item from inside the Case and:

- Set the Jira work item priority to *High*, matching the Case's priority *High*.
- Set the Jira work item component to *UI*, matching the Case Reason *Installation*.
- Review the information being sent to Jira, prior to creating the Jira work item.

## Before you start

- Your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) in Jira.
- Your administrator has [configured the Visualforce pages](/cms_trial/space/CSFJIRA/1873511459/Use+Jira+Issues+(NextGen)+with+Visualforce/) required for the Object.

## Create a Jira work item

1. In a Salesforce record, click **Associate/Create.**

   ![2026-01-16_09-52-17.png](/cms_trial/assets/e33fc791-bce2-431e-8ce5-18ad01aa2896.png)
2. The **Associate/Create Jira Issue** pop-up window appears.

   ![Associate or Create Jira Issue .png](/cms_trial/assets/2430ed4c-c55d-45e8-b463-9a8997723dd2.png)
3. Click **Create Jira Issue**and the **Create Jira Issue** pop-up window will appear.

   ![2026-01-16_09-54-12.png](/cms_trial/assets/ca561512-6617-47b2-937e-40783b2e994d.png)
4. Choose the desired **Jira Project** and **Issue Type**. All field and value mappings set by your administrator will be used to create the Jira work item.

   You can choose to toggle the following options:

   - **View Only** - Manual and automatic synchronization will be disabled
   - **Auto Pull** - Changes to the association Jira work item will be pulled automatically to this record
   - **Auto Push** - Changes to this record are pushed automatically to associated Jira work item, given respective triggers are installed

Some combinations are not possible and cannot be selected. Refer to the help provided under the *What Will Happen?* panel.

1. You can also choose what to do after the Jira issue is created by choosing from the following options:

   1. **Do nothing**
   2. **Pull from Jira**

      ![image-20250605-055954.png](/cms_trial/assets/ec53862b-9aeb-498c-a4a6-eebd3cc66eb1.png)

You can always add, edit, or delete the values if you need. See [Notes on Supported Fields](/cms_trial/space/CSFJIRA/3092088339/Create+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/) for more information.

Upon successful creation, an *Issue created successfully* message is shown.

### Tiles view

![2026-01-16_09-58-41.png](/cms_trial/assets/1607b4bd-0b21-4589-a34e-400c9ff3c970.png)

### Table view

![2026-01-16_09-59-11.png](/cms_trial/assets/f3d5bd84-6a73-4da3-87f9-5d27f6f50c8b.png)

## Notes on supported fields

The *Review & Create* window performs the following actions:

- It renders fields that appear in the original *Create Issue* dialog in Jira, respective to the project and issue type selected.
- Shows all fields regardless of whether they are mapped or not.
- Automatically populates the field value.

- Please note that if the populated value is not mapped and the default value is set to **Raise error,** you can still create a new issue in Jira. However, it won’t allow you to synchronize it with Connector for Salesforce and Jira.
- Value mappings and default values are set by your administrator. Ensure that the correct mappings are in place to prevent synchronization issues.

The following field types are rendered in the *Review & Create* window:

- Text fields like *Summary*

  - Rich text fields *like Description* (If enabled in [connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/), Jira multiline fields will use rich text fields; otherwise, plain text formatting will be applied.)
  - *Request type (only for JSM)*
  - *Priority*
  - *Components*
  - *Versions*
  - *Labels*
  - *Numbers*
  - *Select lists*
  - *Checkboxes*
  - *Radio buttons*
  - *Date*
  - *Date Time*
- The following fields are rendered in this order (after which, any other fields would be rendered in no specific order):

  - *summary*
  - *description*
  - *priority*
  - *components*
  - *versions*
  - *fixVersions*
  - *labels*
  - *epic name*
  - *sprint*

## Related information

- [Configure an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)
- [Automate your integration](/cms_trial/space/CSFJIRA/1874001954/Automate+your+integration/)
- [Associate a Jira Issue from Salesforce with Jira Issues](/cms_trial/space/CSFJIRA/3092284698/Associate+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/) (NextGen)