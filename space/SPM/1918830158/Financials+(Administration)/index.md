# Financials (Administration)

In the Administration configuration you can manage hourly rates for teams and calculation currency.

You can access the settings by clicking the App Settings icon in the upper-right corner of the window:

![financials-administration.png](/cms_trial/assets/530c0994-33ee-41bb-acf9-35637ca261b2.png)

## Team hourly rate

### Create

![financials-team-hourly-rate.png](/cms_trial/assets/60220cd9-bf70-4cf6-ad46-ab465a363b0f.png)

You can create, edit, or delete an hourly rate assigned to a specific team and then used to calculate the estimated costs of initiatives.

To add a new rate:

1. Click **+ New hourly rate** to add a new rate.
2. Choose the start date of the validity of the rate. You can add more than one hourly rate with different start dates to cover rate changes over time.
3. Choose a box from a drop-down menu.
4. When you choose a box, the team list is updated with teams related to this box. Now, you can set an hourly rate for each team.
5. Set an hourly rate for at least one team.
6. Click **Save**.

![add-hourly-rates.png](/cms_trial/assets/2244e120-2587-49cf-b59d-80c454af3697.png)

### Edit/Delete

You can edit or delete a team’s rate by clicking the corresponding icons in the Team hourly rates page.

## Currency

Here, you can change the currency displayed in the Financials module:

![financials-currency.png](/cms_trial/assets/52b02e09-4b11-4391-a6d2-5f8e155b37dc.png)

## Baselines

To find out more about baselines, go to the [Cost Variance](/cms_trial/space/SPM/2265383282/Cost+Variance/) page.

Snapshot information and automation settings can be found in **App Administration** > **Financials** tab > **Baselines**.

![financials-baselines.png](/cms_trial/assets/74220f23-8a12-4095-ac11-448161a71319.png)

### Automation settings

You can set up the app to take the snapshots automatically:

- At the end of **each quarter**
- At the start of **each month**
- **Never**

## Custom expenses

Custom expenses are one-time or recurring expenses that are not associated with specific work items. They can be beneficial for monitoring flexible or miscellaneous project-related expenditures.

![financials-custom-expences.png](/cms_trial/assets/b5f25baa-bbd4-42a2-9c24-766e7a8eceaf.png)

To add a new expense, click **+ Add new expense.**

**Name** - set the cost name.

**Cost ()** - set the cost value. The currency symbol depends on [the currency settings](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1673757073/Financials+Administration#Currency).

**Initiative** - select an initiative to which the cost will be added.

**Valid from** - select the cost validity date.

**Recuring** - you can switch this toggle if you want the cost to be added periodically. Once you do that, choose a period (each month, each quarter or each year) and end date.

**CapEx or OpEx** - choose if the cost is CapEx, OpEx or uncategorized - for more information, check the next section.

![add-custom-expenses.png](/cms_trial/assets/f738e498-842a-4189-928a-7e087722ef9c.png)

Click **Save** to add the cost. Once you do it, it is available in the Work breakdown table in the related initiative:

![custom-cost-initiative.png](/cms_trial/assets/2e82dca8-eca1-4ab8-84fd-99d55d52b725.png)

## CapEx and OpEx

![financials-capex-opex.png](/cms_trial/assets/01bfcec2-77b8-48ed-a08d-626491dbabcc.png)

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

![financials-budget-milestones.png](/cms_trial/assets/8aa5b6be-13de-456b-99b5-79091abd4ea3.png)

Click **+ Add milestone** to add a new entry to the list. Fill in the fields accordingly:

![financials-new-budget-milestone.png](/cms_trial/assets/41535dbc-1810-45db-90fe-3aceff6b9e48.png)

Once the milestone is added, it is visible in the chosen Initiative as a red line:

![financials-milestone.png](/cms_trial/assets/18818e59-6ab6-4ce2-a64c-8e9b06454e95.png)