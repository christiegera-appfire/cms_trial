# Add rich filter flexi charts gadgets to your dashboard

By the end of this tutorial, you will be able to configure and use *Rich Filter Flexi Charts* gadgets and to control the displayed data with a *Rich Filter Controller* gadget.

![rich filter flexi charts gadgets.png](/cms_trial/assets/e3a8be26-ce30-4afb-bb30-9ce76eed75d8.png)

For this tutorial, you need to already have created:

- a *rich filter*
- a dashboard with one *Rich Filter Controller* gadget based on your *rich filter*.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941975/Add+rich+filter+two+dimensional+statistics+gadgets+to+your+dashboard/).

## Add Rich Filter Flexi Charts gadgets

1. Open the dashboard based on your rich filter or build a new one. Click the **Add gadget** button at the top right of the screen to add two **Rich Filter Flexi Charts** gadgets to the dashboard.

   ![contentId-783941981](/cms_trial/assets/8e32ca47-6762-448f-95ac-0918506664f4.png)

   Click twice on the *Add* button to add two *Rich Filter Flexi Charts* gadgets.

   ![addrich filter flexi charts gadgets.png](/cms_trial/assets/c2f09357-25c0-43ad-8a16-96103b848631.png)

   The gadgets will be added to the left column of the dashboard. Move them to the top of the right column (sidebar), using drag & drop, if you want to have the same layout as in our example.
2. In the configuration form of the first gadget select your *rich filter*.

   ![contentId-783941981](/cms_trial/assets/911d6021-2130-4880-944c-2c10a01c24c1.png)
3. Configure the gadget:

   1. Leave **Donut** as the **Chart type** (the default option).
   2. Select **Priority** as the **Statistic type**
   3. Select **Story Points** as the **Value**
   4. Click **Submit**

      ![contentId-783941981](/cms_trial/assets/5f30c4e5-6ff7-48bf-bf9f-cf11f64d42ee.png)

      The gadget displays a *donut chart* with the sum of the *Story Points* broken down by *Priority*.

      ![Story points by priority.png](/cms_trial/assets/728c997d-5f58-4381-a4a9-08463bac4f21.png)
4. In the second gadget's configuration form, select your *rich filter*. Select *Clustered Bar* as *Chart type*, *Status* as *Statistic type* for the *Primary breakdown*, *Priority* as *Statistic type* for the *Secondary breakdown*, and *Original estimate* as *Value*, then click on *Submit*.

   ![contentId-783941981](/cms_trial/assets/53265bc9-1773-4eca-946d-caf86a42940e.png)

   The gadget displays a *clustered bar chart* with the sum of the *Original estimate* broken down by *Status* and *Priority*.

   ![ Original estimate broken down by Status and Priority..png](/cms_trial/assets/d8c414a8-d325-4e0f-a576-11050cef7c8e.png)
5. As always, if you activate *quick filters* in the *Rich Filter Controller* gadget (any combination of *static*, *dynamic*, and smart filters), the other gadgets in the dashboard based on the same rich filter will be updated to use only the issues that satisfy the active *quick filters*.

In addition to statistics based on issue fields, the *Rich Filter Flexi Charts* gadget can also display statistics based on *smart filters*. We've seen an example of statistics based on a *smart filter* in the tutorial [Add Rich Filter statistics gadgets to your dashboard](/cms_trial/space/RFCDOC/783941968/Add+rich+filter+statistics+gadgets+to+your+dashboard/).

## See also

[Rich Filter Flexi Charts Gadgets](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/)