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

![fianncials-portfolio-onboarding.png](/cms_trial/assets/31a8bcff-12c3-4394-9118-5dd38d96a980.png)

#### Import Jira projects

Start typing to search for Jira projects. Choose a type of BigPicture project to be created based on a Jira project:

- Agile Project
- Classic project
- Hybrid Project
- Program

You can choose to create one BigPicture project or a project for each of the selected items:

![Import Jira Projects dialog with several different Jira projects selected for import.](/cms_trial/assets/85be4cca-7054-48db-8150-b5907eeb3513.png)

#### Add existing projects

Choose any required existing projects from a drop-down list:

![Add existing initiatives to this portfolio dialog with example initiatives and projects selected.](/cms_trial/assets/0b7dac4c-489a-483a-9e4b-08e138f47203.png)

### Financials onboarding

Once the portfolio has initiatives, you can start setting up the Financials module. When you first open the Financials module for a box, you will be prompted to create the Financials module configuration. Click the **Let’s Start** button to start the configuration.

![financials-portfolio.png](/cms_trial/assets/07584bbf-ee1a-48f1-9f6b-2fdbc6dd8a97.png)

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

![financials-onboarding-finished.png](/cms_trial/assets/84e8fce2-280a-460e-a9e3-71eeb48d8f5b.png)

## Initiative

### Initial configuration

You can apply financial calculation settings to a single initiative by going to a specific initiative and selecting the Financials module from the module list. The onboarding will take you through a number of steps to complete the initial configuration.

If you’ve already configured financial onboarding for the portfolio, you don’t have to configure it for the initiatives in it. The portfolio rules automatically apply to all initiatives.

### Initiative tasks

Make sure the initiative has tasks (with dates and effort estimations). You can define them before or use the options available upon choosing the Financials module for a specific initiative:

![initiative-onboarding.png](/cms_trial/assets/d69bc45c-d3b4-40de-b3d8-6b18ace118e8.png)

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

![initiative-onboarding-finished.png](/cms_trial/assets/b464551e-f92d-4069-baef-a88b70295852.png)

If the charts in the Planned vs Actual costs panel are not generated, there are no tasks in the initiative or the tasks have not been estimated yet.

If the charts are generated, but some of the tasks in the initiative are not present, an error message is displayed:

![financials -onboarding-errors.png](/cms_trial/assets/e532a011-bb9a-4a8d-b6a7-9e6a71da4895.png)

## Financials module onboarding (new navigation)

Click to expand the guide

The onboarding process is automatically started when you open the Financials module for the first time in a specific portfolio or project box. The process then leads you through the initial Financials module configuration.

## Home box

The onboarding workflow guides you through steps to start using the Financials module in the home box level.

Once you complete the onboarding for the Home box, the settings apply to all the boxes

![home-box-onboarding.png](/cms_trial/assets/90423383-517c-49c9-9eff-0da875e327ff.png)

### Period and boxes

Choose a period for which data will be displayed and boxes:

![home-box-onboarding-2.png](/cms_trial/assets/c299f3ef-6bdc-462e-ac92-64a7ccf12fec.png)

### Default calculations

Choose calculation methods that will apply to boxes without cost calculations assigned.

![home-box-3.png](/cms_trial/assets/1cb7e1cb-9246-4e69-901a-724f1a92c684.png)

## Portfolio

### Initial configuration

The onboarding workflow guides you through steps to start using the Financials module in a specific portfolio.

Once you complete the onboarding for the portfolio, the settings apply to all the initiatives in the portfolio.

If you would rather perform the onboarding for a single initiative, check the *Initiative* section below.

### Portfolio initiatives

Make sure that the portfolio has initiatives - projects with tasks (that have dates and effort estimations). You can define them before or use the options available upon choosing the Financials module from the module selector for a portfolio without initiatives:

- Import Jira spaces
- Add existing projects

![Screenshot of the splash screen in the Financials module.](/cms_trial/assets/b9d6373c-d09f-436c-8e03-609e11159d29.png)

#### Import Jira spaces

Start typing to search for Jira spaces. Choose a type of BigPicture project to be created based on a Jira space:

- Agile Project
- Classic project
- Hybrid Project
- Program

You can choose to create one BigPicture project or a project for each of the selected items:

![Screenshot of importing Jira spaces to the Financials module.](/cms_trial/assets/a152f4f8-059b-4d17-9fc0-c904aac01093.png)

#### Add existing projects

Choose any required existing projects from a drop-down list:

![Screenshot of importing existing projects in the Financials module.](/cms_trial/assets/4758a11d-4c91-40a6-81db-98df4c77f277.png)

### Financials onboarding

Once the portfolio has initiatives, you can start setting up the Financials module. When you first open the Financials module for a box, you will be prompted to create the Financials module configuration. Click the **Let’s Start** button to start the configuration.

![Screenshot of the splash screen in the Financials module.](/cms_trial/assets/13a2b9b4-e214-4261-84bf-a36019b61090.png)

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

![Screenshot of the dashboard in the Financials module.](/cms_trial/assets/046605a7-7e42-4cee-b57f-2058523ed759.png)

## Initiative

### Initial configuration

You can apply financial calculation settings to a single initiative by going to a specific initiative and selecting the Financials module from the module list. The onboarding will take you through a number of steps to complete the initial configuration.

If you’ve already configured financial onboarding for the portfolio, you don’t have to configure it for the initiatives in it. The portfolio rules automatically apply to all initiatives.

### Initiative tasks

Make sure the initiative has tasks (with dates and effort estimations). You can define them before or use the options available upon choosing the Financials module for a specific initiative:

![Screenshot of the onboarding for an initiative in the Financials module.](/cms_trial/assets/fc414943-9d69-4b5d-ac47-fdc668932376.png)

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

![Screenshot of a dashboard in the Financials module after completing the onboarding.](/cms_trial/assets/9e820a6d-ade6-48c2-9eb6-22f77a64b09b.png)

If the charts in the Planned vs Actual costs panel are not generated, there are no tasks in the initiative or the tasks have not been estimated yet.

If the charts are generated, but some of the tasks in the initiative are not present, an error message is displayed:

![Screenshot of the warning message displayed in the Financials module after completing the onboarding.](/cms_trial/assets/bfa484bc-7c1d-4917-a81f-1ea039ebc59e.png)