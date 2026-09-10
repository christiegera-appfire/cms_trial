# Define views for your dashboard

## Overview

By the end of this tutorial, you will know how to display several views of the issues list on the *Rich Filter Results* gadget. A view contains a list of fields to be displayed by the gadget.

![Define views.png](/cms_trial/assets/b15341c6-7972-4562-96b8-22dba2ce0315.png)

Views allow you to display large amounts of information logically organized and avoid horizontal scrolling as much as possible. You can also define different views for different situations (for example, in different contexts, you might want to focus on different fields).

For this tutorial, you need to have already created:

- a *rich filter*
- a dashboard with one *Rich Filter Controller* gadget and one *Rich Filter Filter Results* gadget based on your *Rich Filter*.

We have used the dashboard created in [the previous tutorial](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/).

### Add multiple views to your *Rich Filter Results* gadget

1. Open your *Rich filters* page as described in the [first tutorial](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/).
2. Click the *Views* tab.

   ![Create views.png](/cms_trial/assets/0226a855-7bcb-40ea-b792-538320f46121.png)
3. You can create a new view called `Requester` by clicking the **Create view** button.

   ![Create view_requester.png](/cms_trial/assets/625396f7-e9f7-40a5-ba37-ad9ab37a3b27.png)
4. In the view you just created, add the columns Issue Type, Key, Priority, Summary, Reporter, and *Status*.

   ![Requester_view.png](/cms_trial/assets/71dcf0e4-9d22-43ad-9239-ae876575bdd4.png)
5. Open the dashboard based on your rich filter or build a new one. The *Rich Filter Results* gadget displays the issues using the view (the list of columns) you configured in the previous step.

   ![Rich Filter Result.png](/cms_trial/assets/3c5da8b0-f884-4df8-bb33-c2b5512b707a.png)
6. Go back to the *Views* tab of your *Rich filters* page.

You can keep the dashboard open in the current tab and open the *Rich filters* page in another tab to easily switch between the two.

1. Create another view called `Delivery`with the columns: *Issue Type, Key, Priority, Summary, Assignee, Status, and Resolution*. Your rich filter now has two views: *Requester* and *Delivery*.

![Views for.png](/cms_trial/assets/fd5fb6ec-5dce-4994-9394-2623ede973ce.png)

1. Return to your dashboard and refresh it. The two views you have defined are now available in the *Rich Filter Results* gadget, which allows you to switch easily between views.

![Delivery view.png](/cms_trial/assets/4ad3aab2-dfd3-4c7e-af6d-4b40fa4aedc4.png)

You can reorder the columns within a view. You can also reorder the views.

### See also

[Configuring Views](/cms_trial/space/RFCDOC/783941729/Configure+views/)

[The Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)

[Use working queries in your dashboard](/cms_trial/space/RFCDOC/783941950/Use+working+queries+in+your+dashboard/)