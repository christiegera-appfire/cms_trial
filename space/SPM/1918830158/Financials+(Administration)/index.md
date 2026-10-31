# Financials (Administration)

In the Administration configuration you can manage hourly rates for teams and calculation currency.

You can access the settings by clicking the App Settings icon in the upper-right corner of the window:

Image — asset pipeline pending  
financials-administration.png

## Team hourly rate

### Create

Image — asset pipeline pending  
financials-team-hourly-rate.png

You can create, edit, or delete an hourly rate assigned to a specific team and then used to calculate the estimated costs of initiatives.

To add a new rate:

1. Click **+ New hourly rate** to add a new rate.
2. Choose the start date of the validity of the rate. You can add more than one hourly rate with different start dates to cover rate changes over time.
3. Choose a box from a drop-down menu.
4. When you choose a box, the team list is updated with teams related to this box. Now, you can set an hourly rate for each team.
5. Set an hourly rate for at least one team.
6. Click **Save**.

Image — asset pipeline pending  
add-hourly-rates.png

### Edit/Delete

You can edit or delete a team’s rate by clicking the corresponding icons in the Team hourly rates page.

## Currency

Here, you can change the currency displayed in the Financials module:

Image — asset pipeline pending  
financials-currency.png

## Baselines

To find out more about baselines, go to the [Cost Variance](/cms_trial/space/SPM/2265383282/Cost+Variance/) page.

Snapshot information and automation settings can be found in **App Administration** > **Financials** tab > **Baselines**.

Image — asset pipeline pending  
financials-baselines.png

### Automation settings

You can set up the app to take the snapshots automatically:

- At the end of **each quarter**
- At the start of **each month**
- **Never**

## Custom expenses

Custom expenses are one-time or recurring expenses that are not associated with specific work items. They can be beneficial for monitoring flexible or miscellaneous project-related expenditures.

Image — asset pipeline pending  
financials-custom-expenses.png

To add a new expense, click **+ Add new expense.**

**Manually added or linked to Jira custom field** - you can choose to add expense based on data added in this form or based on a Jira custom field. If you choose the second option, a new field is added: **Jira custom field**. Here you can choose a custom Jira field defined in this Jira instance.

The source of the expanse is displayed in the Source field in the Work cost breakdown table in the related initiative.

If the chosen field is deleted in Jira, information about it is displayed in the Work cost breakdown:

Image — asset pipeline pending  
custom-field-removed.png

**Name** - set the cost name.

**Cost ()** - set the cost value. The currency symbol depends on [the currency settings](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1673757073/Financials+Administration#Currency).

**Initiative** - select an initiative to which the cost will be added.

**Valid from** - select the cost validity date.

**Recuring** - you can switch this toggle if you want the cost to be added periodically. Once you do that, choose a period (each month, each quarter or each year) and end date.

**CapEx or OpEx** - choose if the cost is CapEx, OpEx or uncategorized - for more information, check the next section.

Image — asset pipeline pending  
add-new-custom-expense.png

Click **Save** to add the cost. Once you do it, it is available in the Work breakdown table in the related initiative:

Image — asset pipeline pending  
woek-costs-breakdown-custom-expenses.png

## CapEx and OpEx

Image — asset pipeline pending  
financials-capex-opex.png

CapEx and OpEx costs can be managed in the CapEx vs OpEx widget on the [portfolio](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695482/Actual+vs+Planned#CapEx-vs.-OpEx) and [initiative](/cms_trial/space/SPM/2265317971/Initiative/) level.

### Show widget

Switch the Show on financial dashboard toggle on to make the widget visible in the Financials module.

### Source

Here, you can choose a source for cost categorization. Note that only one source type can be chosen at a time - you cannot track two sources at the same time.

#### Jira custom filters

Choose a Jira filter for CapEx and OpEx. The cost related to work items in the filter's results will be marked as the corresponding cost.

#### Custom field

Assign the ‘CapEx or OpEx’ custom field in Jira to label work items as CapEx or Opex. Once configured, the system reads these tags and include the items in the corresponding cost category.

The ‘CapEx or OpEx’ custom field is added to Jira custom fields upon the app installation. Add the field to issues for which you want to track the CapEx and OpEx costs. Find out more about adding a custom field to an issue in [the Jira documentation](https://confluence.atlassian.com/adminjiraserver/adding-custom-fields-1047552713.html).

## Budget milestones

Budget milestones are checkpoints for your projects. They let you plan ahead by setting key dates and expected costs, giving you better control over your spending.

Image — asset pipeline pending  
financials-budget-milestones.png

Click **+ Add milestone** to add a new entry to the list. Fill in the fields accordingly:

Image — asset pipeline pending  
financials-new-budget-milestone.png

Once the milestone is added, it is visible in the chosen Initiative as a red line:

Image — asset pipeline pending  
financials-milestone.png