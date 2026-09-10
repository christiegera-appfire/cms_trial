# Add smart filters and smart columns to your dashboard

**Smart filters** are another type of filter you can define in *Rich Filters* and use in dashboards. By the end of this tutorial, you can add (to Rich Filter Controller gadgets) drop-down buttons that allow you to filter issues by the criteria you have defined. You will also be able to display (in *Rich Filter Results* gadgets) computed columns (we call these *smart columns*) based on the same criteria.

![Apply smart filters.png](/cms_trial/assets/1a117853-d41b-4465-90fd-5cc6b9ad6e3c.png)

For this tutorial, you need to have already created:

- a *Rich Filter*
- a dashboard with one *Rich Filter Controller* gadget and at least one *Rich Filter Filter Results* gadget based on your *Rich Filter*.

We have used the dashboard we worked with in [the previous tutorial](/cms_trial/space/RFCDOC/783941954/Add+dynamic+filtering+to+your+dashboard/).

On this page:

1. [Add smart filters](/cms_trial/space/RFCDOC/783941961/Add+smart+filters+and+smart+columns+to+your+dashboard/)
2. [Add smart columns](/cms_trial/space/RFCDOC/783941961/Add+smart+filters+and+smart+columns+to+your+dashboard/)

## Add smart filters

1. Open the configuration page of your *Fich filter* as described in the [first tutorial](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/).
2. Click the **Smart Filters** tab.

   ![Smart filters.png](/cms_trial/assets/c731b2b5-a174-47a0-b49c-a9de42d5b40e.png)
3. To create a new smart filter named `Warnings`, click **Create smart filter,**  enter the name in the dialog box, and click **Create**.

   ![Create a smart filter.png](/cms_trial/assets/e16a5cc8-0af4-4592-b4f2-192d317264e7.png)
4. Add the three clauses below by clicking **Create smart clause**button at the top right of the screen and entering the name and the JQL in the dialog box for each clause.

| Name | JQL |
| --- | --- |
| Top Priority | `priority in (1,2) and status = Open` |
| Past Due Date | `duedate < now() and status != Closed` |
| No Due Date | `duedate = EMPTY and status not in (Resolved, Closed)` |

![Create smart clause.png](/cms_trial/assets/c91d0ede-6a65-487c-b60c-53c40166c441.png)![Create a smart clause.png](/cms_trial/assets/478cc8fd-c92f-4229-9c50-7750b4650376.png)

1. Change the colors of the *smart clauses* as shown below:

   ![Clausde color change.png](/cms_trial/assets/ef9f61af-6932-4a75-9a41-2132b8cad09c.png)

1. Open (or refresh) the dashboard based on your rich filter or build a new one. The Rich Filter Controller gadget displays the smart filter containing the three options you have configured.

![filter Warnings.png](/cms_trial/assets/bf77f80d-1bda-4f81-9b6d-c20d5aac8481.png)

If you select options in the *smart filter* and then click **Apply**, the other gadgets in the dashboard based on the same rich filter will be updated to display only the issues that satisfy the JQL conditions of the selected options (the JQL conditions are ORed if more than one option is selected).

## Add smart columns

1. Open the configuration page of your *Rich filter* and click the **Views** tab.
2. In the *Requester* view, you'll notice that it is now possible to add the *smart filter* to be displayed as a computed column (we call this a *smart column*). Add the **Warnings** smart column to the view.

   ![Views with Warnings.png](/cms_trial/assets/45455694-b248-49c6-a85f-3cfa0e9121b5.png)
3. Refresh the dashboard. You'll notice that the *Requester* view of the *Rich Filter Results* gadget now has a new column with the header *Warnings*, displaying labels in colored rectangles for the corresponding issues, as configured in the *smart filter clauses*.

   ![dashboard with warnings.png](/cms_trial/assets/1aaabe3e-7a3c-470f-b055-14a7cf24a727.png)
4. Go back to the *Smart Filters* section of your *rich filter* configuration page. Create a new *smart filter* called `Risk` and add a clause with the name `On` and the JQL `priority in (1,2) AND assignee is EMPTY.`

   ![Risk filter.png](/cms_trial/assets/03717e7d-0da2-4821-a861-55751f0f1ebd.png)
5. Go to the *Views* of your *rich filter*. In the *Delivery* view, add the smart column *Risk* that you have just created.
6. Drag & drop the *Risk* smart column after the *Priority* column. 

   ![Drag and drop.png](/cms_trial/assets/0b2f1caf-3834-458d-a28e-2c72cc446b70.png)
7. To edit the *Risk* smart column, click the **Edit** (▢) icon.

   ![contentId-783941961](/cms_trial/assets/99b82084-70c5-4c16-86a5-8eba0420cd45.png)
8. To make this column as compact as possible, make sure you select:

   1. For **Column heading**,the **Smart filter initials** option
   2. For **Display as**the **Colors Only** option![contentId-783941961](/cms_trial/assets/d0af9fd5-db7d-4e52-b395-6d8b1b6e48d3.png)
9. Click **Update**.
10. Refresh the dashboard. In the *Rich Filter Controller* gadget, select the option *Top Priority* in the smart filter *Warnings,* and click **Apply**. You'll notice that the *Rich Filter Results* gadget displays only the issues that satisfy the JQL condition of the *Top Priority*clause (`priority in (1,2) and status = Open`) and that in the *Delivery* view, next to the *Priority* field, a new column with the header *R* displays color tags for the at-risk issues (`priority in (1,2) and assignee is EMPTY`).

    ![Top priority.png](/cms_trial/assets/321db514-a08c-4f7d-b313-011687a062bf.png)

Smart filters are a very powerful mechanism that allows you to create complex filtering options, add computed columns to your views, and highlight issues using color tags.

## See also

[Configuring Smart Filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/)

[Add Rich Filter Statistics gadgets to your dashboard](/cms_trial/space/RFCDOC/783941968/Add+rich+filter+statistics+gadgets+to+your+dashboard/)