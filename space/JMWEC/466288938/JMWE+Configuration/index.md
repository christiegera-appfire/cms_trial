# JMWE Configuration

Generally, JMWE does not require any global configurations; nearly all of its features - and their configurations - are included in the workflow editing screens or in the other tools available under the *JIRA MISC WORKFLOW EXTENSIONS* section of App administration. However, there are a few options available, detailed below.

## General Settings

### Send notifications

This setting controls the default value of the "Send notifications" option when adding a *new* post function to a transition.

Updating this option will **not update** existing post functions.

**To migrating users**

If you have workflows that have been migrated from the Data Center/Server versions of JMWE to the new "Connect" version on Sept. 19, 2016, this option also controls the default behavior of the [Assign to Role Member](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Assign%20to%20role%20member&linkCreation=true&fromPageId=449839323) and [Assign to Last Role Member](/cms_trial/space/JMWEC/466225934/Assign+to+last+role+member+(Deprecated)/) post functions. If you did not reconfigure these post functions after the migration, the default setting above will be used to control whether they should send notifications.

You can always override the default behavior by editing the post function configuration directly.

## View Issue Screen

Because of the [asynchronous nature of Cloud post-functions](/cms_trial/space/JMWEC/466256571/Changes+made+by+post-functions+are+not+always+visible+immediately/), the outcome of JMWE post functions is generally not visible on the View Issue screen when it is refreshed at the end of a transition. Likewise, no user interaction can be triggered by a post function.

JMWE for Jira Cloud implements a mechanism that supports triggering actions, such as refreshing the screen or navigating to an issue, after the transition completes, *only if the transition was triggered from the View Issue screen*.

### Auto-refresh Issue

**This option is selected by default.** Checking this setting will cause JMWE to refresh the View Issue screen if a change made by a JMWE post function is detected within 10 seconds after the Transition completes.

### Show “Transitions” Activity Tab

JMWE adds a **Transitions** activity tab to the View Issue screen. However, some Jira Cloud instances might show a second Transitions tab, which is implemented by Jira Cloud but only available on "old" Jira Cloud instances. **JMWE**'s Transitions tab can be hidden by unchecking this option.

**Note:** Atlassian's Transitions tab, if you see it, can only be hidden by opening a support ticket with [Atlassian Support](https://support.atlassian.com/contact/#/).

## Application menus

### Display JMWE links

This option will add or remove shortcuts to the JMWE Administration page in the following places:

- Project sidebar
- Board menus (in the upper right corner near the Action menu for the board)
- Action menu of the Issue view (the option **Edit workflow with JMWE**)