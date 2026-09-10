# JMWE Administration

JMWE provides a set of administrative tools, which you can access by following these steps:

1. Log in to your Jira Cloud instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **Apps**.
3. Locate *JIRA MISC WORKFLOW EXTENSIONS* in the left-hand panel.

## Administration pages

The following pages are available:

| Page Name | Description |
| --- | --- |
| Overview | This page provides an introduction to the app, lists the latest releases, and gives you pointers to the JMWE documentation and support. |
| [JMWE workflow extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) | Manage all JMWE-created extensions from a single page. |
| [Shared actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) | Create sequences of one or more workflow post-functions that can then be used in multiple workflow transitions (by using the [Shared Action](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/) post-function). |
| [Scheduled actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/) | Create sequences of one or more workflow post-functions that will be run according to a schedule against issues returned by a JQL search. |
| [Event-based actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/) | Create sequences of one or more workflow post-functions that are run when a change is made to an issue. These changes can include fields being modified, the issue being transitioned, a comment being added, and more. |
| [Use case templates](/cms_trial/space/JMWEC/2196245303/Use+case+templates/) | More than 30 pre-built configurations for JMWE Event-based actions, Scheduled actions, and workflow post functions that can be installed directly. |
| Custom Fields | View your custom fields created with [Jira Misc Custom Fields (JMCF)](https://appfire.atlassian.net/wiki/spaces/JMCFC). |
| Live Fields | View your configurations created with [Live Fields for Jira Cloud](https://appfire.atlassian.net/wiki/spaces/LF). |
| [Nunjucks](/cms_trial/space/JMWEC/465373737/Nunjucks+Template+Tester/) and [Jira expression](/cms_trial/space/JMWEC/466257352/Jira+Expression+Tester/) tester | Test Nunjucks and Jira expressions against existing Jira issues without directly editing a workflow transition. |
| [Shared Nunjucks templates](/cms_trial/space/JMWEC/465473979/Shared+Nunjucks+Templates/) | Manage shared Nunjucks templates (scripts) that can be imported into Nunjucks templates used in JMWE post-functions. This can be used to share macros between post-functions. This can also be used to create templates that are too long for use in post-function configurations. |
| [User properties editor](/cms_trial/space/JMWEC/466256416/User+Properties+Editor/) | Add, modify or remove properties associated with each Jira user. For use in conjunction with the [Set field value from User Entity Property value](/cms_trial/space/JMWEC/466257282/Set+field+value+from+User+Entity+Property+value/) post-function. |
| [Troubleshooting and support](/cms_trial/space/JMWEC/465241931/Troubleshooting+and+Support/) | This page helps you troubleshoot issues you encounter with JMWE. |
| [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/) | This page details the most recent events logged by the JMWE add-on for your Jira Cloud instance. |
| [JMWE Configuration](/cms_trial/space/JMWEC/466288938/JMWE+Configuration/) | In general, the JMWE app does not require global configurations; the post-functions it offers are configured directly within Jira's workflow editor. However, this page allows you to configure a few advanced settings. |

## The JMWE Menu

![JMWE for Jira Cloud administration menu with configuration and management options](/cms_trial/assets/1436eec9-f45d-4372-a935-ceb5c50163d5.png)

Most of the JMWE Administration pages include a header (Figure 1, right), which includes the name of the page, the JMWE logo, and the **JMWE Menu**. This menu includes page-specific links, including:

- **Help with this page** - Links to the help (on this site) for the Administration page.
- **Documentation** - Links to the documentation site for JMWE (this site).
- **Atlassian Community** - Links to the Atlassian community for JMWE Cloud.
- **Troubleshooting & Support** - Links to the JMWE [Troubleshooting and Support](/cms_trial/space/JMWEC/465241931/Troubleshooting+and+Support/) page for your instance.