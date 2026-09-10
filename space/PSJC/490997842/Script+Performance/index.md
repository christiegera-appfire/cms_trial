# Script Performance

The Script Performance section provides a history of script executions and shows information about the history of the scripts execution. This section can be found at **Power Scripts** > **Performance Monitoring** > **Script Performance.**

Information about each script includes:

- **Exec** - Number of times script was executed
- **Min** - Fastest time script was ran and successfully completed
- **Max** - Longest time script was ran and successfully completed
- **Avg** - Average time script was ran and successfully completed
- **Errors** - The number or times a script raised an error in the logs

**Note:** A dramatic difference between the min and max script execution time can often be seen because of logic within the script. Sometimes the script may include logic that states the script should continue to run for specific scenarios. Therefore, the best number to use to understand the cost to system performance for a script would be the **average** execution time.

![Power Scripts for Jira Cloud script snippets panel](/cms_trial/assets/5b726c35-879c-494e-ab46-f3980ca5823a.png)

Note also that first-time the engine is parsing a script it will optimize the resulting code, and this means a greater execution time.

Whenever you see scripts name with an URL like identifier starting with *kepler://* it means scripts that are run internally, without a corresponding file. In the above example, *kepler://inline-sil-source* means scripts run from the editor.

**See More**