# Find users and work items without tracked time

## Introduction

We have composed Excel spreadsheets which connect to the Timetracker API and the DevOps API and fetch data on users who have not tracked time during a time period, and work items without tracked time during a time period.  
In order to use both of these tables you will need to authorize yourself by using a Timetracker issued Reporting API token. You can find a tutorial on how to generate it here: [How to generate 7pace Timetracker API token](/cms_trial/space/7TFA/1253539983/7pace+Timetracker+API+Important+Information/).  
We also have a tutorial here on how to connect to the Timetracker API with Excel: [How to connect Excel or Power BI to 7pace Timetracker API](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).  
To get a list of work items from DevOps you will need to issue a [DevOps Personal Access Token (PAT)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows#create-a-pat).

## Users who have not tracked time

Download: ▢

### Instructions on how to use

1. On the Configuration sheet enter your DevOps organization name and the starting and end dates. The dates cannot be the same. If you wish to look at today's data, then enter tomorrow's date as the end date.
2. Click on the Excel Data tab.
3. Select Queries & Connections
4. Click to refresh the connections in the connections window. Now you will be prompted to authorize your connection.
5. Authorize your connection by using the Timetracker Reporting API token by choosing Basic authentication, and pasting the token value into the password field. The username field should be left blank.
6. Repeat authorization with the Timetracker Reporting API token for all other queries that you see in the Queries & Connections window
7. Now you will see your data has loaded

![FAQ_Find_Users_Not_Track_Time.png](/cms_trial/assets/3e09eca3-1db0-4662-8291-dfb2a627c2ed.png)![FAQ_Find_Users_Not_Track_Time_1.png](/cms_trial/assets/f3c55cee-391e-4999-9458-1d401191007b.png)

## Work items without tracked time

Download: ▢

### Instructions on how to use

1. On the Configuration sheet enter your DevOps organization name and the starting and end dates for Timetracker worklog (tracked time) data. The dates cannot be the same. If you wish to look at today's data, then enter tomorrow's date as the end date.  
   Enter your DevOps issued PAT token, and then enter the work item changed date time period. If you wish to load work items that have been modified in the last 5 days, then enter the number 5.
2. Click on the Excel Data tab.
3. Select Queries & Connections
4. Click to refresh each of the connections in the connections window. Now you will be prompted to authorize your Timetracker API connection.
5. Authorize your Timetracker API connection by using the Timetracker Reporting API token by choosing Basic authentication, and pasting the token value into the password field. The username field should be left blank.
6. Now you will see your data has loaded

![FAQ_Find_Users_Not_Track_Time_Instructions_1.png](/cms_trial/assets/e3d132b8-8afd-4046-90d3-ce9213b6e529.png)![FAQ_Find_Users_Not_Track_Time_Instructions_2.png](/cms_trial/assets/359ca099-d31e-4b7e-8c72-f1b6eb1a6eb8.png)