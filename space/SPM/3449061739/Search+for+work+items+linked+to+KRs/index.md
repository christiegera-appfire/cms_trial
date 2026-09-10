# Search for work items linked to KRs

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

If you want to find work items associated with your OKRs for bulk updates or analysis, you can use JQL (Jira Query Language) to search for work items connected to either a specific Key Result or to all KRs under a specific Objective.

Visit the [Link work items to Key Results](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) page to learn about linking Jira work items to Key Results.

## JQL search in Jira

To use JQL search to find linked work items (Jira work items) to specific OKRs:

1. Select **Search** in the top navigation (or press `/` on your keyboard). Alternatively, select **Filters** in the sidebar.
2. Select **View all work items** at the bottom of the dropdown.
3. On the **All work** page, select **JQL** (next to the search bar).

![Jira All Work page. The JQL button is highlighted.](/cms_trial/assets/2716e0a9-55ae-4bbc-90b4-f52872dc9693.png)

1. Enter your JQL query and press **Enter** to run it. Your search results will be displayed based on the criteria in your JQL query.

## JQL queries for searching linked work items

In the JQL input field, use the following queries to find work items connected to a Key Result or to all KRs under a specific Objective:

| **JQL query** | **Notes** |
| --- | --- |
| - `linkedToKRs("KR-1, KR-2")` | Search for Jira work items linked to the specified KR using the KR key.  e.g.: `work item in linkedToKRs("KR-1,KR-2")` |
| - `linkedToObjectives("O-1, O-2")` | Search for Jira work items linked to all KRs under a specified Objective using the Objective key. |
| - `kr="Key result name"` - `work item.property[okrs2].krNames = "KR Name"` | Search for Jira work items linked to the specified KR using the KR name. |
| - `objective="Objective name"` - `work item.property[okrs2].objectiveNames = "Objective Name"` | Search for Jira work items linked to all KRs under a specified Objective using the Objective name. |
| - `work item.property[okrs2].krIds = {id}` | Search for Jira work items linked to the specified KR using the KR ID. |

The `kr="Key result name"` and `objective="Objective name"` queries will soon be deprecated.