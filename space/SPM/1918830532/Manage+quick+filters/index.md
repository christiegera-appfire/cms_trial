# Manage quick filters

In this section, you will learn how to create [quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/), import them from the Jira board, and set the [inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/).

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the app Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App Admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Quick filters**.  Image — asset pipeline pending Quick filters settings on the box type configuration page. | For a box type (all boxes of a given type), you can configure:   - Inheritance mode - Default quick filters |
| Box configuration | Only a user with a minimum Box Admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Quick filters**.  Image — asset pipeline pending Quick filters settings on the box configuration page. | For a particular box, you can configure:   - Quick filters |

## Inheritance mode

The [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) determines whether a Box Admin can later go to **Box configuration** > **Tasks** > **Quick filters** and edit the quick filters of an individual box. It also determines whether filters set up in upper-level boxes can be used in a box.

Quick filters are inherited from all of their upper-level boxes, which means you can reuse the filters. To change them globally, go to the box configuration of the root box.

## Quick filter configuration

By default, several quick filters are available and can be deleted. Among these filters, you can find:

- My tasks (tasks assigned to the user)
- Unresolved (tasks with Open and Reopened statuses)
- Updated <5d (tasks updated within the last 5 days)

Image — asset pipeline pending  
General Settings, Quick filters options

## Create quick filters

### Box configuration page

Filters added in this way are created and available in the App (they are not saved in Jira).

To create a filter:

1. Click the **+Add a new quick filter** button.
2. Enter the following information:

Image — asset pipeline pending  
A window for creation of new quick filters

- Name – will be displayed in the Quick Filter drop-down and on the favorite Quick Filters buttons. You can also search the list of quick filters using the name.
- Description – use this additional text field too, for example, to explain complicated queries. When you hover over the favorite Filter button, the description will appear in the tooltip.
- Query – JQL query with validation indicated by the "JQL" icon (green = correct, red = incorrect). You will not be able to save a faulty filter.

1. Click the **Save** button to finish the process.

- A parent work item that does not fit the JQL query will be shaded out even though its children do.
- With Quick Filters enabled, a logged-in user might not be able to see search results if the JQL filter that defines the scope of the box is not shared with this user. To learn how to share Jira filters, check [the related Jira documentation entry](https://confluence.atlassian.com/jiracoreserver073/saving-your-search-as-a-filter-861257224.html?_ga=2.25779000.463124992.1568024709-632874800.1527639834#Savingyoursearchasafilter-sharing_filtersSharingafilter).
- When a task is a parent and does not fit the JQL query, while at the same time, its children do fit the JQL filter, the parent task will be shaded out - just like when using the Search box.

### Quick Filters based on existing Jira filters

When you use Jira filters to define BigPicture Quick Filters, make sure that all box users can access them. Otherwise, the Quick Filter will not return any results, as the current user doesn't have sufficient permissions.

Jira filters can be found under Work items > Manage filters. Change filter permissions if needed.

### Quick filters imported from a Jira Board

If you want to import multiple filters at once, you can use the **Import from Jira Board**option. This will allow you to import a set of filters.

Image — asset pipeline pending  
Icon for importing quick filters is highlighted

1. Select a board from a drop-down.
2. Select the filters:

   1. you can check the box at the top to select all filters
   2. manually select each filter
   3. use the search function to find the filters you are interested in
3. Click **Import**to finish the process.

   Image — asset pipeline pending  
   Selecting Jira Boards in the Import Quick Filters window

## Change the order of quick filters

A **Box admin** can change the order in which the Quick Filters are listed in the drop-down.

To make the adjustment, go to Box Configuration > Tasks > Quick Filters.

## Default Quick Filters

Define the default Quick Filters of a Box type - the default filters are automatically available in all newly created boxes of this type.

Once a Box is created, a Box admin can edit the Quick Filters in the Box configuration > Tasks > Quick filters (if the inheritance mode allows it).

Changes to the default Quick filters of a Box type apply **only to newly created boxes**. Existing boxes won't be updated.

In other words, when a new box is created, the roles specified for a box type are copied into the box you create. This is the only time this happens. When a box already exists, changes to the template don't affect it. Note: You can leave the template empty if you prefer to manually set up all roles each time a new box of a given type is created.

Image — asset pipeline pending  
image2022-1-24\_14-30-8.png

### Quick Filters based on existing Jira filters

When you use Jira filters to define Quick Filters in the app, ensure all Box users can access those Jira filters. Otherwise, the Quick Filter will not return any results, as the current user doesn't have sufficient permissions.

Image — asset pipeline pending  
contentId-1918830532

### Quick filters imported from a Jira Board

If you want to import multiple filters simultaneously, you can use the **Import from Jira Board**option. This will allow you to import a set of filters.

Image — asset pipeline pending  
contentId-1918830532

Select a board from a drop-down:

Image — asset pipeline pending  
image-20250210-133306.png

Select the filters:

- you can check the box at the top to select all filters
- manually select each filter
- use the search function to find the filters you are interested in

Click **Import**to finish the process.

Image — asset pipeline pending  
contentId-1918830532

## Apply Quick Filters

Once you create the filters, you can apply them using the filter picker located on the module's header. Instead of predefining long and complicated JQL filters, you can combine your filters using the "AND" and "OR" operators.

For example, the 'In progress tasks'  Quick Filter is selected and added as a favorite using the Scope module.

Image — asset pipeline pending  
contentId-1918830532

## Quick Filter default configuration

Some filters are predefined using box types by default. If the inheritance mode is set to 'Own' or 'Own with inherited, ' you can edit or delete them. When the Quick Filters are inherited, the box admin cannot edit them in the sub-box configuration.

### Description Tooltip

Example of a Description tooltip in the Gantt module.

Image — asset pipeline pending  
contentId-1918830532

Image — asset pipeline pending  
navigating up and down the quick filters using the keyboard arrows.