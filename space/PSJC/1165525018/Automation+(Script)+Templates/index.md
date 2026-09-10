# Automation (Script) Templates

![Power Scripts for Jira Cloud automation templates icon](/cms_trial/assets/956be3df-cab8-4e27-920d-8af427d851bd.png)

## About

Script Templates are an easy way to add automated workflow actions instantly and without any coding. We have taken some of the most common types of scripts and converted them into an easy to use interface.

However, this does not mean scripting is not used. When creating the action using a template the script gets generated for you. We do this because we firmly believe that script is the most flexible, most powerful way to incorporate automation into your Jira system. We release that not everyone is comfortable scripting so we created the templates to guide users through the process.

![Power Scripts for Jira Cloud automation script templates listing](/cms_trial/assets/64f798b5-8afb-4a83-afd4-8490c908223e.png)

In the image above, you can see the script getting written in the SIL code preview panel as the user enters information into the input fields. We do this with the hope that after seeing real word applications of the scripts you will become more familiar with the way they are written and gain confidence in modifying and writing the scripts in the future.

The scripts, after being generated, are also automatically applied so that little to no experience to the administration of Jira is required. However, these templates are designed to be simple guides and continued reliance on them for Jira configuration could result in a less than optimal configuration. It is still advised that someone with more experience reviews the configuration changes after they are applied.

## Who are the templates for?

The Script Templates are for Jira administrators wishing to gain the ultimate power of script based automation but are confused or intimidated by the process. They are for admins or Product Owners who wish to gain the benefits of automation immediately without prior scripting knowledge or experience. They are for users who want to learn by doing instead of reading or watching videos.

Script templates are not for the thousands of existing SIL scripting ninjas already using Power Scripts or related apps. We have built some exiting new tools for them so they will be fine.

## Where can they be found?

The Script Templates can be found in multiple places.

### Jira Administration

Primarily they can be found on the “Find New Apps” or “Manage Apps” administrative pages in Jira.

![Power Scripts for Jira Cloud template editor with script configuration](/cms_trial/assets/5493dec1-8e8f-4a87-a7f9-da78ea00c0d5.png)

When using script templates from the Jira admin pages, all script types will be available for use

![Power Scripts for Jira Cloud automation template configuration panel](/cms_trial/assets/9149a3ba-5be8-4761-819f-83ec2148ec55.png)

### Workflows

Additionally, script templates can also be found in other areas like while editing the workflows. You must first add a SIL Condition, SIL Validator, or SIL Post Function to the workflow as seen below.

![Power Scripts for Jira Cloud script template selection interface](/cms_trial/assets/946a83e8-49d1-4596-8371-c65f23e7b8c7.png)

As seen below, when configuring the SIL Post Function the user can choose between adding a new template, writing a new script, or reusing an existing script.

![Power Scripts for Jira Cloud automation workflow configuration](/cms_trial/assets/947b7a61-c005-46eb-9f80-3add3edd304e.png)

However, it is important to note that the templates will be filtered based on the type of workflow action being configured. So, for example, when setting up a SIL Post Function, only action script templates will be available for use.

![Power Scripts for Jira Cloud template execution settings panel](/cms_trial/assets/e2871052-ad1c-45b9-8b6a-5e603ba18309.png)

## What happens when the template is applied?

When a template gets applied, the script that was seen in the preview window actually gets created in the system. The SIL Manager is the code editor for SIL scripts and holds the repository for all the scripts used by Power Scripts. Inside this repository you will find a folder called *generated\_templates*. Inside this folder will be subfolders that correspond to different script types and under those you will find that actual script that was generated.

![Power Scripts for Jira Cloud automation rule configuration interface](/cms_trial/assets/8a153ebc-7686-45dd-bfa1-effbbcb81a31.png)

Next, a configuration must be added so that Jira knows which script corresponds to specific events or actions. For example, for a listener script to run it must be associated with an internal event within Jira. In the example below we can see which scripts correspond to events like “Issue Closed” and “User Created”.

![Power Scripts for Jira Cloud template workflow settings dialog](/cms_trial/assets/f6c1d89c-e756-434c-8b8e-7563a7a52fc4.png)

Many configurations are found within the Power Scripts administration section of the Jira admin. However, this is not true for all of them. Some configurations, like actions, are added to the issues workflow. If not familiar with editing workflows this may not seem very straight forward so the configurations will get added to those workflows automatically.

Our hope is for you to then investigate the script and the configuration so you can see how these two things relate to each other and how they get configured. Our main goal is to guide you through setting up these configurations so that you can set them up without the assistance of the templates in the future.

## How to make changes existing template scripts?

As mentioned above, there are script files that get created when a template is applied. This means that changes to the applied template can be made directly in those scripts so that it can be customized to your specific needs. Changing the code within a script file does not affect the configuration. This changes can be made independently without updating the workflow or any other type of configuration.

**WARNING:** Changing the name of a script or moving its location to a different folder will impact existing configurations since the configuration will no longer be able to locate that file. If you wish to change the name or move the file location the configuration needs to updated.

## What type of templates are available?

## Action (Post-Function) Templates

[Excerpt "" from page "DRAFT\_Post-Function Templates" not found]

[See more…](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Action%20%28Action%29%20Templates&linkCreation=true&fromPageId=1165525018)

## Listener Templates

[Excerpt "" from page "DRAFT\_Listener Templates" not found]

[See more…](/cms_trial/space/PSJC/1165525361/Listener+Templates/)

## Recurrent (Scheduled) Job Templates

[Excerpt "" from page "DRAFT\_Recurrent (Scheduled) Job Templates" not found]

[See more…](/cms_trial/space/PSJC/1165525384/Recurrent+(Scheduled)+Job+Templates/)

## Live Fields Templates

[Excerpt "" from page "DRAFT\_Live Field Templates" not found]

[See more…](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/1165525417)

## Custom Field Templates

Custom fields template scripts are scripts that directly affect the value, appearance, configuration, or behavior of a custom field. With Power Scripts, there isn’t a concept of a custom field specific script/trigger, instead the scripts in this category are actually types like, workflow actions, listeners, and Live Fields scripts. These different script types accomplish the goal of updating and controlling the custom field types that are natively found in Jira. However, if you have advanced and complex problems that can’t be solved using standard Jira fields, [Power Custom Fields](https://marketplace.atlassian.com/apps/1210749/power-custom-fields-for-jira?hosting=datacenter&tab=overview) introduces new custom field types that are directly controlled by SIL scripts.

The templates will create the custom field script by adding the script to the configuration that corresponds to the individual script.

[See more…](/cms_trial/space/PSJC/1165525454/Scripted+Custom+Field+Templates/)

## Notification Templates

Notification template scripts are scripts that directly relate to communication and messaging through writing to files or sending notifications, like emails, directly.

The templates will create the notification script by adding the script to the configuration that corresponds to the individual script.

[See more…](/cms_trial/space/PSJC/1165525488/Notification+Templates/)

## User Templates

User template scripts are scripts that directly related to specific users in Jira. These are scripts that may set field values with specific users or control behaviors based on the specific user session using Jira.

The templates will create the user script by adding the script to the configuration that corresponds to the individual script.

[See more…](/cms_trial/space/PSJC/1165525512/JQL+Templates/)

## Will new templates be added?

Yes, from time to time new templates will be created and added to the list. The templates chosen for created will be determined by demand and specific templates can be requested for consideration through our support portal.

However, the goal of these templates is to provide you with an example of how to create a similar solution, not to necessarily take all of the work out of creating a new script and solve everyone's problems. Again, we firmly believe that scripting makes the most flexible and powerful solutions and which to guide you into becoming a SIL scripting ninja!