# Scheduled actions - Agile sprint scope

The following use cases use JQL Search Extensions (JSE) filters based on [Agile sprint functions](/cms_trial/space/JQLSEARCH/604209345/Agile+sprints/) to set the scope for [scheduled actions](https://appfire.atlassian.net/wiki/spaces/JMWEC/pages/466321868) in JMWE.

## Problem to solve

Agile teams often face challenges managing workload visibility throughout and between sprints. New issues added after a sprint starts can disrupt capacity and workload management, while incomplete preparation for upcoming sprints can introduce delays and reduce predictability. This dual challenge impacts effective sprint planning, resource allocation, and prioritization, resulting in a lack of visibility into tasks added mid-sprint and what needs attention before the next sprint begins.

## Solution

Schedule email notifications to highlight scope creep and ensure issues are prioritized ahead of time for upcoming sprints.

## Create a scheduled action that sends a daily email with a list of issues added to the current sprint after the start date

|  |  |
| --- | --- |
| **JSE function** | `addedToSprintAfterStart()` |
| **JMWE scheduled action** | `Every day at 12:0 UTC` |
| **JMWE action** | Email Issues |
| **Method** | 1. In JQL Extended Search, perform a search for issues added to a sprint after the start, for example:  ```text    issue in addedToSprintAfterStart(ACME)    ``` Screenshot of the JQL function as described on this page. 2. Click **Save the query as a filter**. 3. Enter a name for the filter, then click **Save**. For this example, the filter is called `Issues added after sprint start`. 4. In JMWE, create or edit a [scheduled action](https://appfire.atlassian.net/wiki/spaces/JMWEC/pages/466321868) to occur `daily at 12:00 UTC`. 5. Under IF SCOPE, click **Select Target Issues**. 6. In the *JQL Expression* input box, enter the filter name, for example, `filter="Issues added after sprint start"`. Screenshot of the configured Scheduled action in JMWE as described on this page. 7. Add the *Email issues* post function and configure the recipients and message subject. 8. Save the action.  Now, every day, the team lead will receive an email with a list of issues added to a sprint after the start date. |

## Create a scheduled action that sends an email every week with a list of issues to review before the next sprint starts

|  |  |
| --- | --- |
| **JSE keyword** | `nextSprint ()` |
| **JMWE scheduled action** | `Every week on Tuesday at 08:30 UTC` |
| **JMWE action** | Email Issues |
| **Method** | 1. In JQL Extended Search, perform a search for child issues matching a given query, for example:  ```text    issue in nextSprint(15)    ``` Screenshot of the Extended Search page with the query as described on this page. 2. Click **Save the query as a filter**. 3. Enter a name for the filter, then click **Save**. For this example, the filter is called `Issues in next sprint`. 4. In JMWE, create or edit a [scheduled action](https://appfire.atlassian.net/wiki/spaces/JMWEC/pages/466321868) to occur `weekly on a Tuesday at 08:30 UTC.` 5. Under IF SCOPE, click **Select Target Issues**. 6. In the *JQL Expression* input box, enter the filter name, for example, `filter="Issues in next sprint"`. 7. Add the *Email issues* post function and configure the recipients and message subject. 8. Save the action. JSE-JMWE-scheduled-email-issues-in-next-sprint.png Now, every week, the team PM will receive an email with a list of issues planned for the next sprint. |