# Initial setup: bringing your financial data into BigPicture

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Enable the Financials module

To start working with the Financials module, activate it in [the box settings or box type settings](https://appfire.atlassian.net/wiki/x/XwMEbg). Note that you cannot activate the module for the home box.

## Security roles

A user has to have access to a specific box (for which calculations are made) or to the Home box (which gives access to all the boxes) to access the Financials module. To find out more, check [the box-level permission settings](/cms_trial/space/SPM/1918797447/Box-level+permissions/).

The following table presents detailed relations between the security role and the box role.

| **Role in Administration** | **Role in a Box configuration** | **Access to the module/administration** | **Possibility of editing** |
| --- | --- | --- | --- |
| App Admin | not necessary | Has access to both: the Financials module and Financials administration. | Can edit module and administration settings |
| none of Financials roles | Box Admin / Box Editor / Box Viewer | Has no access to the module and Financials administration. | none |
| App Financial Admin | none | Cannot see the module (because cannot see any box in the BP). Has access to the Financials administration. | Can edit administration settings |
| App Financial Admin | Box Admin | Has access to both: the Financials module and Financials administration. | Can edit module and administration settings |
| App Financial Admin | Box Editor | Has access to both: the Financials module and Financials administration. | Can edit module and box administration settings |
| App Financial Admin | Box Viewer | Has access to both: the Financials module and Financials administration. | Can edit module and box administration settings |
| App Financials Viewer | none | Has no access to any box in the app. | none |
| App Financials Viewer | Box Admin | Has access to the module but not the Administration. | Cannot edit calculation settings and budget. |
| App Financials Viewer | Box Editor | Has access to the module but not the Administration. | Cannot edit calculation settings and budget. |
| App Financials Viewer | Box Viewer | Has access to the module but not the Administration. | Cannot edit calculation settings and budget. |

## Configure global financial settings

You can configure global settings, like currency, baselines and custom expenses, in [the app administration](/cms_trial/space/SPM/1918830158/Financials+(Administration)/).

## Assign hourly rates to boxes/teams

To use Team hourly rates in the calculation, you must have teams configured. Refer to the [Teams module](/cms_trial/space/SPM/1918829775/Teams+module/) page to learn more.

You can set up hourly rates for teams in [the app administration](/cms_trial/space/SPM/1918830158/Financials+(Administration)/).

You can set up box rates (Flat Rate for a box) in the Financials module → Initiative view.

## Prepare tasks for the Financials module

Both basic and Jira tasks are taken into consideration when making financial calculations.

For a task to be taken under consideration, it has to:

- Have a start or end date within the chosen financial period.
- Have effort estimates.
- Tasks are assigned to teams
- [Workload contouring mode](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918831697) affects cost calculations - it is important when it comes to task cost distribution between days.

## Box onboarding

The onboarding will take you through configuration of the Financials module for a specific box. For more information, check [Financials module onboarding](/cms_trial/space/SPM/2269872177/Financials+module+onboarding/) .