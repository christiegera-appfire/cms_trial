# OKRs as task structure builders

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## OKRs as task structure builders (old navigation)

Click to expand the guide

If in your box you have:

- OKRs with Jira work items linked to their respective KRs
- or, only OKRs with no Jira work items linked to their respective KRs,

then, BigPicture can automatically build the task hierarchy based on the relationships between the Strategic themes/Objectives, Key Results, and the work items linked to them (if present). This can be done by activating the Objective & Key Result [task structure builder](/cms_trial/space/SPM/1918832018/Task+structure/).

## Activate Objective & Key Result task structure

Operations on task structure builders require a Jira/App Admin role. Changing a structure builder in a box will change a task hierarchy.

Task structure builders can be configured on the box configuration page.

The **Objective & Key Result** builder is available as a built-in template on the **Task structure** page. Click the template tile to select it.

Under the **Advanced Configuration** tab, you can see that your task tree will be built according to the following hierarchy:

Objective and Key Result (Strategic Theme > Objective > Key Result) > Epic > Sub-tasks.

![OKR-structure-builder.png](/cms_trial/assets/72dd770b-d837-4c08-9b54-fd8e3fc91f1b.png)

If your Objectives or sub-objectives have other Objectives as their parent(s), this relationship will also be reflected on the task tree in the Gantt module.

![task-tree-by-okr-structure-builder.png](/cms_trial/assets/742f55f8-f3c4-450a-828a-99322d6fd156.png)

When you activate the **Objectives & Key Results** structure builder, the app will pull the Objectives and Key Results data from the respective fields in the OKR module. See the [OKR fields vs Jira fields page](/cms_trial/space/SPM/1918765790/OKR+fields+vs+BigPicture+fields/) for more information.

## Limitations

Currently, the **Objective & Key Result** structure builder on Gantt only works with [work items linked](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) to a single Key Result.

- If multiple work items are assigned to a Key Result, the task structure and aggregations will be incorrect.
- If a work item is linked to multiple Key Results, it will be displayed only once on the Gantt chart.

This limitation does not prevent you from linking more than one work item to a Key Result in the OKR module.

- The OKR structure builder is not available in the non-scope boxes.
- [Linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) are not displayed anywhere on Gantt.

## OKRs as task structure builders (new navigation)

Click to expand the guide

If in your box you have:

- OKRs with Jira work items linked to their respective KRs
- or, only OKRs with no Jira work items linked to their respective KRs,

then, BigPicture can automatically build the task hierarchy based on the relationships between the Strategic themes/Objectives, Key Results, and the work items linked to them (if present). This can be done by activating the Objective & Key Result [task structure builder](/cms_trial/space/SPM/1918832018/Task+structure/).

## Activate Objective & Key Result task structure

Operations on task structure builders require a Jira/App Admin role. Changing a structure builder in a box will change a task hierarchy.

Task structure builders can be configured on the box configuration page.

The **Objective & Key Result** builder is available as a built-in template on the **Task structure** page. Click the template tile to select it.

Under the **Advanced Configuration** tab, you can see that your task tree will be built according to the following hierarchy:

Objective and Key Result (Strategic Theme > Objective > Key Result) > Epic > Sub-tasks.

![Screenshot of the Objective and Key Result task structure in the box configuration.](/cms_trial/assets/03c2d392-5ce6-4c64-be68-9f24bc6b3c37.png)

If your Objectives or sub-objectives have other Objectives as their parent(s), this relationship will also be reflected on the task tree in the Gantt module.

![Screenshot of the Objectives and Key Results column view in the Gantt module.](/cms_trial/assets/977ae447-9c4e-4204-986c-b0d9b5c9cca8.png)

When you activate the **Objectives & Key Results** structure builder, the app will pull the Objectives and Key Results data from the respective fields in the OKR module. See the [OKR fields vs Jira fields page](/cms_trial/space/SPM/1918765790/OKR+fields+vs+BigPicture+fields/) for more information.

## Limitations

Currently, the **Objective & Key Result** structure builder on Gantt only works with [work items linked](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) to a single Key Result.

- If multiple work items are assigned to a Key Result, the task structure and aggregations will be incorrect.
- If a work item is linked to multiple Key Results, it will be displayed only once on the Gantt chart.

This limitation does not prevent you from linking more than one work item to a Key Result in the OKR module.

- The OKR structure builder is not available in the non-scope boxes.
- [Linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) are not displayed anywhere on Gantt.