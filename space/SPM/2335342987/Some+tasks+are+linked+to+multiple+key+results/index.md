# Some tasks are linked to multiple key results

## Problem

You enabled the [**Objective & key result**](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) [structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) and when you go to the Gantt or Scope module, you see the following warning message:

![warning-linked-issues-to-okr.png](/cms_trial/assets/b389e1d2-dfdf-47bf-9354-d4a223ff7f5b.png)

The warning tells you that you [linked a work item](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Link%20issues%20to%20Key%20Results&linkCreation=true&fromPageId=2335342987) to several different key results.

- In the OKR module, the same work item is displayed under every key result you linked it to.
- In the Gantt and Scope modules, the same work item can be displayed only once. For that reason, you will not see it under only one key result while the Objective & key result hierarchy is active.

## Solution

### Solution #1

If the linked work items support the [manual KR](/cms_trial/space/SPM/1918702967/Manual+KR/) (that is, they don’t impact the KR’s progress) and you keep them under KR only for visibility, consider unlinking the “duplicates.” So that a work item appears only once in the OKR hierarchy.

To do so, you need to [edit linked issues](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Edit%20issues%20linked%20to%20Key%20Result&linkCreation=true&fromPageId=2335342987) under every relevant KR.

### Solution #2

If the linked work items impact the progress of the [auto-KRs](/cms_trial/space/SPM/1918670238/Auto-KR/), then unlinking them is not the optimal solution. But even without the Objective & key result hierarchy you can have a good visibility into your OKRs and progress of the associated tasks:

1. De-activate the Objective & key result structure.
2. Activate another structure builder (and customize it if needed).
3. On the Gantt/Scope module, switch to the **Objectives and Key Results** column view (or add the **Objectives**, **Key Results**, and **Strategic Theme** columns individually).
4. Add the **OKR Type** column.

Your view will now display the following information in the respective OKR columns next to the work item that is linked to a key result:

- **Objectives**: The name of the key result’s Objective. Click the link to open the modal with the Objective details. If the work item is linked to multiple key results under different Objectives, click the number on the column to see the list of those Objectives.
- **Key Results**: The name of the key result the work item is linked to. Click the link to open the modal with the key result’s details. If the work item is linked to multiple key results, click the number on the column to see the list of those key results.
- **Strategic Theme**: The name of the key result’s strategic theme. Click the link to open the modal with the strategic theme’s details. If the work item is linked to multiple key results under different strategic themes, click the number on the column to see the list of those strategic themes.
- **OKR Type**: The key result type.

![Strategic themes, objectives, key results, and okr type columns with data in the Gantt module.](/cms_trial/assets/7ea18b0c-f3f9-4459-8a96-41b14243ff77.png)

Visit the [Track OKRs across modules](/cms_trial/space/SPM/1918835163/Track+OKRs+across+modules/) page to learn how you can further utilize the OKR columns in the Gantt and Scope modules.

## More information

- [Column view (Gantt and Scope modules)](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/)
- [Manage task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/)
- <https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Link%20issues%20to%20Key%20Results&linkCreation=true&fromPageId=2335342987>
- [OKR types](/cms_trial/space/SPM/1918635736/OKR+types/)