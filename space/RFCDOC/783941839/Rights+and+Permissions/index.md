# Rights and Permissions

Rich Filters for Jira Dashboards use the following permissions:

#### **Rich filter view permission**

The *rich filter view permission* allows users to browse the rich filter and see its configuration, use it in gadgets, and see the results it returns. This permission is granted to all users who can view the Jira filter on which the rich filter is based. In other words, *the view permission is inherited from the base Jira filter*.

Suppose you wish to share a rich filter with other users. In that case, you must either share the Jira filter (see the Jira documentation on [sharing a filter](https://support.atlassian.com/jira-core-cloud/docs/save-your-search-as-a-filter/)) or choose a different base filter (see the [Rich Filter General Configuration](/cms_trial/space/RFCDOC/783941695/Details+configuration/)).

#### **Rich filter edit permission**

The **Administrators** option on the rich filter's [*Details*](/cms_trial/space/RFCDOC/783941695/Details+configuration/) screen specifies its administrators. Only the administrators and Jira admins are allowed to change the rich filter's configuration, including editing its list of administrators. When a rich filter is created, the user who created it is automatically set as its administrator.

#### **Rich filter create permission**

The *rich filter create permission* allows users to create new rich filters (including the right to copy existing rich filters). This permission can be granted to all logged-in users or to specific Jira groups. Jira admins can manage this permission on the App Configuration page, which is available from Jira’s [*Apps*](https://support.atlassian.com/jira-cloud-administration/docs/integrate-apps) administration section.

#### **Gadget export permission**

The *gadget export permission* allows users to export results displayed by rich filter gadgets (this applies to all export types – PDF, Excel, CSV). This permission can be granted to *Anyone* or specific Jira groups. Jira admins can manage this permission on the [App Configuration](/cms_trial/space/RFCDOC/783943002/App+configuration/) page available from Jira’s [*Apps*](https://support.atlassian.com/jira-cloud-administration/docs/integrate-apps) administration section.

Authorized users can only export results they have access to, i.e., results they can see in dashboards. If *Anyone* is selected, this also applies to non-logged-in (anonymous) users, who can see and export only results based on public issues.