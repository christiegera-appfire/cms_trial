# Technical info

## Security and access

Only Jira administrators can access this page.

1. Click the **wrench** **icon** at the top right and select**Advanced** from the drop-down list. Next, go to the **Technical info** tab.

   ![image-20250325-113630.png](/cms_trial/assets/b68197a1-5e78-4699-83b4-c7f67aa45705.png)

## Technical info and troubleshooting

The features for checking and clearing the cache are available on the [Plugin cache](/cms_trial/space/SPM/1918635809/Plugin+cache/) page.

| **Feature** | **Description** |
| --- | --- |
| Show Integrity report | The integrity check is the process of comparing the current state of stored data and/or programs to a previously recorded state to detect any changes. |
| Fix integrity checker errors | Fix the identified integrity errors. The most common problem resolved by fixing integrity errors is the app reversing date fields mapped as start/end dates after they are cleared. |
| Allow JCMA migration | Keeping JCMA migration disabled prevents unintended overwriting of BigPicture data. |
| Download support zip | A zip file with logs used when contacting our Support. |
| Generate thread dumps | A log informing about the processes and threads currently running within the Java Virtual Machine. Used in solving support tickets, in particular, in diagnosing performance problems. You can download such logs directly from the Technical info section of the BigPicture Advanced configuration. |

## Onboarding tour

Turn the onboarding tour pop-ups on/off by toggling the switch.

![contentId-1918766683](/cms_trial/assets/c492617a-46d1-4564-83cf-2a1c5cac14ba.png)

## Hide onboarding entry pages

When you enable the **Hide onboarding entry pages** option, new users who enter BigPicture will skip the onboarding pages and go directly to the Overview module.

## Technical user

When the person responsible for a change cannot be put down as the person responsible, the selected technical user is listed as the user making changes to your tasks (instead of an anonymous user (Jira Server fallback user)).

For example, when a task change is committed from BigPicture to an integration instance (such as Jira) and the known user context fails due to insufficient user permissions, the same action is retried using the technical user (which typically has higher permissions).

- Changes made as a result of a scheduling cascade will be pushed out, even if the user doesn't have permissions for the tasks in cascade, as long as the user has the permissions for the first task that is moved
- Changes made as a result of administrative actions (eg. changing the sub-scope sync field) will be pushed out, even if the user doesn't have permissions for all the tasks
- Beyond these two cases, this change should not allow the user to commit any action that they weren't able to make before
- Changes, where the user had permissions to edit the task but lost them between the permission check and the actual commit, will be pushed out

#### **Jira Cloud**

When BigPicture is hosted on Jira Cloud, a technical user is created automatically and used by the app. The technical user defaults to the **anonymous** **user** and can't be changed.