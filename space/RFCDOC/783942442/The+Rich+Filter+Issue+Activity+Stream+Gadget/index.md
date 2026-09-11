# The Rich Filter Issue Activity Stream Gadget

## About the Issue Activity Stream gadget

The *Issue Activity Stream* gadget displays the recent activity on the issues. It resembles Jira’s built-in *Activity Stream* gadget, but it is based on a rich filter and thus adds new features:

- The content displayed can be further filtered by using *Rich Filter Controller* gadgets;
- The gadget itself can further refine the results by:

  - applying a gadget-specific JQL query called a *working query;*
  - filtering the activity items by their author and activity type;
- You can [export the gadget content](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

Watch the video to see the Issue Activity Stream gadget features:

![ Issue Activity Stream gadget.png](/cms_trial/assets/bdd1e576-8292-474b-a2bc-0ab2a51a40ae.png)

## Configuring the Issue Activity Stream gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Issue Activity Stream* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783942442](/cms_trial/assets/3c3dde25-4ade-4686-b743-aa664ac499a2.png)

Edit the gadget configuration as described in the following table:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter on which the gadget will be based.  Click the *Rich Filter* selector to display the list of rich filters; you can either scroll through or use the search box to find the filter you need.  The gadgets’ configuration forms only show the rich filters you can view. Check the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page for more details. |
| **Working Query** | The working query is an additional JQL query permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues displayed by the gadget. |
| **Items filtering** | This optional setting allows activity items to be filtered by their **Author***,* **Application***,* and **Activity** type. For each of the filters, you can select the operator (*is* or *is not*) and one or more values:   - It means that the gadget will display only the items whose author, application or activity type matches the selected values; - This does not mean the gadget will exclude the items whose author/activity type matches the selected values and display the remaining items.   The options available for activity type filtering are *Issue created*, *Issue edited*, *Issue transitioned*, *Issue resolved*, and *Comment*. contentId-783942442 |
| **Maximum initial items** | The maximum number of items the gadget will display initially is 10. The default is 10; it can be changed but cannot exceed 100. Users can display more items by clicking the *Show More...* button at the bottom of the items list. |