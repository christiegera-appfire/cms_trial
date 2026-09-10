# Salesforce Reporting on Jira Issue key

## Purpose

Reporting Jira associations on Salesforce is not possible at the moment. A workaround for customers, when they ask about Reporting on Salesforce, is to send the Jira Key field value to a Salesforce string Field and create a report based on the Jira key.

This is useful when Salesforce users might not have/don't need access to Jira and wish to report on :

- How many cases have an association with a Jira issue.
- Jira Issue key associated to an Object.
- Jira issue link on another field.

### Limitation

The limitation is that you cannot list more than one association per record.

## Answer

## Sending the Jira issue key to a String

More information about Field mapping can be found [here](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754325/Configuring+Entity+Mappings+and+Field+Mappings).

For this we need to map the Jira Key to a String.

1. Add a String field on Salesforce and map the Key value to that new Field (that we will call Jira Key).

The binding is only one way, since the Key in Jira is Read-only.

![contentId-3104407562](/cms_trial/assets/f5583642-93a6-472b-93e6-e325e92a8a33.png?version=1&modificationDate=1678858805321&cacheVersion=1&api=v2)

1. You will get the Jira Key as a String on Salesforce.

![contentId-3104407562](/cms_trial/assets/f92de75e-51e9-49f7-8e6b-b5967f35a1ef.png?version=1&modificationDate=1678858805190&cacheVersion=1&api=v2)

1. Create a Salesforce report with the new Jira Key field.

Now you need to create a report and add the new Jira key field. for that we will use the Case object as an example.

- Click on the App launcher (9 dots) Service → Reports → New Report.
- In the Search box type "Cases" and click **Continue** on the bottom right.
- Add the Column "Jira Key" and click Refresh.

![contentId-3104407562](/cms_trial/assets/f8ca7657-1dae-45b2-b66d-0ebdc58e37ab.png?version=1&modificationDate=1678858805518&cacheVersion=1&api=v2)

The Report configuration will look like this:

![contentId-3104407562](/cms_trial/assets/c2543ba9-0598-47ba-87ea-f121531846c0.png?version=1&modificationDate=1678858805650&cacheVersion=1&api=v2)

- Save the new report.

1. Now you can select the new report. After this you can add any columns with information that's coming from Jira (you can add the Status, Assignee, etc.)

![contentId-3104407562](/cms_trial/assets/23e2fc8c-8c26-4f03-a503-1e082c3d92e1.png?version=1&modificationDate=1678858805451&cacheVersion=1&api=v2)

This is the fastest way to get a report in Salesforce of all the Case records with an association.

If you want to have a report in Jira, please take a look at this documentation:

[Running an association report in Jira](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754196/Running+an+association+report)