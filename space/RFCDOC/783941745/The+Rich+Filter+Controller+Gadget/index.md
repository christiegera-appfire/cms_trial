# The Rich Filter Controller Gadget

## About the Rich Filter Controller gadget

The *Rich Filter Controller* gadget controls what other rich filter gadgets display (on the same dashboard and based on the same rich filter as the controller). The controller does not display any issue data; it only shows the quick filters defined in the rich filter. Instead of forcing teams to navigate between multiple saved filters and static dashboards, the Controller acts as a centralized switch, instantly synchronizing the data displayed across all connected dashboard gadgets the moment you apply a filter.

![ Controller gadget](/cms_trial/assets/78123751-e208-4b41-99e4-b1c7d530d734.png)

The quick filters can be reordered and organized in sections. Additionally, the *Rich Filter Controller* allows the users to export the dashboard content to PDF or Excel files – for more details, see the [Exporting data](/cms_trial/space/RFCDOC/783942966/Export+data/) documentation page.

Example 1: controller gadget displaying filters organized in named sections:

![filters organized in named sections](/cms_trial/assets/211e2108-cc81-4d87-b486-e8349a28bbe6.png)

Example 2: controller gadget with configured presets for a Green team:

![image-20260330-103552.png](/cms_trial/assets/07d22c08-4007-4ab9-846c-8e3cf39ece58.png)

## Configuring the Rich Filter Controller gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Controller* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783941745](/cms_trial/assets/9c3204bc-0b03-4f76-b238-46691671dbaf.png)

Edit the gadget configuration as described in the following table:

| **Setting** | **Description** |
| --- | --- |
| **Rich Filter** | Select the rich filter the gadget will use.  Click the **Rich Filter** button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. For details, see the Rights and Permissions documentation page. |
| **Quick filters & sections** | Once you have selected a rich filter for your gadget, you can customize which quick filters you want to display in your controller. By default, controllers show all available quick filters. You can use the radio buttons to change this and display only JQL filtering, or you can choose to customize in detail which quick filters to show and in what order using the last option.  If you choose the *Customize shown filters* option, the configuration form changes to display the list of quick filters. You can add, remove, or reorder (drag the vertical “grid” icon) the quick filters to be displayed. contentId-783941745 You can also organize your quick filters in named sections and customize filter colors. organize your quick filters In addition to the individual quick filters, the custom list menu includes three grouping options: *All Static*, *All Dynamic,* and *All Smart*. If these options are used, the gadget will display all the quick filters of the specified type in their place *except*those that are explicitly included. For example, you can use this to show the *Labels* dynamic filter first, then all static filters, and then all dynamic filters other than *Labels,* if any. Select quick filters |

## Filtering modes

The user can select a filtering mode alongside the values for the dynamic filters that display dropdowns (e.g., Assignee, Components, Status, Labels). The filtering modes correspond to the logical operators used to combine the selected values when generating the JQL filtering condition. Understanding filtering modes helps you get exactly the issues you're looking for.

- **OR**: this is the default filtering mode – when multiple values are selected in a dynamic filter, they are combined with OR, which means that the filter returns the issues that match any (at least one) of the selected values:

  ![or operator as the default filtering mode](/cms_trial/assets/d17b3d24-c0d5-47bf-b377-0f6e5df05e33.png)

  The JQL generated for the example above is "`component in (Admin, Architecture)`," which is functionally equivalent to "component = Admin OR component = Architecture."
- **AND**: The default OR behavior isn't always what you need. The AND filtering mode is available for fields that can have several values simultaneously. For example, a label field can store multiple values for a single issue. When multiple values are selected in a dynamic filter, they are combined with AND, which means that the filter returns the issues that match all the selected values simultaneously:

  ![AND operator filtering mode](/cms_trial/assets/b474573a-fa44-4438-a938-c46b6212a88a.png)

  The JQL generated for the example above is "`component = Admin AND component = Architecture"`.
- **NOT**: available for all fields – the selected values are negated and combined with AND, which means that the filter returns the issues that don't match any of the selected values:

  ![NOT operator operator filtering mode ](/cms_trial/assets/0ebbdfe8-fd89-41e4-b192-a956416f51bd.png)

  The JQL generated for the example above is "`component not in (Admin, Architecture) OR component is EMPTY`," which is functionally equivalent to "(component != Admin AND component != Architecture) OR component is EMPTY."

You can also use the AND filtering mode for smart filters by enabling the AND operator.

The AND filtering mode is available only for fields with several values simultaneously (for example, Labels, multiple selection fields). For instance, users can search for issues with components A and B simultaneously. Still, searching for issues with priority High and Low simultaneously doesn't make sense because the priority field can have only one value at a time. For fields that cannot have several values simultaneously, only the OR and NOT filtering modes are available.

## Dashboard state permalinks

Dashboard state permalinks are URLs that encode the current state of the *Rich Filter Controller* gadgets in the dashboard. Later, the generated URL can open the dashboard and restore the quick filters to the same state.

The permalink can be generated by clicking the **Permalink** icon in the footer of the *Rich Filter Controller* gadget. It will then be automatically copied to the clipboard.

![permalink](/cms_trial/assets/d4e54985-ceaf-439b-937e-c886fd6c50ac.png)

The generated URL can be bookmarked or sent to another user. When the URL is opened, the rich filter gadgets are restored to the same state as when the link was generated—the same quick filters are selected in the *Rich Filter Controller* gadgets.

## Presets

Presets are saved combinations of quick filter selections that can be applied with a single click. Instead of reselecting multiple filters each time, each combination is saved as a preset so it can be applied with one click. They appear as toggle buttons at the top of the Rich Filter Controller, allowing users to instantly restore frequently used filter combinations without manually selecting individual filters each time.

The **Show** **presets** (▢) option under **Menu** (▢) in the footer opens preset configuration when none exist, or shows the presets section when presets are already defined.

![Show presets option](/cms_trial/assets/6c873eac-186b-492d-ac52-efa1c333d9ff.png)

When creating a preset, users can configure their filters and customize both the label and display color to help them quickly identify different presets.

![Save preset](/cms_trial/assets/39d13934-0d70-4805-b97d-eef767e02403.png)

You can create multiple presets to suit various filtering needs, and switch between them by clicking the corresponding toggle buttons displayed at the top of the Rich Filter Controller.

![Switch between presets](/cms_trial/assets/02368402-db15-44bc-8a72-a006398431aa.png)

Modifying the presets or hiding the presets section is available through the **Menu** icon that appears when hovering the **Presets** (▢) icon

![Edit presets](/cms_trial/assets/9d65d38b-035a-4c5b-a4e3-9688205ec740.png)

The preset configuration is saved in the Jira user preferences, ensuring personal presets remain available when working with the dashboard on different browsers or computers.

## Navigation options

You can move back and forth between previous filter states in the dashboard—just like navigating through your browser history. Simply click the **Arrow** icons (▢) to step through your filter history without the need to apply the filters again.

![click to go back option](/cms_trial/assets/0775db38-757d-4a8d-8c3b-caccf88f20b4.png)![Click to go forward](/cms_trial/assets/036e11d8-3b83-4d40-a4cc-a4e785f5e195.png)

You can use keyboard to navigate between the dynamic filters for the *Rich filter Controller* gadget. Navigate filter options using arrow keys, select filters with Enter, and close dropdowns with Esc. When you press Enter, the focus moves to the **Apply** button. So you can apply the filters using your keyboard.

You can also navigate between the footer controls, such as filtered issue count, Export, Permalink, Menu, JQL, Apply, and Cancel icons. Press Enter while focused on total issues to open the Issue Navigator and display all issues. Use arrows to navigate the Export or Menu options. Select the options with Enter or close the dropdown with Esc.

### Learn more

[Build a simple interactive Jira dashboard](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/)