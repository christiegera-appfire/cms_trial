# Default box type settings

The box type settings described on this page are the **default settings created during the installation**.

A Jira administrator can change the default box type settings. This means the setup of box types available to you can deviate from the information on this page. Confirm your setup with an admin.

## Box type settings

To check or edit box type settings:

1. Click the **wrench** icon.
2. Go to **Administration** > **Box types**.
3. Choose a box type from the list by clicking its name.

![Screenshot of the Box types page in Administration.](/cms_trial/assets/e4a1e399-4509-49d3-97b8-be4b2915fbf1.png)

Example box type settings view:

![Screenshot of the example box type settings page.](/cms_trial/assets/bda26bb8-ab6e-4911-9259-b99c0575b781.png)

## Default values

### Own scope box types

|  | **Agile Project (AGILE)** | **Classic Project (PROJ)** | **Hybrid Project (HYBR)** | **LeSS Requirement Area (REQAR)** | **Program (PROG)** | **SAFe ART (ART)** |
| --- | --- | --- | --- | --- | --- | --- |
| **General** |
| **Basics**   - **Parent types** | Main, Portfolio | Main, Portfolio | Main, Portfolio | Main | Main, Portfolio | Main |
| **Advanced**   - **Period mode** | Auto bottom-up | Auto bottom-up | Auto bottom-up | Auto bottom-up | Manual | Auto bottom-up |
| **Advanced**   - **Sequentiality** | Overlapping allowed | Overlapping allowed | Overlapping allowed | Overlapping allowed | Overlapping allowed | Overlapping allowed |
| **Modules**   - **Default** | Gantt | Gantt | Gantt | Gantt | Gantt | Gantt |
| **Modules**   - **Active** | Active:   - Overview - Gantt - Scope - Board - Objectives - Resources - Teams - Risk Management - Risks - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Resources - Teams - Risk Management - Risks - Calendar - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Objectives - Resources - Teams - Risk Management - Risks - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Board - Objectives - Teams - Risk Management - Risks - Reports - OKR - Priorites - Financials | Active:   - Overview - Gantt - Scope - Board - Objectives - Resources - Teams - Risk Management - Risks - Calendar - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Board - Objectives - Teams - Risks - Risk Management - Reports - OKR - Priorities - Financials |
| Inactive:   - Calendar | Inactive:   - Board - Objectives | Inactive:   - Board - Calendar | Inactive:   - Resources - Calendar | Inactive:   - n/a | Inactive:   - Resources - Calendar |
| **Tasks** |
| **Scope Definition**   - **Scope type** | Own scope | Own scope | Own scope | Own scope | Own Scope | Own scope |
| **Task Structure** | Agile | Agile - multiple projects | Agile | Agile | Agile - multiple projects | Agile |
| **Scheduling**   - **Task scheduling mode** | Auto bottom-up | Auto bottom-up | Auto bottom-up | Auto bottom-up | Auto bottom-up | Auto bottom-up |
| **Workload contouring**   - **Default contouring mode** | Flat | Flat | Flat | Flat | Flat | Flat |
| **Quick Filters**   - **Inheritence mode** | Own | Own | Own | Own | Own | Own |
| **Quick Filters**   - **Default Quick Filters** | Epics only  Scheduled to sprints  Not started tasks  In progress tasks  Resolved | My tasks  Epics only  Not started tasks  In progress tasks  Resolved | Epics only  Scheduled to sprints  Not started  In progress tasks  Resolved | Epics only  Scheduled to sprints  Not started tasks  In progress tasks  Resolved | My tasks  Epics only  Not started tasks  In progress tasks  Resolved | Epics only  Scheduled to sprints  Not started tasks  Resolved |
| **Task templates**   - **Inheritance mode** | Own | Own | Own | Own | Own | Own with inherited |
| **Resources** |
| **Basics**   - **Manually allocated teams** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Basics**   - **Configurable Story Point conversion ratio** | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |
| **Basics**   - **Auto-inherited upper-level teams** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Security** |
| **Basics**   - **Inheritence mode** | Own with inherited | Own with inherited | Own with inherited | Own with inherited | Own with inherited | Own with inherted |
| **Overview** |  |  |  |  |  |  |
| **Inheritance mode** | Own | Own | Own | Own | Own | Own |
| **Hierarchy Column Views** | Agile  Essentials  Time tacking | Time tracking  Essentials  Financial  Baseline | Time Tracking  Essentials  Financial  Baseline | Agile  Essentials  Time Tracking | Essentials  Financial  Time tracking  Agile | Agile  Time tracking |
| **Timeline Column Views** | Agile  Essentials  Time tacking | Time Tracking  Essentials  Financial  Baseline | Time tracking  Essentials  Financial  Baseline | Agile  Essentials  Time Tracking | Essentials  Financial  Time tracking  Agile | Agile  Essentials  Time tracking |
| **Gantt** |
| **Column Views**   - **Inheritance mode** | Own | Own | Own | Own | Own | Own |
| **Column Views**   - **Default Column Views** | Task scheduling  Essentials  Teams  Agile  Resources | Task scheduling  Essentials  Baseline  Time tracking  Resources | Task scheduling  Hybrid view  Time tracking  Teams  Resources | Task scheduling  LeSS  Essentials  Teams  Resources | Task scheduling  Agile  Essentials  Time tracking  Baseline  Teams  Resources | Task scheduling  SAFe view  Essentials  Teams  Resources |
| **Scope** |
| **Column Views**   - **Inheritance mode** | Own | Own | Own | Own | Own | Own |
| **Column Views**   - **Default Column Views** | Agile  Essentials  Teams | Essentials  Baseline  Time tracking | Hybrid view  Time Tracking  Teams | LeSS  Essentials  Teams | Agile  Essentials  Time Tracking  Baseline  Teams | SAFe view  Essentials  Teams |
| **Board** |
| **Card View**   - **Inheritance mode** | Own | N/A | N/A | Own | Own | Own |
| **Card View**   - **Default Card Views** | Essentials  Agile  Teams | N/A | N/A | Essentials  LeSS  Teams | Essentials  Agile  Teams | Essentials  SAFe  Teams |
| **Objectives** |
| **Basics**   - **Business value**    - **Business Value for Main Objectives can be set** | ✅ | N/A | ✅ | ✅ | ❌ | ✅ |
| **Basics**   - **Business Value for Team Objectives can be set** | ✅ | N/A | ✅ | ✅ | ❌ | ✅ |
| **Basics**   - **Associated work for objectives can be set** | ✅ | N/A | ✅ | ✅ | ✅ | ✅ |
| **Risks** |
| **Card Views**   - **Inheritance mode** | Own | Own | Own | Own | Own | Own |
| **Card Views**   - **Default Card Views** | Essentials  Details  Teams | Essentials  Details  Teams  Due Date | Essentials  Details  Teams | Essentials  Details  Teams | Essentials  Details  Teams | Essentials  Details  Teams |

### Sub-scope box types

|  | **Hybrid Stage (HSTAG)** | **Iteration (ITER)** | **Program Increment (PI)** | **Stage (STAGE)** |
| --- | --- | --- | --- | --- |
| **General** |
| **Basics**   - **Parent types** | Hybrid Project | Agile Project  Hybrid Stage  Less Requirement Area  Program  Program Increment | Program  SAFe ART | Classic Project  Program  Stage |
| **Advanced**   - **Period mode** | Auto top-down | Auto top-down | Auto top-down | Auto top-down |
| **Advanced**   - **Sequentiality** | Sequential | Sequential | Sequential | Sequential |
| **Modules**   - **Default** | Gantt | Scope | Scope | Gantt |
| **Modules**   - **Active** | Active:   - Overview - Gantt - Scope - Board - Objectives - Resources - Teams - Risk Management - Risks - Calendar - Reports - OKR - Priorities - Financials | Active:   - Gantt - Scope - Teams - Risk Management - Risks - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Board - Objectives - Resources - Teams - Risk Management - Risks - Calendar - Reports - OKR - Priorities - Financials | Active:   - Overview - Gantt - Scope - Resources - Teams - Risk Management - Risks - Calendar - Reports - OKR - Priorities - Financials |
| Inactive:   - n/a | Inactive:   - Overview - Board - Objectives - Resources - Teams - Calendar | Inactive:   - n/a | Inactive:   - Board - Objectives |
| **Tasks** |
| **Scope Definition**   - **Scope type** | Sub-scope | Sub-scope | Sub-scope | Sub-scope |
| **Task Structure** | N/A | N/A | N/A | N/A |
| **Scheduling**   - **Task scheduling mode** | N/A | N/A | N/A | N/A |
| **Workload contouring**   - **Default contouring mode** | N/A | N/A | N/A | N/A |
| **Quick Filters**   - **Inheritence mode** | Inherited only | Inherited only | Inherited only | Inherited only |
| **Quick Filters**   - **Default Quick Filters** | N/A | N/A | N/A | N/A |
| **Task templates**   - **Inheritance mode** | Own | Own with inherited | Own with inherited | Own with inherited |
| **Resources** |
| **Basics**   - **Manually allocated teams** | ❌ | ❌ | ❌ | ❌ |
| **Basics**   - **Configurable Story Point conversion ratio** | ❌ | ❌ | ❌ | ❌ |
| **Basics**   - **Auto-inherited upper-level teams** | ✅ | ✅ | ✅ | ✅ |
| **Security** |
| **Basics**   - **Inheritence mode** | Inherited only | Inherited only | Inherited only | Inherited only |
| **Overview**   - **Inheritance mode** | Own with inherited | N/A | Own | Own with inherited |
| - **Hierarchy Column Views** | Hybrid stage | N/A | Agile  Time tracking | Stage |
| - **Timeline Column Views** | Hybrid stage | N/A | Agile  Time tracking | Stage |
| **Gantt** |
| **Column Views**   - **Inheritance mode** | Inherited only | Inherited only | Own with inherited | Inherited only |
| **Column Views**   - **Default Column Views** | N/A | N/A | Sample view | N/A |
| **Scope** |
| - **Column Views**    - **Inheritance mode** | Inherited only | Inherited only | Own with inherited | Inherited only |
| - **Column Views**    - **Default Column Views** | N/A | N/A | system default | N/A |
| **Board** |
| **Card View**   - **Inheritance mode** | Inherited only | N/A | Own with inherited | N/A |
| **Card View**   - **Default Card Views** | N/A | N/A | system default | N/A |
| **Objectives** |
| **Basics**   - **Business value**    - **Business Value for Main Objectives can be set** | ❌ | N/A | ❌ | N/A |
| **Basics**   - **Business Value for Team Objectives can be set** | ❌ | N/A | ✅ | N/A |
| **Basics**   - **Associated work for objectives can be set** | ✅ | N/A | ✅ | N/A |
| **Risks** |
| **Card Views**   - **Inheritance mode** | Inherited only | Inherited only | Own with inherited | Inherited only |
| **Card Views**   - **Default Card Views** | N/A | N/A | system default | N/A |

### None scope box type

|  | **Portfolio (PORT)** |
| --- | --- |
| **General** |
| **Basics**   - **Parent types** | Main |
| **Advanced**   - **Period mode** | Auto bottom-up |
| **Advanced**   - **Sequentiality** | Overlapping allowed |
| **Modules**   - **Default** | Overview |
| **Modules**   - **Active** | Active:   - Overview - Gantt - Scope - Resources - Teams - Risk Management - Risks - Reports - OKR - Priorities - Financials |
| Inactive:   - Board - Objectives - Calendar |
| **Tasks** |
| **Scope Definition**   - **Scope type** | None |
| **Task Structure** | N/A |
| **Scheduling**   - **Task scheduling mode** | N/A |
| **Workload contouring**   - **Default contouring mode** | N/A |
| **Quick Filters**   - **Inheritance mode** | Own |
| **Quick Filters**   - **Default Quick Filters** | Epics only  Milestones only (with label)  Tasks in active sprint  My tasks  Not started tasks  In progress tasks  Resolved |
| **Task templates**   - **Inheritance mode** | Own |
| **Resources** |
| **Basics**   - **Manually allocated teams** | ✅ |
| **Basics**   - **Configurable Story Point conversion ratio** | ❌ |
| **Basics**   - **Auto-inherited upper-level teams** | ❌ |
| **Security** |
| - **Basics**    - **Inheritance mode** | Own with inherited |
| **Overview**   - **Inheritance mode** | Own |
| - **Hierarchy Column Views** | Essentials  Financial  Time tracking  Agile |
| - **Timeline Column Views** | Essentials  Financial  Time tracking  Baseline  Agile |
| **Gantt** |
| **Column Views**   - **Inheritance mode** | N/A |
| **Column Views**   - **Default Column Views** | Essentials Portfolio  Agile Portfolio  Classic Portfolio |
| **Scope** |
| **Column Views**   - **Inheritance mode** | N/A |
| **Column Views**   - **Default Column Views** | Essentials Portfolio  Agile Portfolio  Classic Portfolio  Baseline Portfolio  Time tracking Portfolio |
| **Board** |  |
| **Card View**   - **Inheritance mode** | N/A |
| **Card View**   - **Default Card Views** | N/A |
| **Objectives** |
| **Basics**   - **Business value**    - **Business Value for the Main Objectives can be set** | N/A |
| **Basics**   - **Business Value for Team Objectives can be set** | N/A |
| **Basics**   - **Associated work for objectives can be set** | N/A |
| **Risks** |
| **Card Views**   - **Inheritance mode** | Own |
| **Card Views**   - **Default Card Views** | Essentials  Details  Teams |