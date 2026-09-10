# Foxly Permissions

If you want to restrict who can customize prioritization templates, prioritize issues, or access the *Prioritization* tab, you can use Foxly permissions settings.

One permission (Administer Foxly) is available on a global level, and two permissions (Edit Foxly and View Foxly) are available on the project level.

These permissions are available for company-managed (former Classic) and team-managed (former Next-gen) projects.

## Administer Foxly permission

Users with this permission are allowed to:

- Access the priority table and the priority matrix
- Access priorities issue glance panel
- Prioritize issues
- Customize prioritization templates (delete, update, and create)

To edit this permission, you need to be a Jira Administrator, and it is set up as a global permission.

[How to Add or remove Administer Foxly permission](/cms_trial/space/FOX/602538012/Foxly+Permissions/)

## Edit Foxly permission

The Edit Foxly permission is assigned on the project level to each project separately or multiple projects if you have multiple projects in your [permission scheme](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html).

Users with this permission can perform the following tasks in Foxly in the projects where this permission is granted:

- Access the priority table and the priority matrix
- Access priorities issue glance panel
- Prioritize issues

[How to Add or Remove permission in Classic projects](/cms_trial/space/FOX/602538012/Foxly+Permissions/)

[How to Add or Remove permission in Next-gen projects](/cms_trial/space/FOX/602538012/Foxly+Permissions/)

## View Foxly permission

The View Foxly permission is assigned on the project level to each project separately or multiple [projects](/cms_trial/space/FOX/602538012/Foxly+Permissions/) if you have multiple projects in your [permission scheme](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html).

Users with this permission can perform the following tasks in Foxly in the projects where this permission is granted:

- Access the priority table and the priority matrix
- Access priorities issue glance panel

A user with this permission cannot prioritize issues in the projects where this permission is granted.

[How to Add or Remove permission in Classic projects](/cms_trial/space/FOX/602538012/Foxly+Permissions/)

[How to Add or Remove permission in Next-gen projects](/cms_trial/space/FOX/602538012/Foxly+Permissions/)

## Jira Project Administration

As an addition to the Foxly permissions[,](/cms_trial/space/FOX/602538012/Foxly+Permissions/) if the user has Jira Project Administrator, they can do the following actions:

- [Disable/Enable Foxly Prioritization tab in the project settings](/cms_trial/space/FOX/602538374/Hide+Prioritization+tab+from+the+project+menu/)
- [Select and change prioritization template in the project](/cms_trial/space/FOX/602538305/Change+the+prioritization+template/)

## Permission matrix

|  | **Global - Administer Foxly** | **Project - Edit Foxly** | **Project - View Foxly** |
| --- | --- | --- | --- |
| Access the Foxly Priorities table | ✅ | ✅ | ✅ |
| Access the Foxly Priority matrix | ✅ | ✅ | ✅ |
| Access the Foxly Priority score in the issue glance panel | ✅ | ✅ | ✅ |
| Use filters | ✅ | ✅ | ✅ |
| Prioritize issues (edit metrics) | ✅ | ✅ | ❌ |
| Access *Customize* screen | ✅ | ❌ | ❌ |
| Edit existing template | ✅ | ❌ | ❌ |
| Create a new template | ✅ | ❌ | ❌ |
| Change the template in the project | ✅ | ❌ | ❌ |
| Delete template | ✅ | ❌ | ❌ |
| Create a Priority Planning Poker game | ✅ | ✅ | ❌ |