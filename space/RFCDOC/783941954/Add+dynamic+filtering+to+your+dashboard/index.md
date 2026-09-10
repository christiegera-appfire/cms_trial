# Add dynamic filtering to your dashboard

We've already seen how to [use](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/) [*static filters*](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/) [to build dashboards](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/) in which users can rapidly find the issues they are looking for. We'll now focus on another filtering mechanism that is better suited for use cases, such as filtering by one or several user-selected assignees, statuses, labels, etc. By the end of this tutorial, you can add (to Rich Filter Controller gadgets) drop-down buttons (dynamic filters), which allow you to filter by such option fields.

![Filter assignee.png](/cms_trial/assets/a0f33274-e6d8-48fd-87bd-14b8343bb949.png)

For this tutorial, you need to have already created:

- a *Rich Filter*
- a dashboard with one *Rich Filter Controller* gadget and at least one *Rich Filter Filter Results* gadget based on your Rich Filter.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941950/Use+working+queries+in+your+dashboard/).

## Add dynamic filters

1. Open the configuration page of your *Rich filter* as described in the [first tutorial](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/).
2. Click the *Dynamic Filters* tab.
3. Add new *Dynamic Filters* based on Assignee, Priority, Status, Labels, and Resolution.

   ![Dynamic filters.png](/cms_trial/assets/69dad33b-2145-4c97-bcad-ed3a3d3a1453.png)
4. Open (or refresh) the dashboard based on your rich filter or build a new one. The Rich Filter Controller gadget now displays the dynamic filters you added in the previous step.

   ![apply filtr.png](/cms_trial/assets/596cfe44-4353-487a-a898-4ce6dc352417.png)

   If you select options in any dynamic filter and then click **Apply**, the other gadgets in the dashboard that are based on the same rich filter will be updated to display only the issues that satisfy the selected criteria.

   ![FIltered priority.png](/cms_trial/assets/1a9dcd3b-ac88-4ae3-a9fa-fe7f8a410845.png)

   [Unmapped macro: legacy-content — no content to fall back on]

   You can deactivate all the active filters of the *Rich Filter Controller* gadget by clicking on the X at the bottom right.

   ![clear filters.png](/cms_trial/assets/d78eb0b5-1292-484f-9be6-d4a423b5962e.png)

In the rich filter configuration, you can change the order of the dynamic filters. In each Rich Filter Controller gadget, you can use this default order or customize the list of filters to be displayed by selecting the ones you want and placing them in the order you want.

## See also

[Configure Dynamic Filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/).

[Add smart filters and smart columns to your dashboard](/cms_trial/space/RFCDOC/783941961/Add+smart+filters+and+smart+columns+to+your+dashboard/).