# Share view

## Share view (old navigation)

Click to expand the guide

With the **Share view** option, you can allow other users to see your current view of a module (for example, selected column views or layout mode).

The view can be shared by sending an automatically generated URL link.

The shareable link expires 360 days after its last use. If the link is frequently used and remains valid, there is no need to manually regenerate it every 360 days.

![Screenshot of the Share view feature in the Gantt module.](/cms_trial/assets/f385e2f4-8de5-4b28-a549-e0f2cf717cd3.png)

When a user opens a shared link, they will see a modal where they can decide whether they want to adjust their view based on the settings of the shared view or keep their view settings.

![Shared view settings modal.](/cms_trial/assets/29dd3766-8ac9-4032-93b8-6f916a7ec5fb.png)

Note that the security settings are always respected and not shared, which can affect the recipient’s shared view.

## Shareable data

When a user shares a view in the Gantt module or the Overview timeline, **the URL also includes the zoom level and viewport position.**

The person who opens the link and adjusts the view settings can see the same taskbars as the person who shared the URL (there can be slight differences due to different screen sizes and resolutions).

The **Share view** feature of the app lets you share selected features across different modules. The overview of the features is presented in the table below:

| **Module/ App location** | **Data shared** |
| --- | --- |
| [Gantt module](/cms_trial/space/SPM/1918797129/Gantt+module/) | 1. **Selected scenario (if made public)** 2. **Group tasks** 3. **View menu**     1. Show:        - Baselines       - Period warnings       - Progress       - Critical path       - Overdue    2. Task color:        - Manual       - Status 4. **Dependencies menu**     - Category:       - Strong      - Soft    - Display 5. **Resource panel menu**     1. Enabled/Disabled    2. Settings:        - Effort mode       - Aggregation 6. **Active column view** 7. **Active filters**     1. Quick Filters        - Active Quick Filters       - AND/OR operator    2. Date range filter    3. Query filter (TXT/JQL)    4. Show Basic tasks in results (ON/OFF)    5. Timeline:        - Scale       - Markers       - Time-boxes       - Week numbers 8. **Selected tasks** |
| [Scope module](/cms_trial/space/SPM/1918666763/Scope+module/) | 1. **View menu**     1. Layout    2. Detail View 2. **Active column view** 3. **Active filters**     1. Quick Filters:        - Active Quick Filters       - AND/OR operator    2. Query filter (TXT/JQL) 4. **Selected tasks** |
| [Board module](/cms_trial/space/SPM/1918796888/Board+module/) | - Query type - Query filters chosen - Visibility for tasks only with dependencies - Visibility for box children tasks - View id - Board layout type - Swimlanes collapsed - Swimlanes hidden - Objectives visibility - Task warning visibility - Totals settings - Report settings - Live sync - Links category type - Correction type - Display collapsed - Sort by - Zoom level - Level of display on the hierarchy (PI/ITER) - Collapsed/expanded swimlanes on the hierarchy |
| [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918504353) | - Swimlane values - Reports view - Sorting - Achievement settings - Heatmap settings - Zoom level |
| [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/) | - Effort mode - Unit - Team view - Skill panel - Views - workload, warnings - Period - Aggregations - Quick filters:    1. Active Quick filters   2. AND/OR operator |
| [Teams module](/cms_trial/space/SPM/1918829775/Teams+module/) | - View - show archived resources - Text filtering |
| [Risks module](/cms_trial/space/SPM/1918666681/Risks+module/) | 1. **View** **settings** a. Compact mode b. Heatmap mode c. Transpose the matrix d. Invert consequence matrix e. Invert probability axis f. Matrix or table viewing. Sorting by order 2. **Filters** a. Text query b. Operator query c. Filters chosen d. Date range: Start and End date |
| [Calendar module](/cms_trial/space/SPM/1918699000/Calendar+module/) | 1. **View menu**     1. Layout    2. Task color    3. End Date mode    4. Heat Map mode    5. Show assignee    6. First weekday 2. **Active filters**     1. Quick Filters:        - Active Quick filters       - AND/OR operator    2. Query filter (TXT/JQL) 3. **Selected month** 4. **Upcoming tasks bar** |
| [Priorities module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Priorities%20module%20%28NEW%29&linkCreation=true&fromPageId=1918504353) | unavailable |
| [Risk management module](/cms_trial/space/SPM/1918798201/Risk+management+module+(new+module)/) | unavailable |
| [Financials module](/cms_trial/space/SPM/1918633194/Financials+management/) | unavailable coming soon |
| [OKR module](/cms_trial/space/SPM/1918405440/Objectives+%26+Key+Results+(OKR+module)/) | The OKR module has a separate [share view](/cms_trial/space/SPM/1918408436/Share+view+(OKR+module)/) option. |
| [Strategic areas](/cms_trial/space/SPM/2325217590/Strategic+Areas/) | The shared view is provided as is. If it is filtered, the user is notified. An infobar sating List is limited by filters. To display all existing initiatives remove filters. |

## Limitations

- Share view is not available for:

  - **Priorities** module
  - **Risk management** module
  - **Financials** module
- The **OKR module** has a separate [share view](/cms_trial/space/SPM/1918408436/Share+view+(OKR+module)/) option.
- The URL to the **Gantt module** of a given box does not change when you apply a JQL search filter.
- **Strategic Areas**: Since the link recipient cannot see only some of the boxes in the **Initiative** tab, they need to be granted the [Box Viewer role](/cms_trial/space/SPM/1918829579/Permissions/) on the Home/root-level box. This way, they will have a full view of the shared Strategic Areas.

**Workaround:**

1. Enable the [WBS widget](/cms_trial/space/SPM/1918767142/WBS+widget/).
2. Use the **Show on Gantt** link.

   ![Screenshot of an issue page with the Show on Gantt button.](/cms_trial/assets/3958cf80-b954-4758-b9e0-0574c1dfba9b.png)
3. You are redirected to the Gantt view, where a given issue is highlighted.

   ![Screenshot of the Gantt module with a highlighted issue.](/cms_trial/assets/8fd41872-aa2a-4e89-8902-0f201d8c830f.png)

## Share view (new navigation)

Click to expand the guide

With the **Share view** option, you can allow other users to see your current view of a module (for example, selected column views or layout mode).

The view can be shared by sending an automatically generated URL link.

The shareable link expires 360 days after its last use. If the link is frequently used and remains valid, there is no need to manually regenerate it every 360 days.

![Screenshot of the Share view option in the Gantt module.](/cms_trial/assets/8370352c-a4a4-4a31-8f62-a31ca3cb7868.png)

When a user opens a shared link, they will see a modal where they can decide whether they want to adjust their view based on the settings of the shared view or keep their view settings.

![Shared view settings modal.](/cms_trial/assets/29dd3766-8ac9-4032-93b8-6f916a7ec5fb.png)

Note that the security settings are always respected and not shared, which can affect the recipient’s shared view.

## Shareable data

When a user shares a view in the Gantt module or the Overview timeline, **the URL also includes the zoom level and viewport position.**

The person who opens the link and adjusts the view settings can see the same taskbars as the person who shared the URL (there can be slight differences due to different screen sizes and resolutions).

The **Share view** feature of the app lets you share selected features across different modules. The overview of the features is presented in the table below:

| **Module/ App location** | **Data shared** |
| --- | --- |
| [Gantt module](/cms_trial/space/SPM/1918797129/Gantt+module/) | 1. **Selected scenario (if made public)** 2. **Group tasks** 3. **View menu**     1. Show:        - Baselines       - Parent task conflicts       - Progress       - Critical path       - Overdue tasks    2. Task color:        - Manual       - Status 4. **Dependencies menu**     - Category:       - Strong      - Soft    - Display 5. **Resource panel**     1. Enabled/Disabled    2. Settings:        - Effort mode       - Aggregation 6. **Active column view** 7. **Active filters**     1. Quick Filters        - Active Quick Filters       - AND/OR operator    2. Date range filter    3. Query filter (TXT/JQL)    4. Show BigPicture tasks in results (ON/OFF)    5. Timeline:        - Scale       - Markers       - Timeboxes       - Week numbers 8. **Selected tasks** |
| [Scope module](/cms_trial/space/SPM/1918666763/Scope+module/) | 1. **View menu**     1. Layout    2. Detail View 2. **Active column view** 3. **Active filters**     1. Quick Filters:        - Active Quick Filters       - AND/OR operator    2. Query filter (TXT/JQL) 4. **Selected tasks** |
| [Board module](/cms_trial/space/SPM/1918796888/Board+module/) | - Query type - Query filters chosen - Visibility for tasks only with dependencies - Visibility for box children tasks - View ID - Board layout type - Swimlanes collapsed - Swimlanes hidden - Objectives visibility - Task warning visibility - Aggregation settings - Report settings - Live sync - Links category type - Correction type - Display collapsed - Sort by - Zoom level - Level of display on the hierarchy (PI/ITER) - Collapsed/expanded swimlanes on the hierarchy |
| [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918504353) | - Swimlane values - Reports view - Sorting - Achievement settings - Heatmap settings - Zoom level |
| [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/) | - Effort mode - Unit - Team view - Skill panel - Views - workload, warnings - Period - Aggregations - Quick filters:    1. Active Quick filters   2. AND/OR operator |
| [Teams module](/cms_trial/space/SPM/1918829775/Teams+module/) | - View - show archived resources - Text filtering |
| [Risks module](/cms_trial/space/SPM/1918666681/Risks+module/) | 1. **View** **settings** a. Compact mode b. Heatmap mode c. Transpose the matrix d. Invert consequence matrix e. Invert probability axis f. Matrix or table viewing. Sorting by order 2. **Filters** a. Text query b. Operator query c. Filters chosen d. Date range: Start and End date |
| [Calendar module](/cms_trial/space/SPM/1918699000/Calendar+module/) | 1. **View menu**     1. Layout    2. Task color    3. End Date mode    4. Heat Map mode    5. Show assignee    6. First weekday 2. **Active filters**     1. Quick Filters:        - Active Quick filters       - AND/OR operator    2. Query filter (TXT/JQL) 3. **Selected month** 4. **Upcoming tasks bar** |
| [Priorities module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Priorities%20module%20%28NEW%29&linkCreation=true&fromPageId=1918504353) | Unavailable |
| [Risk management module](/cms_trial/space/SPM/1918798201/Risk+management+module+(new+module)/) | Unavailable |
| [Financials module](/cms_trial/space/SPM/1918633194/Financials+management/) | Unavailable coming soon |
| [OKR module](/cms_trial/space/SPM/1918405440/Objectives+%26+Key+Results+(OKR+module)/) | The OKR module has a separate [share view](/cms_trial/space/SPM/1918408436/Share+view+(OKR+module)/) option. |
| [Strategic areas](/cms_trial/space/SPM/2325217590/Strategic+Areas/) | The shared view is provided as is. If it is filtered, the user is notified. An infobar sating List is limited by filters. To display all existing initiatives remove filters. |

## Limitations

- Share view is not available for:

  - **Priorities** module
  - **Risk management** module
  - **Financials** module
- The **OKR module** has a separate [share view](/cms_trial/space/SPM/1918408436/Share+view+(OKR+module)/) option.
- The URL to the **Gantt module** of a given box does not change when you apply a JQL search filter.
- **Strategic Areas**: Since the link recipient cannot see only some of the boxes in the **Initiative** tab, they need to be granted the [Box Viewer role](/cms_trial/space/SPM/1918829579/Permissions/) on the Home/root-level box. This way, they will have a full view of the shared Strategic Areas.

**Workaround:**

1. Enable the [WBS widget](/cms_trial/space/SPM/1918767142/WBS+widget/).
2. Use the **Show on Gantt** link.

   ![Screenshot of the WBS on a work item page in Jira.](/cms_trial/assets/ca8062fe-4313-4a52-b8fc-e6993ca14a9a.png)
3. You are redirected to the Gantt view, where a given issue is highlighted.

   ![Screenshot of a Jira work item highlighted in the Gantt module.](/cms_trial/assets/fe5418e3-ae96-4788-a2d0-4d5a33906cc7.png)