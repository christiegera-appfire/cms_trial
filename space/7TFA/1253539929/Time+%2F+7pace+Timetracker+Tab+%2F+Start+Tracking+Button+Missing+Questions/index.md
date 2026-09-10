# Time / 7pace Timetracker Tab / Start Tracking Button Missing Questions

## Question - How do I remove Timetracker from a work item?

How to completely remove Timetracker from a certain work item? (If the Timetracker tab is missing or you don’t see the button to track time, then implement the described procedure in reverse order)

### Answer - Adjust the item’s layout in Azure DevOps

This can be worked around by adjusting a layout of a given item type in Azure DevOps settings (Organization Settings -> Boards -> Process -> [Process name] -> [Item type name]). There, you can hide 7pace Timetracker controls on item level (1); or even the whole 7pace tab (2). Just consider the fact that removing 7pace tab (2) will also strip you of the beneficial insights available directly on an item, so I would recommend hiding the Timetracker section on Item detail (1) only.

![Time_Tracking_Button.png](/cms_trial/assets/1b4d9513-d729-40be-8603-e95a62c89301.png)

## Question - Where is my 7pace Timetracker tab after a Cloud migration?

We recently switched from 7pace Timetracker (on-prem) for DevOps Server to 7pace Timetracker (cloud) for DevOps Services. The "7pace Timetracker" tab (formerly the "Time" tab) is not showing up on the work item form; is there a way to fix that?

### Answer - Modify the WI XML template

Unfortunately, when you migrate from DevOps Server to DevOps Services, extensions are not inserted into the work item form template (it is marked as modified internally in DevOps Services). Therefore, you have to modify your WI xml templates in order to add 7pace Timetracker-specific fields like the "7pace Timetracker" tab and "Start Tracking" button on the work item form.   
  
The basic process is described here: <https://docs.microsoft.com/en-us/vsts/extend/develop/configure-workitemform-extensions?view=vsts>   
  
In this specific case, do the following:  
1. Navigate to "https://dev.azure.com/[youraccount]/\_admin/\_process".  
2. Locate the process template you want to modify, click on "..." button and Export it. This will produce a zip archive with a lot of folders and files inside.  
3. Open the "WorkItem Tracking\TypeDefinitions" folder. There, you should see a lot (10-20) of xml files of Work Item Types.  
4. Select the types you want to have "Time" and "Work" added to the work item form (or maybe all) and apply edits to each xml:  
    a. Add this into your <WebLayout> as the first element:

<Extensions>  
 <Extension Id="7pace.Timetracker"/>  
</Extensions>

   b. Add two (2) new groups to enable "Time" and "Work".   
       Work is located by default (but you can change the location as you wish) inside <Page> second <Section>, before closing </Section> add:

<GroupContribution Label="Work" Id="7pace.Timetracker.work-item-form-group" />

       Time is a "page", add it after </Page>:

<PageContribution Label="Time" Id="7pace.Timetracker.work-item-form-page" />

       Apply the same edits to all affected xmls.

5. Save and import Template. After that, "Time" and "Work" will reappear.

## Question (on-premise only) - Installation of DevOps 2019 failed with errors

I was installing 7pace Timetracker for DevOps 2019 and after the installation of work item form contributions, I received an error message that installation had finished, but with errors.

### Answer (on-premise only) - Are Boards disabled for your projects?

DevOps issues an error when Boards have been disabled for a project and you try to install work item form contributions.

Here is the error message you will see in the log if this is the case:

*[Error found in log] Message: VS403121: Extension(s) "7pace.TimetrackerOnPremises" does not exist or has no work item form contribution.*

If you see this error message in the log, please first check to see if Boards have been disabled for your projects.

![Time_Tracking_Button_On_Premise_Installation.png](/cms_trial/assets/f714705e-256c-4a27-808e-202349e9d69e.png)![Time_Tracking_Button_On_Premise_Installation_Details.png](/cms_trial/assets/42959076-02ff-43d4-8f9e-d038daf8905a.png)

The screenshot above shows the list of enabled features for projects, including Boards. If the error message in question displays after installation and you have Board *disabled* for projects, rest assured, your work item's form contributions have been installed correctly to your projects.

## Question (on-premise only) - Installation error: TFS237070

We were installing the on-premise version of 7pace Timetracker and after finally reaching the point where it begins adding the "Start Tracking" button and the "7pace Timetracker" tab (formerly the "Time" tab) to each work item dialog, an error occurred: "TF237070: Importing the definition failed. The definition you are trying to import did not validate against the schema. Edit the definition, then try to import it again."\*

Can you help us to resolve this issue?

*\*Please note that the error message, above, may or may not contain additional details such as:*  
- The element 'ALLOWEDVALUES' has incomplete content. List of possible elements expected: 'GLOBALLIST, LISTITEM'.  
- The element 'GROUPEDVALUES' has incomplete content. List of possible elements expected: 'GLOBALLIST, LISTITEM'.

### Answer (on-premise only) - Review work item template definitions

**Background**

*Note: This is for on-premise only.*

During the installation of 7pace Timetracker, we adjust your work item template by adding 7pace Timetracker-specific elements or contributions such as the "Start Tracking" button and the "7pace Timetracker" tab.

The only way for us to add these extra elements to your work item template is described in the Microsoft article found [here](https://docs.microsoft.com/en-us/azure/devops/extend/develop/configure-workitemform-extensions?view=vsts). So, unfortunately, there is no way for us to deviate from this process on our side.

DevOps Server behaves inconsistently in that it may work properly with these broken xml definitions day-to-day, however when 7pace Timetracker tries to import them during our installation process, they fail validation and we are unable to add our 7pace Timetracker contributions like "Start Tracking" and the "7pace Timetracker" tab.

**Fix/Workaround**

The only way to avoid receiving these errors during installation is to fix the broken work item template definitions on your end or to use 7pace Timetracker without its contributions (just click the "Cancel" button on the 7pace Timetracker installation error dialog and you can use it without them).

One example of an issue that could be causing broken work item templates might be:

An error caused by a self-closing tags such as:  
<SUGGESTEDVALUES some\_parameters />

The valid tag should be:  
<SUGGESTEDVALUES>some\_content\_here</SUGGESTEDVALUES>  
  
Please contact  Microsoft DevOps Server support; they may be able to provide you with a fix or workaround.

## Question (on-premise only) - Where is my 7pace Timetracker tab?

We have multiple project collections within the same project collection, and we have some work items that show the "Time"/"7pace Timetracker" tab and some that don't. Why is this and is there a way to resolve it?

### Answer (on-premise only) - Use the Timetracker Configuration Tool to reapply extensions

Starting with TFS 2018, we install the "Time"/"7pace Timetracker" tab and "Start Tracking" button into existing projects and collections during the installation of Timetracker or during an update. When a user creates a project after Timetracker installation, these Timetracker-specific add-ons are not configured for the new projects.

To fix this and update Work Item Extensions, like the Work Item "Time"/"7pace Timetracker" tab and "Start Tracking" button, please open the Timetracker Configuration Tool and reapply these extensions by clicking "Update Availability".

![Time_Tracking_Button_Config_Tool.png](/cms_trial/assets/63932840-dbb0-40be-af61-229efb7f7216.png)

## Question (on-premise only\_ - Missing “Time” tab on TFS Epics, Features, Stories, and Tasks

We have TFS 2017 update 1, and on-premise Timetracker for TFS, but we don't see the “Time” tab on TFS Epics, Features, Stories and Tasks. How do we enable the "Time" tab on the work item form? Answer (on-premise only)

### Answer - Known issue in TFS2017

This is a known issue in TFS 2017 - TFS has recently updated the work item dialog form, and users can choose to use the old or new form. Unfortunately, the "Time" tab won't work on the old work item form, which is why you don't see it. We currently have this in our backlog and will update you when we implement it.

To get the "Time" tab working on the new work item form, please see the instructions below on how to configure TFS to use this new form:

![Time_Tracking_Button_TFS_Dashboard.png](/cms_trial/assets/da95b3c0-94ae-4046-ad13-e62d570b20ac.png)