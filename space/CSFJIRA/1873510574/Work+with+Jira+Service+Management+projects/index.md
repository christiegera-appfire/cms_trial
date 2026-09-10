# Work with Jira Service Management projects

Connector for Salesforce & Jira works with Jira Service Management out of the box.

However, due to a [known bug](https://ecosystem.atlassian.net/browse/JSDECO-14) in Jira Service Management, an extra permission configuration may be required to make it work. This bug most likely affects Jira Service Management projects created prior to August 2016.

If your instance is affected, see [Configuring Project Permissions for Project Role](/cms_trial/space/CSFJIRA/1596752326/Configuring+Project+Permissions+for+Project+Role+(atlassian-addons-project-access)/). The guide assumes that you have installed Connector for Salesforce & Jira.

## Support for JSM comments in cloud

With the latest release of Connector for Salesforce & Jira (Cloud), users can now control the visibility of JSM comments through Salesforce package settings.

![sfjc-comment.png](/cms_trial/assets/2d1f4376-1b0e-4c91-afc4-2d2dc0d06435.png)

## Limitations

Connector for Salesforce & Jira (Server) currently does not work with the Jira Service Management comment visibility setting.

However, Jira Issue comments can be viewed in Salesforce through a dedicated Visualforce panel and Chatter. For more details about this configuration, see [View Jira comments in Salesforce](/cms_trial/space/CSFJIRA/1962607212/View+Jira+comments+in+Salesforce/).

## Next steps

If you have not installed the Salesforce package, go to [Installing the Salesforce Package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).

Otherwise, view [Set up a connection to Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).