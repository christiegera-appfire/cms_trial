# Detailed feature comparison

The information on this page was last updated on July 8, 2026.

## Intro

The main parameters to consider for comparison are listed below.

## **On-prem - System Info**

![image-20251104-140923.png](/cms_trial/assets/dce4fadd-c93b-4fd5-b9bd-d8b408e78ac2.png)

## On-prem - Time to SLA installed (v 11.3)

![image-20251104-141307.png](/cms_trial/assets/51b2f5fe-e093-4acd-8990-865a67d37d17.png)

## On-prem - Atlassian Apps Installed

![image-20251104-141119.png](/cms_trial/assets/a0883a0d-da38-4d66-8a15-a44364819ea8.png)

## Cloud - Time to SLA installed (Before Forge remote conversion)

![image-20251106-181851.png](/cms_trial/assets/bf53d28f-6af7-4d46-a765-6f9f180df033.png)

The comparison table reflects the customer's view based on menu items. See the parity tables of Time to SLA features below for details.

## Main features

## SLAs

This is the home page for SLA admins to perform essential tasks, such as listing, creating, updating, and deleting SLA configurations.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| **List / Filter SLAs** |  | ✅ | ✅ | The SLAs page lists and filters existing SLA configurations, though it has no specific label or menu section in the UI. |
| Columns | ✅ | ✅ |  |
| Hide disabled SLAs | ✅ | ✅ |  |
| View SLA | ✅ | ✅ |  |
| Edit SLA | ✅ | ✅ | In Cloud, this appears in the overflow menu as three dots. |
| Notifications | ✅ | ✅ | In Cloud, this appears in the overflow menu as three dots. |
| Duplicate SLA | ✅ | ✅ | In Cloud, this appears in the overflow menu as three dots. |
| Delete SLA | ✅ | ✅ | In Cloud, this appears in the overflow menu as three dots. |
| **Import JSM SLAs** | ✅ | ❌ |  |
| **Add New SLA Definition** | ✅ | ✅ | We overhauled the entire UX/UI after a year to make Time to SLA user-friendly for existing customers, trial users, and novice SLA admins. |
| Create from **template** | ❌ | ✅ | [Time to SLA Cloud offer templates](https://appfire.atlassian.net/wiki/x/WYA6Ag) for the most commonly used scenarios: Time to resolution, Time to first response, and Time in "In Progress". |
| Create from **scratch** | ✅ | ✅ |  |
| SLA Name |  | ✅ | ✅ |  |
| Enable SLA |  | ✅ | ✅ | You can access it from the three dots menu on the SLA home page when selecting an existing SLA. |
| SLA Scope |  | ✅ | ✅ |  |
| Projects | ✅ | ✅ |  |
| Issues (JQL) | ✅ | ❌ | Although JQL is unavailable in the SLA scope, you can use it in the SLA Goal definition. Users can still use JQL whenever needed. |
| Workflow | ✅ | ❌ | This legacy feature has been removed.  You can achieve the same outcome by adding corresponding projects or work item types in the SLA definition. |
| Conditions |  | ✅ | ✅ |  |
| Grouped Conditions | ❌ | ✅ | Grouped conditions are used to enforce [All / Any of the following conditions](/cms_trial/space/TTSC/35456221/SLA+conditions/). |
| Start |  | ✅ | ✅ |  |
| Status is changed | ✅ | ✅ |  |
| Field value is changed | ✅ | ✅ |  |
| Comment is made | ✅ | ✅ |  |
| Date field is reached | ✅ | ✅ | Renamed as `Date field is met`. |
| Triggered by another SLA | ❌ | ✅ |  |
| End |  | ✅ | ✅ |  |
| Status is changed | ✅ | ✅ |  |
| Field value is changed | ✅ | ✅ |  |
| Comment is made | ✅ | ✅ |  |
| Date field is reached | ✅ | ✅ | Renamed as `Date field is met`. |
| Triggered by another SLA | ❌ | ✅ |  |
| Reset |  | ✅ | ✅ |  |
| Status is changed | ✅ | ✅ |  |
| Field value is changed | ✅ | ✅ |  |
| Comment is made | ✅ | ✅ |  |
| Date field is reached | ✅ | ✅ | Renamed as `Date field is met`. |
| Pause |  | ✅ | ✅ |  |
| Status is any of selected status(es)... | ✅ | ✅ |  |
| Field value satisfies a condition... | ✅ | ✅ | ⚠️ These clauses are not available on Cloud: Is not equal to any of the selected values and is not empty... |
| Triggered by another SLA | ❌ | ✅ |  |
| Goals |  | ✅ | ✅ |  |
| (Enable) All remaining issues | ✅ | ✅ |  |
| Add new SLA goal |  | ✅ | ✅ |  |
| Issues (JQL) | ✅ | ✅ |  |
| Priority | ✅ | ✅ |  |
| Issue Type | ❌ | ✅ |  |
| Request Type | ❌ | ✅ |  |
| Assignee | ❌ | ✅ |  |
| Issue Filter | ❌ | ✅ |  |
| Goal (type) |  | ✅ | ✅ |  |
| Negotiation Date | ✅ | ✅ |  |
| Dynamic Duration | ✅ | ✅ | On Cloud, [the same capability](https://appfire.atlassian.net/wiki/x/tIAiAg) exists with one difference: Cloud lacks a built-in duration custom field, so users select text-based custom fields to define dynamic duration goals. |
| Duration | ✅ | ✅ |  |
| Next Business Day | ✅ | ✅ |  |
| No Target | ✅ | ✅ |  |
| Goal (value) | ✅ | ✅ |  |
| Calendar |  | ✅ | ✅ |  |
| Add New Calendar | ❌ | ✅ |  |
| Select Calendar via Jira Issue | ❌ | ✅ |  |
| Choose existing calendars | ✅ | ✅ |  |
| Order | ✅ | ✅ | Users can rank their goals using chevrons, but there is no explicit label or menu. |
| Calculation Method | ✅ | ✅ |  |
| Critical Zone | ✅ | ✅ |  |
| Event Order | ❌ | ✅ |  |
| Linked Issue SLA |  | ❌ | ✅ |  |
| The "Push" Action | Share this SLA on linked issues | ❌ | ✅ | This option makes this issue’s SLA panel visible on linked issues. This is ideal for creating shared accountability, like making a 'Dev' team aware of the main 'Customer' SLA. |
| The "Pull" Action | Display linked issues' SLAs | ❌ | ✅ | This option displays all SLAs from linked issues *on this issue*. This is ideal for tracking dependencies, like monitoring all sub-tasks for an "Employee Onboarding" ticket. |
| Asynchronous Update | ✅ | ❌ | On Cloud, every update must be asynchronous by design, so no explicit configuration option is needed for this feature. |
| **Notifiers** | ✅ | ✅ |  |
| List Notifiers |  | ✅ | ✅ |  |
| Edit | ✅ | ✅ |  |
| Delete | ✅ | ✅ |  |
| Associate with goals | ✅ | ✅ |  |
| Add New SLA Notification |  | ✅ | ✅ |  |
| Enable Notifier | ✅ | ✅ |  |
| Trigger When SLA | ✅ | ✅ |  |
|  | is breached | ✅ | ✅ |  |
|  | will be breached in | ✅ | ✅ |  |
|  | has been breached for | ✅ | ✅ |  |
|  | has reached (% of SLA Goal) | ✅ | ✅ | Renamed as `has reached`. |
|  | is over | ✅ | ✅ |  |
| Repeat every | ✅ | ✅ |  |
| Enable working calendar | ✅ | ✅ |  |
| When triggered |  | ✅ | ✅ |  |
| Send an email |  | ✅ | ✅ |  |
| Default recipients |  | ✅ | ✅ |  |
| Assignee | ✅ | ✅ |  |
| Reporter | ✅ | ✅ |  |
| Project lead | ✅ | ❌ |  |
| Component lead(s) | ✅ | ❌ |  |
| Voters | ✅ | ✅ |  |
| Watchers | ✅ | ✅ |  |
| Custom recipients |  | ✅ | ✅ |  |
| Jira Users | ✅ | ✅ |  |
| Group | ✅ | ✅ |  |
| User Field | ✅ | ✅ |  |
| Group Field | ✅ | ✅ |  |
| Project Role | ✅ | ❌ |  |
| Email Address | ✅ | ❌ |  |
| Other Recipient Types |  | ✅ | ❌ |  |
| CC | ✅ | ❌ |  |
| BCC | ✅ | ❌ |  |
| Preview Email Content | ✅ | ❌ |  |
| Send a Slack message | ✅ | ✅ |  |
| Fire an event | ✅ | ✅ | Use `Trigger a Jira Automation Rule` to achieve this function. |
| Trigger a Jira Automation Rule | ❌ | ✅ |  |

## Calendars

This is the main function to allows users to set their business working hours. The working hours set in the calendar are used to calculate SLA durations.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| **List/Filter Calendars** |  | ✅ | ✅ |  |
| View | ✅ | ✅ |  |
| Edit | ✅ | ✅ |  |
| Delete | ✅ | ✅ |  |
| **Add New Calendar** |  | ✅ | ✅ | The calendar experience in Cloud has been redesigned to simplify configuring business hours, breaks, and holidays. |
| Name | ✅ | ✅ |  |
| Region | ✅ | ✅ | In Cloud, Region and Time Zone form a single UI component rather than two. |
| Time Zone | ✅ | ✅ |  |
| **Business Hours** |  | ✅ | ✅ |  |
| Working Day | ✅ | ✅ |  |
| Working Hours | ✅ | ✅ | Unlike the 24-hour shifts in DC, a maximum shift on Cloud runs from 00:00 to 23:59. |
| Length of Business Day |  | ✅ | ✅ | In Cloud, it has been moved to the **Advanced** section. |
| **Holidays** | ✅ | ✅ |  |
| Show Past | ✅ | ✅ | Cloud has a single `Show previous holidays` option instead of separate buttons for showing and hiding past holidays. |
| Hide Past | ✅ | ✅ |  |
| Add Holiday (+) |  | ✅ | ✅ |  |
| Name | ✅ | ✅ |  |
| Date | ✅ | ✅ |  |
| Recurring | ✅ | ✅ |  |
| Type | ✅ | ✅ |  |
| **Shared Holidays** | ✅ | ✅ |  |
| Show Past | ✅ | ✅ |  |
| Hide Past | ✅ | ✅ |  |
| Add Shared Holiday (+) |  | ✅ | ✅ |  |
| Name | ✅ | ✅ |  |
| Date | ✅ | ✅ |  |
| Recurring | ✅ | ✅ |  |
| Type | ✅ | ✅ |  |

## SLA fields

These are SLA-related custom fields to enrich the Jira work item view.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| TTS - Time to SLA | ✅ | ✅\* | \*This field (Time to SLA field on DC) is supported as the “[TTS - SLA Duration](/cms_trial/space/TTSC/2969239557/SLA+Duration+field/)” on Cloud, with only a few configuration differences.  Cloud users can also utilize the [Linked Issue SLA](https://appfire.atlassian.net/wiki/x/awAgAg) feature as a workaround if they currently use this custom field to configure Display SLAs of linked issues on DC. |
| TTS - Overdue Status | ✅ | ❌ |  |
| TTS - SLA Indicator | ✅ | ✅\* | \*As the field functionality differs, we recommend you check the [documentation](/cms_trial/space/TTSC/2878930952/SLA+Indicator+field/). |
| TTS - SLA Overview | ✅ | ❌ |  |
| TTS - Duration Field | ✅ | ✅\* | \*Users can define an SLA goal with a [dynamic duration using a text-only custom field.](https://appfire.atlassian.net/wiki/x/tIAiAg) |
| TTS - SLA Date | ✅ | ✅\* | \*As the field functionality differs, we recommend you check the [documentation](/cms_trial/space/TTSC/2879160326/SLA+Date+field/). |

## SLA panels

Color-coded panel for Jira work item view. s

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Auto refresh | ✅ | ✅ | The SLA Panel in the issue view refreshes automatically when significant events occur. For example, when the current user moves the issue to done status, the SLA Panel updates its status and color codes without needing to refresh the Jira work item. |
| Show in SLA panel | ✅ | ✅ | The SLA Panel appears under the “Settings” menu in Cloud, not as a separate item. |
| Duration Format | ✅ | ✅ |  |
| SLA Context | ✅ | ✅ |  |
| External issue changes | ✅ | ✅ |  |
| Hide Completed SLAs | ✅ | ✅ |  |
| Out of working hours | ✅ | ✅ |  |
| Not started SLAs | ✅ | ✅ |  |
| Panel Position (Display Options) | ✅ | ✅ | The Panel Position (Top/Bottom) option is unavailable on Cloud due to Atlassian’s framework limitations, so the SLA panel cannot be placed at the top in the issue view. |
| SLA Order | ✅ | ✅ |  |
| Hide Paused SLAs | ❌ | ✅ |  |

## Permissions

This is the main place to grant the SLA admin role to Jira users and to assign permissions granularly.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Define TTS Admins |  | ✅ | ❌ | - **Permissions** tab is represented in the **Settings** menu in Cloud rather than a separate menu item. - Although there is no explicit `TTS Admins` definition on Cloud, there is no functionality loss because users still grant permissions in the same manner. For example, assigning Calendars to certain groups or users. |
| Jira Admins | ✅ | ❌ |  |
| Groups | ✅ | ❌ |  |
| Users | ✅ | ❌ |  |
| Granular permission for each view, create, update, and delete operation | ✅ | ❌ |  |
| Calendar Configuration | ✅ | ✅ |  |
| SLA Configuration | ✅ | ✅ |  |
| Notifier Configuration | ✅ | ❌ | Cloud has no explicit permission for notifiers because notifications fall under SLA configurations. The `SLA Configuration` permission covers both. |
| SLA Fields/Panels | ✅ | ✅ |  |
| SLA Panel Customization | ✅ | ✅ |  |
| Custom Fields Configuration | ✅ | ❌ | This is because no custom fields are available on Cloud yet. |
| SLA Recalculation | ✅ | ✅ |  |
| Report | ✅ | ✅ |  |
| Import/Export | ✅ | ✅ |  |
| Issue View Menu SLA Actions | ✅ | ✅ |  |

## SLA report

This is main place to create reports and subscriptions for periodic delivery.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| **Export** |  | ✅ | ✅ |  |
| **Search** |  | ✅ | ✅ |  |
| Save filter as | ✅ | ✅ |  |
| Format | ✅ | ✅ |  |
| Issue Columns | ✅ | ✅ |  |
| Report Type |  | ✅ | ✅ |  |
| Executive | ❌ | ✅ |  |
| SLA Summary | ✅ | ✅ |  |
| SLA Detail | ✅ | ✅ |  |
| SLA Durations | ✅ | ✅ |  |
| SLA Status | ✅ | ✅ |  |
| Filter Type |  | ✅ | ✅ |  |
| Project | ✅ | ✅ |  |
| JQL | ✅ | ✅ |  |
| Issue Filters | ✅ | ✅ |  |
| SLAs | ✅ | ✅ |  |
| More |  | ✅ | ✅ |  |
| SLA Start Date | ✅ | ✅ |  |
| SLA Target Date | ✅ | ✅ |  |
| SLA End Date | ✅ | ✅ |  |
| SLA State | ✅ | ✅ |  |
| SLA Indicator | ✅ | ✅ |  |
| Remaining | ✅ | ✅ |  |
| Elapsed | ✅ | ✅ |  |
| Critical Zone | ✅ | ✅ |  |
| Is SLA Extended | ❌ | ✅ |  |
| Clear filters | ✅ | ✅ |  |
| **Generate** |  | ✅ | ✅ |  |
| Execute | ✅ | ✅ | This is the typical user behaviour when pressing the **Generate** button. |
| Schedule | ✅ | ✅ | Users can find this option in the menu accessed by clicking the chevron next to the **Generate** button. |
| Background | ✅ | ✅ | This appears in the menu when users click the chevron next to the **Generate** button. |

## SLA recalculation

This is for recalculating the SLA data when users need to refresh SLA metrics.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| JQL | ✅ | ✅ | On Cloud, each [recalculation](https://appfire.atlassian.net/wiki/x/oAUdAg) task handles up to 20,000 work items and 10 SLA configurations. |
| SLAs | ✅ | ✅ |  |
| Recalculation Concurrency | ✅ | ❌ | This is unavailable on Cloud because it lacks threading capabilities. By design, every operation works in a threaded way. |
| Exclude Finished SLAs | ✅ | ✅ |  |

## Integrity checker

This is for scanning the database for out-of-date SLA related information similar to the Jira one for admins.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Integrity Checker | ✅ | ❌ |  |
| SLA configuration | ✅ | ❌ |  |
| Issue SLA data | ✅ | ❌ |  |
| Redundant configuration | ✅ | ❌ |  |
| Scheduled Tasks | ✅ | ❌ |  |
| SLA function configuration | ✅ | ❌ |  |

## Settings

This is where users can change the settings of the Time to SLA app.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| General |  | ✅ | ✅ | In Cloud, the only setting in **General** is the timezone for the 24/7 calendar. |
| Time Format (Long/Short/Shorter) | ✅ | ❌ |  |
| Overview Tab JQL | ✅ | ❌ |  |
| SLA Panel JQL | ✅ | ❌ |  |
| TTS Menu JQL | ✅ | ❌ |  |
| SLA Status Labels |  | ✅ | ❌ |  |
| Localizable Indicator | ✅ | ❌ |  |
| Use i18n keys | ✅ | ❌ |  |
| Met | ✅ | ❌ |  |
| Progress | ✅ | ❌ |  |
| Exceeded | ✅ | ❌ |  |
| Inactive | ✅ | ❌ |  |
| Paused | ✅ | ❌ |  |
| Invalid | ✅ | ❌ |  |
| SLA Notifiers | ✅ | ✅ | Renamed as `SLA Notification Template`. |
| SLA Calculation Scope | ✅ | ✅ |  |
| Scheduled Tasks | ✅ | ❌ | No functionality is lost because it applies intrinsically to the backend SLA services. |
| Escalation Services | ✅ | ❌ | - The name can be misleading because the functionality schedules SLA recalculation. - Given the cost of Cloud operations, we recalculate only on demand, not on a schedule. |
| Cache | ✅ | ❌ | It does not apply on Cloud. |
| Advanced Configuration |  | ✅ | ✅ |  |
| Report Scope Limit | ✅ | ❌ | Cloud has an internal limitation. |
| JQL Rows Limit | ✅ | ❌ | Cloud has an internal limitation. |
| Gadget Issue Limit | ✅ | ❌ | Cloud has an internal limitation. |
| Recurring Notifier Limit | ✅ | ❌ | Cloud has an internal limitation. |
| Recalculation Concurrency | ✅ | ❌ | Not technically feasible on Cloud. |
| Asynchronous Calculation Thread Type | ✅ | ❌ | Not technically feasible on Cloud. |
| Asynchronous Calculation Thread Count | ✅ | ❌ | Not technically feasible on Cloud. |
| System-wide asynchronous SLA calculations | ✅ | ❌ | Not technically feasible on Cloud. |
| Support Tools | ✅ | ❌ | Not technically feasible on Cloud. |

## Import/Export

This is the traditional backup restore function for the existing instance.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Export | ✅ | ✅ |  |
| Import | ✅ | ✅ |  |
| Import JSM SLAs | ✅ | ❌ |  |

## License management

This is a legacy feature and not applicable on Cloud.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| License Information: Time to SLA (TTS) |  | ✅ | ❌ |  |
| License information issued by Atlassian Marketplace | ✅ | ❌ |  |
| License information issued by Appfire | ✅ | ❌ |  |

## Time to SLA preferences

**Brief Description:**

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Time to SLA preferences |  | ✅ | ❌ | This is a legacy design choice and should be under settings. |
| Preferences | ✅ | ❌ | Not feasible in the cloud |
| Mute SLA Notifications | ✅ | ✅ | It is available via Atlassian User Profile |

## Features in project settings

## Customer Portal SLAs

This is the place to add existing SLAs to customer portal.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Customer Portal SLAs | ✅ | ✅ | According to Atlassian’s new design language, projects are called “spaces”. This feature is available under Service space > **Settings** > **Apps** > **Time to SLA**. |
| Define For All Request Types | ✅ | ✅ |  |
| Selected Request Type | All SLAs | ✅ | ✅ |  |
| Some SLAs | ✅ | ✅ |  |
| No SLA | ✅ | ✅ |  |

## Features in workflow

## Conditions

Conditions are used to check to make sure the user should be able to perform a transition.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Conditions | ❌ | ❌ | No conditions available on both hosting types. |

## Validators

Validators are rules that check for specific criteria to be met after a user attempts a transition, preventing the issue from moving to a new status if the validation fails.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Validators | ❌ | ❌ | No validators available on both hosting types. |

## Post functions

Post functions are used to execute automated actions after the transition is performed.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| TTS - Release Re-index Queue of the Issue | ✅ | ❌ | Technically not feasible on Cloud. |
| TTS - Reset SLA | ✅ | ✅ |  |

## Features in dashboards

## Gadgets

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| SLA Status Pie Chart | ✅ | ❌ |  |
| TTS - Periodic Met vs Exceeded Issue | ✅ | ❌ |  |
| TTS - Periodic Met vs Exceeded SLA | ✅ | ✅ |  |
| TTS - SLA Durations | ✅ | ❌ |  |
| TTS - SLA Success/Fail Counts Chart | ✅ | ❌ |  |
| TTS - SLA Success/Fail Rates Chart | ✅ | ❌ |  |
| TTS - SLA Working Duration Analysis | ✅ | ❌ |  |
| TTS - SLA/Assignee Performance Gadget | ❌ | ✅ |  |

## Features in issue search

## JQL functions

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| State functions |  | ✅ | ❌ |  |
| - isNotStarted([Optional List of SLA IDs or/and Name(s)]) - isFinished([Optional List of SLA IDs or/and Name(s) ]) - isRunning([Optional List of SLA IDs or/and Name(s)]) - isPaused([Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Duration functions |  | ✅ | ❌ |  |
| - remainingDuration(Duration, [Optional List of SLA IDs or/and Name(s)]) - elapsedDuration(Duration, [Optional List of SLA IDs or/and Name(s)]) - breachDuration(Duration, [Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Date functions |  | ✅ | ❌ |  |
| - slaStartDate(Date or Duration or timeFunction, [Optional List of SLA IDs or/and Name(s)]) - slaTargetDate(Date or Duration or timeFunction, [Optional List of SLA IDs or/and Name(s)]) - slaEndDate(Date or Duration or timeFunction, [Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Percentage functions |  | ✅ | ❌ |  |
| - remainingPercentage(Percentage, [Optional List of SLA IDs or/and Name(s)]) - elapsedPercentage(Percent, [Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Breach functions |  | ✅ | ❌ |  |
| isBreached([Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Critical zone functions |  | ✅ | ❌ |  |
| isInCriticalZone([Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Business hours functions |  | ✅ | ❌ |  |
| isInBusinessHours([Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| Contains SLA function |  | ✅ | ❌ |  |
| containsSla([List of at least 1 SLA ID or/and Name(s)]) | ✅ | ❌ |  |
| Complex functions |  | ✅ | ❌ |  |
| - isMet([Optional List of SLA IDs or/and Name(s)]) - isAllMet([Optional List of SLA IDs or/and Name(s)]) - isNotBreachedAndNotFinished([Optional List of SLA IDs or/and Name(s)]) - isAllNotBreachedAndNotFinished([Optional List of SLA IDs or/and Name(s)]) | ✅ | ❌ |  |
| SLA definition queries |  | ✅ | ❌ |  |
| - slaFunction is EMPTY - slaFunction is not EMPTY | ✅ | ❌ |  |

## **Features in work item view**

## Work item actions

These are work item-specific SLA actions that can be accessed via Jira work item view.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| **Issue Actions** |  | ✅ | ✅ |  |
| SLA Report | ✅ | ❌ |  |
| Reset SLA | ✅ | ✅ |  |
| Undo Reset SLA | ✅ | ✅ |  |
| Where is My SLA? | ✅ | ✅ |  |
| Regenerate SLA Data | ✅ | ✅ |  |
| Mute SLA | ✅ | ✅ |  |
| **SLA History** | ✅ | ✅ |  |
| **SLA Overview** | ✅ | ❌ |  |
| **SLA Panel** |  | ✅ | ✅ |  |
| SLA Info ℹ️ | ✅ | ✅ | This is a shortcut menu to open SLA configuration details. |
| SLA Contract Extension | ❌ | ✅ | [This is a new feature](https://appfire.atlassian.net/wiki/x/LwNMdw) to handle exceptional cases and extend SLAs per issue. |

## Features in non-GUI access

## REST APIs

This allows programmatic access to SLA data.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Calendars | ✅ | ✅ |  |
| SLA Configurations | ✅ | ✅ |  |
| Custom Fields | ✅ | ✅ |  |
| Issue SLAs | ✅ | ✅ |  |
| Recalculation | ✅ | ✅ |  |
| Reports | ✅ | ✅ |  |
| Permissions | ✅ | ✅ |  |
| Notifiers | ✅ | ✅ |  |

## Integrations

## App integrations

This is for a better-together experience by integrating other apps.

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Better Excel Exporter | ✅ | ❌ |  |
| Configuration Manager for Jira | ✅ | ❌ |  |
| eazyBI | ✅ | ✅ |  |
| Theme Extension for JSM | ✅ | ❌ |  |
| PowerBI Connector for Jira | ✅ | ❌ |  |
| Automation for Jira | ✅ | ✅ | On Cloud, you can [trigger Jira automation rules via notifiers](https://appfire.atlassian.net/wiki/x/kgVEVw). |
| Dashboard Hub Pro (Charts, Reports, Time in Status for Jira) | ❌ | ✅ |  |