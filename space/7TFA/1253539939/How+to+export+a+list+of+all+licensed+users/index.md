# How to export a list of all licensed users

## How do I export a list of all Timetracker licensed users with their roles?

In order to get a list of all licensed users, you will need to use the Timetracker REST CRUD API and the [users/roles endpoint](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/). You can simply send an API call via Postman or another third party software to fetch the list of all licensed users with their respective roles.

The API call should look like this:

GET https://{your-organization}.timehub.7pace.com/api/rest/users/roles?api-version={version}&$expand=user.displayName

We have also created an Excel template file that achieves the same purpose. You can use the attached Excel file [**Get users and roles - example.xlsx**](https://appfire.atlassian.net/wiki/download/attachments/1253540003/Get%20users%20and%20roles%20-%20example.xlsx?api=v2)to quickly get your first report up and running. By following the instructions, you will obtain a list of all users and their roles in under five minutes.

Please be aware of certain limitations:

- The instructions inside of the Excel file only work for Windows version of Excel.
- You need to have a 7pace Timetracker Administrator or a Project Collection Administrator role assigned for the REST CRUD API users/roles endpoint to work, for security reasons.  
  *Alternatively, you can use a token of Service Account, but this is out of scope of this manual, you can refer to*[*Service Account Configuration manual*](/cms_trial/space/7TFA/1253540308/Reporting+%26+API%3A+Service+Account%2C+Reporting+%26+REST+API+and+Access+Tokens/)*for more information.*