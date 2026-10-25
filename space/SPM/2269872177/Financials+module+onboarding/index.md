# Financials module onboarding

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Financials module onboarding (old navigation)

Click to expand the guide

The onboarding process is automatically started when you open the Financials module for the first time in a specific portfolio or project box. The process then leads you through the initial Financials module configuration.

## Portfolio

### Initial configuration

The onboarding workflow leads you through steps that will allow you to start using the Financials module in a specific portfolio.

Once you complete the onboarding for the portfolio, the settings apply to all the initiatives in the portfolio.

If you would rather perform the onboarding for a single initiative, check [the Onboarding for initiative](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/2258142322/Financials+module+onboarding#Initiative).

### Portfolio initiatives

Make sure that the portfolio has initiatives - projects with tasks (that have dates and effort estimations). You can define them before or use the options available upon choosing the Financials module from the module selector for a portfolio without initiatives:

- Import Jira projects
- Add existing projects

![fianncials-portfolio-onboarding.png](/cms_trial/assets/45170047-2e60-42e9-a4b0-0c07a22de155.png)

#### Import Jira projects

Start typing to search for Jira projects. Choose a type of BigPicture project to be created based on a Jira project:

- Agile Project
- Classic project
- Hybrid Project
- Program

You can choose to create one BigPicture project or a project for each of the selected items:

![Import Jira Projects dialog with several different Jira projects selected for import.](/cms_trial/assets/5bcdeb98-90cb-4c9a-922f-70c3d963e9ad.png)

#### Add existing projects

Choose any required existing projects from a drop-down list:

![Add existing initiatives to this portfolio dialog with example initiatives and projects selected.](/cms_trial/assets/940876ee-815e-4ece-986e-4ece35e8e676.png)

### Financials onboarding

Once the portfolio has initiatives, you can start setting up the Financials module. When you first open the Financials module for a box, you will be prompted to create the Financials module configuration. Click the **Let’s Start** button to start the configuration.

![financials-portfolio.png](/cms_trial/assets/03af02f9-4d87-49df-bdb6-88f4a483d89c.png)

#### Select period

Choose the timeframe for tracking initiative costs (can be switched later):

- Current quarter
- Current year
- Next quarter
- Next year

#### Configure calculations settings

Task and hourly rate that are the base for the cost calculation:

#### Select initiatives to apply settings to

Choose initiatives within the portfolio that will be considered for financial calculation.

#### How do you estimate work effort?

- Man-days
- Story points

#### Which hourly rate should we use?

- Flat rate - use a single hourly rate for all tasks, regardless of the team.
- Team hourly rate - use the team hourly rate if the tasks are assigned to teams and each team needs a different rate. If the team hourly rate is chosen and a team has not been set, the app sets $100 for the calculations. To define hourly rates for teams, see the [Financials (Administration)](/cms_trial/space/SPM/1918830158/Financials+(Administration)/) page.

#### Flat hourly rate ($)

Set an hourly rate.

The currency symbol is set on the [Financials (Administration)](/cms_trial/space/SPM/1918830158/Financials+(Administration)/) page.

### Finish onboarding

Click **Finish** on the last step of the onboarding. If the charts in the *Planned vs Actual costs* panel are not generated, it means that there are no tasks in the initiatives or the tasks have not been estimated yet.

If the charts are generated, but some of the initiatives are marked with a warning icon, that means those initiatives do not have tasks or the tasks have not been estimated yet. Hover over the warning icon to get more information.

![financials-onboarding-finished.png](/cms_trial/assets/b1cdfab7-4d04-4162-8bd8-c65d322187aa.png)

## Initiative

### Initial configuration

You can apply financial calculation settings to a single initiative by going to a specific initiative and selecting the Financials module from the module list. The onboarding will take you through a number of steps to complete the initial configuration.

If you’ve already configured financial onboarding for the portfolio, you don’t have to configure it for the initiatives in it. The portfolio rules automatically apply to all initiatives.

### Initiative tasks

Make sure the initiative has tasks (with dates and effort estimations). You can define them before or use the options available upon choosing the Financials module for a specific initiative:

![initiative-onboarding.png](/cms_trial/assets/dc3518dd-7894-4652-84ba-503af56cddb2.png)

Click **Create new** to add a single task. Click **Define scope** and complete the [Scope definition](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/).

### Financials onboarding

Once the initiative has tasks, you can configure the Financials module.

#### Select period

Choose the timeframe for tracking initiative costs (can be switched later):

- Current quarter
- Current year
- Next quarter
- Next year

#### Calculation settings

Task and hourly rate that will be base for the cost calculation:

#### How do you estimate work effort?

- Man-days
- Story points

#### Which hourly rate should we use?

- Box hourly rate - use a single hourly rate for all tasks, regardless of the team.
- Team hourly rate - use different hourly rates for each team in the initiative.

#### Box hourly rate ($)

Set an hourly rate.

The currency symbol is based on [the Administration setting](/cms_trial/space/SPM/1918830158/Financials+(Administration)/).

### Finish onboarding

Click **Finish** on the last step of the onboarding. You can now see the Financials module with data:

![initiative-onboarding-finished.png](/cms_trial/assets/ceb08776-f381-4c68-9528-84a03a36a715.png)

If the charts in the Planned vs Actual costs panel are not generated, there are no tasks in the initiative or the tasks have not been estimated yet.

If the charts are generated, but some of the tasks in the initiative are not present, an error message is displayed:

![financials -onboarding-errors.png](/cms_trial/assets/2f7a2dc2-76e8-4a25-8e3a-f75e7cddea3d.png)

## Financials module onboarding (new navigation)

Click to expand the guide

The onboarding process is automatically started when you open the Financials module for the first time in a specific portfolio or project box. The process then leads you through the initial Financials module configuration.

## Portfolio

### Initial configuration

The onboarding workflow guides you through steps to start using the Financials module in a specific portfolio.

Once you complete the onboarding for the portfolio, the settings apply to all the initiatives in the portfolio.

If you would rather perform the onboarding for a single initiative, check the *Initiative* section below.

### Portfolio initiatives

Make sure that the portfolio has initiatives - projects with tasks (that have dates and effort estimations). You can define them before or use the options available upon choosing the Financials module from the module selector for a portfolio without initiatives:

- Import Jira spaces
- Add existing projects

![Screenshot of the splash screen in the Financials module.](/cms_trial/assets/33c837c3-21d8-4274-ba24-867fc29b927e.png)

#### Import Jira spaces

Start typing to search for Jira spaces. Choose a type of BigPicture project to be created based on a Jira space:

- Agile Project
- Classic project
- Hybrid Project
- Program

You can choose to create one BigPicture project or a project for each of the selected items:

![Screenshot of importing Jira spaces to the Financials module.](/cms_trial/assets/5b0e0d2c-f775-4f43-96f0-124cb72eee14.png)

#### Add existing projects

Choose any required existing projects from a drop-down list:

![Screenshot of importing existing projects in the Financials module.](/cms_trial/assets/4eb37140-6353-4c0c-9ba8-4ee89d9e35b5.png)

### Financials onboarding

Once the portfolio has initiatives, you can start setting up the Financials module. When you first open the Financials module for a box, you will be prompted to create the Financials module configuration. Click the **Let’s Start** button to start the configuration.

![Screenshot of the splash screen in the Financials module.](/cms_trial/assets/78389eb6-5e70-422e-ba70-b0d4d62179b2.png)

#### Select period

Choose the timeframe for tracking initiative costs (can be switched later):

- Current quarter
- Current year
- Next quarter
- Next year

#### Configure calculations settings

Task and hourly rate that are the base for the cost calculation:

#### Select initiatives to apply settings to

Choose initiatives within the portfolio that will be considered for financial calculation.

#### How do you estimate work effort?

- Man-days
- Story points

#### Which hourly rate should we use?

- Flat rate - use a single hourly rate for all tasks, regardless of the team.
- Team hourly rate - use the team hourly rate if the tasks are assigned to teams and each team needs a different rate. If the team hourly rate is chosen and a team has not been set, the app sets $100 for the calculations. To define hourly rates for teams, see the [Financials (Administration)](/cms_trial/space/SPM/1918830158/Financials+(Administration)/) page.

#### Flat hourly rate ($)

Set an hourly rate.

The currency symbol is set on the [Financials (Administration)](/cms_trial/space/SPM/1918830158/Financials+(Administration)/) page.

### Finish onboarding

Click **Finish** on the last step of the onboarding. If the charts in the *Planned vs Actual costs* panel are not generated, it means that there are no tasks in the initiatives or the tasks have not been estimated yet.

If the charts are generated, but some of the initiatives are marked with a warning icon, that means those initiatives do not have tasks or the tasks have not been estimated yet. Hover over the warning icon to get more information.

![Screenshot of the dashboard in the Financials module.](/cms_trial/assets/f6f4f9f9-798c-4a4f-bab0-bda2ae3d37f7.png)

## Initiative

### Initial configuration

You can apply financial calculation settings to a single initiative by going to a specific initiative and selecting the Financials module from the module list. The onboarding will take you through a number of steps to complete the initial configuration.

If you’ve already configured financial onboarding for the portfolio, you don’t have to configure it for the initiatives in it. The portfolio rules automatically apply to all initiatives.

### Initiative tasks

Make sure the initiative has tasks (with dates and effort estimations). You can define them before or use the options available upon choosing the Financials module for a specific initiative:

![Screenshot of the onboarding for an initiative in the Financials module.](/cms_trial/assets/e30bd167-2d2a-4671-9dfe-f496510d40bd.png)

Click **Define scope** and complete the [add work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/).

### Financials onboarding

Once the initiative has tasks, you can configure the Financials module.

#### Select period

Choose the timeframe for tracking initiative costs (can be switched later):

- Current quarter
- Current year
- Next quarter
- Next year

#### Calculation settings

Task and hourly rate that will be base for the cost calculation:

#### How do you estimate work effort?

- Man-days
- Story points

#### Which hourly rate should we use?

- Box hourly rate - use a single hourly rate for all tasks, regardless of the team.
- Team hourly rate - use different hourly rates for each team in the initiative.

#### Box hourly rate ($)

Set an hourly rate.

The currency symbol is based on [the Administration setting](/cms_trial/space/SPM/1918830158/Financials+(Administration)/).

### Finish onboarding

Click **Finish** on the last step of the onboarding. You can now see the Financials module with data:

![Screenshot of a dashboard in the Financials module after completing the onboarding.](/cms_trial/assets/efd76d55-d39c-4cd9-86cc-6c721f49f517.png)

If the charts in the Planned vs Actual costs panel are not generated, there are no tasks in the initiative or the tasks have not been estimated yet.

If the charts are generated, but some of the tasks in the initiative are not present, an error message is displayed:

![Screenshot of the warning message displayed in the Financials module after completing the onboarding.](/cms_trial/assets/73568f66-4094-4b79-8c70-b230ebfbb68c.png)