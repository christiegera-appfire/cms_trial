# Dependencies

Dependencies specify the relationships between tasks, milestones, and other items that can be presented on the timeline and displayed by the Gantt and Board type modules (Gantt and Board are the default module names used). By defining dependencies, you can automate task scheduling and highlight relations between tasks without impacting the schedule.

Note: the items presented on the Gantt chart are system-wide, and changing their dependencies might affect tasks in other Boxes or connected tools.

## Dependency types

Dependency type determines the direction of the dependency and also which of the tasks' dates are relevant. We call them "relevant", because certain changes to those dates might cause either rescheduling of the dependant tasks or can be even impossible to perform (the app will immediately revert their task to the previously calculated dates). Changes of the dates that are not "relevant" do not cause rescheduling of this dependency (but might still cause changes to its parent's or children's periods).

There are two basic types of dependencies:

- [**Strong dependencies**](/cms_trial/space/SPM/1918701700/Strong+dependencies/) → have a scheduling impact.
- [**Soft dependencies**](/cms_trial/space/SPM/1918506080/Soft+dependencies/) → serve a purely informational purpose and don't have any scheduling impact.
- External links → External links show dependencies between tasks within the scope of different boxes. Such a dependency might constrain, so the task period mode is set to "locked".

## Dependency configuration and link synchronization

You can configure link mapping on the App Configuration page. See [the Dependencies (global configuration)](/cms_trial/space/SPM/1918832470/Dependencies+(App+configuration)/) page for more information.

## Dependency details

![contentId-1918536086](/cms_trial/assets/b17a1e9b-da75-472a-868d-951dc3b3b2b9.png)

The following can be defined for a dependency:

|  | **Strong** | **Soft** |
| --- | --- | --- |
| Target task | YES | YES |
| Dependency type | YES  [Four types available](/cms_trial/space/SPM/1918701700/Strong+dependencies/) | YES  Soft dependencies don't have different types |
| [Lag time](/cms_trial/space/SPM/1918406747/Lag+time/) | YES | NO |
| [ASAP mode](/cms_trial/space/SPM/1918764948/ASAP+mode/) | YES | NO |
| Description | YES | YES |

## Display dependencies

Displaying of dependencies varies based on a module:

- [Gantt](/cms_trial/space/SPM/1918797129/Gantt+module/)
- [Board](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297667675)

## Dependency loops and cross-box relationship

See the [Dependency loops and cross-box relationship](/cms_trial/space/SPM/1918700470/Dependency+loops+and+cross-box+relationship/) article to learn more.