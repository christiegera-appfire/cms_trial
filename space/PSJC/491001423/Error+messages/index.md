# Error messages

## Problem

When a script is not working right, the first thing to check is for error messages.

## Click the Check button

- Clicking on the **Check** button checks the code for syntax errors. Hover over the red X mark to see the specific error.

## Check the Jira system logs for errors

- When running the script, error messages are posted to the Jira system logs. The error logs can usually be seen by navigating to <`JIRA HOME>/log/atlassian-jira.log`.
- You can also view those logs by clicking **Load log** at the bottom of the SIL Manager.

## Viewing the entire error stack

- Create a mark in the logs so the beginning of the log stack is easy to find.

  - One method is to use `logPrint()` to create a long line of dashes. Place the `logPrint()` function at the top of the code you are using.
  - The `logPrint()` code follows the example shown:

    ```text
     logPrint(“ERROR”, “SIL DEBUGGING ------------------------ “ + currentDate());
    ```
  - Another method is described in Atlassian’s [Mark Jira Data Center Logs for Easier Troubleshooting](https://confluence.atlassian.com/jirakb/mark-logs-for-easier-troubleshooting-in-jira-server-827334452.html) page.
  - Reproduce the error.
  - Search for the mark created in the system logs. The beginning of the error stack will be found after the mark in the logs.

## Check the JavaScript console for errors and debugging information.

- When running Live Fields scripts, another place to check for errors is in the JavaScript console. For most browsers, you can open the JavaScript console by pressing`F12` on your keyboard.