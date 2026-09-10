# Use working queries in your dashboard

## Overview

By the end of this tutorial, you can split your list of issues into two groups: canceled and non-canceled. Each group will be displayed by its own *Rich Filter Results* gadget, which will be controlled by the same *Rich Filter Controller* gadget.

In this example, we consider *canceling* all the issues that have a non-empty resolution different from *Fixed* and *Done*. Depending on your Jira configuration, you might have different resolutions and conventions.

![Working queries.png](/cms_trial/assets/f2aa90da-f9f2-44d0-a5ab-22034129a219.png)

For this tutorial, you need to have already created:

- a *Rich Filter*
- a dashboard with one *Rich Filter Controller* gadget and one *Rich Filter Filter Results* gadget based on your *Rich Filter*.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941943/Define+views+for+your+dashboard/).

### Use Working Queries

1. At the bottom of the *Rich Filter Results* gadget, click  **Menu** (▢) > **Configure gadget** for the *Rich Filter Results* gadget you already have in your dashboard.

   ![53722952-532b-4fa7-8c14-13dd3a6f0fc3.png](/cms_trial/assets/17f0c805-afd8-4b8d-a583-70e89685001a.png)
2. Add the JQL resolution in the Working query field in (EMPTY, Fixed, and Done). This JQL filtering condition will always be combined (`AND`ed) with the JQL filter that feeds the gadget. Therefore, this gadget will display only issues with no resolution or the resolution *Fixed* or *Done* (which we consider *not-cancelled* in this example). Click **Submit**.

   ![contentId-783941950](/cms_trial/assets/8baa3eaf-b66f-41ba-b7d1-13af6b416e17.png)
3. Rename the *Rich Filter Results* gadget as *Not Cancelled* so that users easily understand what the gadget displays.

   ![contentId-783941950](/cms_trial/assets/ce143941-e389-413d-9437-3d767b434380.png)
4. The gadget's title is Not Cancelled, and it only displays issues with resolution, either EMPTY (Unresolved), FixedorDone.  
   If you now click the *Closed* static filter in the *Rich Filter Controller*, the *Rich Filter Results* gadget will be updated to show only *fixed*/*done* issues. 

   ![Closed_Delivery.png](/cms_trial/assets/7c9bd80d-9b02-4985-8602-121cc41f28d0.png)
5. Add a new *Rich Filter Results* gadget to your dashboard. Configure it based on the same *rich filter* as the two other gadgets and add the *working query* `resolution that is not in (EMPTY, Fixed, Done)`.

   ![contentId-783941950](/cms_trial/assets/e35058ba-1fdd-4082-b664-e2b4803bb92b.png)
6. Select *Customize shown views,* and add only the *Delivery* view; the gadget will display only this view for the *canceled* issues. Submit the configuration of your gadget.   
     

   [Unmapped macro: inline-media-image — no content to fall back on]
7. Rename the gadget as *Cancelled*.

   ![Rename.png](/cms_trial/assets/0c0159cb-9039-4901-9290-25cd782fda9a.png)

   The gadget's title is *Cancelled* and only displays *canceled* issues using the *Delivery* view.
8. Optionally, select a different color for this gadget.

   ![Change color.png](/cms_trial/assets/3f97a342-1d18-4ec0-bbe1-6e43971808ec.png)
9. Click the *Controller's* **Assigned to Me**static filterto turn it on. This will impact both *Rich Filter Results* gadgets (i.e., all gadgets based on the same rich filter in the dashboard). The first will show the fixed/done issues assigned to the current user, and the second will show the canceled issues assigned to the current user.

   ![Closed_Assigned to me.png](/cms_trial/assets/ccc91563-6c26-4611-9b82-76f84fd39f9c.png)

The *working query* is a powerful and versatile mechanism for customizing your gadgets. For instance, it allows you to split your issues in different groups (overlapping or not), to be used by different gadgets. Except for the controller, all the rich filter gadgets provide this feature.

Also, if you use the `ORDER BY` clause in a working query, this will take precedence over the `ORDER BY` clause of the base filter, allowing you to customize the default sorting of issues for that gadget.

### See also

[Add dynamic filtering to your dashboard](/cms_trial/space/RFCDOC/783941954/Add+dynamic+filtering+to+your+dashboard/).