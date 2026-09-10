# Data security and availability

![TryItButton (2).png](/cms_trial/assets/d3929411-c589-4ff1-8312-c66ee3257da7.png)

Time added by users (called time entries or worklogs) is stored in the 7pace database. For proper integration, the app needs access to data from your Jira account.

## Data security

7pace Timetracker accesses data in your Jira account. This access is needed for use cases like item search, reading planning data (for example Story Points) from your tables, and understanding when items are renamed or moved. The access is **read-only**, we will not alter data in Jira.

Time entries created via 7pace Timetracker (also called worklogs) are always stored within 7pace. 7pace also stores some additional data from Jira to optimize reporting performance and allow future cross-platform reporting. We store the following information:

- Account: Account ID, Account name
- Users: User ID, User name, User e-mail, 'is admin' flag
- Items: Item ID, Item title, Parent item title (in case of subitems), Group, Board, Workspace.

- We store this information only for items you tracked time on; meaning the information is stored within time entries.

✅ All stored data is encrypted at rest.

**Your data is secure with us.**Check the [Appfire Trust Center](https://trust.appfire.com/) for full information about how we adhere to security standards like SOC 2, ISO 27001, and others.

Visibility of time added via 7pace Timetracker is based on the specific role assigned in the app. However, Jira permissions still apply. For example, if you're a 7pace Timetracker administrator and have access to all time tracking data but *not* to all Jira boards, the related information is hidden.

## Data removal

All data related to your account (time entries, users, related Jira information) is subject to [Appfire’s Privacy Policy](https://appfire.com/privacy-policy). If you need to remove data sooner than stated in the given policy, please contact us at [legal@appfire.com](mailto:legal@appfire.com).

## Permissions

7pace Timetracker integrates with Jira, combining its roles and permissions with those defined in Jira. This means that a user’s 7pace role is automatically assigned based on their corresponding Jira role, whether they are a user or an Administrator.

![jiramonday-permissionsgrid.png](/cms_trial/assets/b2380041-461c-4671-a2d7-4bc27edeecd0.png)

**Note**: Jira Administrator users are automatically assigned to the **7pace Admin** role. Jira Users can be automatically added to the **7pace Team** role using the toggle in Role Management. Only users with permissions to browse projects and edit their own worklogs will be granted this role automatically.

This permission setting can be customized in two ways: either by modifying the default association between 7pace and Jira roles or by adjusting roles for individual users. Find more detailed information in [Manage roles and permissions](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=7TFMS&title=Roles%20and%20Permissions&linkCreation=true&fromPageId=2020573385).

**7pace never shows info from private boards to unauthorized users.** For example, if User A records time on a private item, users who can see the time of others will see that User A recorded hours, but they will not see the related Jira item.